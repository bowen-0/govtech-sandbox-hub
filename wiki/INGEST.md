# Ingesting a Source into the Sandbox Knowledge Hub Wiki

> The canonical ingest procedure for this wiki. If you (the LLM / human contributor) want to add a new source — a sandbox report PDF, a paper, a URL, a transcript — this file is the contract.

This wiki is designed to be substrate-portable. The ingest procedure travels with it. It is auto-loaded as a Claude Code / Cowork / Claude Agent SDK skill from [`.claude/skills/ingest/SKILL.md`](.claude/skills/ingest/SKILL.md) when this folder is the working directory. For any other runtime — Claude.ai Projects with a GitHub connector, a custom GPT, a raw API call — paste this file as system instructions plus [`CONVENTIONS.md`](CONVENTIONS.md) and [`index.md`](index.md) as context. The procedure is identical across runtimes; only the file-I/O and tooling mechanism differs.

**Recommended runtime for ingest: Cowork or local Claude Code.** Other runtimes work for *editorial* operations on already-ingested sources, but the paragraph-anchoring step (see the contract below) needs a real execution environment.

---

## The contract

The wiki is the source of truth, and the citation backbone is paragraph-anchored to source PDFs. **Every substantive claim added to the wiki must trace to a paragraph in a source.** If you can't cite, you can't add it.

Three rules follow from that:

1. **Never invent a paragraph anchor.** Anchors come from the Docling extraction pipeline, not from your reading of the PDF. If anchors aren't available for this source yet, fall back to page-level citation (`p.17`) and flag the source page's `paragraphs: []` for backfill.
2. **Never machine-translate a German verbatim quote.** Source PDFs are German; quotes stay exact. Translate in the surrounding prose. See [`CONVENTIONS.md`](CONVENTIONS.md) §5.
3. **Ingest is collaborative, not automated.** The procedure has four phases and requires user approval at the end of phases 1 and 2. The discussion shapes the output.

[`CONVENTIONS.md`](CONVENTIONS.md) is the schema spec — frontmatter, taxonomies, callout syntax, citation anchor syntax. Read it before executing. This file is the *procedure*; CONVENTIONS is the *contract*.

---

## Procedure

### Phase 1 — READ

1. **Determine the source and where it lives.** Common cases:
   - Sandbox project report: `pdfs/{de,en}/p<phase>-<slug>.pdf` — German is citation-authoritative
   - Phase-overview booklet: `00-overview-phase<N>-...` — contains the cross-cutting principles
   - External paper / web URL / video / transcript / dataset — see [`CONVENTIONS.md`](CONVENTIONS.md) §2 for `source_type` values
   - Pasted content in conversation — save the raw text to `pdfs/notes/<slug>.md` so future ingests can re-resolve citations
2. **Read [`index.md`](index.md)** — the navigable inventory of every existing page. Note which projects, concepts, regulations, stakeholders, lessons, and synthesis pages already exist. This is what you'll integrate with, not just add to.
3. **Read [`CONVENTIONS.md`](CONVENTIONS.md) §2 (frontmatter) and §3 (page body)** — the schema you'll write to. Re-skim §4 (taxonomies) if the source touches a sector or partner-role you haven't ingested before.
4. **Read the source content itself.** Identify:
   - **Project facts** — sector, phase, partner orgs, timeline, outcomes, deployment status (`completed` vs `analysis-only`)
   - **Stakeholders named** — people and organisations, plus their `partner_role` (test-partner, technical-implementation, mandated-expert, domain-sparring, supervisory-authority)
   - **Regulations engaged** — Swiss federal/cantonal + EU + standards
   - **Concepts used** — especially ones not yet in `concepts/`
   - **Atomic transferable lessons** — the highest-value extractions. See [`lessons/integrate-regulation-early.md`](lessons/integrate-regulation-early.md) for the shape: one sentence stating the claim, one verbatim quote establishing it, one bullet per supporting project
   - **Paragraph anchors** — if the source page's `paragraphs:` index already exists (from a prior Docling run), use those IDs. If not, note paragraphs by page + opening words for later backfill
