---
title: AI for Building Permits
type: project
slug: building-permits
phase: II
year: 2026
status: completed
sector: construction
sources: [p2-building-permits]
stakeholder: [raphael-von-thiessen, stephanie-volz, nokema, byte-studio, gossweiler-ingenieure, stadt-kloten]
regulation: [dsg-fadp, idg-zh, postulate-ai-building-permits]
concept: [llm-benchmarks, frontier-models, generative-ai, real-world-testing]
created: 2026-05-28
updated: 2026-05-28
priority: high
---

# AI for Building Permits

The **flagship Phase II project**: the only one with a working deployed prototype and a published evaluation pipeline. The most operationally concrete report in the corpus, and the one most likely to demo well at the hackathon. Two parallel tracks:

## Track 1 — Capability benchmark

A **3,336-evaluation benchmark** across eight frontier LLMs:

| Provider | Models |
|---|---|
| OpenAI | gpt-5-mini, gpt-5.1, o3 |
| Google | gemini-3-pro-preview, gemini-2.5-flash, gemini-2.5-flash-lite |
| Anthropic | claude-opus-4.5, claude-sonnet-4.5 |

Scored 0–10 via *LLM-as-a-Judge* against expert reference answers on real building applications from Stadt Kloten. Five capability dimensions: information extraction, counting, measuring/calculating, spatial understanding, context understanding. Each query repeated three times to measure consistency.

**Headline numbers**: best model 60.2% accuracy on perfect answers, average 37.9%, worst 18.5%. Speed range 3.2s — 41.7s. Cost range USD 0.0001 — 0.033 per query — **full preliminary check on one application under CHF 2**.

## Track 2 — Working prototype

Notification procedure (*Meldeverfahren*) for solar panels, heat pumps, and charging stations — selected because complexity is bounded. Partners: [[nokema]] (project submission), [[byte-studio]] (technical implementation), [[gossweiler-ingenieure]] (specialist support), [[stadt-kloten]] (test data — real building applications). 4-step UX: address capture → project-type selection (rule-based) → document upload with AI pre-checks → downloadable summary.

## Headline findings

- **Rule-based beats generative AI when decision logic is clear** — the prototype uses pure rule-based logic for procedure determination; generative AI is reserved for unstructured document quality checks.
- **No single best provider** — different models win on different metrics; **model-agnostic architecture is mandatory**.
- **Probabilistic AI fights administrative reproducibility** — 95% vs 99% reliability is a substantive question requiring political decision.
- **Greatest leverage is pre-submission quality improvement** — catching the recurring formal deficiencies (wrong scales, missing drawings) before they enter formal proceedings.

## Regulatory framing

PBG (Cantonal Planning and Building Act), BVV §§ 2a, 3, 4, 14 (Construction Procedures Ordinance); EMBAG (Federal Act on Electronic Means); IDG ZH (currently being revised to add a transparency register for algorithmic decision-making systems); FADP Art. 21 (automated decisions / right to human review); BV Art. 29 (constitutional right to be heard). Cantonal Parliamentary postulate **KR no. 226/2023** — this project's results were the technical input into the executive's response.

## Stakeholders

[[raphael-von-thiessen]], [[stephanie-volz]]; project partners [[nokema]], [[byte-studio]], [[gossweiler-ingenieure]], [[stadt-kloten]]. Extensive specialist support from FHNW (Walzer, Jost, Schneider), University of St. Gallen (Klingler), Canton of Zürich Building Department (Meyer, Hüppin, Baldwin, Louis, Späti), Wüest Partner (Arnold), onprem.ai (Polach).

## See also

- [[p2-building-permits]] — the source PDF.
- [[machine-translation]] — fellow "AI in administrative procedures" report.
- [[llm-benchmarks]] / [[frontier-models]] / [[llm-as-a-judge]] — concepts canonicalised here.
