# Data Architecture Walkthrough — Sandbox Knowledge Hub

> Concrete view of the **data substrate** for the AI Innovation Sandbox Knowledge Hub challenge. Sibling to [`team-handout.md`](team-handout.md) (which covers the UX). Full architectural rationale in [`architecture-route.md`](architecture-route.md). Designed to be read in 5-10 minutes by anyone joining the team.

---

## The data layer in one sentence

> **A folder of markdown files where each file is one entity, the folder structure is the schema, the YAML frontmatter is the graph, and every claim cites a paragraph in the source PDF.**

This is the primary deliverable per the brief ("Strukturierung / Aufbereitung der Datenbasis") — the UI is what makes it visible, but the substrate is what makes it credible.

---

## What's actually on disk

```
wiki/
├── projects/        ~10 files — one per sandbox pilot
├── concepts/        ~15-20 files — data-access, bias-audit, pseudonymisation, edge-computing…
├── regulations/     ~10 files — DSG-Art-22, EU-AI-Act, FADP, EU-Machinery-Reg…
├── stakeholders/    ~8 files — DPO, ITSL-UZH, Stephanie-Volz, Baudirektion-ZH…
├── lessons/         ~30-50 atomic transferable lessons across pilots
├── sources/         12 files — one per source PDF with paragraph-anchor index
└── synthesis/       ~5 cross-cutting pattern pages (Phase-I-tech vs Phase-II-legal, etc.)
```

