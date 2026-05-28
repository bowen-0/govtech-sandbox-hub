---
title: Rule-based systems outperform generative AI when decision logic is well-defined
type: lesson
slug: rule-based-beats-generative-for-defined-logic
phase: II
project: [building-permits, bridge-monitoring]
concept: [generative-ai, llm-benchmarks]
regulation: []
stakeholder: [raphael-von-thiessen]
sources:
  - 00-overview-phase2-build-and-share#para-04-technology
  - p2-building-permits#para-21
confidence: high
freshness: 2026-05
applies_to_lifecycle_stage: [scoping, deployment]
created: 2026-05-28
updated: 2026-05-28
---

# Rule-based systems outperform generative AI when decision logic is well-defined

The most operationally consequential generative-AI lesson from Phase II. Stated almost verbatim in [[00-overview-phase2-build-and-share]] §04 Technology:

> *"Generative AI models demonstrate strengths in processing unstructured information, such as summarisation, transcription, information structuring, or preliminary checks (e.g. medical documentation or pre-checks in building permit procedures). However, they reach their limits in clearly defined, traceable, and legally relevant decision processes. In such cases, rule-based approaches deliver more robust and transparent results."*

## Evidence base

- **[[building-permits]]** — the prototype uses *pure rule-based logic* for procedure determination (8 project types × ~20 zone/protection criteria → if/then matrix). Generative AI is reserved for unstructured document quality checks (e.g. solar-datasheet against "low reflectivity" criteria). Quantitative support: best LLM accuracy on perfect answers is 60.2%; average 37.9%. For administrative decisions, that's insufficient — and probabilistic AI fights the administrative-reproducibility requirement (95% vs 99% reliability is a *substantive political* question).
- **[[bridge-monitoring]]** — data-driven approaches complement standards-based engineering; they do not replace deterministic structural-engineering logic.
- **[[inspection-robots]]** — deterministic safety logic vs. self-evolving ML is named as the operative tension under the EU Machinery Regulation.

## How to apply

When scoping a new public-sector AI use case:

1. **Map the decision logic**: is it definable as a finite if/then matrix? If yes, rule-based first; generative AI only for the unstructured-input subtasks.
2. **Quantify the accuracy floor required**: 95% reliability is too low for administrative decisions if the system makes the decision unsupervised.
3. **Hybrid architectures are normal**: building-permits is a working example of rule-based-by-default + generative-AI-on-unstructured-inputs.

## See also

- [[building-permits]] — the canonical case study.
- [[llm-benchmarks]] — what makes the 60.2% headline number believable.
- [[generative-ai]] — the contrast concept.
