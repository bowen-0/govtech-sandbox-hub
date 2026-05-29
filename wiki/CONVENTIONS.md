# Wiki Conventions

> The schema, written as conventions rather than rules. Lint warnings will flag deviations; nothing here is enforced at write time. This file is the source of truth for **what a well-formed wiki page looks like** — but the schema is expected to evolve. See *How to evolve the schema* at the bottom.

---

## 1. File layout

```
wiki/
├── projects/           type: project
├── concepts/           type: concept
├── regulations/        type: regulation
├── stakeholders/       type: stakeholder
├── lessons/            type: lesson
├── sources/            type: source
├── synthesis/          type: synthesis
└── pdfs/               binary assets — not pages. PDFs sit under pdfs/de/, pdfs/en/, etc. and are linked from sources/<slug>.md.
```

One file = one entity. Folder determines type. Frontmatter `type:` must match the folder (this is the one hard invariant; the lint pass enforces it). `pdfs/` is the only folder without page-type semantics — it is the static-asset companion to `sources/`.

---

## 2. Frontmatter — the graph layer

Frontmatter is YAML. List-valued fields are typed edges in the implicit knowledge graph.

### Universal fields (every page)

```yaml
title: <human-readable title>     # English by default; see §5 on language
type: <project|concept|regulation|stakeholder|lesson|source|synthesis>
slug: <kebab-case>                # matches filename without .md; optional, inferred if absent
created: 2026-05-28               # ISO date the page was first written
updated: 2026-05-28               # ISO date of most recent meaningful edit
```

### Per-type fields

#### `projects/` — one page per sandbox pilot

```yaml
type: project
phase: I | II                     # which sandbox phase
year: 2023                        # publication year of the underlying report
status: completed | analysis-only # "analysis-only" = regulatory analysis without real-world testing
sector: healthcare | mobility | autonomous-systems | public-administration | education-and-work | construction | other
sources: [p2-building-permits]    # slugs from wiki/sources/
stakeholder: [stephanie-volz, raphael-von-thiessen, byte-studio]
regulation: [dsg-art-22, eu-ai-act]
concept: [data-access, llm-as-a-judge]
related_projects: [smart-parking] # other pilots this one references or extends
```

#### `concepts/` — reusable ideas / vocabulary

```yaml
type: concept
canonical_source: 00-overview-phase2-build-and-share#para-26-glossary   # if from the booklet glossary
related: [generative-ai, frontier-models]                                # other concepts in the same neighbourhood
appears_in: [p2-building-permits, p2-medical-documentation]              # projects where this concept is operative
```

#### `regulations/` — legal instruments

```yaml
type: regulation
jurisdiction: ch-federal | ch-canton-zh | ch-canton-other | eu | international
instrument: act | ordinance | standard | postulate | court-ruling | convention
domain: [data-protection, machinery-safety, medical-devices, ai-governance]
year: 2024                        # year of entry into force (or most recent revision)
project: [p2-building-permits]    # pilots where this regulation is operative
```

#### `stakeholders/` — people and organisations

```yaml
type: stakeholder
kind: person | org | role         # "role" for generic functions (e.g. "data-protection-officer")
partner_role: [test-partner, technical-implementation, mandated-expert, domain-sparring, supervisory-authority]
                                  # The 5-role taxonomy from the booklet p.8.
                                  # Pages may have multiple roles across different projects.
affiliation: <org-slug>           # only for kind: person
project: [p2-building-permits, p2-bridge-monitoring]
contact: <email or URL>           # optional, only for public-facing roles
```

#### `lessons/` — atomic transferable lessons (**the highest-value page type**)

```yaml
type: lesson
phase: I | II
project: [p2-building-permits]                                        # which pilot(s) the lesson is drawn from
concept: [data-access, pseudonymisation, partner-bottleneck]
regulation: [dsg-art-22, eu-ai-act-art-9]
stakeholder: [data-protection-officer, baudirektion-zh]
sources:
  - p2-building-permits#para-47                                       # required; paragraph-anchored
  - p2-building-permits#para-52
confidence: high | medium | low                                       # how transferable is this lesson?
freshness: 2026-04                                                    # source publication month; drives stale-warning UI
applies_to_lifecycle_stage: [scoping, procurement, deployment]        # optional, helps the generator filter
cross_cutting: true | false                                           # optional. Set true when the lesson is a general
                                                                      # principle the booklet states across multiple
                                                                      # pilots (e.g. anything in [[00-overview-phase2-build-and-share]]
                                                                      # §04 Technology/Legal/Organisation). The future
                                                                      # generator should weight these higher for
                                                                      # general queries vs. case-study-specific ones.
```

