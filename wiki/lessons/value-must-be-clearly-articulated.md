---
title: AI value must be clearly articulated, not assumed from technical feasibility
type: lesson
slug: value-must-be-clearly-articulated
phase: II
project: [bridge-monitoring, digital-eye-clinic, building-permits]
concept: []
regulation: []
stakeholder: []
sources:
  - 00-overview-phase2-build-and-share#para-04-organisation
confidence: high
freshness: 2026-05
applies_to_lifecycle_stage: [scoping]
cross_cutting: true
created: 2026-05-28
updated: 2026-05-28
---

# AI value must be clearly articulated

From [[00-overview-phase2-build-and-share]] §04 Organisation, p. 19:

> *"The benefits of AI are not always immediately apparent to domain experts (e.g. sensor-based monitoring of bridge vibration behaviour as a complement to visual inspections). The key is a clear link to concrete decisions and operational value in day-to-day activities. AI should be deployed where it creates tangible value, not merely because it is technologically feasible."*

## What "clearly articulated" means

A clear AI value articulation has three properties:

1. **Linked to a concrete decision** — what choice does the AI enable or improve? (Not "it analyses the data" but "it tells the maintenance team which span to inspect next.")
2. **Quantified against the status quo** — how much better, cheaper, faster, or safer than the current process? (Not "it's an improvement" but "it reduces inspection time by 40%.")
3. **Defensible to operational staff** — would the domain experts who do this work today agree the AI helps? (Not assumed from the modeller's perspective.)

## Evidence base

- **[[bridge-monitoring]]** — the booklet's named example: sensor-based monitoring complements (rather than replaces) visual structural inspection. Value = earlier signal on deteriorating components, not "replacing" engineers.
- **[[digital-eye-clinic]]** — value = throughput against rising patient volumes + shortages of skilled professionals, not "AI replaces ophthalmologists."
- **[[building-permits]]** — value = preliminary check costing under CHF 2/application + catching formal deficiencies before formal proceedings, not "AI decides the permit."

Each of these articulations names a concrete operational benefit. None of them claims AI is *replacing* the human work.

## How to apply

For any AI use case scoping:

1. **Write the value in one sentence**, structured: *"The AI lets [user role] [do specific thing] so that [concrete benefit]."*
2. **If you can't, refine the use case.** "Apply AI to X" is not a value articulation; "Help the X team prioritise their next decision" is.
3. **Validate with domain experts** before procurement. If they shrug, the articulation is wrong.

## See also

- [[ai-is-rarely-the-primary-challenge]] — broader scoping framing.
- [[new-ways-of-working-need-change-management]] — companion at the people layer.
- [[scoping-is-ai-the-right-approach]] — broader theme.
