# Contributing to the Sandbox Knowledge Hub Wiki

> **Handover doc for new contributors** — SMEs, challenge owners, or anyone granted access who wants to add a source, draft a lesson, or correct a page. Assumes you are starting from scratch.

This wiki is a folder of plain markdown files in a GitHub repo. Every claim cites a paragraph in a source PDF. You can contribute from three runtimes — pick the one that matches your access and what you want to do.

If you only read one other file: [`INGEST.md`](INGEST.md). It is the procedure. This file is the *operator's manual* — how to drive each runtime correctly. INGEST is the contract — what the output must look like, regardless of runtime.

---

## Who can do what

| Runtime                                | Add a new PDF (with anchors)        | Edit existing pages | Commit directly | Account needed                                  |
| -------------------------------------- | ----------------------------------- | ------------------- | --------------- | ----------------------------------------------- |
| **Cowork** (or local Claude Code)      | ✅ — full ingest with Docling        | ✅                   | ✅ via PR        | Claude.ai plan with Cowork + GitHub repo access |
| **Claude.ai Projects + GitHub**        | ⚠️ draft only (no Docling here)      | ✅                   | ✅ via connector | Claude.ai Pro + GitHub OAuth                    |
| **ChatGPT** (or any other web LLM)     | ⚠️ draft only                        | ⚠️ draft only        | ❌ — hand off    | Account on that LLM                             |

**Read this before picking:** new PDFs need paragraph anchors before the wiki will accept citations. That anchoring runs in a Python + Docling pipeline that only executes in Cowork or local Claude Code. If you draft against a new PDF in ChatGPT, the citations will be page-level (`p.17`) and a maintainer will backfill `#para-N` later. That is fine — but know it's a two-step process.

For editing what's already in the wiki (a new lesson from an existing source, a prose fix, a translation tweak), all three runtimes work fully.

---

## Path A — Cowork (recommended)

The skill is auto-loaded. You type `ingest`, the wiki tells you what to do.

1. **Get access.** Confirm with Bowen that your GitHub account is added to the repo. Confirm you have a Claude.ai plan that includes Cowork.
2. **Open the repo in Cowork.** Point Cowork at this GitHub repo. Open a session on the `main` branch (it will create a working branch for your changes).
3. **Drop the source in.** For a new PDF: copy it into `wiki/pdfs/de/` (German is citation-authoritative) and, if you have it, `wiki/pdfs/en/`. For pasted content, save to `wiki/sources/notes/<slug>.md` first. URLs and papers — just describe them in chat.
4. **Trigger the ingest skill.** Type one of: *"ingest p2-new-thing"*, *"process this report"*, *"compile this into the wiki"*. The `ingest` skill auto-loads. If it doesn't (older Cowork harness, skill not discovered), paste [`INGEST.md`](INGEST.md) into the chat and say "follow this procedure".
5. **Approval gate 1 — READ.** Cowork reads the source, reads `index.md`, and presents 3–5 takeaways. Discuss. Push back on anything that isn't actually new, that overstates a single-project finding, or that the corpus already covers.
6. **Approval gate 2 — PLAN.** Cowork proposes the file changes (new source page, new project page, lessons, pages to update). Review the plan. Skip lessons that aren't transferable. Add updates Cowork missed.
7. **EXECUTE.** Cowork writes the files. Watch the wiki grow.
8. **BOOKKEEP.** Cowork updates `index.md` and verifies no orphans, no broken `[[wikilinks]]`, every claim anchored. Read the diff.
9. **Commit and PR.** Per `CLAUDE.md`, commit specific paths, never `-A`. Open a PR. A maintainer reviews and merges.

If the source is a new PDF and `paragraphs: []` is empty on the source page, Cowork should run the Docling extraction before writing citations. If it doesn't, tell it to. The wiki contract says: **never invent an anchor.** Page-level fallback (`p.17`) is acceptable until anchors backfill.

---

## Path B — Claude.ai Projects + GitHub connector

Same model as Cowork (Claude), different harness. Good for editorial work on existing sources.

1. **Set up the Project.** Go to claude.ai → New Project. Name it "Sandbox Knowledge Hub — Ingest".
2. **Paste the procedure into the system prompt.** Open [`INGEST.md`](INGEST.md), copy the whole file, paste as the project's system instructions.
3. **Attach the schema and inventory.** Upload [`CONVENTIONS.md`](CONVENTIONS.md) and [`index.md`](index.md) as Project knowledge.
4. **Connect GitHub.** Project settings → connect the GitHub repo. This gives Claude read/write access to wiki files via the GitHub API.
5. **Drop the source in.** For a new PDF: upload it to the chat. For pasted content: paste it. For a URL: paste the URL (Claude will fetch).
6. **Drive the four-phase procedure manually.** Say "ingest this following INGEST.md". The skill won't auto-trigger here, but the system prompt does the same job.
7. **Approval gates work the same** — READ takeaways, then PLAN, then EXECUTE. You review at each gate.
8. **Commits happen via the connector** — Claude writes files into a branch, you confirm, the connector pushes. Open a PR through GitHub's web UI.