5. **Present 3–5 key takeaways to the user.** Frame as: what's *new* here, what does this *reinforce* across the existing corpus, what does this *challenge*?

**Wait for the user before proceeding.** This is the first approval gate.

### Phase 2 — PLAN

After discussion, present a structured plan. Use the shape below — file-pathed, type-tagged, no abstract bullet lists:

```
Source page:    sources/<slug>.md                       (type: source)
Project page:   projects/<slug>.md                      (type: project)
                — or update if it already exists
Lessons to CREATE (highest-value output):
  - lessons/<slug>.md                                   (cross_cutting: ?)
  - lessons/<slug>.md
Pages to UPDATE (highest-value integration):
  - concepts/data-access.md           — add project to appears_in[]; weave a subsection
  - stakeholders/stephanie-volz.md    — add project to project[]
  - regulations/dsg-fadp.md           — add lesson cross-reference if engaged
  - synthesis/phase-2-cross-cutting-principles.md — add lesson if cross_cutting
Cross-references to add:
  - [[new-concept]] linked from [[adjacent-existing-concept]]
  - > [!tension] callout where this source disagrees with an existing page
New stakeholders / regulations / concepts to CREATE:
  - stakeholders/<slug>.md            (kind: person, partner_role: [...])
  - regulations/<slug>.md             (jurisdiction: ..., instrument: ...)
```

Present the plan and wait for approval. The user may:

- Skip a proposed lesson ("not transferable — that's a single-project quirk")
- Promote or demote `cross_cutting:` on a lesson
- Flag an existing page that needs updating but you missed
- Override the proposed taxonomy values (sector, partner_role, instrument)
- Add a tension callout you didn't surface

**This is the second approval gate.** Don't write files before approval.

### Phase 3 — EXECUTE

Write the pages per the approved plan. Page formats are defined in [`CONVENTIONS.md`](CONVENTIONS.md) §2 (frontmatter) and §3 (body). The anchors below are quick orientation; CONVENTIONS is the spec.

**Source page** (`sources/<slug>.md`):

- Filename = `p<phase>-<slug>` for sandbox reports; bare `<slug>` for other source types
- Frontmatter per CONVENTIONS §2 `sources/`. Include `path` (file) *or* `url` (web), `language`, `year`, `publisher`, `authors[]` (as stakeholder slugs)
- Body shape: H1 (repeats the title), one framing paragraph, **Provenance**, **Use as citation**, **See also** with `[[wikilinks]]`
- Canonical example to model: [`sources/p2-building-permits.md`](sources/p2-building-permits.md)
- **Populate `paragraphs:`** if a Docling-produced index exists. Otherwise leave `paragraphs: []` and note in the body that the anchor index is pending. Never fabricate paragraph IDs

**Project page** (`projects/<slug>.md`):

- Filename drops the `p<phase>-` prefix; phase lives in frontmatter (`phase: I | II`)
- Frontmatter per CONVENTIONS §2 `projects/`. Use `status: analysis-only` for projects without real-world deployment
- Body uses paragraph-anchored citations: `[(p2-building-permits#para-25)](../sources/p2-building-permits.md#para-25)`
- Preserve German verbatim quotes; translate in surrounding prose
- Cross-link to all relevant existing entities — stakeholders, regulations, concepts, related projects — using `[[wikilinks]]`

**Lessons** (`lessons/<slug>.md`) — the highest-value output type:

- One lesson = one **atomic, transferable** claim. If a candidate takes more than a paragraph to state, it's two lessons or it's a synthesis page
- Frontmatter per CONVENTIONS §2 `lessons/`. Required: `phase`, `project[]`, `sources[]` (paragraph-anchored), `confidence`, `freshness`
- Set `cross_cutting: true` *only* when the lesson is stated as a general principle in `00-overview-phase2-build-and-share` §04 Technology/Legal/Organisation (or the Phase I equivalent). This flag is a retrieval-priority boost; don't apply it loosely
- Body shape: H1 = the full lesson statement (one sentence), then a verbatim quote from the source establishing it, then **Evidence base** with one bullet per supporting project, then **How to apply** with concrete steps, then **See also**
- Canonical example to model: [`lessons/integrate-regulation-early.md`](lessons/integrate-regulation-early.md)

