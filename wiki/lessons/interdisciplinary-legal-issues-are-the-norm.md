---
title: Interdisciplinary legal issues are the norm for AI applications
type: lesson
slug: interdisciplinary-legal-issues-are-the-norm
phase: II
project: [medical-documentation, digital-eye-clinic, inspection-robots, building-permits]
concept: []
regulation: [dsg-fadp, eu-ai-act, machinery-regulation]
stakeholder: [itsl-uzh]
sources:
  - 00-overview-phase2-build-and-share#para-04-legal
confidence: high
freshness: 2026-05
applies_to_lifecycle_stage: [scoping, procurement]
cross_cutting: true
created: 2026-05-28
updated: 2026-05-28
---

# Interdisciplinary legal issues are the norm

From [[00-overview-phase2-build-and-share]] §04 Legal, p. 18:

> *"AI applications typically span multiple areas of law (e.g. data protection and medical device regulation in the digital eye clinic). Isolated assessments are insufficient. AI providers require a holistic legal evaluation across the entire use case, rather than isolated compliance assessments of individual components."*

## Why this matters operationally

A typical AI deployment in healthcare faces *at least*:

- Data protection ([[dsg-fadp]])
- Medical device regulation (potentially MDR / IVDR for the EU layer)
- Sector regulation (Swissmedic remit)
- Liability law
- AI-specific regulation ([[ai-convention-ch-implementation]], emerging)
- Procurement law (for public-sector deployments)

A compliance review that addresses only one of these will miss the interactions. The interactions are often where the binding constraints live (a system that passes data-protection review may still fail medical-device classification).

## Evidence base

- **[[digital-eye-clinic]]** — data protection + medical device + ethics simultaneously.
- **[[medical-documentation]]** — data protection + healthcare regulation + supervisory-authority engagement.
- **[[inspection-robots]]** — EU AI Act + EU Machinery Regulation + ISO/IEC 42001 management standard.
- **[[building-permits]]** — cantonal building law + federal data protection + EMBAG + automated-decision regulation.

The pattern is so consistent that the booklet treats interdisciplinary legal analysis as the *default*, with isolated single-instrument compliance reviews as the exception.

## How to apply

1. **Engage a mandated expert with breadth**, not just depth in one instrument. [[itsl-uzh]] is the corpus's default for this reason.
2. **Map the regulation interaction surface** explicitly: which instruments apply, how they interact, what each requires.
3. **Pre-engage supervisory authorities** with overlapping remits — see [[regulatory-roundtable-is-high-leverage]].

## See also

- [[itsl-uzh]] — the institutional default for cross-instrument legal analysis.
- [[integrate-regulation-early]] — the companion lesson on timing.
- [[continuous-regulatory-learning-beats-rigid-approval]] — the companion lesson on regulatory dynamics.
