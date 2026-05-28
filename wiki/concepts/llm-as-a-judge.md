---
title: LLM-as-a-Judge
type: concept
slug: llm-as-a-judge
canonical_source: null
related: [llm-benchmarks, frontier-models, large-language-models]
appears_in: [building-permits]
created: 2026-05-28
updated: 2026-05-28
---

# LLM-as-a-Judge

A methodology where one LLM is used to evaluate the outputs of another LLM against reference answers — typically scoring on a 0-10 scale across multiple capability dimensions. **Not in the booklet glossary**, but operationally central to [[building-permits]] as the scoring backbone of the 3,336-evaluation benchmark.

## How [[building-permits]] uses it

| Element | Value |
|---|---|
| Models evaluated | 8 frontier LLMs across OpenAI, Google, Anthropic |
| Queries per model | ~417 |
| Runs per query | 3 (for consistency measurement) |
| Total evaluations | 3,336 |
| Scoring | LLM-as-a-Judge → 0–10 against expert reference |
| Dimensions | information extraction · counting · measuring/calculating · spatial understanding · context understanding |

## Why it matters as a concept

The booklet ([[00-overview-phase2-build-and-share]] §04 Technology) explicitly flags that generic [[llm-benchmarks]] have *"limited explanatory power"*. LLM-as-a-Judge is the corpus's answer: domain-specific scoring on real administrative tasks, calibrated to expert ground truth. It makes the benchmark *trust-worthy for a specific use case* rather than *internally consistent on a generic test set*.

## Methodological caveats

- The judge LLM may share biases with the judged LLMs (especially if from the same provider family).
- Scoring 0-10 collapses different failure modes — a hallucinated number scored 4 isn't the same as a missing entry scored 4.
- Reproducibility across judge-model versions is non-trivial; the [[building-permits]] team scored each query 3 times specifically to measure consistency.

## See also

- [[llm-benchmarks]] — the broader category.
- [[building-permits]] — the canonical case study.
- [[model-agnostic-architecture]] — what you build *after* the benchmark shows no single best model.
