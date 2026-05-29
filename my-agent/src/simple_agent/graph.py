"""Risk assessment + wiki-grounded agent for AI sandbox projects (Swiss public sector)."""

from __future__ import annotations

import json
import os
import uuid
from pathlib import Path
from typing import Annotated, Literal

from langchain.chat_models import init_chat_model
from langchain_core.callbacks.manager import adispatch_custom_event
from langchain_core.messages import AIMessage, SystemMessage, ToolMessage
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langchain_core.tools import InjectedToolCallId
from langgraph.prebuilt import ToolNode
from langgraph.types import Command
from pydantic import BaseModel
from typing_extensions import TypedDict

from .risks_db import RiskMitigation, get_all_risks, get_risk_mitigation
from .risks_db import Risk as RiskData

# ── Models ────────────────────────────────────────────────────────────────────

CHAT_MODEL = os.getenv("CHAT_MODEL", "openai:gpt-4o-mini")
ANALYSIS_MODEL = os.getenv("ANALYSIS_MODEL", "openai:gpt-4o")

# ── Wiki ──────────────────────────────────────────────────────────────────────

# Wiki root resolves to ../wiki relative to this file by default; override via env.
_DEFAULT_WIKI_ROOT = (Path(__file__).resolve().parents[3] / "wiki").resolve()
WIKI_ROOT = Path(os.getenv("WIKI_ROOT", str(_DEFAULT_WIKI_ROOT))).resolve()

# Page-type folders the wiki organises content into.
_WIKI_FOLDERS = (
    "projects",
    "concepts",
    "regulations",
    "stakeholders",
    "lessons",
    "sources",
    "synthesis",
)

# Root-level pages addressable by bare slug (no folder).
_ROOT_PAGES = ("index", "README", "QUERY", "CONVENTIONS", "INGEST")

# Cap response sizes so a single wiki call can't blow context on a small chat model.
_MAX_READ_BYTES = 60_000
_MAX_SEARCH_HITS = 25
_SEARCH_SNIPPET_CHARS = 160


def _safe_path(candidate: Path) -> Path:
    """Resolve `candidate` and ensure it stays inside WIKI_ROOT."""
    resolved = candidate.resolve()
    if WIKI_ROOT not in resolved.parents and resolved != WIKI_ROOT:
        raise ValueError(f"Path escapes wiki root: {candidate}")
    return resolved


def _try_safe(candidate: Path) -> Path | None:
    try:
        return _safe_path(candidate)
    except ValueError:
        return None


def _find_page(slug: str) -> Path | None:
    """Resolve a slug to a markdown file. Accepts bare slugs and folder/slug paths."""
    slug = slug.strip().removesuffix(".md")
    if "/" in slug:
        candidate = _try_safe(WIKI_ROOT / f"{slug}.md")
        return candidate if candidate and candidate.is_file() else None
    if slug in _ROOT_PAGES:
        candidate = _try_safe(WIKI_ROOT / f"{slug}.md")
        if candidate and candidate.is_file():
            return candidate
    for folder in _WIKI_FOLDERS:
        candidate = _try_safe(WIKI_ROOT / folder / f"{slug}.md")
        if candidate and candidate.is_file():
            return candidate
    return None

# ── State ─────────────────────────────────────────────────────────────────────


def _merge_project_input(left: dict, right: dict) -> dict:
    """Merge project input field-by-field — right-hand values win on conflict."""
    return {**left, **right}


class RiskAssessment(TypedDict):
    risk: RiskData
    relevance_reason: str
    mitigation: str
    regulatory_refs: list[str]


class State(TypedDict):
    messages: Annotated[list, add_messages]
    # Merged incrementally — tools add one field at a time.
    project_input: Annotated[dict, _merge_project_input]
    all_risks: list[RiskData]
    relevant_risks: list[RiskData]
    risk_assessments: list[RiskAssessment]


# ── Tools ─────────────────────────────────────────────────────────────────────


