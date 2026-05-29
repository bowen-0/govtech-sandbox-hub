# Sandbox Knowledge Hub

> Submission for the *AI Innovation Sandbox Knowledge Hub* challenge at the **GovTech Hackathon Switzerland 2026** (Thu 28 — Fri 29 May, FOITT Zollikofen). Challenge by the **Canton of Zurich** (Lukas Willi, Projektleiter KI).

This repo has three layers:

```
.
├── wiki/              The knowledge layer — structured markdown with YAML frontmatter + source PDFs
├── my-agent/          LangGraph agent that answers questions grounded in the wiki
└── agent-chat-ui/     Next.js chat UI for the agent
```

## Quick navigation

| Want to… | Read |
|---|---|
| Browse what we know | [`wiki/index.md`](wiki/index.md) |
| Understand the wiki substrate | [`wiki/README.md`](wiki/README.md) |
| Add a wiki page | [`wiki/CONVENTIONS.md`](wiki/CONVENTIONS.md) + [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| Read the source corpus | [`wiki/pdfs/`](wiki/pdfs/) (DE + EN source PDFs) |
| Run the agent locally | [`my-agent/README.md`](my-agent/README.md) |
| Run the chat UI locally | [`agent-chat-ui/README.md`](agent-chat-ui/README.md) |

## What this hub is, in one paragraph

The Canton of Zurich's *AI Innovation Sandbox* has produced ~13 detailed reports across two phases (2022–2026) — legal frameworks, data-access patterns, regulatory analyses, technical playbooks. Hard-won knowledge, currently locked in static PDFs. **This hub structures that corpus** as a navigable, citable wiki where each claim links back to a paragraph in the source PDF, and where new sources (papers, web pages, transcripts, future sandbox reports) can be added as first-class citizens. The agent on top consumes the wiki to answer questions without hallucinating beyond what's cited.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). The short version: drop sources into `wiki/pdfs/<lang>/`, create a `wiki/sources/<slug>.md`, then extract lessons + concepts as you read.

## Licensing

The source reports in `wiki/pdfs/` are © Canton of Zurich and may be shared with proper attribution per the publisher's terms (booklet impressum, p. 28).

The wiki content and application code in this repo are released under [MIT License](LICENSE) unless individual files specify otherwise.