**Limitation:** the Docling pipeline does **not** run in this environment. For a brand-new PDF that needs anchoring, draft the source/project/lessons with page-level citations (`p.17`) and flag in the PR description that paragraph anchors need backfill. A maintainer with Cowork access closes that loop.

---

## Path C — ChatGPT (or any other LLM)

No GitHub access required. Output is a draft for handoff.

1. **Open a fresh chat.** GPT-4 or newer. (Same procedure works in Gemini, Mistral, etc.)
2. **Paste three files in order, in one message:**
   - The full text of [`INGEST.md`](INGEST.md)
   - The full text of [`CONVENTIONS.md`](CONVENTIONS.md)
   - The full text of [`index.md`](index.md)
3. **Paste the source content.** PDF text (extracted), notes, transcript, or URL contents.
4. **Prompt:** *"Follow the INGEST.md procedure. Start with phase 1: present 3–5 takeaways. Wait for me before proceeding to phase 2."*
5. **Walk through the four phases manually.** READ → discuss → PLAN → discuss → EXECUTE → BOOKKEEP. ChatGPT will produce markdown blobs for each new and updated page.
6. **Save the output.** Copy each markdown blob into a draft file locally, or paste them into a single handoff document.
7. **Send the drafts to a maintainer.** Either email/share with Bowen, or open a GitHub PR manually if you have web access to the repo. The maintainer reviews, runs the Docling pipeline if a new PDF was involved, and commits.

**Honest about the limits:** ChatGPT will guess at paragraph anchors if you don't watch carefully. The contract says *never invent an anchor*. Insist on page-level citations (`p.17`) when in doubt — the maintainer backfills. Also: ChatGPT will not check `index.md` orphans or `[[wikilink]]` resolution automatically. The maintainer handles bookkeeping on commit.

---

## What "correct ingest" looks like — the non-negotiables

Regardless of runtime, every contribution honours:

1. **Every substantive claim cites a source.** `[(source-slug#para-N)](sources/source-slug.md#para-N)` is the preferred form. `p.<N>` is the fallback. **Never invent a paragraph anchor.**
2. **German verbatim quotes stay German.** Translate in the surrounding prose, not in the quote itself. (See [`CONVENTIONS.md`](CONVENTIONS.md) §5.)
3. **Lessons are atomic.** One sentence stating the claim. If it needs two paragraphs, it's two lessons or it belongs in `synthesis/`.
4. **No orphan pages.** Every new page is linked from at least one other and listed in [`index.md`](index.md).
5. **Update existing pages too.** The highest-value integration is weaving the new source into existing concepts, stakeholders, regulations, and lessons. Don't just append.

A maintainer will spot violations on review. But spotting them yourself saves a round-trip.

---

## Where things live, in one paragraph

Source PDFs sit in [`wiki/pdfs/{de,en}/`](pdfs/). Each PDF gets a page in [`wiki/sources/`](sources/) describing it and listing its paragraph anchors. Each sandbox pilot gets a page in [`wiki/projects/`](projects/). The transferable claims extracted from a project become pages in [`wiki/lessons/`](lessons/) — these are the unit the future generative UI will surface. Reusable ideas go in [`wiki/concepts/`](concepts/), people and orgs in [`wiki/stakeholders/`](stakeholders/), laws and standards in [`wiki/regulations/`](regulations/), cross-cutting patterns in [`wiki/synthesis/`](synthesis/). The graph is the YAML frontmatter at the top of each file; the prose is the body. Both are plain markdown.

---

## If you get stuck

- **The skill isn't triggering in Cowork.** Paste [`INGEST.md`](INGEST.md) into the chat and say "follow this procedure". Same outcome.
- **You don't have Docling and the source is a new PDF.** Draft with page-level citations. Flag in the PR description: *"paragraph anchors pending — `paragraphs: []` empty"*. A maintainer with Cowork backfills.
- **You're not sure if an existing page exists.** Read [`index.md`](index.md). If it's not there, it doesn't exist (or `index.md` is stale — flag that too).
- **A claim spans two projects and you can't tell if it's cross-cutting.** It's `cross_cutting: true` only if it's stated as a general principle in `00-overview-phase2-build-and-share` §04 (or the Phase I equivalent). Otherwise, it's case-specific. When in doubt, default to false; the maintainer can promote.
- **You hit a tension between two sources.** Don't smooth it over. Add a `> [!tension]` callout per [`CONVENTIONS.md`](CONVENTIONS.md). Tensions are signal.

---

## Maintainer contact

For access, review, or anchor backfills: open a GitHub issue or contact the team listed in the project [`CLAUDE.md`](../CLAUDE.md).
