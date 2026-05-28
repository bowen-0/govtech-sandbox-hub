---
title: FADP Art. 21 — Automated Individual Decisions
type: regulation
slug: fadp-art-21
jurisdiction: ch-federal
instrument: act
domain: [data-protection, ai-governance]
year: 2023
project: [machine-translation, building-permits, medical-documentation]
parent: dsg-fadp
created: 2026-05-28
updated: 2026-05-28
---

# FADP Art. 21 — Automated Individual Decisions

Article 21 of the Swiss Federal Act on Data Protection ([[dsg-fadp]]). Provides individuals with the right to human review when a decision affecting them is taken solely by automated means. Functionally parallel to GDPR Art. 22, but with distinctly Swiss statutory framing.

## Why it's load-bearing in the corpus

This is the single most-cited article when sandbox projects engage automated administrative decisions:

- **[[building-permits]]** — flags this as the reason fully automated rejection of a building application would *"likely breach"* the FADP. The prototype is designed as a *pre-check* — non-binding, human-reviewed — specifically to stay clear of Art. 21.
- **[[machine-translation]]** — referenced in the original FADP framing for AI-in-administrative-procedures.
- **[[medical-documentation]]** — relevant whenever AI-generated medical notes inform clinical decisions; emphasised in the regulatory roundtable convened with the data-protection supervisory authority.

## The "voluntary AI pre-check" liability gotcha

From [[building-permits]] (source: [[p2-building-permits]] ~p. 25):

> Even non-binding AI pre-check tools may trigger **state liability under "protected trust"** if users reasonably rely on them — they must be clearly labelled as non-binding.

This is a subtle constraint on UX: a "pre-check" affordance must visibly communicate its non-binding nature or it may functionally become the decision in users' minds (and the law follows their reasonable expectations).

## See also

- [[dsg-fadp]] — the parent statute.
- [[bv-art-29]] — constitutional right to be heard, paired with Art. 21 for the full automated-decision framing.
- [[building-permits]] — canonical project for the Art. 21 + pre-check pattern.
