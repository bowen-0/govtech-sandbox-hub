# Architecture Route — Wiki vs Knowledge Graph

> Pre-hackathon decision doc for the AI Innovation Sandbox Knowledge Hub challenge. Lives next to [`README.md`](README.md); fulfils the §8 checklist item "sketch a 1-page rough architecture before Thursday." Working doc — update as Thursday Q&A with Lukas changes the picture.

---

## TL;DR — recommended route

**LLM-wiki as the substrate and the front-end, with knowledge-graph-shaped frontmatter as a queryable side-channel.**

Concretely: markdown pages (one per project / concept / regulation / lesson / stakeholder / source), Obsidian-style `[[wikilinks]]`, paragraph-anchored citations to the German PDFs, plus structured YAML frontmatter that can be exported to JSON-LD / DuckDB / Neo4j on demand for the "GraphRAG" secondary-goal demo.

This route is recommended because:
1. The four hard constraints from [`README.md`](README.md) §3 (non-technical audience, traceability, easy update, German UX) all favour prose over triples.
2. The corpus is tiny and bounded (~12 PDFs). The KG ergonomics tax doesn't earn its keep at this scale.
3. Bowen already has working muscle memory for this pattern via `~/Coding Projects/bowen-wiki/` (Karpathy-inspired LLM-wiki, ~170 wiki pages, weekly compilation rhythm). The schema, conventions, and ingest workflow port almost 1:1 to the sandbox corpus.
4. Frontmatter-as-graph keeps the "yes, this is also a knowledge graph" claim defensible to the jury without paying for a triplestore during the hackathon.

---

## The framing — why "wiki vs KG" is a false binary

Both routes produce a graph. The decision is **where the prose lives** and **how strict the edge types are**.

| | LLM-Wiki | Knowledge Graph |
|---|---|---|
| Node | A page of natural language | An entity (URI / ID) |
| Edge | `[[wikilink]]` — untyped or loosely typed | Predicate — strictly typed |
| Prose | Is the content | Sits in `rdfs:label` / `schema:description` |
| Schema enforcement | Frontmatter conventions (soft) | Ontology (hard) |
| Primary interface | Reading a page | Querying triples |
| Query power | LLM over prose + grep | SPARQL / Cypher multi-hop |
| Update cost | Edit a markdown file | Schema-aware reconciliation |

The brief at [`challenge/slides.pdf`](challenge/slides.pdf) slide 4 explicitly names both as acceptable primary goals — so the choice is about *fit to constraints*, not about following the brief.

---

## Scorecard against the brief's hard constraints

From [`README.md`](README.md) §3, plus the secondary goals from §2.

| Constraint | LLM-Wiki | Knowledge Graph | Why |
|---|---|---|---|
| Non-technical audience | 3/3 | 1/3 | Markdown pages read like Wikipedia. Triples/SPARQL/node-link UIs scare Verwaltungsmitarbeitende. |
| Traceability (claim → report) | 3/3 | 2/3 | Wiki: paragraph anchor lives inline. KG: needs explicit `prov:wasDerivedFrom` per triple. |
| Easy to update | 3/3 | 1/3 | Wiki: edit one file, re-ingest one PDF. KG: schema changes ripple; entity reconciliation is the hard part. |
| Sensitivity / legal hedging | 2/3 | 2/3 | Prose hedges naturally ("laut Bericht X …"). Triples force commitment unless reified. |
| Embeddability on zh.ch | 2/3 | 1/3 | Static HTML export is trivial. KG needs a SPARQL endpoint or flattens anyway. |
| German UX | 3/3 | 2/3 | Wiki: content IS German. KG: predicate names + UI chrome both need translation. |
| Demo-day surface area | 3/3 | 2/3 | Pages are browsable; graph viz is impressive once but hard to use. |
| **Structured multi-hop queries** | 1/3 | 3/3 | The one thing pure wiki loses. The hybrid recovers most of it via frontmatter. |
| Update-cycle "production thinking" signal to jury | 3/3 | 2/3 | "Drop a PDF, re-run ingest" is a 30-second live demo. |

