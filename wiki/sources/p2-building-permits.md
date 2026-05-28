---
title: "AI for Building Permits — Use Cases, Prototypes and Practical Insights"
type: source
source_type: pdf
slug: p2-building-permits
path: ../../context/reports/de/p2-building-permits.pdf
en_path: ../../context/reports/en/p2-building-permits.pdf
language: bilingual
year: 2026
publisher: Standortförderung Kanton Zürich
authors: [raphael-von-thiessen, stephanie-volz]
created: 2026-05-28
updated: 2026-05-28
paragraphs: []
priority: high
---

# AI for Building Permits

Phase II project report — **the most recent and most concrete** report in the corpus, and the only one with a working deployed prototype and a published evaluation pipeline. Two tracks: (1) a **3,336-evaluation benchmark** across 8 frontier LLMs (gpt-5-mini, gpt-5.1, o3, gemini-3-pro-preview, gemini-2.5-flash, gemini-2.5-flash-lite, claude-opus-4.5, claude-sonnet-4.5) scored via *LLM-as-a-Judge*, and (2) a working prototype for the **notification procedure** (Meldeverfahren) for solar panels, heat pumps, and charging stations — deployed with partners [[nokema]], [[byte-studio]], [[gossweiler-ingenieure]], and Stadt Kloten. Headline finding: rule-based logic outperforms generative AI for clearly-defined administrative decisions; full preliminary check costs under CHF 2 per application.

## Provenance

Published April 2026. Original filename: `InnovationSandbox_AI_for_building_permits.pdf`. Most recent + most operationally concrete report; fed directly into Cantonal Parliament postulate KR no. 226/2023 response.

## Use as citation

Authoritative source for:
- LLM benchmark methodology in Swiss government-task contexts (the multi-model evaluation harness is the most reusable engineering artifact in the corpus).
- The "rule-based beats generative for defined logic" pattern.
- Swiss administrative-law framing for AI: FADP Art. 21, BV Art. 29, *Algorithmische Entscheidungsfindungssysteme*.
- Cost figures for LLM-based administrative preliminary checks (per-application unit economics).
- The notification-procedure subset of building permits as a scoping precedent.

## See also

- [[building-permits]] — project page.
- [[machine-translation]] — fellow "AI in administrative procedures" report.
- [[llm-as-a-judge]] / [[frontier-models]] / [[llm-benchmarks]] — concepts from this source.
