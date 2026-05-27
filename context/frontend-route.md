# Frontend Route — Three Surfaces, Wiki-Backed Generative UI

> Pre-hackathon decision doc for the AI Innovation Sandbox Knowledge Hub challenge. Companion to [`architecture-route.md`](architecture-route.md) — that doc decides *where the prose lives*; this one decides *how users see it*. Working doc — update after Thursday Q&A with Lukas and once team composition is known.

---

## TL;DR — recommended route

**Three surfaces on a Next.js 15 app, all reading from the same `wiki/` markdown content layer: a Wikipedia-shaped Wiki Reader (static, embeddable), a generative-UI Guideline Generator, and an Admin/Ingest surface that demos the update flow live.**

Concretely: shadcn/ui + Tailwind + Lucide for the shell, velite to turn `wiki/*.md` into typed TS content, Pagefind for static search, Vercel AI SDK's `streamUI` for the generator, and react-pdf for paragraph-anchored citation previews. Zod is the shared schema spine across frontmatter, LLM outputs, and component props.

This route is recommended because:
1. It inherits the [`architecture-route.md`](architecture-route.md) decision cleanly — the wiki IS the source of truth, the UI is a set of views over it.
2. **Generative UI here generates *projections of wiki pages*, not free-form content.** The model picks which components to render and which wiki slugs they reference; the prose comes from disk. This bounds the hallucination surface structurally.
3. Three named surfaces gives three demo beats (browse → generate → update), each ~90 seconds, mapping to the three user groups in [`challenge/brief.md`](challenge/brief.md).
4. Static export of the Wiki Reader satisfies the "Einbettung auf der Webseite der AI Innovation Sandbox" line from the brief without extra infra.

---

## How `architecture-route.md` shapes the UI plan

The substrate decision (wiki-first with frontmatter-as-graph) is not neutral for the frontend. It pushes the UI in specific directions:

| Architecture decision | Frontend consequence |
|---|---|
| Frontmatter is typed (`phase`, `regulation`, `stakeholder`, `concept`) | Retrieval is **filterable like a library catalog**, not just fuzzy similarity. UI gets faceted browse + tag chips, not just a search box. |
| Paragraph-anchored citations (`reports/de/p2-building-permits.pdf#para-47`) | Citation UI can pop the actual PDF at the highlighted paragraph — a meaningfully higher-fidelity citation experience than page-level references. |
| Wiki pages exist on disk as the source of truth | Generative UI components are **projections of wiki content**, not generators of new claims. Components take wiki slugs as props, never raw prose. |
| German source content + bilingual shipping target | **Three orthogonal language axes**: (1) **development UI = English** (so Bowen can iterate without translation friction); (2) **report content stays German** (citations quote PDFs verbatim — no machine translation of source material); (3) **shipped UI = bilingual via i18n**, demo-time default deferred. |
| Static HTML export expected for embeddability | Wiki Reader uses Next.js `output: 'export'`; Generator + Admin are SSR. Two render modes in one repo. |
| "Drop a PDF, re-run ingest" as a 30-second live demo | Admin surface is **load-bearing for the pitch**, not a stretch goal. It demonstrates the update flow the brief explicitly calls out. |
| Lint workflow (orphans, broken links, contradictions) | Becomes the **Quality tab** of the Admin UI — production-thinking signal to the jury. |
| `[!gap]` / `[!tension]` callouts from bowen-wiki port | First-class UI primitives in the Wiki Reader — colored cards where reports disagree. |

---

## The three surfaces

### 1. Wiki Reader — `/wiki/[...slug]`

The Wikipedia-shaped browse experience. What Verwaltungsmitarbeitende actually use day-to-day.

- **Layout**: left rail with faceted nav (by phase / by regulation / by stakeholder / by project), centre column for prose, right rail Wikipedia-style infobox showing frontmatter.
- **Inline citations**: every claim hyperlinks to a citation chip; clicking opens the PDF slideover at `#para-N` with the passage highlighted.
- **Backlinks** at page bottom, computed from `[[wikilink]]` resolution.
- **Search**: Pagefind static index, cmdk command palette.
- **Render**: static export — `output: 'export'`. Embeddable on zh.ch via iframe with `?embed=1` chrome-stripping.

### 2. Guideline Generator — `/generator`

The "describe your project → get a tailored briefing" surface. The pitch hero shot.

- **Entry**: textarea + a few optional structured prompts ("which phase?" "which regulations apply?"). Defaults to free text.
- **Output**: a **Project Readiness Canvas** — a sectioned page assembled by the LLM choosing which components to render in which slots, each component reading from `wiki/`.
- **Streaming**: sections fade in as the model decides them (Framer Motion stagger).
- **Refinement**: chat input below the canvas; "show only legal risks" re-renders the same sources through different components.
- **Render**: SSR with `streamUI`.

