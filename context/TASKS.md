# TASKS — Sandbox Knowledge Hub

> Workstream split pre-seeded from [`team-handout.md`](team-handout.md). Move/copy to the new project repo root once it's created. Lightweight project board — claim items by adding `@yourname` next to them, mark progress with the status legend, mark done by checking the box.

---

## How to use

- **Claim**: add `@yourname` next to an item you're working on. Don't claim more than 2 active items at once.
- **Status legend** in the title prefix: `☐` open · `◐` in-progress · `✓` done · `✗` cut (with reason)
- **Workstreams are vertical slices** — each owner ships their surface end-to-end (data → API → UI). Cross-stream dependencies are flagged with → `depends on X`.
- **Don't add new items below the "Cut line" without team agreement.** Discipline beats ambition at hour 30.

---

## Phase 0 — Shared spine (first 60 minutes after team formation)

These must happen before anyone splits up to build. Single owner runs them; everyone reviews/commits to schema together.

- [ ] **Bootstrap**
  - [ ] Pick repo name, create GitHub repo (private during dev, open at submission per hackathon rules) @_____
  - [ ] `pnpm create next-app@latest` + Tailwind + shadcn init + lucide + zod @_____
  - [ ] `pnpm add ai @ai-sdk/anthropic velite remark-wiki-link next-intl framer-motion` @_____
  - [ ] Connect repo to Vercel — preview deploy per branch verified working @_____
  - [ ] Add `CLAUDE.md` pointing at `context/` route docs (so any AI assistants the team uses get full context) @_____
- [ ] **Schema lock** *(blocking — no parallel work until this commits)*
  - [ ] `packages/wiki/schema.ts` — Zod schemas for the 7 page types from [`data-architecture-walkthrough.md`](data-architecture-walkthrough.md) @_____ + @_____
  - [ ] `apps/web/registry.ts` — typed component registry contract (kind + props per component) @_____
  - [ ] Both committed and pushed to `main` before anyone starts surface work
- [ ] **Smoke-test deploy**
  - [ ] One placeholder page renders on the Vercel preview URL
  - [ ] Lunch happens around something already deployed

---

## Phase 1 — Day 1 workstreams (Thu 12:00 → 22:00)

### WS-A · Wiki + ingest *(owned by wiki/ingest dev)*

Day 1 focus: hand-seed enough content for the demo to work. Day 2: pipeline.

- [ ] @_____ Create `wiki/` folder structure (`projects/`, `lessons/`, `concepts/`, `regulations/`, `stakeholders/`, `sources/`, `synthesis/`)
- [ ] @_____ Hand-seed `projects/building-permits.md` from digest
- [ ] @_____ Hand-seed `projects/smart-parking.md` and `projects/medical-documentation.md`
- [ ] @_____ Hand-seed 5 lessons connected to building-permits (incl. 1 with `[!tension]` against medical-documentation)
- [ ] @_____ Hand-seed `regulations/dsg-art-22.md`, `regulations/eu-ai-act.md`
- [ ] @_____ Hand-seed `stakeholders/data-protection-officer.md`, `stakeholders/baudirektion-zh.md`
- [ ] @_____ Hand-seed `concepts/data-access.md`, `concepts/pseudonymisation.md`
- [ ] @_____ Hand-seed `sources/building-permits.md` with manual `#para-N` anchors for cited paragraphs

### WS-B · Wiki Reader *(owned by Wiki Reader dev)*

Day 1 focus: pages rendering with sidebar + infobox + citation slideover.

- [ ] @_____ Dynamic route `/wiki/[...slug]` reading from velite → `depends on` schema lock
- [ ] @_____ Layout: left nav rail, prose center, right infobox showing frontmatter
- [ ] @_____ MDX components for `[!tension]` and `[!gap]` callouts
- [ ] @_____ Wikilink resolution (`[[slug]]` → internal link) via `remark-wiki-link`
- [ ] @_____ Backlinks computed from frontmatter + rendered at page bottom
- [ ] @_____ Citation chip component (clickable, opens slideover)
- [ ] @_____ **PDF slideover with paragraph highlight at `#para-N`** *(THE wow moment — invest here)*
- [ ] @_____ Pagefind static search integration
- [ ] @_____ Faceted left-rail filter (by phase, by regulation)

### WS-C · Generator *(owned by frontend lead — Bowen)*

Day 1 focus: streamUI orchestration with at least 2 components working end-to-end.

- [ ] @bowen `/generator` route + textarea entry + optional structured fields
- [ ] @bowen `streamUI` orchestration with Anthropic, tool definitions for each component kind → `depends on` registry contract
- [ ] @bowen `<LessonCard slug="…">` — reads `wiki/lessons/*` at render time
- [ ] @bowen `<RegulationCallout slug="…">` — reads `wiki/regulations/*`
- [ ] @bowen `<ChecklistFromLessons lessons={[...]}>` — projects atomic items
- [ ] @bowen `<TensionCallout>` — the contradiction surface (one of our differentiators)
- [ ] @bowen `<SourceQuote source="…#para-N">` — renders the PDF paragraph
- [ ] @bowen Framer Motion staggered fade-in as components stream
- [ ] @bowen Refinement chat box below canvas ("show only legal risks" → re-stream)

### WS-D · Design / polish *(threaded by Bowen throughout)*

- [ ] @bowen Design tokens: accent colour, type scale, spacing rhythm
- [ ] @bowen Hero / landing surface
- [ ] @bowen EN/DE language toggle component (no-op until i18n strings exist)
- [ ] @bowen Empty / loading / error states for generator
- [ ] @bowen shadcn theme tweaks to remove the "default shadcn look"

### WS-E · Domain / narrator / PM

