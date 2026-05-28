# Sandbox Knowledge Hub

> Pre-hackathon + working repository for the *AI Innovation Sandbox Knowledge Hub* challenge at the **GovTech Hackathon Switzerland 2026** (Thu 28 — Fri 29 May, FOITT Zollikofen). Challenge by the **Canton of Zurich** (Lukas Willi, Projektleiter KI).

This repo currently has three layers:

```
.
├── context/        Pre-hackathon prep: challenge brief, source PDFs, digests, decision docs
├── wiki/           The knowledge layer — structured markdown with YAML frontmatter
└── CLAUDE.md       Project memory for Claude Code sessions
```

The application layer (Next.js app, ingest pipeline, generator UI) will be bootstrapped during the hackathon as a sibling directory or at the root.

## Quick navigation

| Want to… | Read |
|---|---|
| Understand the challenge | [`context/README.md`](context/README.md) |
| Browse what we know | [`wiki/index.md`](wiki/index.md) |
| Add a wiki page | [`wiki/CONVENTIONS.md`](wiki/CONVENTIONS.md) + [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| Review pre-event design decisions | [`context/architecture-route.md`](context/architecture-route.md), [`context/frontend-route.md`](context/frontend-route.md), [`context/data-architecture-walkthrough.md`](context/data-architecture-walkthrough.md) |
| See the corpus | [`context/digests/`](context/digests/) (English summaries) + [`context/reports/`](context/reports/) (DE + EN source PDFs) |

## What this hub is, in one paragraph

The Canton of Zurich's *AI Innovation Sandbox* has produced ~13 detailed reports across two phases (2022–2026) — legal frameworks, data-access patterns, regulatory analyses, technical playbooks. Hard-won knowledge, currently locked in static PDFs. **This hub structures that corpus** as a navigable, citable wiki where each claim links back to a paragraph in the source PDF, and where new sources (papers, web pages, transcripts, future sandbox reports) can be added as first-class citizens. The eventual application layer renders this substrate as the **wiki reader** + **guideline generator** described in [`context/frontend-route.md`](context/frontend-route.md).

## Status

- **Pre-hackathon**: Wiki skeleton seeded (sources, projects, concepts from booklet glossary, key stakeholders + regulations, 2 seed lessons, 1 synthesis page). Schema is **soft** — see [`wiki/CONVENTIONS.md`](wiki/CONVENTIONS.md) §7 "How to evolve the schema."
- **Hackathon (28-29 May 2026)**: Bootstrap the application layer, extend lessons + concepts as the team converges on the demo narrative, ship a working generator.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). The short version: drop sources into `context/reports/`, create a `wiki/sources/<slug>.md`, then extract lessons + concepts as you read.

## Licensing

The source reports in `context/reports/` are © Canton of Zurich and may be shared with proper attribution per the publisher's terms (booklet impressum, p. 28).

The wiki content, decision docs, and any application code in this repo are released under [MIT License](LICENSE) unless individual files specify otherwise.
