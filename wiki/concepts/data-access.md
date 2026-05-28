---
title: Data Access
type: concept
slug: data-access
canonical_source: null
related: [partner-bottleneck, pseudonymisation]
appears_in: [smart-parking, infrastructure-maintenance, digital-eye-clinic, medical-documentation, building-permits]
created: 2026-05-28
updated: 2026-05-28
---

# Data Access

A derived concept (not in the booklet glossary, but the booklet's §04 Technology calls it out explicitly):

> *"Data access is the most powerful lever: even seemingly simple datasets can generate substantial value for the development and optimisation of AI systems. When made accessible, they enable a wide range of providers to train, validate, and improve their models."*
> — [[00-overview-phase2-build-and-share]] §04 Technology, p. 17.

## The pattern across the corpus

Data access is the chokepoint that recurs in **every project** — but the specific blocker differs:

| Project | Data-access constraint |
|---|---|
| [[smart-parking]] | Property-owner consent for camera placement. |
| [[infrastructure-maintenance]] | Military base access for drone deployment. |
| [[ai-in-education]] | School-IT access. |
| [[digital-eye-clinic]] | Hospital data-sharing agreements. |
| [[medical-documentation]] | Patient-record protection blocked operational use. |
| [[building-permits]] | Negotiated access to real applications via Stadt Kloten. |

The booklet calls this out as the *"partner-bottleneck"* pattern more often than as a model-quality issue — see [[partner-bottleneck]].

## Productive responses

- **Make derived datasets public** when possible. [[infrastructure-maintenance]] → IBM Research dataset on Hugging Face is the canonical example.
- **Pseudonymise upstream**. [[pseudonymisation]] is the technique that unlocks otherwise-blocked data sources.
- **Codify partner expectations early**. [[00-overview-phase2-build-and-share]] §04 Organisation, "Strong stakeholder engagement is decisive" — committed implementation partners with clear expectations from the outset.