### 3. Admin / Ingest — `/admin`

The update-flow demo. Drop a PDF → watch it become wiki pages → see the diff.

- **Upload**: drag-and-drop a PDF. Server action triggers the ingest pipeline.
- **Live log**: streams the chunk → extract → cross-link → lint steps back to the UI.
- **Diff view**: after ingest, shows which wiki pages were created / touched / contradicted.
- **Quality tab**: orphan pages, broken `[[wikilinks]]`, frontmatter validation errors, `[!tension]` callouts across reports.
- **Render**: SSR with server actions.

---

## Recommended stack

### Spine (commit on day 1)

| Job | Pick | Why |
|---|---|---|
| Framework | **Next.js 15** App Router | Two render modes in one repo (static export for `/wiki`, SSR for `/generator` + `/admin`); first-class Vercel AI SDK support. |
| Language | **TypeScript** | Required to make Zod + structured outputs feel magical. |
| Content layer | **velite** | Typed Markdown → TS objects with Zod schemas for frontmatter. Better DX than Contentlayer (unmaintained) for hackathon speed. |
| LLM orchestration | **Vercel AI SDK** (`ai`, `@ai-sdk/anthropic`) | `streamUI` for generative UI, `streamObject` for typed JSON, `useChat` for refinement loop. |
| Schemas | **Zod** | Shared spine: frontmatter validation, LLM output coercion, component prop types. |
| Components | **shadcn/ui** | Copy-paste Radix components you own and can edit; the default 2026 hackathon look that doesn't read as hackathon. |
| Styling | **Tailwind CSS v4** | Shadcn substrate. |
| Icons | **Lucide** | Shadcn default; one consistent stroke weight throughout. |

### Wiki Reader specifics

- **Pagefind** — static full-text search. Points at the build output, gives a working search box with zero infra.
- **rehype-slug + rehype-autolink-headings** — anchor links on headings.
- **remark-wiki-link** — `[[foo]]` → resolved internal links, with computed backlinks.
- **MDX** with custom components for `[!gap]` / `[!tension]` callouts.
- **next-intl** — EN strings during dev (so the feedback loop works); DE strings added in parallel or late; demo-time default deferred. See "Open questions."

### Guideline Generator specifics

Component registry — 4–6 Zod-typed React components, each taking wiki references as props (not raw content):

```ts
type CanvasComponent =
  | { kind: 'LessonCard',          props: { slug: string, emphasis?: string[] } }
  | { kind: 'RegulationCallout',   props: { slug: string } }
  | { kind: 'ChecklistFromLessons',props: { lessons: string[] } }
  | { kind: 'ProjectCompareTable', props: { projects: string[], dimensions: string[] } }
  | { kind: 'StakeholderRow',      props: { stakeholders: string[] } }
  | { kind: 'SourceQuote',         props: { source: string /* "...pdf#para-47" */ } }
```

The LLM emits a `CanvasComponent[]`. A renderer maps each entry to its React component. Components read wiki content from velite at render time. No free-text claims are generated — only structure and selection.

- **Framer Motion** — staggered fade-in as sections stream.
- **Sonner** — toasts for "Generating section…" / "Updated source data."

### PDF citation experience (the wow moment)

- **react-pdf** (pdf.js wrapper) inside a shadcn `<Sheet>` slideover.
- Pre-compute `#para-N → {page, bbox}` mapping during ingest; highlight on render.
- This single interaction is the screenshot the jury remembers — worth disproportionate time investment.

### Admin / Ingest specifics

- **Server Actions** for upload + re-ingest trigger.
- Stream pipeline logs back to the UI (treat like watching CI).
- **Quality tab** wraps the lint workflow output from [`architecture-route.md`](architecture-route.md)'s ingest pipeline.

---

## Generative UI — what it actually buys us here

Generative UI is "the LLM emits structured outputs that a renderer turns into React components," not "the LLM writes HTML." In this project specifically it gives:

1. **Bespoke briefings instead of search results.** Default hackathon entry returns "here are 3 reports." This returns a Project Readiness Canvas tailored to the user's intent.
2. **Citations as a typed field, not prose.** Components reject empty `sources` props structurally — traceability is enforced by the type system, not by prompting.
3. **Refinement via re-render.** "Show only legal risks" doesn't restart a chat; it re-runs the registry selection with a filter applied.
4. **Component-level freshness metadata.** Each component carries `as-of` from its wiki source, can render staleness warnings. Directly serves the brief's "Aktualität" constraint.
5. **Demo-able differentiation.** Streaming sections assembling into a canvas reads as a generation of design effort, not just text.

What it does NOT buy us:
- New retrieval power (the typed frontmatter already gives us that).
- Solved hallucination (it bounds the surface; the wiki-as-source-of-truth solves it).
- Easier development (registry pattern has upfront cost; pays back when adding the 4th+ component).

