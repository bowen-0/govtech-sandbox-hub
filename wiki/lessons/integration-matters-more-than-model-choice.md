---
title: Scaling fails on integration, not on model performance
type: lesson
slug: integration-matters-more-than-model-choice
phase: II
project: [building-permits, digital-eye-clinic]
concept: []
regulation: []
stakeholder: []
sources:
  - 00-overview-phase2-build-and-share#para-04-organisation
confidence: high
freshness: 2026-05
applies_to_lifecycle_stage: [deployment]
cross_cutting: true
created: 2026-05-28
updated: 2026-05-28
---

# Scaling fails on integration, not on model performance

From [[00-overview-phase2-build-and-share]] §04 Organisation, p. 19:

> *"Scaling often fails at integration, not at AI performance: the transition from pilot to operational deployment frequently fails due to insufficient integration into existing systems, processes, and governance structures, rather than limitations of the models themselves."*

## Evidence base

- **[[building-permits]]** — the prototype is explicitly architected for integration with **eBaugesucheZH** (cantonal building-permit platform) and the **GIS-Browser**. The booklet's source describes "isolated AI bolted onto a paper workflow creates media discontinuity and increases errors."
- **[[digital-eye-clinic]]** — clinical workflow integration was as load-bearing as the diagnostic model itself; the **modular open-source platform** was designed around integration constraints.
- **[[smart-parking]]** — successful Frauenfeld roll-out followed *exactly* because integration into city operations was deliberate; the model was the easy part.

## How to apply

When taking an AI pilot toward production:

1. **Map the system integration surface** before optimising the model. Existing CMSs, databases, GIS layers, identity systems, audit logs.
2. **Map the process integration** — where does the AI fit in the human workflow? Who reviews? Who escalates?
3. **Map the governance integration** — who is accountable? What's the change-management plan? How do users learn the new affordance?

A 60% accurate model that integrates well beats a 90% accurate model that doesn't.

## See also

- [[ai-is-rarely-the-primary-challenge]] — broader scoping framing.
- [[building-permits]] / [[digital-eye-clinic]] — canonical cases.
- [[new-ways-of-working-need-change-management]] — companion lesson at the people layer.
