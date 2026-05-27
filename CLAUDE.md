# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository state

This is the **pre-hackathon preparation repo** for the *AI Innovation Sandbox Knowledge Hub* challenge at the GovTech Hackathon Switzerland (Thu 28 — Fri 29 May 2026, FOITT Zollikofen). There is **no application code yet**. Everything currently in the repo is planning material under `context/`:

- The challenge brief and organiser handbook
- The source corpus (12 sandbox-report PDFs in DE and EN + structured digests)
- Eight pre-hackathon planning docs (architectural and product decisions)

The actual application repo will be bootstrapped during the hackathon — see `context/TASKS.md` Phase 0 for the sequence. Until then, do not look for a `package.json`, build commands, or tests; there are none.

## Start here

`context/README.md` is the canonical hub. It indexes everything else and contains cross-cutting patterns extracted from reading the full corpus. Read it first whenever entering this repo.

## Doc map — which doc answers which question

| Question | Doc |
|---|---|
| What is the challenge, what corpus do we have, what are the hard constraints? | `context/README.md` |
| Original challenge text (German + English translation) | `context/challenge/brief.md`, `context/challenge/brief.en.md` |
| What's in each of the 12 source reports? | `context/digests/` (one ~700-word digest per report) |
| Why wiki-first markdown over a triple-store knowledge graph? | `context/architecture-route.md` |
| What does the UI look like and why three surfaces? | `context/frontend-route.md` |
| What does the user actually see (walkthrough with mockups)? | `context/team-handout.md` |
| What does the data substrate actually look like on disk? | `context/data-architecture-walkthrough.md` |
| Which brief requirements does each design choice address? | `context/success-criteria.md` |
| Team roles, schema-lock sequence, fallback plans | `context/team-formation.md` |
| Workstream split with claimable items (template for the project repo) | `context/TASKS.md` |

The pre-hackathon decision docs (`architecture-route.md`, `frontend-route.md`) each carry their own *Decision log* table. Before re-deriving a substrate, stack, or UI choice, check those logs — if the decision still holds, follow it; if it's being revisited, update the log.

## Durable rules (do not re-litigate without reason)

1. **Language orientation is three-axis**:
   - Development UI = **English** (so the dev feedback loop works for non-German-readers on the team)
   - Source report content = **German** (citations quote PDFs verbatim — never machine-translate source material)
   - Shipped UI = **bilingual via i18n** (next-intl), demo-time default language deferred
2. **Generator never invents claims.** Components in the generative-UI registry take wiki slugs as props, not raw prose. The LLM picks which components to render and which wiki pages they reference; content comes from disk. This is how the no-hallucination constraint is solved structurally, not by prompting.
3. **Citations are paragraph-anchored.** Every claim links to `…pdf#para-N`. Page-level citations are a fallback if anchor stability slips, not a default.
4. **Wiki pages are the source of truth.** The graph lives in YAML frontmatter; markdown prose lives in the body. Both are edited as plain text files. JSON-LD / DuckDB exports are derivative.

## Stack commitments (for the application repo, once built)

Locked in `context/frontend-route.md` and `context/architecture-route.md`:

- **Next.js 15** App Router (static export for `/wiki`, SSR for `/generator` and `/admin`)
- **shadcn/ui + Tailwind v4 + Lucide** for components
- **velite** for typed Markdown → TS with Zod-validated frontmatter
- **Vercel AI SDK** (`ai`, `@ai-sdk/anthropic`) with `streamUI` for generative UI
- **Anthropic Claude** (Sonnet for extraction/rerank, Haiku for query classification)
- **Pagefind** for static full-text search
- **react-pdf** for the paragraph-anchored citation slideover
- **Python + Docling + pydantic** for the ingest pipeline
- **next-intl** for the bilingual layer
- **Zod** as the shared schema spine across frontmatter, LLM outputs, and component props

Do not propose alternative stacks during the hackathon without explicit team agreement — schema-lock is the slowest decision to reverse.

## Workflow notes

- Commit deliberately — `git add` specific paths, never `git add -A` (the `.gitignore` excludes `.claude/`, `.DS_Store`, `node_modules`, `.env*`, Python venvs, but be explicit anyway).
- Pre-hackathon docs are tracked in this repo. The hackathon project itself will be a sibling or nested Next.js project with its own `package.json`, lockfile, and CI — when it's bootstrapped, this CLAUDE.md gains an update with the actual run/build/test commands.
- Per-project memory lives at `~/.claude/projects/-Users-Bowen-Coding-Projects-govtech-hackathon/memory/` (auto-loaded). Two memories exist: project shape pointing at the route docs, and the English-first-dev language rule.

## Voice / format for new docs in this style

The existing prep docs share a recognisable shape that's worth matching for any new docs added here:

- TL;DR or "what this doc decides" up top
- Scorecard tables and decision logs where trade-offs matter
- Concrete examples (real frontmatter, real ASCII mockups) over abstract description
- Explicit "open questions" sections rather than hidden assumptions
- Cross-links to sibling docs as `[backtick-path](backtick-path)` markdown links
- Direct, terse prose — no filler, no apologies, no narration of intent