@tool
def update_project_field(
    field: str,
    value: str,
    tool_call_id: Annotated[str, InjectedToolCallId],
) -> Command:
    """Store one piece of project information. Call once per field — never batch.

    Supported fields:
      name          – project name
      description   – what the project does (1–3 sentences)
      sector        – e.g. health, wellness, finance, transport, education
      size          – startup / sme / enterprise / government-unit
      data_types    – comma-separated categories (e.g. "personal, health, behavioral")
      timeline      – e.g. "6-month pilot", "production in Q3 2026"
      deployment    – cloud / on-prem / hybrid
      budget_range  – e.g. "< 50k CHF", "50k–200k CHF", "> 200k CHF"
    """
    return Command(
        update={
            "project_input": {field: value},
            "messages": [ToolMessage(f"Set {field} = {value!r}", tool_call_id=tool_call_id)],
        }
    )


@tool
def start_risk_analysis(
    tool_call_id: Annotated[str, InjectedToolCallId],
) -> Command:
    """Trigger the automated risk analysis pipeline.

    Only call after confirming with the user. Requires at minimum:
    name, description, sector, and at least one of (data_types, deployment, size).
    """
    return Command(
        update={
            "messages": [ToolMessage("Starting risk analysis pipeline.", tool_call_id=tool_call_id)],
        },
        goto="get_risks",
    )


@tool
def list_wiki_pages(folder: str | None = None) -> str:
    """List wiki pages from the Sandbox Knowledge Hub, optionally filtered to one folder.

    Use to enumerate every entry of one type (every project, every lesson). For broad
    queries, prefer reading 'index' first via read_wiki_page.

    Args:
        folder: One of projects, concepts, regulations, stakeholders, lessons,
            sources, synthesis. If omitted, lists pages in every folder.
    """
    folders = (folder,) if folder else _WIKI_FOLDERS
    lines: list[str] = []
    for f in folders:
        if f not in _WIKI_FOLDERS:
            return f"Unknown folder: {f}. Valid folders: {', '.join(_WIKI_FOLDERS)}."
        folder_path = _try_safe(WIKI_ROOT / f)
        if not folder_path or not folder_path.is_dir():
            continue
        slugs = sorted(p.stem for p in folder_path.glob("*.md"))
        if not slugs:
            continue
        lines.append(f"## {f}/")
        lines.extend(f"- {slug}" for slug in slugs)
        lines.append("")
    return "\n".join(lines).rstrip() or "No pages found."


@tool
def read_wiki_page(slug: str) -> str:
    """Read a wiki page from the Sandbox Knowledge Hub and return its full markdown.

    The wiki is the source of truth for questions about the Canton of Zürich's
    AI Innovation Sandbox. Slugs are kebab-case. Examples:
    - 'index'              — the navigable inventory; read this FIRST for any wiki query.
    - 'QUERY'              — the answering procedure (citation rules, voice).
    - 'digital-eye-clinic' — a project page.
    - 'data-access'        — a concept page.
    - 'eu-ai-act'          — a regulation page.

    A folder-qualified path like 'projects/digital-eye-clinic' also works.

    Args:
        slug: The page slug or folder/slug path. Omit the .md extension.
    """
    page = _find_page(slug)
    if page is None:
        return (
            f"No page found for slug '{slug}'. Try list_wiki_pages() to see what "
            f"exists, or search_wiki('{slug}') for keyword matches."
        )
    text = page.read_text(encoding="utf-8")
    rel = page.relative_to(WIKI_ROOT)
    header = f"# wiki/{rel}\n\n"
    if len(text) > _MAX_READ_BYTES:
        text = text[:_MAX_READ_BYTES] + f"\n\n[... truncated at {_MAX_READ_BYTES} bytes]"
    return header + text


