---
title: Model-Agnostic Architecture
type: concept
slug: model-agnostic-architecture
canonical_source: null
related: [frontier-models, large-language-models, llm-benchmarks, llm-as-a-judge]
appears_in: [building-permits]
created: 2026-05-28
updated: 2026-05-28
---

# Model-Agnostic Architecture

An AI system design where the underlying model is treated as a swappable component rather than a hardcoded dependency. Models can be changed without changing the application code; new models can be benchmarked continuously and adopted as evidence supports it.

## Why the corpus insists on this

From [[00-overview-phase2-build-and-share]] §04 Technology ("Model-agnostic architecture proves advantageous"):

> *"Given the rapid pace of technological development, systems should be designed to allow models to be exchanged and continuously evaluated (e.g. benchmarking in the «AI for building permits» project)."*

The empirical foundation: [[building-permits]] benchmarked 8 frontier models and found **no single best provider** — different models win on different metrics (accuracy, speed, cost, consistency). For a system that must work across many sub-tasks, locking in one model creates either over-spend (when you pay for the best model on tasks where a cheaper model would suffice) or under-perform (when you commit to a cheap model that fails on harder sub-tasks).

## Practical implications

- **Abstraction at the API layer**: prompts and outputs go through a unified interface that hides provider differences.
- **Configuration over code**: model choice is a config-file value, not a hardcoded constant.
- **Continuous benchmarking** rather than a one-time selection — see [[llm-as-a-judge]] for the methodology.
- **Cost monitoring per task**: different tasks may use different models depending on cost-quality tradeoffs.

## See also

- [[building-permits]] — the empirical source for "no single best model".
- [[llm-as-a-judge]] / [[llm-benchmarks]] — the evaluation methodology that justifies the abstraction.
- [[frontier-models]] — the booklet's recommendation to combine frontier + open-source strategically.
