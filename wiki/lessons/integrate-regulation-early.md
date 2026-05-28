---
title: AI providers should integrate regulation early into product development
type: lesson
slug: integrate-regulation-early
phase: I-and-II
project: [autonomous-systems, inspection-robots, medical-documentation, building-permits]
concept: []
regulation: [eu-ai-act, machinery-regulation, dsg-fadp]
stakeholder: []
sources:
  - 00-overview-phase2-build-and-share#para-04-legal
  - p1-autonomous-systems#para-recert
confidence: high
freshness: 2026-05
applies_to_lifecycle_stage: [scoping, procurement]
cross_cutting: true
created: 2026-05-28
updated: 2026-05-28
---

# AI providers should integrate regulation early into product development

From [[00-overview-phase2-build-and-share]] §04 Legal, p. 18:

> *"AI providers should integrate regulatory considerations early into product development: if regulatory requirements are addressed too late, flawed assumptions may arise in the business model. Early clarification is essential to avoid pursuing an incorrect development path. For example, the «Autonomous Systems» project showed that retrofitting existing agricultural vehicles for automation may require full recertification of the product."*

## Evidence base

- **[[autonomous-systems]]** — the canonical case: agricultural-vehicle retrofitting required full re-certification. The business model assumed retrofit; the regulation imposed re-cert.
- **[[inspection-robots]]** — engaged [[eu-ai-act]] + [[machinery-regulation]] interplay early; ISO/IEC 42001 piloted in parallel rather than bolted on later.
- **[[medical-documentation]]** — patient-data protection blocked operational deployment entirely; had the data-protection regime been engaged at product-design time, the operational design might have been different (e.g. on-prem deployment from day one).

## How to apply

1. **In the first sprint of an AI product**, map the applicable regulations and the *cheapest* changes that would put you out of scope.
2. **Engage supervisory authorities** before locking in product architecture — see [[regulatory-roundtable]] for the high-leverage format.
3. **Treat regulation as a design constraint**, not a compliance audit at the end.

## See also

- [[autonomous-systems]] — the canonical case.
- [[continuous-regulatory-learning-beats-rigid-approval]] — what the regulator-side equivalent looks like.
- [[scoping-is-ai-the-right-approach]] — broader scoping theme.
