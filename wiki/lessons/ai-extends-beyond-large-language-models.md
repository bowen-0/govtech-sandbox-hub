---
title: AI extends beyond large language models
type: lesson
slug: ai-extends-beyond-large-language-models
phase: I-and-II
project: [smart-parking, infrastructure-maintenance, bridge-monitoring]
concept: [computer-vision, large-language-models]
regulation: []
stakeholder: []
sources:
  - 00-overview-phase2-build-and-share#para-04-technology
confidence: high
freshness: 2026-05
applies_to_lifecycle_stage: [scoping]
cross_cutting: true
created: 2026-05-28
updated: 2026-05-28
---

# AI extends beyond large language models

A corrective principle from [[00-overview-phase2-build-and-share]] §04 Technology, p. 17:

> *"Many high-impact use cases in the public sector are based on computer vision or sensor data rather than language models (e.g. smart parking, drone inspections, sensor-based bridge monitoring)."*

## Why it matters

The post-2022 LLM hype cycle compressed public discourse about AI into "AI = LLMs = ChatGPT." The corpus pushes back hard. Of the 10 implemented sandbox pilots, **4 are predominantly LLM-based**, the other **6 are computer vision / sensor / image-recognition** in their core technical layer. The biggest impact-to-date pilots (Smart Parking → Frauenfeld production roll-out; the Hugging-Face-published drone dataset; the SOB bridge monitoring) are non-LLM use cases.

## How to apply

When scoping a public-sector AI use case:

1. **Don't anchor on LLMs by default.** Start from the problem and let the modality follow.
2. **Computer vision is mature** for a wide range of perception/inspection use cases — the technology is rarely the binding constraint (see [[ai-is-rarely-the-primary-challenge]]).
3. **Sensor + AI patterns** unlock infrastructure monitoring, predictive maintenance, anomaly detection — modalities LLMs are not the right tool for.
4. **Combine modalities deliberately** — multi-modal problems (e.g. [[building-permits]] with images + text) are different from single-modality ones.

## See also

- [[computer-vision]] — the dominant Phase I paradigm.
- [[large-language-models]] — what this lesson contrasts against.
- [[scoping-is-ai-the-right-approach]] — broader scoping theme.
