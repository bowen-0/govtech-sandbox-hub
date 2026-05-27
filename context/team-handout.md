# Team Handout — Sandbox Knowledge Hub

> One-page kickoff doc for the **GovTech Hackathon, Thu 28 May 2026, 09:30 onwards**. Pre-event prep distilled. Full rationale in [`architecture-route.md`](architecture-route.md) and [`frontend-route.md`](frontend-route.md); brief in [`challenge/brief.md`](challenge/brief.md); corpus in [`digests/`](digests/).

---

## The pitch

> **Search returns reports. We return a project plan. And the Wikipedia of Swiss public-sector AI sits underneath it.**

We're solving the AI Innovation Sandbox Knowledge Hub challenge — turning ~12 dense PDFs into discoverable, citable, applicable knowledge for a civil servant about to start a new AI pilot.

## Who it's for

**Primary persona** (per the brief): a civil servant in a cantonal department (e.g. Baudirektion, Gesundheitsdirektion) who's been asked to scope an AI pilot. Domain expert, not a developer. Working in German. Needs to navigate legal, data, organisational, and procurement questions in parallel.

Secondary personas (also named in the brief): companies/startups developing AI in regulated settings; other public bodies wanting to learn from prior pilots.

## What we're building — three surfaces, one wiki

A Next.js 15 app with three connected surfaces, all reading from the same markdown wiki layer:

1. **Wiki Reader** (`/wiki/[slug]`) — Wikipedia-shaped browse. Static-exportable, embeddable on zh.ch via iframe. Every claim hyperlinks to a paragraph in the source PDF.
2. **Guideline Generator** (`/generator`) — "Describe your AI pilot in a sentence." Watch a tailored briefing assemble in front of you — similar pilots, regulations, stakeholders, readiness checklist, where reports disagree.
3. **Admin / Ingest** (`/admin`) — Drop a PDF, watch it become wiki pages live. The 30-second answer to "but how do you keep it current?"

## What it looks like

### The Generator (the hero demo)

```
┌──────────────────────────────────────────────────────────────────┐
│ Briefing: AI pre-check for solar building permits                │
├──────────────────────────────────────────────────────────────────┤
│ ① Similar sandbox pilots                                  [2]    │
│   [AI for Building Permits — Phase II]  [Smart Parking — Phase I]│
│                                                                  │
│ ② Regulatory landscape                                           │
│   DSG Art. 22 · EU AI Act · Auftragsdatenbearbeitung             │
│                                                                  │
│ ③ Stakeholders to involve                                        │
│   [DPO] [Baudirektion] [AI Competence Unit]                      │
│                                                                  │
│ ④ Readiness checklist (8 items from prior pilot reports)         │
│   ☐ Clarify access to historical permit submissions  …           │
│                                                                  │
│ ⑤ ⚠ Where reports disagree                                       │
│   Centralised vs. decentralised data handling — both cited       │
│                                                                  │
│ 💬 Refine: "Show only legal risks" …                             │
└──────────────────────────────────────────────────────────────────┘
```

### The Wiki Reader (the depth)

Wikipedia-shaped: left rail with faceted nav, prose centre column with inline paragraph citations, right rail infobox showing project metadata. Backlinks at the bottom. `⚠ Tension` callouts where two reports contradict.

### The Admin (the trust signal)

Drag-and-drop a PDF → live-streamed ingest log → diff view ("3 new pages, 12 updated, 1 new tension detected") → publish.

## The three moments we want people to remember

1. **The canvas assembling itself** — sections fading in as the model decides them.
2. **The PDF slideover** — click any citation chip, the original German PDF slides in with the paragraph highlighted.
3. **The live re-ingest** — drop a PDF on stage, the wiki updates in 30 seconds.

## What our approach prioritises

The brief invites multiple valid responses. The choices below reflect our specific reading of *"discoverable, applicable, and citable for non-technical people":*

- **A tailored briefing artifact**, not just a chat interface — the user leaves with something they can paste into an internal memo.
- **Paragraph-anchored citations** that open the actual source passage, not just report-level references — trust made tactile.
- **Bilingual via i18n** — UI translatable; report content preserved in its source German rather than machine-translated.
- **Update flow demoed live**, addressing the brief's "Aktualität" concern concretely rather than aspirationally.
- **Three connected surfaces** (browse, generate, update) — each serving a different user moment named in the brief.

## Stack at a glance

| Layer | Pick |
|---|---|
| Framework | Next.js 15 App Router (static export for `/wiki`, SSR for `/generator` + `/admin`) |
| Content | velite — typed Markdown → TS with Zod-validated frontmatter |
| LLM | Vercel AI SDK (`streamUI`) + Anthropic Claude |
| Components | shadcn/ui + Tailwind + Lucide |
| Search | Pagefind (static FTS) + frontmatter filters |
| Citations | react-pdf (slideover with highlighted paragraph) |
| Ingest | Python — Docling for PDFs → typed extractions via Claude |
| i18n | next-intl — EN strings during dev; DE added in parallel |

## Day 1 / Day 2 rough split

**Day 1** — substrate up
- velite + 3 hand-written wiki pages render at `/wiki/[slug]`
- Pagefind search across them
- Faceted filter left rail + tag chips
- `/generator` with one component wired through `streamUI`
- PDF slideover with paragraph highlight ← invest here

**Day 2** — pipeline + polish
- Ingest pipeline (Python) running, demoed live in Admin
- Pick 2 differentiator moves (current vote: `[!tension]` contradiction surface + Admin diff view)
- DE strings layered in via i18n
- Demo path rehearsal

## Open decisions for the team

1. **Hero demo flow** — open with the generator ("watch this assemble for your project") or with the wiki ("look at the depth of this knowledge base")?
2. **Visual personality** — Kanton Zürich blue, or a more neutral palette that reads as cantonally-neutral?
3. **Generator entry point** — pure free text, or hybrid form with an "or describe in your own words" escape?
4. **Differentiator picks** — from the menu in `frontend-route.md`, which 2 commit? (Current vote: contradiction surface + Admin diff view.)
5. **Scope honesty** — three surfaces is ambitious. Comfortable cutting Admin to a pre-recorded video if generator + wiki need the time?
6. **Demo-time language default** — DE (likely, given Kanton Zürich audience) or EN (international jury / simpler narration)? Bilingual either way; this is just which side the toggle starts on.

## What we need from Lukas at the 09:30 challenge presentation

See `README.md` §8 for the full Q-list. The single most load-bearing question:

> *"Where in the pilot lifecycle is your typical user when they'd open this tool? Pre-idea, validating an approach, or scoping procurement?"*

Each answer implies a different generator output shape. We'll commit after his answer.

## Where to read more

- [`README.md`](README.md) — full context hub (challenge framing, corpus, cross-cutting patterns)
- [`architecture-route.md`](architecture-route.md) — substrate decision (wiki-first with frontmatter-as-graph)
- [`frontend-route.md`](frontend-route.md) — UI decision (three surfaces, generative UI via component registry)
- [`success-criteria.md`](success-criteria.md) — the brief's requirements as a triable checklist
- [`digests/`](digests/) — ~50 min of structured digests across all 12 reports