---

## Areas of exploration (pick 2 after the spine ships)

In order of differentiation-per-hour:

1. **Diff view in Admin** — when re-ingesting a PDF, show which wiki pages changed. Directly addresses "leicht aktualisierbar." High signal, ~3 hours.
2. **Contradiction surface** — surface `[!tension]` callouts wherever two reports disagree; the generator can highlight contested claims with both sources cited. Strong credibility signal for honest knowledge synthesis.
3. **Embed mode** — `?embed=1` strips chrome for iframe use on zh.ch. Shows you read the brief carefully. Cheap.
4. **Faceted navigator polish** — Wikipedia-style left rail with multi-select filter chips that update the URL. Reads as "real product."
5. **Graph preview pane** — small force-directed view of the frontmatter neighbourhood around the current wiki page. Defends the "yes, it's also a knowledge graph" claim cheaply.
6. **Live re-generation on filter change** — toggle a regulation chip on the canvas; canvas re-streams with that lens applied. Conceptually impressive but interaction-heavy.

---

## Build order (suggested foundation)

1. **velite + 3 hand-written wiki pages** → renders at `/wiki/[slug]` with frontmatter sidebar. *~½ day.*
2. **Pagefind search** across them. *~2 hours.*
3. **Faceted filter left rail + tag chips on cards.** *~½ day.*
4. **`/generator` with one component** (`<LessonCard>`) wired through `streamUI`. *~½ day.*
5. **PDF slideover with highlight at `#para-N`.** *~½ day — invest here.*
6. **Ingest pipeline** (offline Python from [`architecture-route.md`](architecture-route.md), demoed live in Admin). *Day 2 morning.*
7. **Pick 2 from the exploration menu.** *Day 2 afternoon.*

Working app end of day 1; polish and differentiator moves day 2.

---

## Open questions to resolve before locking in

Move these into [`README.md`](README.md) §8's pre-event checklist or the Thursday Q-list for Lukas.

- [ ] **Demo-time language default** — dev happens in English (see "Language orientation" above and [[feedback-english-first-dev]]). For the jury submission, do we ship with DE as the default (likely, given the Kanton Zürich audience) or EN (if international jury / simpler narration)? Bilingual via i18n either way; this is just which side the toggle starts on.
- [ ] **Hero demo flow** — is the 5-minute demo wiki-browse-first ("look how navigable this is") or generator-first ("describe your project, watch this assemble")? Determines where polish budget lands.
- [ ] **Team composition** — is there a frontend specialist or does Bowen own UI end-to-end? Determines exploration menu depth.
- [ ] **For Lukas, Thu 09:30** — is there an existing design system / brand we should align with for the zh.ch embedding? (Could mean swapping shadcn defaults for a constrained palette.)
- [ ] **For Lukas, Thu 09:30** — does the AI Innovation Sandbox already have any UI prior art we should reference or visibly diverge from?
- [ ] **Generator entry point** — free-text textarea, structured form, or hybrid (form with "or describe in your own words" escape hatch)? Affects how much of the canvas can be deterministic.
- [ ] **Static export vs SSR for `/generator`** — does the embedding context on zh.ch require fully static? If yes, the generator becomes pre-baked variants rather than truly dynamic, and the architecture needs adjusting.

---

## What ports directly from prior work

| From | To | Adjustment |
|---|---|---|
| bowen-wiki page-rendering conventions (frontmatter sidebar, backlinks, callouts) | Wiki Reader | Port the visual grammar; restyle for shadcn + Tailwind. |
| bowen-wiki `[!gap]` / `[!tension]` callout components | MDX components in `/wiki` | Same semantics; new look. |
| Any prior Next.js + shadcn project skeletons | Bootstrap | Reuse `pnpm dlx shadcn init` defaults; copy `components.json`. |
| Familiarity with Anthropic SDK + tool use | Generator component registry | The `streamUI` pattern is one layer above raw tool use — same mental model. |

What does NOT port:
- bowen-wiki's monolingual setup — sandbox hub is bilingual via i18n (EN during dev, DE layered in). Report content stays in source German regardless.
- bowen-wiki's weekly-compilation rhythm — replaced by Admin's drop-a-PDF flow.

---

## Decision log

| Date | Note |
|---|---|
| 2026-05-27 | Initial doc. Recommendation: three surfaces (Wiki Reader / Guideline Generator / Admin) on Next.js 15, wiki as content source for both browsing and generation, component-registry generative UI for the generator. Pending validation: hero demo flow, team composition, zh.ch design constraints (Thu 09:30 with Lukas). |
| 2026-05-27 | Flipped language orientation. Dev now English-first (so the dev feedback loop works for the team); German added in parallel via i18n; source report content stays German. Demo-time default language is now an open question rather than assumed-DE. |