#### `sources/` — citation backbone

```yaml
type: source
source_type: pdf | url | paper | video | transcript | note | dataset
path: ../pdfs/de/p2-building-permits.pdf                              # for files (lives under wiki/pdfs/<lang>/)
en_path: ../pdfs/en/p2-building-permits.pdf                           # optional sibling for bilingual sources
url: https://...                                                       # for web sources (mutually exclusive with path)
language: en | de | bilingual                                          # source-content language
year: 2026
publisher: Canton of Zurich                                            # if known
authors: [raphael-von-thiessen, lukas-willi]                           # stakeholder slugs if known
paragraphs:                                                             # the anchor index, populated by the ingest pipeline
  - id: para-1
    page: 1
    text_preview: "..."                                                # first ~100 chars for human readability
```

#### `synthesis/` — cross-cutting patterns

```yaml
type: synthesis
connects: [p1-machine-translation, p2-medical-documentation, dsg-art-22]
# what does this synthesis weave together?
```

---

## 3. Page body — the prose layer

After frontmatter, write markdown prose. A few conventions:

- **First-level heading repeats the title.** `# {{title}}` as the first body line. Some renderers strip frontmatter; the H1 makes the page legible without it.
- **Cite paragraph anchors inline**, e.g. *"The prototype combines rule-based and generative AI [(p2-building-permits#para-23)](../sources/p2-building-permits.md#para-23)."* For now write the anchor URL by hand; later the build pipeline will resolve `[[p2-building-permits#para-23]]` shorthand.
- **Use `[[wikilinks]]`** for in-wiki cross-references. Resolved at render time to the matching file under any of the seven folders. Broken wikilinks are surfaced by the lint pass.
- **German verbatim quotations** for citation strength. Always keep the German exact, then translate into English in the surrounding sentence. Pattern:

  > *«AI can support building authorities, but the justification and responsibility for decisions remain with humans.»* (Volz, [p2-building-permits#para-25](../sources/p2-building-permits.md#para-25))

- **Callouts** for non-prose structure (Obsidian-compatible):
  - `> [!tension]` — pages making opposing claims (e.g. centralised vs. decentralised data handling).
  - `> [!gap]` — known unknowns; missing data or unanswered questions.
  - `> [!update-needed]` — flag for stale content; pair with the page's `freshness:`.

---

## 4. Taxonomies — soft enums

These are **starting sets** drawn directly from the corpus. Pages should use these values when they apply; pages may introduce new values; new values that recur 3+ times should be codified here.

### `sector` (from Build & Share booklet figure 1, p. 6 — the buckets the steering committee uses)

| Slug | Definition (from booklet) |
|---|---|
| `mobility` | Traffic data collection, visitor tracking, sensor-based bridge monitoring. |
| `autonomous-systems` | Autonomous inspection robots, autonomous machinery, drones. |
| `public-administration` | Semantic search, document understanding, chatbots for enquiries, AI-supported appeal decisions. |
| `education-and-work` | Vocational training environments, skills assessment, exam preparation. |
| `healthcare` | Medical documentation, health assistant, symptom diagnosis, ophthalmology AI. |
| `construction` | Building permits, construction project assistance. |
| `other` | Deepfake detection, humanitarian demining, raw material procurement, anti-littering. |

### `partner_role` (from Build & Share booklet p. 8 diagram — the 5 role types around a sandbox project)

| Slug | Definition (from booklet) |
|---|---|
| `test-partner` | Provides real-world application context, data, operational environment. |
| `technical-implementation` | Designs and builds prototypes, models, infrastructure. |
| `mandated-expert` | Contributes regulatory or domain expertise under a formal mandate. |
| `domain-sparring` | Informal expert exchange, validation, quality assurance — no formal mandate. |
| `supervisory-authority` | Provides oversight-perspective feedback, regulatory clarification. |

### `phase`

`I` (2022–2024) · `II` (2024–2026) · (Phase III is on the roadmap for 2026–2029 per the booklet conclusion.)

### `confidence` (on `lessons/`)

| Slug | When to use |
|---|---|
| `high` | Stated explicitly in a source, supported by the underlying evidence. Transferable claim. |
| `medium` | Reasonable inference across multiple sources; might not transfer to a different sectoral context. |
| `low` | Single source, anecdotal, or interpretation — useful but flag for revisit. |

### `source_type`

`pdf` · `url` · `paper` · `video` · `transcript` · `note` · `dataset`

---

## 5. Language

Working baseline:

- **Wiki body language is English by default.** Reason: the team's dev feedback loop is English; the German report content is preserved as **verbatim quotations** inline (see §3).
- **Source PDFs and verbatim citations stay in their original language**, almost always German. Never machine-translate a source quote.
- **Page slugs are English.** Filenames don't change with locale.
- **Titles are English.** German equivalents go in a `title_de:` frontmatter field when useful.

This is reversible. When the application UI is bilingual via `next-intl`, the wiki will likely grow `page.de.md` siblings for the pages that need them. Not yet.

---

## 6. Citation anchors — paragraph IDs

PDF citations use the syntax `<source-slug>#para-N` where `N` is the paragraph number assigned by the ingest pipeline.

Paragraph IDs are **stable across re-ingests of the same PDF**, achieved by deterministic chunking + checksum-on-anchor-resolution. If a citation resolves to a checksum mismatch, the lint pass flags it as broken and the page-level citation (`#page-12`) is used as fallback.

For non-PDF sources (URLs, transcripts), use the most stable available anchor: a CSS selector, a timestamp (`#t=2m14s`), or omit and cite the whole page.

---

## 7. How to evolve the schema

The schema is **soft by design**. The five rules:

1. **Folder names = page types.** Adding a new type means adding a folder + updating §1 here + adding a section in §2 with required fields. Don't add a folder lightly; ~7 is already a lot to hold in mind.
2. **Frontmatter fields are open.** A page can introduce a new field at any time. If the field appears on 3+ pages, **codify** it: add a row to the relevant §2 schema, set a default, decide if it's required.
3. **Taxonomies are open.** The soft enums in §4 are starting sets. Pages can introduce new values; values that recur 3+ times should be codified.
4. **Removal is harder than addition.** Deprecating a field or value requires touching every page that uses it. Prefer adding a new field and migrating gradually.
5. **Rationale lives next to the rule.** When a convention is updated, record the *why* in the change log at the bottom of this file — not in a separate decision doc.

---

## 8. Lint pass — what's checked

When the wiki has a build pipeline (post-hackathon), the lint pass will surface:

- Broken `[[wikilinks]]` — referenced slugs not found in any folder.
- Orphan pages — no incoming references from any other page.
- Type mismatch — `type:` value doesn't match folder.
- Missing required frontmatter — per the §2 spec for each type.
- Citation drift — `#para-N` anchor resolves to a different checksum than recorded.
- Conflicting `[!tension]` callouts that haven't been responded to (e.g. one page claims X, another claims ¬X, neither acknowledges the other).
- Stale `freshness:` (>18 months on a regulation; >12 months on a project).

Until the lint pass exists, these are conventions, not enforcement. Reviewers should still check at PR time.

---

## 9. What changed and when

| Date | Change |
|---|---|
| 2026-05-28 | Initial conventions file. Soft schema chosen over a triple-store knowledge graph for editability and substrate-portability. Sector taxonomy (§4) and partner-role taxonomy (§4) seeded from the Build & Share booklet (figure 1 p.6, role diagram p.8). |
| 2026-05-28 | Added `cross_cutting: true \| false` to the lesson schema. Used on lessons that are *general principles* drawn from [[00-overview-phase2-build-and-share]] §04 — these should retrieve before case-study-specific lessons for general queries. Codified after applying to 14 lessons in the same commit (well past the 3+ rule). Source: cross-cutting principles synthesis page `wiki/synthesis/phase-2-cross-cutting-principles.md`. |
| 2026-05-29 | Added `pdfs/` folder as a static-asset companion to `sources/`. All 23 source PDFs (DE + EN) live under `wiki/pdfs/{de,en}/`, and `sources/*.md` frontmatter `path:` / `en_path:` references them via `../pdfs/...`. Each `sources/<slug>.md` also carries a **Read the report** link under its H1. Rationale: the wiki is meant to be substrate-portable (per `README.md`) and hostable as static HTML — PDFs must live inside the deployable tree. |
