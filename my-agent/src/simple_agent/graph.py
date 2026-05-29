"""Risk assessment agent for AI sandbox projects (Swiss public sector)."""

from __future__ import annotations

import json
import os
import uuid
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


_TOOLS = [update_project_field, start_risk_analysis]

# ── Chat node ─────────────────────────────────────────────────────────────────

_CHAT_SYSTEM = """You are a risk assessment assistant for AI projects.

Your job is to build a complete project profile by asking focused questions, \
then trigger an automated risk analysis.

The current project state is shown at the end of this message under "COLLECTED INFO".

Process:
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
