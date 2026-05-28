---
title: AI is rarely the primary challenge
type: lesson
slug: ai-is-rarely-the-primary-challenge
phase: II
project: [smart-parking, infrastructure-maintenance, digital-eye-clinic, medical-documentation, building-permits]
concept: [data-access, partner-bottleneck]
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

# AI is rarely the primary challenge

The Phase II booklet opens its Technology insights with this finding ([[00-overview-phase2-build-and-share]] §04, p. 17):

> *"In many cases, the deployed AI technologies are already available and mature (e.g. computer vision in smart parking or speech recognition for medical transcription). The more significant challenges lie in infrastructure, data access, integration, governance, and adoption in day-to-day operations."*

## Evidence

The model rarely fails. The surrounding system does:

| Project | What the AI did | What was actually hard |
|---|---|---|
| [[smart-parking]] | Camera-based vehicle detection — mature CV | Property-owner consent for camera placement |
| [[infrastructure-maintenance]] | Drone-based defect detection — mature CV | Military base access permissions |
| [[digital-eye-clinic]] | Retinal-image classification — established medical AI | Hospital data-sharing agreements + in-house platform engineering |
| [[medical-documentation]] | LLM transcription — commodity capability | Patient-data protection blocking deployment entirely |
| [[building-permits]] | Plan-document understanding — frontier capability | Integration with eBaugesucheZH + administrative-reproducibility tension |

## How to apply

When scoping a new AI pilot, do **not** start with model choice. Start with:

1. **Who needs to give you access** (partners, supervisors, data subjects)?
2. **What data exists, and what's its access regime?**
3. **What's the integration surface** (existing systems, processes, governance)?
4. **What's the adoption barrier** (training, change management, organisational alignment)?

If you can't answer those four, model choice is premature. If you *can*, model choice is often a swap-in decision rather than a hard engineering problem — see [[model-agnostic-architecture]].

## See also

- [[scoping-is-ai-the-right-approach]] — the broader theme this lesson anchors.
- [[partner-bottleneck]] — the cross-cutting failure mode this lesson names.
- [[data-access]] / [[data-access-is-the-most-powerful-lever]] — the most-cited blocker.