Each file is one node. The folder it lives in determines its **type** (which determines what frontmatter fields it must have and how it's rendered in the UI).

---

## Anatomy of one wiki page

Here is what `wiki/lessons/data-access-building-permits.md` actually looks like on disk:

```yaml
---
title: Data access for AI pre-check in building permits
type: lesson
phase: II
project: [building-permits]
concept: [data-access, pseudonymisation, partner-bottleneck]
regulation: [dsg-art-22, eu-ai-act-art-9]
stakeholder: [data-protection-officer, baudirektion-zh, ebaugesuche-platform]
sources:
  - reports/de/p2-building-permits.pdf#para-47
  - reports/de/p2-building-permits.pdf#para-52
confidence: high
freshness: 2026-04
language: en
source-language: de
---

# Data access for AI pre-check in building permits

Accessing historical building permit submissions for model training
required an [[ebaugesuche-platform]] data-access agreement and a
[[pseudonymisation]] step before any training corpus could be assembled.

The [[data-protection-officer]] required that the pseudonymisation
process itself be auditable — see [[dsg-art-22]] on automated
individual decisions.

> [!tension] Conflicts with [[medical-documentation]]
> Medical Documentation argued for decentralised data handling based
> on cantonal hospital constraints; this pilot adopted centralised
> handling. Compare and choose deliberately for your context.

## Why this matters for new pilots
…
```

The whole product is in this microcosm:

- `type: lesson` → lives in `wiki/lessons/`, rendered as a `<LessonCard>` in the generator
- `project: [building-permits]` → typed edge to `wiki/projects/building-permits.md`
- `regulation: [dsg-art-22]` → typed edge to `wiki/regulations/dsg-art-22.md`
- `sources: […#para-47]` → the PDF slideover knows exactly where to scroll and highlight
- `[[pseudonymisation]]` → inline wikilink resolved at render time to a concept page
- `[!tension]` callout → surfaces in the UI as a yellow contradiction card
- `freshness: 2026-04` → drives the "as-of" badge and the soft-warning chip for pre-2024 content

---

## The seven page types

| Folder | Type | What it represents | Frontmatter must include |
|---|---|---|---|
| `projects/` | A pilot | One sandbox project | `phase`, `status`, `year`, `stakeholder`, `regulation`, `sources` |
| `concepts/` | A reusable concept | data-access, bias-audit, edge-computing | `project[]` (where it appears), `related[]` |
| `regulations/` | A legal instrument | DSG Art. 22, EU AI Act, etc. | `jurisdiction`, `domain[]`, `project[]` |
| `stakeholders/` | A person/org | DPO, ITSL-UZH, Baudirektion | `role`, `project[]`, optional `contact` |
| `lessons/` | An atomic transferable lesson | The unit the generator surfaces | `project[]`, `concept[]`, `regulation[]`, `stakeholder[]`, `sources[]`, `confidence`, `freshness` |
| `sources/` | A source PDF | One file per report | `path`, `language`, `year`, `paragraphs[]` (the anchor index) |
| `synthesis/` | A cross-cutting pattern | "Phase I is technical, Phase II is legal" | `connects[]` (which pages it weaves together) |

The **`lessons/`** folder is the most important. Lessons are what the generator surfaces, what the user copies into their internal memo, what makes the system more than a search box over PDFs.

---

## From PDF to wiki — the ingest journey

When `report-medical-documentation.pdf` arrives, the pipeline does roughly this:

```
report-medical-documentation.pdf
   │
   ▼
1. Chunk into paragraphs with stable IDs
   → 47 paragraph chunks with anchors #para-1 … #para-47
   │
   ▼
2. Create the source page
   → wiki/sources/medical-documentation.md
     (paragraph index, language, year, full PDF path)
   │
   ▼
3. LLM extraction passes (Claude Sonnet, pydantic-typed outputs)
   ├─ Entities  → 3 new stakeholders, 2 new regulations, 4 concepts
   ├─ Lessons   → 6 atomic lessons (created in wiki/lessons/)
   └─ Project metadata → wiki/projects/medical-documentation.md updated
   │
   ▼
4. Cross-link pass
   → Scan all wiki pages, resolve [[wikilinks]], rebuild backlinks index,
     touch 12 existing pages that gain a reference
   │
   ▼
5. Lint pass
   → Orphans: 0
     Broken links: 0
     Contradictions detected: 1 (data-handling vs. building-permits)
     Missing sources: 0
   │
   ▼
6. Diff + publish
   → 3 new pages, 12 updated, 1 new tension surfaced
```

This is what Lukas sees streaming live on the Admin surface. Each step is a typed, idempotent operation — re-running the ingest produces the same result.

---

## From user query to generator output — the retrieval journey

When a user types *"AI to pre-check solar building permits"*:

```
user query (free text)
   │
   ▼
1. LLM classifies the query (Haiku, fast, cheap)
   → {domain: building-permits, technique: image-classification,
       lifecycle: scoping, regulations_likely: [dsg-art-22]}
   │
   ▼
2. Frontmatter filter (deterministic, sub-millisecond)
   → wiki/lessons/* WHERE
       (concept ∩ [data-access, image-classification, ...] ≠ ∅) OR
       (project ∩ [building-permits, smart-parking] ≠ ∅) OR
       (regulation ∩ [dsg-art-22] ≠ ∅)
   → returns ~20 candidate lesson pages
   │
   ▼
3. LLM rerank (Sonnet, 1 call with all candidates)
   → keeps 5-8 most relevant to user's specific framing
   │
   ▼
4. Component selection (same LLM call, structured output)
   → For each kept page, choose component kind:
     - This is a regulation reference  → RegulationCallout
     - This is an atomic lesson         → LessonCard
     - These two contradict             → TensionCallout
     - These 4 are similar pilots       → ProjectCompareTable
     - 8 action items extracted         → ChecklistFromLessons
   │
   ▼
5. Stream to UI
   → Components fade in section by section as the model emits each one
   → Each component reads its source wiki page at render time
   → Citations are typed props, not generated text
```

The crucial property: **the generator never invents claims**. It picks structure, then defers to the wiki for content. That is how H3 (no hallucination — see [`success-criteria.md`](success-criteria.md)) is solved structurally rather than by prompting.

---

## What "the graph" looks like in practice

Take one project — Building Permits — and look at its frontmatter neighborhood:

```
                            ┌──────────────────┐
                            │ projects/        │
                            │ building-permits │
                            └─┬────────────────┘
                              │
            ┌─────────────────┼─────────────────┬────────────────┐
            ▼                 ▼                 ▼                ▼
     ┌────────────┐    ┌─────────────┐   ┌──────────────┐   ┌──────────┐
     │ lessons    │    │ regulations │   │ stakeholders │   │ sources  │
     │ (12 pages) │    │ (5 pages)   │   │ (4 pages)    │   │ p2-bp.pdf│
     └────────────┘    └─────────────┘   └──────────────┘   │ 47 paras │
            │                 │                 │           └──────────┘
            │                 │                 │
            ▼                 ▼                 ▼
     ┌────────────────────────────────────────────┐
     │ concepts/ — shared with other pilots       │
     │ data-access, pseudonymisation,             │
     │ partner-bottleneck                         │
     └────────────────────────────────────────────┘
            │
            ▼
     ┌────────────────────────────────────────────┐
     │ ⚠ tensions — contradictions                │
     │ data-handling vs. medical-documentation    │
     └────────────────────────────────────────────┘
```

Every arrow is a typed frontmatter edge. The whole structure is queryable as JSON-LD if anyone asks; it is also just markdown files anyone can edit.

---

## The three operations this data layer enables

1. **Faceted retrieval** — *"show me lessons where `concept=data-access` AND `regulation=eu-ai-act`"* returns a small typed set in milliseconds. No vector math. This is what makes the left-rail filters work and the generator's first retrieval pass fast.
2. **Cross-pilot pattern surfacing** — lessons that reference multiple projects in their frontmatter ARE the patterns. Sorting `wiki/lessons/*` by `len(project) > 1` surfaces them automatically.
3. **Tension detection** — the lint pass finds pairs of pages making opposing claims with overlapping `concept` tags. These become the `[!tension]` callouts the jury notices.

---

## How this compares to alternatives

| Alternative | Problem |
|---|---|
| **Pure vector RAG** (embeddings + cosine over PDF chunks) | No typed retrieval; can't easily filter by regulation; citations are page-level not paragraph-level; no place for transferable lessons that span projects; updates require re-embedding. |
| **Pure knowledge graph** (Neo4j / triple store / SPARQL) | Hard to edit by non-developers; prose has nowhere natural to live; schema changes are expensive; legal hedging is awkward to encode as triples; deployment infra alone eats half the hackathon. |
| **Our hybrid (wiki-with-frontmatter)** | Markdown is the substrate everyone can edit. Typed frontmatter gives 80% of KG querying. Prose hedging stays natural. Graph exports on demand if anyone wants it. |

---

## What this looks like at the end of day 1

Concretely, by Thursday end-of-day, the disk state should be:

```
wiki/
├── projects/building-permits.md       ← hand-written from digest
├── projects/smart-parking.md          ← hand-written from digest
├── projects/medical-documentation.md  ← hand-written from digest
├── lessons/data-access-building-permits.md      ← seeded by hand
├── lessons/pseudonymisation-public-data.md      ← seeded by hand
├── lessons/centralised-vs-decentralised-data.md ← seeded with [!tension]
├── regulations/dsg-art-22.md
├── stakeholders/data-protection-officer.md
├── concepts/data-access.md
└── sources/p2-building-permits.md     ← with #para anchors
```

That is enough for the generator to produce a real briefing for a real query (building permits + solar). Day 2 the ingest pipeline backfills the rest from the remaining 9 PDFs.

---

## Open decisions / risks

1. **Lessons-extraction is the LLM step with the most leverage.** Atomic, transferable, well-cited lessons are what makes the generator feel intelligent. Worth a half-day of prompt-engineering on day 1.
2. **Paragraph-anchor stability across re-ingests** is the single technical risk that could kill the PDF slideover demo. Deterministic chunking + checksum-on-anchor-resolution is the mitigation; if it slips, render page-level citations instead and lose some "wow."
3. **Hand-seeded vs. fully-LLM-extracted wiki**: day 1 hand-seed 3-5 lessons to control the demo's quality. Day 2 the pipeline produces the rest at lower polish. Discuss the right balance with the team.
4. **Schema lock-in** — once committed to the seven page types and their frontmatter, changing them ripples. Lock by Thursday lunch.
5. **Bilingual content strategy** — wiki pages can have English titles + German body (citation quotes are German), or fully bilingual via filename suffix (`page.de.md` / `page.en.md`). The first is simpler; the second is more honest if shipping DE default. Decide once language-default is decided.

---

## Where to read more

- [`architecture-route.md`](architecture-route.md) — full substrate decision (wiki vs KG, scorecard, kill-switches)
- [`frontend-route.md`](frontend-route.md) — how this substrate becomes the three UI surfaces
- [`team-handout.md`](team-handout.md) — the UX side of the picture
- [`success-criteria.md`](success-criteria.md) — which constraints from the brief this substrate addresses
- [`digests/`](digests/) — the source material this wiki structures
