---
title: Model selection is task-specific — design model-agnostic architectures
type: lesson
slug: model-selection-is-task-specific
phase: II
project: [building-permits]
concept: [model-agnostic-architecture, frontier-models, llm-benchmarks, llm-as-a-judge]
regulation: []
stakeholder: []
sources:
  - 00-overview-phase2-build-and-share#para-04-technology
  - p2-building-permits#para-bench
confidence: high
freshness: 2026-05
applies_to_lifecycle_stage: [scoping, deployment]
cross_cutting: true
created: 2026-05-28
updated: 2026-05-28
---

# Model selection is task-specific — design model-agnostic architectures

From [[00-overview-phase2-build-and-share]] §04 Technology, p. 17:

> *"Different models exhibit distinct strengths and weaknesses depending on the task (e.g. visual plan interpretation versus text extraction in building applications). Unlike generic LLM benchmarks, practical experience shows that a single 'best' model often does not exist, particularly in diverse use cases involving multiple data inputs (e.g. images and text)."*

## Evidence base

[[building-permits]] benchmarked 8 frontier LLMs across 3,336 evaluations using [[llm-as-a-judge]]. Findings:

- **Best model**: 60.2% accuracy on perfect answers
- **Average**: 37.9%
- **Worst**: 18.5%
- **Speed range**: 3.2s — 41.7s per query
- **Cost range**: USD 0.0001 — 0.033 per query
- **Different models win on different metrics** — there is no Pareto-dominant model

## How to apply

Per [[00-overview-phase2-build-and-share]] §04: *"systems should be designed to allow models to be exchanged and continuously evaluated."*

1. **Abstract at the API layer** — prompts and outputs through a unified interface; provider-specific quirks hidden.
2. **Configuration over code** — model choice is a config-file value.
3. **Continuous benchmarking** rather than one-time selection.
4. **Per-task model choice** is acceptable — cheap model for easy subtasks, frontier model for hard ones; the whole system pays the lower aggregate cost.

## See also

- [[model-agnostic-architecture]] — the concept this lesson canonicalises.
- [[building-permits]] — empirical foundation.
- [[llm-as-a-judge]] / [[llm-benchmarks]] — the evaluation methodology.