---

## Recommended architecture (1-page sketch)

```
hackathon-repo/
├── context/                        # Existing — pre-event prep, untouched
├── reports/                        # Symlink or copy from context/reports/
│   ├── de/                         # Citation source (German — what the system cites)
│   └── en/                         # Reference only (English — for team prep)
├── wiki/                           # The LLM-maintained knowledge layer
│   ├── projects/                   # 1 page per pilot (10 pages)
│   │   └── p2-building-permits.md
│   ├── concepts/                   # Verantwortlichkeit, Datenzugang, Bias-Audit…
│   ├── regulations/                # DSG, EU AI Act, Maschinenverordnung, sektorale Gesetze
│   ├── lessons/                    # Atomic, transferable lessons across pilots
│   ├── stakeholders/               # Datenschutzbeauftragter, Fachstelle, etc.
│   ├── sources/                    # 1 page per PDF, with paragraph-anchored citations
│   └── synthesis/                  # Cross-pilot patterns (Phase I tech ↔ Phase II legal)
├── index.md                        # LLM-readable navigation (mirrors bowen-wiki pattern)
├── CLAUDE.md                       # Schema + ingest conventions, ported from bowen-wiki
├── ingest/                         # PDF → wiki pages pipeline
│   ├── chunk.py                    # Paragraph-level chunking with stable anchors
│   ├── extract.py                  # LLM extraction → frontmatter triples
│   └── build_graph.py              # Frontmatter → JSON-LD / DuckDB index for GraphRAG
├── app/                            # The user-facing surface
│   ├── pages/                      # Static-site export of wiki/ (Next.js or Astro)
│   ├── guideline-generator/        # "Describe your pilot → get checklist + lessons + citations"
│   └── admin/                      # Upload-new-report flow → re-runs ingest (update-flow demo)
└── README.md
```

### Frontmatter schema (the "graph" layer)

Every wiki page carries typed frontmatter. This is the bridge between human-readable prose and machine-queryable triples.

```yaml
---
title: Datenzugang bei der KI-Vorprüfung im Baugesuch
type: lesson
phase: II
project: [p2-building-permits]
concept: [datenzugang, datenpseudonymisierung]
regulation: [dsg-art-22, eu-ai-act-art-9]
stakeholder: [datenschutzbeauftragter, baudirektion-zh]
sources:
  - reports/de/p2-building-permits.pdf#para-47
  - reports/de/p2-building-permits.pdf#para-52
confidence: high
freshness: 2026-04
language: de
---
```

**Why this works as a graph substrate:**
- Every list-valued field is an edge: `regulation: [dsg-art-22]` ⇔ triple `<lesson:xyz> :touchesRegulation <reg:dsg-art-22>`.
- `sources:` with `#para-N` anchors gives `prov:wasDerivedFrom` for free.
- A 30-line script turns the whole `wiki/` tree into JSON-LD or seeds DuckDB / Neo4j for the GraphRAG demo.
- Updates remain markdown edits; the graph rebuilds on commit.

### The two demo surfaces

1. **Wiki reader** — browse pages. Each claim hyperlinks to the cited paragraph. This is what Verwaltungsmitarbeitende actually use day-to-day. Static HTML — embeddable on zh.ch via iframe or markdown-embed.

2. **Guideline generator** — text box: "I'm planning an AI pilot for [domain]." LLM does: frontmatter-filtered retrieval over `wiki/lessons/` and `wiki/regulations/` → ranks by tag overlap → returns 3–5 lessons + checklist + citation cards with PDF previews. This is the "GraphRAG" secondary-goal demo and the pitch hero shot.

---

## When to flip and go pure-KG instead

These are kill-switch conditions, not preferences. If any one fires, revisit the choice on Thursday morning.

