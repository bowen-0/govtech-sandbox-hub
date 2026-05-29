"""Tiny local markdown retriever for the sandbox wiki."""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import TypedDict


class WikiHit(TypedDict):
    title: str
    path: str
    excerpt: str
    score: int


_WORD_RE = re.compile(r"[a-zA-ZÀ-ÿ0-9][a-zA-ZÀ-ÿ0-9_-]{2,}")
_FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)


def _repo_root() -> Path:
    configured = os.getenv("WIKI_ROOT")
    if configured:
        return Path(configured).expanduser().resolve()
    return Path(__file__).resolve().parents[3]


def _wiki_root() -> Path:
    configured = os.getenv("WIKI_DIR")
    if configured:
        return Path(configured).expanduser().resolve()
    return _repo_root() / "wiki"


def _tokens(text: str) -> set[str]:
    return {token.lower() for token in _WORD_RE.findall(text)}


def _clean_markdown(text: str) -> str:
    text = _FRONTMATTER_RE.sub("", text)
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"^#+\s*", "", text, flags=re.MULTILINE)
    return re.sub(r"\s+", " ", text).strip()


def _title_for(path: Path, text: str) -> str:
    match = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
    if match:
        return match.group(1).strip()
    return path.stem.replace("-", " ").title()


def _excerpt(text: str, query_terms: set[str], limit: int = 520) -> str:
    clean = _clean_markdown(text)
    lower = clean.lower()
    positions = [lower.find(term) for term in query_terms if lower.find(term) >= 0]
    start = max(min(positions) - 120, 0) if positions else 0
    snippet = clean[start : start + limit].strip()
    if start > 0:
        snippet = f"...{snippet}"
    if start + limit < len(clean):
        snippet = f"{snippet}..."
    return snippet


def search_wiki_documents(query: str, *, limit: int = 6) -> list[WikiHit]:
    """Search local wiki markdown files with a lightweight keyword scorer."""
    wiki_root = _wiki_root()
    if not wiki_root.exists():
        return []

    query_terms = _tokens(query)
    if not query_terms:
        return []

    hits: list[WikiHit] = []
    for path in wiki_root.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        title = _title_for(path, text)
        haystack = f"{title}\n{text}".lower()
        score = sum(haystack.count(term) for term in query_terms)
        if score <= 0:
            continue
        rel_path = path.relative_to(wiki_root.parent).as_posix()
        hits.append(
            WikiHit(
                title=title,
                path=rel_path,
                excerpt=_excerpt(text, query_terms),
                score=score,
            )
        )

    hits.sort(key=lambda hit: hit["score"], reverse=True)
    return hits[:limit]
