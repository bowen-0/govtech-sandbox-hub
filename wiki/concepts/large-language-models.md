---
title: Large Language Models (LLMs)
type: concept
slug: large-language-models
canonical_source: 00-overview-phase2-build-and-share#para-glossary
related: [frontier-models, generative-ai, llm-benchmarks]
appears_in: [medical-documentation, building-permits]
created: 2026-05-28
updated: 2026-05-28
---

# Large Language Models (LLMs)

> *"Large neural network–based language models trained on extensive text corpora to understand and generate natural language; they form the foundation of many generative AI applications."*
> — [[00-overview-phase2-build-and-share]], glossary p. 26.

The most operationally tested LLM use cases in Phase II are [[medical-documentation]] (transcription + structuring of medical notes — analysis-only) and [[building-permits]] (document understanding, completeness checks, plan-document interpretation — with real prototype). The booklet's strongest LLM-specific caveat ([[00-overview-phase2-build-and-share]] §04 Technology, "Model selection is task-specific"):

> *"Unlike generic LLM benchmarks, practical experience shows that a single 'best' model often does not exist, particularly in diverse use cases involving multiple data inputs (e.g. images and text)."*

This caveat is the operational source of the "model-agnostic architecture is mandatory" pattern that [[building-permits]] canonicalises.

## See also

- [[frontier-models]] — most production LLMs in the corpus are frontier models.
- [[llm-benchmarks]] — and their limits.
- [[generative-ai]] — the application domain.
