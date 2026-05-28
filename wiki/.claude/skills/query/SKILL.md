---
name: query
description: >
  Answer questions by reading and synthesising across the Sandbox Knowledge Hub wiki.
  Trigger when the user asks a question about wiki content, wants to find connections,
  asks "what does the corpus say about X", "how does X relate to Y", "summarise what
  we have on X", or wants cross-cutting analysis. Also trigger for sector-specific
  scoping ("what should I consider for an AI project in healthcare"), regulatory
  questions, comparisons, persona-specific framings ("for a startup", "for a
  public administrator"), and "find tensions / agreements about X". Do NOT trigger
  for operational questions about the wiki itself (file structure, linting) or for
  adding new sources (that's an ingest operation).
allowed-tools: Read, Glob, Grep
---

# Query

Answer questions by reading the wiki, following cross-references, and synthesising across pages with paragraph-anchored citations.

**The canonical procedure lives in [`wiki/QUERY.md`](../../../QUERY.md).** Read that file before answering any query. It contains the four-step procedure, voice rules, citation patterns, and don'ts.

Summary of the procedure (for quick orientation; the full version is in `QUERY.md`):

1. **Find relevant pages** — read `wiki/index.md` for the navigable inventory and the retrieval-priority quick reference.
2. **Read 3–5 pages, follow links** — walk `[[wikilinks]]` between pages; the answer often lives at the intersection.
3. **Synthesise** — cite inline source-voice forward, distinguish synthesis from single source, surface tensions, name gaps.
4. **(Optional) Suggest a contribution back** — flag patterns that deserve their own page, but don't create pages during a query.

The wiki is the source of truth. Answer from compiled wiki pages, not from training data. If the wiki doesn't cover something, say so explicitly and point at `index.md`'s *Open areas* section.

Default voice is neutral knowledge-transfer (explaining what the corpus shows), not sandbox-recruitment ("you should engage the sandbox"). Default audience is a non-technical administrator planning their own AI pilot, learning from the case studies — adapt to other personas only when the query makes one obvious.

Citation pattern (per `CONVENTIONS.md` §6): `[(<source-slug>#para-N)](sources/<source-slug>.md#para-N)`. Use Obsidian-style `> [!tension]` / `> [!gap]` callouts where they apply.

**Readability rule — wikilink discipline.** Wikilink named entities (projects, people, organisations, regulations, sources) inline — the slug reads as a noun. *Do not* wikilink principle or lesson slugs inline — they read as YAML filenames. Italicise the principle in prose; put the wikilink in parentheses on first mention only, and drop it on subsequent references. Soft cap: ≤3 wikilinks per paragraph in narrative prose; link-density is acceptable only in closing reading lists or `> [!see-also]` callouts. Full rule and examples in `QUERY.md`.

**Read `wiki/QUERY.md` now if you have not already.** It is the contract; this file is just the trigger.
