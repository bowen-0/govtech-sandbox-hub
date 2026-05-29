# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository state

This is the submission repo for the *AI Innovation Sandbox Knowledge Hub* challenge at the GovTech Hackathon Switzerland (Thu 28 — Fri 29 May 2026, FOITT Zollikofen). Three layers:

- `wiki/` — the knowledge substrate: structured markdown with YAML frontmatter, plus the source PDFs under `wiki/pdfs/{de,en}/`. Self-contained and substrate-portable.
- `my-agent/` — a LangGraph agent that answers questions grounded in the wiki. Has its own `pyproject.toml`, `Dockerfile`, and Cloudflare `wrangler.jsonc`.
- `agent-chat-ui/` — a Next.js chat UI that talks to the agent. Has its own `package.json` and `wrangler.jsonc`.

Treat each subproject as its own workspace — run/build/test commands live inside each one's README and config files.

## Start here

`wiki/README.md` is the canonical hub for the knowledge layer. It indexes everything else in the wiki and describes the seven-folder schema. Read it first when working anywhere inside `wiki/`.

## Doc map — which doc answers which question

| Question | Doc |
|---|---|
| What does the wiki look like and how is it organised? | `wiki/README.md` |
| What's the wiki schema (frontmatter, taxonomies, citation syntax)? | `wiki/CONVENTIONS.md` |
| How do I add a new source to the wiki? | `wiki/INGEST.md` |
| How does the agent answer queries against the wiki? | `wiki/QUERY.md` |
| What's in the navigable inventory of every wiki page? | `wiki/index.md` |
| How do I run / develop the agent? | `my-agent/README.md` |
| How do I run / develop the chat UI? | `agent-chat-ui/README.md` |
| How do I contribute a page or source? | `CONTRIBUTING.md` |

## Durable rules (do not re-litigate without reason)

1. **Language orientation is three-axis**:
   - Development UI = **English** (so the dev feedback loop works for non-German-readers on the team)
   - Source report content = **German** (citations quote PDFs verbatim — never machine-translate source material)
   - Shipped UI = **bilingual via i18n** (next-intl), demo-time default language deferred
2. **Generator never invents claims.** Content comes from the wiki on disk; the LLM picks which wiki pages a response references but does not fabricate prose around the citations. The no-hallucination constraint is solved structurally, not by prompting.
3. **Citations are paragraph-anchored.** Every claim links to `…pdf#para-N`. Page-level citations are a fallback if anchor stability slips, not a default.
4. **Wiki pages are the source of truth.** The graph lives in YAML frontmatter; markdown prose lives in the body. Both are edited as plain text files. JSON-LD / DuckDB exports are derivative.

## Workflow notes

- Commit deliberately — `git add` specific paths, never `git add -A` (the `.gitignore` excludes `.claude/`, `.DS_Store`, `node_modules`, `.env*`, Python venvs, but be explicit anyway).
- Per-project memory lives at `~/.claude/projects/-Users-Bowen-Coding-Projects-govtech-hackathon/memory/` (auto-loaded).

## Voice / format for new docs in this style

The existing docs share a recognisable shape that's worth matching for any new docs added here:

- TL;DR or "what this doc decides" up top
- Scorecard tables and decision logs where trade-offs matter
- Concrete examples (real frontmatter, real ASCII mockups) over abstract description
- Explicit "open questions" sections rather than hidden assumptions
- Cross-links to sibling docs as `[backtick-path](backtick-path)` markdown links
- Direct, terse prose — no filler, no apologies, no narration of intent