1. **Team has a graph-DB native** who would otherwise be underused. Then LINDAS + Neo4j + Cypher becomes a differentiator, and the Thursday 15:00 LINDAS mentoring slot becomes a real lever (see [`README.md`](README.md) §5).
2. **Lukas Willi confirms at Thu 09:30** that downstream consumers expect SPARQL / LINDAS interoperability. zh.ch is Linked Data-active; worth asking.
3. **The wider field converges on a single approach.** If most submissions cluster around RAG/chatbot patterns, a graph-shaped submission becomes a stronger differentiation play. Use the differentiation risk-budget deliberately.

---

## Open questions to resolve before locking in

Move these into [`README.md`](README.md) §8's pre-event checklist or the Thursday Q-list for Lukas.

- [ ] **Team composition** — graph person on the team, or RAG/web-dev-shaped? (Determines whether the kill-switch above fires.)
- [ ] **For Lukas, Thu 09:30** — is there a downstream expectation to connect to LINDAS or other cantonal Linked Data infrastructure? (Load-bearing for substrate choice.)
- [ ] **For Lukas, Thu 09:30** — what's the expected refresh cadence and who maintains post-hackathon? (Validates the "markdown edit = update" demo.)
- [ ] **Primary user moment** — does the system answer in prose-with-citations (wiki-shaped) or show a filtered subgraph of analogous projects (KG-shaped)? Pick the one demo-able in 5 minutes.
- [ ] **GraphRAG ambition** — is the secondary-goal demo a "yes, the frontmatter is also a graph" tech-credibility moment, or a load-bearing user-facing feature? (Determines how much polish the graph layer needs.)

---

## What ports directly from `bowen-wiki`

Bowen's existing wiki at `~/Coding Projects/bowen-wiki/` is a working instance of this exact pattern. The following ports near-1:1:

| From bowen-wiki | To hackathon repo | Adjustment |
|---|---|---|
| `CLAUDE.md` schema (frontmatter, page types, conventions) | `CLAUDE.md` | Swap domains (systems-thinking → sandbox-pilots); add `phase` and `regulation` fields. |
| `index.md` navigation pattern | `index.md` | Domain becomes "by phase" and "by topic"; add a "by regulation" cross-cut. |
| `wiki/people/`, `wiki/concepts/`, `wiki/frameworks/`, `wiki/sources/` directory shape | `wiki/projects/`, `wiki/concepts/`, `wiki/regulations/`, `wiki/lessons/`, `wiki/stakeholders/`, `wiki/sources/` | Rename to domain entities; add `wiki/lessons/` as the atomic-extractable unit. |
| Ingest workflow (source → source-page → touch existing pages → cross-reference) | Same pipeline, automated via `ingest/` scripts | Add deterministic chunking with stable paragraph anchors for citation. |
| Wiki-link discipline + `[!gap]` / `[!tension]` callouts | Same | Useful for "this lesson contradicts that report" cases the jury will appreciate. |
| Lint workflow (orphans, broken links, contradictions) | Same | Become the "quality" tab of the admin UI. |

What does NOT port:
- Weekly compilation rhythm — replaced by automated ingest because the corpus is bounded.
- `seeds/` lifecycle — no content-idea layer needed for the hackathon.
- Project tags — replaced by `phase` + `project` frontmatter.
- Monolingual constraint — bowen-wiki is English. Sandbox hub is bilingual: report content stays German (citations quote source PDFs verbatim), code and internal docs are English, UI is English during dev with German layered in via i18n. See [`frontend-route.md`](frontend-route.md) "Language orientation" for the full split.

---

## Decision log

| Date | Note |
|---|---|
| 2026-05-27 | Initial doc. Recommendation: wiki-first with KG-shaped frontmatter. Pending validation: team composition, LINDAS expectation (Thu 09:30 with Lukas). |
| 2026-05-27 | Clarified language split (see [`frontend-route.md`](frontend-route.md) decision log): dev English-first, report content stays German, UI bilingual via i18n. |