**Updates to existing pages** (the highest-value integration step — don't skip this):

- **Concept pages**: add the new project to `appears_in[]` frontmatter; weave a subsection in the body that *positions* this source against existing ones (agreement / nuance / contradiction / different vocabulary). Don't just append a paragraph
- **Stakeholder pages**: add the new project to `project[]` frontmatter; add one line of body context (what role did they play in this project)
- **Regulation pages**: add the new project to `project[]`; if the source provides a substantive interpretation or counter-case, add it to the body
- **Lesson pages**: if the new project supports an existing lesson, add it to `project[]` and add a bullet to the **Evidence base** section
- **Synthesis pages** (especially [`synthesis/phase-2-cross-cutting-principles.md`](synthesis/phase-2-cross-cutting-principles.md)): if a new cross-cutting lesson was extracted, link it into the appropriate Technology / Legal / Organisation subsection

**Wikilink discipline at write-time** (same rule as the query layer — see [`QUERY.md`](QUERY.md) for the full version):

- **Entity wikilinks** — projects, people, organisations, regulations, sources. The slug reads as a noun; use them inline freely
- **Principle / lesson wikilinks** — slugs like `ai-is-rarely-the-primary-challenge` read as YAML filenames mid-sentence, not as nouns. Italicise the principle in prose; put the wikilink in parentheses on first mention only, drop it on subsequent references
- **Soft cap**: ≤3 wikilinks per paragraph in narrative prose. The `See also` section and closing reading lists don't count

**German verbatim quote pattern** (CONVENTIONS §3):

> *«AI can support building authorities, but the justification and responsibility for decisions remain with humans.»* [(p2-building-permits#para-25)](sources/p2-building-permits.md#para-25)

The German stays exact. The English translation is the surrounding sentence, not a replacement for the quote.

### Phase 4 — BOOKKEEP

1. **Update [`index.md`](index.md)**:
   - Add the new project under "By type → Projects → Phase I/II" with one-line summary and sector tag
   - Add new lessons under "Lessons" — split between cross-cutting and case-study-specific
   - Add new concepts under "Concepts" (booklet-glossary vs derived subgroup)
   - Add new sources under "Sources"
   - Add new stakeholders under the appropriate "Stakeholders" subgroup
   - Update the *By sector* and *By phase* sections if the new project enters a bucket
   - **Cross-reference the *Open areas* list** — if your ingest fills a known gap, strike it off the list

2. **Verify no orphans**:
   - Every new page is linked from at least one other wiki page (the project page is the natural anchor for new lessons; the lesson page is the natural anchor for new concepts; the source page is the natural anchor for new stakeholders)
   - Every new page is listed in `index.md` in the right section

3. **Verify no broken `[[wikilinks]]`**:
   - Quick grep: `grep -oE '\[\[[a-z0-9-]+\]\]' <new-files>` then check each slug resolves to a real file under any of the seven folders. Either create the missing page or remove the link. Broken wikilinks will be caught by the future lint pass — don't leave them for it

4. **Verify the citation backbone**:
   - Every substantive claim in every new page traces to either `<source-slug>#para-N` (preferred) or `p.<N>` page-level (fallback)
   - If anchors weren't available, the source page's `paragraphs: []` is empty and the body notes "anchor index pending"
   - No invented anchors

5. **Suggest a commit**. Per CLAUDE.md, commits are deliberate — `git add` specific paths, not `-A`. List the new and updated files; let the user pick the boundary. A typical sandbox-report ingest is one commit; a multi-source synthesis run is often two.

---

## Source-type specifics

**Sandbox project reports (PDF — the canonical case).** `pdfs/{de,en}/p<phase>-<slug>.pdf`

- Highest density. Expect: 1 source page + 1 project page + 2–6 lessons + 3–10 page updates
- German PDF is the citation-authoritative version per CONVENTIONS §5. The English PDF is a translation aid; never cite from it as primary
- Always populate stakeholders for named project participants (test partner, technical implementation, mandated expert, supervisory authority)
- Always cross-check `regulations/` before creating a regulation page — most relevant Swiss + EU instruments are already there

**Phase-overview booklets.** `00-overview-phase<N>-...`

- Contain the cross-cutting principles (§04 Technology / Legal / Organisation in the Phase II booklet)
- Lessons extracted from these are nearly always `cross_cutting: true`
- The booklet's glossary (Phase II: `#para-26-glossary`) is the canonical source for concept definitions. When creating a concept from the glossary, set `canonical_source:` per CONVENTIONS §2 `concepts/`

**External papers, web sources, videos, transcripts, datasets.**

- Lower volume, narrower contribution. Often 1 source page + 1 lesson + 1–2 page updates
- For URLs, set `url:` (mutually exclusive with `path:`); for videos, anchor by timestamp (`#t=2m14s`); for transcripts, anchor by speaker turn or timestamp; for datasets, point at the canonical location
- Lower-confidence sources warrant `confidence: medium` or `low` on derived lessons. CONVENTIONS §4 defines when to use each

**Pasted content in conversation.**

- Save the raw text to `pdfs/notes/<slug>.md` first — without a persisted source, future ingests can't re-resolve citations
- Then ingest as any other source

---

## Anti-patterns

- **Never invent paragraph anchors.** Use page-level fallback (`p.17`) and flag for backfill
- **Never machine-translate German verbatim quotes.** Preserve exact; translate in surrounding prose
- **Never create orphan pages.** Every new page is linked from at least one other + listed in `index.md`
- **Never modify source PDFs in `pdfs/`.** Immutable
- **Never auto-run an ingest.** READ → PLAN → EXECUTE → BOOKKEEP requires user approval at the end of phases 1 and 2
- **Never write a lesson that takes more than a paragraph to state.** Split it, or promote it to a synthesis page
- **Never set `cross_cutting: true` without booklet §04 evidence.** The flag is a retrieval boost; it's load-bearing for the query layer
- **Never adopt sandbox-recruitment voice.** Default is neutral knowledge-transfer per [`QUERY.md`](QUERY.md). The wiki explains the corpus; it doesn't advertise the programme
- **Never just append to a concept page.** Weave the new project's contribution into the existing structure, noting agreements *and* tensions
- **Never force a cross-cutting connection.** If a link feels argued-for, drop it. The best connections are the ones that make the reader say "oh, that's the same idea"
- **Never skip the `index.md` update.** This is how the wiki stays navigable

---

## A note on consumer-specific behaviour

Different runtimes give the ingest procedure different leverage:

- **Cowork / local Claude Code / Claude Agent SDK** — this file auto-loads as a skill from `.claude/skills/ingest/SKILL.md`. You have `Read`, `Write`, `Edit`, `Glob`, `Grep`, `Bash` against the repo. Run the Docling pipeline for paragraph anchors before writing source pages. **This is the recommended runtime for ingest.**
- **Claude.ai Projects with GitHub connector** — paste this file as the project system prompt, attach [`CONVENTIONS.md`](CONVENTIONS.md) and [`index.md`](index.md), enable the GitHub connector pointed at this repo. The connector can read and write files via the GitHub API, but the Docling pipeline does **not** run in this environment. Use claude.ai for *editorial* operations on already-ingested sources — drafting a new lesson from an existing source, cross-references, prose tightening, fixing a citation — not for ingesting new PDFs that need paragraph anchoring
- **Raw API call (single-shot)** — concatenate this file with CONVENTIONS, index, and the source content. Anchor-aware ingest is not feasible here; treat output as a draft for review

The procedure is identical across all three. What differs is whether the Docling pipeline can run, and whether files can be written directly vs. proposed for human commit.

---

## What this file is not

- **Not the schema spec.** [`CONVENTIONS.md`](CONVENTIONS.md) is. This file is the procedure; CONVENTIONS is the contract
- **Not a UI spec.** The wiki is the substrate; UIs sit on top
- **Not enforcement.** The future lint pass enforces structural conventions; voice and discipline are upheld by the human reviewer at PR time
- **Not exhaustive.** New failure modes — when they recur — should be added to *Anti-patterns*. New page-type specifics should be added to CONVENTIONS §2 first, then mirrored here