- [ ] @_____ Read all 12 digests in `context/digests/` (if not already)
- [ ] @_____ Pair with WS-A on lesson seeding — bring domain accuracy
- [ ] @_____ Draft 60-second pitch script (the pitch line + the 3 moments)
- [ ] @_____ Draft 5-min demo flow — which surface opens, what's the narration arc
- [ ] @_____ Slides outline for dribdat submission

---

## Thu end-of-day checkpoint (~21:00)

- [ ] Re-score [`success-criteria.md`](success-criteria.md) — any hard constraint still at `☐`?
- [ ] **Scope decision**: keep Admin (WS-F below) or cut to pre-recorded video?
- [ ] Confirm Day 2 plan + owners
- [ ] Hard stop: 22:00. Don't push past.

---

## Phase 2 — Day 2 (Fri 09:00 → 14:00)

### WS-A · Wiki + ingest pipeline

- [ ] @_____ Docling setup: PDF → paragraph chunks with stable `#para-N` IDs
- [ ] @_____ LLM extraction pass (Claude Sonnet, pydantic-typed): entities, lessons, project metadata
- [ ] @_____ Cross-link pass: resolve `[[wikilinks]]`, build backlinks index
- [ ] @_____ Lint pass: orphans, broken links, missing sources, contradictions
- [ ] @_____ Run end-to-end on `p2-medical-documentation.pdf` — validate output
- [ ] @_____ Run on remaining unbuilt projects (priorities: bridge-monitoring, inspection-robots)

### WS-F · Admin *(stretch — own only if Day 1 finished cleanly)*

- [ ] @_____ `/admin` route + drag-drop PDF upload
- [ ] @_____ Server action triggers ingest pipeline
- [ ] @_____ Stream pipeline logs to UI (live progress)
- [ ] @_____ Diff view after ingest (new pages / updated pages / tensions)
- [ ] @_____ Quality tab: lint output table

### WS-B / WS-C polish

- [ ] @_____ Loading skeletons per generator component
- [ ] @_____ `<ProjectCompareTable>` component for the canvas
- [ ] @_____ Embed mode (`?embed=1` strips chrome) — addresses bonus B1 in success-criteria
- [ ] @_____ Faceted nav: multi-select filter chips, URL-driven state
- [ ] @_____ cmdk command palette (⌘K)
- [ ] @_____ German i18n strings layered in via next-intl

### WS-G · Differentiators *(pick 2 — current vote: Contradiction + Admin diff)*

From [`frontend-route.md`](frontend-route.md) exploration menu. Lock the picks by Fri midday.

- [ ] Contradiction surface across wiki (lint-derived `[!tension]` rendering)
- [ ] Diff view in Admin
- [ ] Embed mode for zh.ch iframe
- [ ] Faceted navigator polish
- [ ] Graph preview pane
- [ ] Live re-generation on filter change
- [ ] Video summary placeholder (or real if Lukas confirms availability)

---

## Fri midday checkpoint (~12:00)

- [ ] Lock differentiator picks — no new features after this
- [ ] Re-score [`success-criteria.md`](success-criteria.md) one more time
- [ ] All hands: integration smoke-test

---

## Phase 3 — Pitch prep (Fri 14:00 → 16:00)

- [ ] @_____ Full demo path rehearsal — clock it, target 4:30 to leave Q&A room
- [ ] @_____ Record fallback video of Admin re-ingest flow (in case live fails)
- [ ] @_____ dribdat upload: slides + screen recording per organiser rules
- [ ] @_____ 3 anticipated questions + crisp answers ready
- [ ] @_____ Demo machine offline-cached (`localhost` deploy + recordings on disk)

**Fri 16:00 — pitch.**

---

## Won't do *(scope guard — these are explicitly out)*

From [`success-criteria.md`](success-criteria.md) + brief §"Nicht im Fokus stehen":

- ✗ Production-ready system
- ✗ Full new data collection
- ✗ Complete legal review of all content
- ✗ Access to arbitrary additional government data beyond bundled material
- ✗ Machine translation of report content into English (source German preserved as authoritative)
- ✗ Custom auth (use a stub if needed)
- ✗ Multi-tenant features
- ✗ Custom design system tokens beyond shadcn defaults + accent colour
- ✗ Mobile responsive polish (desktop demo only — make sure it works at 1440x900)
- ✗ Real-time collaboration features
- ✗ Native vector DB (small-corpus in-memory cosine is sufficient)

---

## Cut line *(emergency triage if running out of time)*

If at Fri 12:00 we are behind, cut in this order:

1. WS-F (Admin) → replace with pre-recorded video
2. WS-G differentiator #2 → ship only 1
3. WS-A Day 2 ingest pipeline → use only hand-seeded content, frame ingest as "designed but not demoed live"
4. WS-B `cmdk` command palette
5. WS-B Pagefind search → fall back to faceted nav only
6. German i18n layer → ship English-only with clear "DE strings layered in via i18n, demo'd in English"

**What we do NOT cut**: PDF slideover with paragraph highlight (WS-B), the generator canvas itself (WS-C), source-traceability throughout (H2 in success-criteria). These are non-negotiable for credible submission.

---

## Pointers

- Pitch + UX picture: [`team-handout.md`](team-handout.md)
- Data substrate detail: [`data-architecture-walkthrough.md`](data-architecture-walkthrough.md)
- Substrate rationale: [`architecture-route.md`](architecture-route.md)
- UI rationale: [`frontend-route.md`](frontend-route.md)
- Requirements + review cadence: [`success-criteria.md`](success-criteria.md)
- Full context hub: [`README.md`](README.md)
- Source corpus digests: [`digests/`](digests/)
