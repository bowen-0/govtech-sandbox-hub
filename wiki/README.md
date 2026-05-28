# Sandbox Knowledge Hub — Wiki

> The structured knowledge layer for the *AI Innovation Sandbox Knowledge Hub* (GovTech Hackathon Switzerland 2026 · challenge by Canton Zürich).

This folder is the **substrate**. Each markdown file is one entity. The folder it lives in determines its type. The YAML frontmatter is the graph. Every claim cites a paragraph in a source PDF.

If you only read one other file: [`CONVENTIONS.md`](CONVENTIONS.md). It defines the schema. If you only read two: also skim [`index.md`](index.md) — the auto-navigation across the whole wiki.

---

## What this is, in one paragraph

The Canton of Zürich runs the *Innovation Sandbox for Artificial Intelligence* — a regulatory + technical playground where public administration, businesses, and researchers pilot AI applications under real conditions. Across two phases (2022–2026) it produced ~13 detailed PDF reports. Those reports hold hard-won knowledge (legal frameworks, data access, organisational prerequisites, technical learnings) that today is locked inside static documents. **This wiki restructures that corpus as a navigable, citable, extensible knowledge base** so a non-technical administrator planning a new AI pilot can find what they need and trust where it came from.

The corpus is bounded but **the wiki is not**. New sources — papers, web pages, transcripts, news articles, future sandbox reports — can be added as first-class citizens. See `sources/` below.

---

## The seven folders

| Folder | What lives here | Required frontmatter |
|---|---|---|
| [`projects/`](projects/) | One page per sandbox pilot (10 today) | `type: project`, `phase`, `sector`, `sources` |
| [`concepts/`](concepts/) | Reusable ideas / vocabulary (data-access, pseudonymisation, edge-computing, intrapreneurship…) | `type: concept`, `related[]` |
| [`regulations/`](regulations/) | Legal instruments (DSG, EU AI Act, FADP, EU Machinery Reg, ISO/IEC 42001…) | `type: regulation`, `jurisdiction`, `domain[]` |
| [`stakeholders/`](stakeholders/) | People and organisations (DPO, ITSL-UZH, Stephanie Volz, MPAssist, ANYbotics…) | `type: stakeholder`, `kind` (person / org), `partner_role[]` |
| [`lessons/`](lessons/) | Atomic, transferable lessons. **The unit the future generator surfaces.** | `type: lesson`, `project[]`, `concept[]`, `sources[]`, `confidence`, `freshness` |
| [`sources/`](sources/) | One page per source artefact (PDF, URL, paper, video, transcript…). The citation backbone. | `type: source`, `source_type`, `path` *or* `url`, `language`, `year` |
| [`synthesis/`](synthesis/) | Cross-cutting patterns. Pages that weave multiple primary entries together. | `type: synthesis`, `connects[]` |

> The seven types are a **starting set** chosen because they map cleanly onto what the source corpus actually contains. They are *conventions*, not enforcement. If a new pattern keeps appearing in 3+ pages, propose a new folder (see `CONVENTIONS.md` → "How to evolve the schema").

---

## How to read this wiki

Two ways:

**As a human** — browse by type (folders above), or follow `[[wikilinks]]` between pages. Each page is self-contained and reads like a Wikipedia article. Citations resolve to a specific paragraph in a source PDF.

**As an LLM / retrieval system** — read [`index.md`](index.md) for the full navigable inventory, then read individual pages. Frontmatter is structured so you can filter (`type: lesson AND concept: data-access AND regulation: dsg-art-22`) without opening the prose.

---

## How to add to this wiki

Three common cases (full detail in [`CONVENTIONS.md`](CONVENTIONS.md)):

### Add a new source (PDF, paper, web page, video, transcript)
1. If it's a file, drop it into `../context/reports/` (or another sensible folder).
2. Create `sources/<slug>.md` with `type: source`, `source_type:` set to one of `pdf | url | paper | video | transcript | note`, plus `path` (for files) or `url` (for the web).
3. Optionally write the paragraph-anchor index in the same file (only needed for PDFs you intend to cite paragraph-level).

### Add a lesson
1. Read the source. Identify an atomic, transferable claim.
2. Create `lessons/<slug>.md` with `type: lesson`, link to `project[]`, `concept[]`, `regulation[]`, `stakeholder[]`, and cite the source with paragraph anchor.
3. Use `[[wikilinks]]` in the body wherever you reference another wiki entity.

### Add a concept
1. Confirm it's not already in `concepts/`.
2. Create `concepts/<slug>.md` with `type: concept`, a one-paragraph definition, and `related[]` to nearby concepts.
3. If the concept comes from the booklet glossary, mark `canonical_source:` to the relevant page in the booklet — these definitions are authoritative.

If you're unsure which type a page should be, **open an issue** using the "Propose a new concept/tag" template (`.github/ISSUE_TEMPLATE/`). Patterns we haven't seen yet are the patterns worth talking about.

---

## What this is *not*

- **Not a chat interface.** That's a later layer. The wiki is the substrate; UIs sit on top.
- **Not a knowledge graph in a triple store.** The graph lives in YAML frontmatter and is *exportable* to JSON-LD / DuckDB / Neo4j on demand. See [`../context/architecture-route.md`](../context/architecture-route.md) for the rationale.
- **Not a database with enforced schema.** Frontmatter conventions are linted, not validated. Easier evolution > stricter typing during the formative phase.
- **Not the only place truth lives.** The German PDFs in `../context/reports/de/` are the citation-authoritative ground truth. The wiki structures them; it does not replace them.

---

## Relationship to `../context/`

`../context/` holds the **prep material** for the hackathon — the challenge brief, the source PDFs, English digests of each report, and the pre-event decision docs (`architecture-route.md`, `frontend-route.md`, `data-architecture-walkthrough.md`, etc.). Those docs are the *why* behind the wiki's design. This folder is the *what* — the knowledge itself in the chosen substrate.

When the application repo is bootstrapped during the hackathon, it will live in a sibling folder (or take over the root) and **consume** `wiki/` as static input. The wiki is decoupled from the app on purpose.

---

## File-naming conventions (quick)

- `kebab-case-slugs.md`, ASCII only, no spaces.
- For PDFs that have both DE and EN versions, the wiki uses the language-neutral slug (e.g. `building-permits.md`, not `building-permits-en.md`).
- Sources use the same slug as their underlying file: `sources/p2-building-permits.md` ↔ `context/reports/{de,en}/p2-building-permits.pdf`.

Full naming + frontmatter rules in [`CONVENTIONS.md`](CONVENTIONS.md).
