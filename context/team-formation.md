# Team Formation & Role Planning

> Pre-event planning doc for Thursday morning team-building. Outlines realistic team shape, role coverage, and the first-hour sequence after a team forms. Companion to [`team-handout.md`](team-handout.md) and [`TASKS.md`](TASKS.md).

---

## Realistic team size

Effective hackathon working units tend to be **3-4 active builders + 1 narrator/coordination lead**. Beyond five, coordination overhead starts eating the gain from extra hands.

If interest on the project page exceeds this, sensible options:

- Run as **two sub-pods within one umbrella team** (e.g. one pod on data/wiki, one on UI/generator) — single shared repo, single demo, lower per-person coordination cost.
- Expect **natural attendance fluctuation** — a portion of sign-ups don't show up or shift focus by day 2. Don't over-plan around the sign-up list.
- **Stay flexible**: let the actual room compose the team rather than committing to a plan before meeting people.

---

## Role shape

The product needs four kinds of contribution, mapping to the workstreams in [`TASKS.md`](TASKS.md):

| Role | Owns | Skills that fit well |
|---|---|---|
| **Frontend lead / architect** | `/generator` surface end-to-end, design system, architectural ownership | Generative UI, React/Next.js, design eye, comfortable holding full-stack context |
| **Wiki + ingest dev** | `wiki/` schema, Python ingest pipeline, hand-seeds lessons day 1 | LLM API work, structured outputs, content modelling, Python or TypeScript |
| **Wiki Reader dev** | `/wiki/[slug]` pages, faceted nav, search, PDF slideover | Next.js, MDX, static sites, Tailwind/shadcn, has built docs-shaped sites before |
| **Domain / narrator / PM** | Lesson-seeding accuracy, pitch script, Friday demo narration | Public-sector or legal familiarity, comfortable presenting, ideally German speaker |

**Ideal team-of-4**: one of each.
**Team-of-5**: add an Admin-surface dev or a second domain/content person.
**Solo or pair**: see the fallback section below — the prep stack supports a reduced-scope version.

---

## Things worth aligning on early

When a team starts forming, useful questions for mutual fit and clean role allocation:

1. What part would you most enjoy owning end-to-end?
2. What's your strongest stack right now?
3. Have you worked with LLM APIs, Next.js, or Python content extraction before?
4. Anything in the route docs you'd want to discuss or push back on before we start?
5. What's your realistic end-of-day on Thursday and Friday?

The fourth question matters most — surface any substrate or stack conversations *before* people start building, not at 2pm Friday.

---

## The first 60 minutes after a team forms

Before anyone splits up to build, run this sequence. The schema lock is blocking — no parallel work until those two files are committed.

```
T+0    Team forms (Thu ~11:00)
T+10   Walk through team-handout.md + frontend-route.md together
T+20   Roles assigned, owners named for the workstreams in TASKS.md
T+30   Frontend lead + wiki dev: lock the Zod frontmatter schema
       (packages/wiki/schema.ts) — commit and push
T+45   Frontend lead: lock the component registry contract
       (apps/web/registry.ts) — commit and push
T+60   Everyone starts building. Lunch happens around something
       already running on a Vercel preview URL.
```

After T+60, parallel work has clean seams. Before T+60, no one is building on assumptions someone else might invalidate.

See [`TASKS.md`](TASKS.md) Phase 0 for the concrete checklist.

---

## Fallback plans if a team doesn't form

Plausible. The prep stack is intentionally designed to support a reduced-scope solo or pair build.

1. **Pair or solo execution at reduced scope.** Wiki Reader + Generator only — skip the Admin surface. Hand-seed wiki content rather than building the ingest pipeline. Still ships a coherent two-surface demo.
2. **Join another team's project** working on a related challenge (legal/admin AI, knowledge management, document analysis). The prep work is portable as a starting point if relevant to their angle.
3. **Pivot to a concept/design-track submission.** The brief explicitly accepts "ein klar ausgearbeitetes Lösungskonzept" as a valid deliverable — the route docs plus a working slice of one surface is a credible submission of that shape.

None of these are failures. A focused smaller deliverable is often stronger than a sprawling larger one.

---

## Where to read more

- [`team-handout.md`](team-handout.md) — the one-pager to walk through with prospective teammates
- [`TASKS.md`](TASKS.md) — workstream split with claimable items
- [`data-architecture-walkthrough.md`](data-architecture-walkthrough.md) — substrate detail for the wiki/ingest workstream
- [`frontend-route.md`](frontend-route.md) — UI detail for the React workstream
- [`success-criteria.md`](success-criteria.md) — requirements checklist
- [`README.md`](README.md) — full context hub