@tool
def search_wiki(query: str) -> str:
    """Full-text search across every wiki page for a substring (case-insensitive).

    Use when you don't know the slug but have a keyword (a name, a regulation
    acronym, a German term). For broad conceptual queries prefer reading 'index'
    and following links.

    Args:
        query: Substring to match. Short, distinctive terms work best.
    """
    needle = query.strip().lower()
    if len(needle) < 2:
        return "Query too short — use at least 2 characters."
    hits: list[str] = []
    for md_path in sorted(WIKI_ROOT.rglob("*.md")):
        if not _try_safe(md_path):
            continue
        try:
            text = md_path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        idx = text.lower().find(needle)
        if idx == -1:
            continue
        start = max(0, idx - _SEARCH_SNIPPET_CHARS // 2)
        end = min(len(text), idx + len(needle) + _SEARCH_SNIPPET_CHARS // 2)
        snippet = text[start:end].replace("\n", " ").strip()
        rel = md_path.relative_to(WIKI_ROOT)
        hits.append(f"- `wiki/{rel}` … {snippet} …")
        if len(hits) >= _MAX_SEARCH_HITS:
            hits.append(f"\n[truncated at {_MAX_SEARCH_HITS} hits — narrow the query]")
            break
    if not hits:
        return f"No matches for '{query}'."
    return "\n".join(hits)


_TOOLS = [
    update_project_field,
    start_risk_analysis,
    list_wiki_pages,
    read_wiki_page,
    search_wiki,
]

# ── Chat node ─────────────────────────────────────────────────────────────────

_CHAT_SYSTEM = """You are a risk assessment assistant for AI projects in the \
Canton of Zürich AI Innovation Sandbox.

Your primary job is to build a complete project profile by asking focused \
questions, then trigger an automated risk analysis.

You also have access to the Sandbox Knowledge Hub wiki — the structured \
corpus of prior sandbox projects, concepts, regulations, and lessons. Use it \
in two situations:

A. **The user asks a question about the corpus** (e.g. "what does the wiki say \
about data access?", "what projects ran in healthcare?", "explain the EU AI \
Act"). Answer it from the wiki — do not gather a project profile in this case. \
Start with `read_wiki_page('index')` to find the right entry pages, then read \
3-5 relevant pages, then synthesise. Cite paragraph anchors as \
`[(source-slug#para-N)](sources/source-slug.md#para-N)` when available; never \
invent anchors. The full procedure lives at `read_wiki_page('QUERY')`.

B. **Grounding a profile question or risk discussion** in prior projects \
(e.g. when the user mentions a sector, briefly note a comparable wiki project \
to make the next question more concrete). Keep this lightweight — one or two \
references, not a synthesis essay.

The current project state is shown at the end of this message under "COLLECTED INFO".

Profile-gathering process:
1. Read COLLECTED INFO to see what is already known — never ask for something already there.
2. Extract any new information from the user's message and save it immediately with \
   `update_project_field` (one call per field — never batch multiple fields).
3. Ask the single most important missing question. One question per turn, no lists.
4. Repeat until you have: name, description, sector, plus at least one of \
   (data_types, deployment, size).
5. Confirm with the user ("I have enough info to run the analysis — shall I proceed?") \
   then call `start_risk_analysis`.

Required fields: name, description, sector
Important fields: data_types, deployment, size, timeline, budget_range

Be concise and friendly."""


def chat_node(state: State) -> dict:
    pi = state.get("project_input") or {}
    collected = (
        f"\n\nCOLLECTED INFO:\n{json.dumps(pi, indent=2, ensure_ascii=False)}"
        if pi
        else "\n\nCOLLECTED INFO: (nothing yet)"
    )
    system = SystemMessage(content=_CHAT_SYSTEM + collected)
    llm = init_chat_model(CHAT_MODEL).bind_tools(_TOOLS)
    response = llm.invoke([system] + state["messages"])
    return {"messages": [response]}


def route_after_chat(state: State) -> Literal["tools", "__end__"]:
    last = state["messages"][-1]
    if hasattr(last, "tool_calls") and last.tool_calls:
        return "tools"
    return "__end__"


# ── Analysis nodes ────────────────────────────────────────────────────────────


def get_risks_node(_state: State) -> dict:
    """Fetch the full risk catalogue from the internal database."""
    return {"all_risks": get_all_risks()}


class _RiskSelectionItem(BaseModel):
    id: str
    relevance_reason: str  # one sentence, specific to the project


class _RiskSelection(BaseModel):
    selections: list[_RiskSelectionItem]


def filter_risks_node(state: State) -> dict:
    """LLM selects 3–7 risks relevant to this specific project."""
    llm = init_chat_model(ANALYSIS_MODEL).with_structured_output(_RiskSelection)

    prompt = (
        "You are a risk analyst for AI projects.\n\n"
        f"Project profile:\n{json.dumps(state['project_input'], indent=2)}\n\n"
        "Select the 3–7 most relevant risks from the catalogue below. "
        "For each, write a single sentence explaining why it applies to this specific project "
        "(not generic boilerplate).\n\n"
        f"Risk catalogue:\n{json.dumps(state['all_risks'], indent=2)}"
    )

    result: _RiskSelection = llm.invoke(prompt)

    id_to_reason = {s.id: s.relevance_reason for s in result.selections}
    relevant = [r for r in state["all_risks"] if r["id"] in id_to_reason]

    # Carry relevance reasons forward via a hidden message read by assess_risks_node.
    return {
        "relevant_risks": relevant,
        "messages": [
            AIMessage(
                content="",
                id="__relevance_reasons__",
                additional_kwargs={"relevance_reasons": id_to_reason},
            )
        ],
    }


def assess_risks_node(state: State) -> dict:
    """Look up mitigations from the internal database for each relevant risk."""
    reasons: dict[str, str] = {}
    for msg in reversed(state["messages"]):
        if getattr(msg, "id", None) == "__relevance_reasons__":
            reasons = (msg.additional_kwargs or {}).get("relevance_reasons", {})
            break

    assessments: list[RiskAssessment] = []
    for risk in state["relevant_risks"]:
        mitigation_data: RiskMitigation | None = get_risk_mitigation(risk["id"])
        if mitigation_data is None:
            continue
        assessments.append(
            RiskAssessment(
                risk=risk,
                relevance_reason=reasons.get(risk["id"], "Relevant to this project."),
                mitigation=mitigation_data["mitigation"],
                regulatory_refs=mitigation_data["regulatory_refs"],
            )
        )

    return {"risk_assessments": assessments}


async def push_ui_node(state: State, config: RunnableConfig) -> dict:
    """Dispatch the risk accordion UI event and emit a summary message."""
    msg_id = str(uuid.uuid4())

    await adispatch_custom_event(
        "ui",
        {
            "id": str(uuid.uuid4()),
            "name": "risk_accordion",
            "props": {
                "project": state["project_input"],
                "assessments": state["risk_assessments"],
            },
            "metadata": {"message_id": msg_id},
        },
        config=config,
    )

    n = len(state["risk_assessments"])
    severities = [a["risk"]["severity"] for a in state["risk_assessments"]]
    critical = severities.count("critical")
    high = severities.count("high")

    lines = [
        f"Risk analysis complete — **{n} relevant risks** identified for "
        f"**{state['project_input'].get('name', 'your project')}**.",
    ]
    if critical:
        lines.append(f"- {critical} critical risk{'s' if critical > 1 else ''}")
    if high:
        lines.append(f"- {high} high risk{'s' if high > 1 else ''}")
    lines.append("\nSee the accordion above for mitigations and regulatory references.")

    return {"messages": [AIMessage(content="\n".join(lines), id=msg_id)]}


# ── Graph assembly ────────────────────────────────────────────────────────────

_tool_node = ToolNode(_TOOLS)

builder = StateGraph(State)
builder.add_node("chat", chat_node)
builder.add_node("tools", _tool_node)
builder.add_node("get_risks", get_risks_node)
builder.add_node("filter_risks", filter_risks_node)
builder.add_node("assess_risks", assess_risks_node)
builder.add_node("push_ui", push_ui_node)

builder.add_edge(START, "chat")
builder.add_conditional_edges("chat", route_after_chat, {"tools": "tools", "__end__": END})
builder.add_edge("tools", "chat")
builder.add_edge("get_risks", "filter_risks")
builder.add_edge("filter_risks", "assess_risks")
builder.add_edge("assess_risks", "push_ui")
builder.add_edge("push_ui", END)

graph = builder.compile()
graph.name = "risk_assessment_agent"
