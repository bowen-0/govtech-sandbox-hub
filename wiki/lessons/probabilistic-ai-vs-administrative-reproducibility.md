---
title: Probabilistic AI fights administrative reproducibility
type: lesson
slug: probabilistic-ai-vs-administrative-reproducibility
phase: II
project: [building-permits, machine-translation]
concept: [generative-ai]
regulation: [fadp-art-21]
stakeholder: []
sources:
  - p2-building-permits#para-reproducibility
confidence: high
freshness: 2026-04
applies_to_lifecycle_stage: [scoping]
created: 2026-05-28
updated: 2026-05-28
---

# Probabilistic AI fights administrative reproducibility

A tension named explicitly in [[building-permits]]: administrative law expects *the same case to receive the same outcome* — the principle of *equal treatment* and *prohibition of arbitrariness*. Probabilistic AI is by construction non-deterministic: ask it the same question three times and get three (slightly) different answers.

## What the corpus says

From the building-permits source: *"95% vs 99% reliability is a substantive question requiring political decision."* The framing matters — this is presented as a political-administrative question, not a technical one. The probabilistic system might be cheaper, faster, and on-average accurate, but it cannot reproduce the case-by-case determinism that Swiss administrative law assumes.

The corpus also notes that the benchmark measured consistency-across-3-runs at 86.8% (best) to 78.8% (worst). Meaning: a non-trivial fraction of building applications would receive *different* AI assessments from the same model run twice.

## How to apply

Three responses to the tension:

1. **Constrain AI to non-binding pre-checks** (the [[building-permits]] approach). The AI suggests; a human decides. [[fadp-art-21]] requires this for individual decisions anyway.
2. **Use rule-based logic for the determinative step** ([[rule-based-beats-generative-for-defined-logic]]) and reserve AI for unstructured input handling.
3. **Increase reliability through ensembles or repeat-and-vote** — but this multiplies cost and doesn't fully resolve the principle.

There is no clean technical fix; the design choice is whether to accept the loss of determinism or to design the system so AI is never the deterministic actor.

## See also

- [[building-permits]] — canonical case.
- [[fadp-art-21]] — the legal framing for the human-in-the-loop response.
- [[rule-based-beats-generative-for-defined-logic]] — the design pattern that resolves much of the tension.
