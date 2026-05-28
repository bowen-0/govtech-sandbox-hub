---
title: Pre-submission quality improvement is higher-leverage than post-submission AI processing
type: lesson
slug: pre-submission-quality-is-the-leverage
phase: II
project: [building-permits]
concept: []
regulation: []
stakeholder: [raphael-von-thiessen]
sources:
  - p2-building-permits#para-leverage
confidence: high
freshness: 2026-04
applies_to_lifecycle_stage: [scoping]
created: 2026-05-28
updated: 2026-05-28
---

# Pre-submission quality improvement is higher-leverage than post-submission AI processing

From the [[building-permits]] source, attributed to Raphael von Thiessen:

> *"The greatest leverage of AI currently lies in improving the quality and completeness of building applications before submission."*
> — [[raphael-von-thiessen]], p. 7.

## What it means

In any process where errors cascade — incomplete inputs trigger queries, suspensions, prolonged proceedings — fixing errors **at the input stage** beats handling them at every downstream stage. For building permits, a large share of applications arrive incomplete or formally incorrect. An AI-assisted **pre-submission** check that catches missing drawings, wrong scales, or unsigned forms eliminates the largest single cost driver in the process — far more than an AI-assisted *review* that processes the same incomplete inputs more cleverly.

## Generalising the pattern

The lesson holds beyond building permits. In any administrative process:

- **Define the formal-completeness criteria** that must be true for a submission to enter formal proceedings.
- **Build a pre-check** that AI can run on the applicant's draft.
- **Make the pre-check explicitly non-binding** to avoid [[fadp-art-21]] / state-liability complications.

The downstream review is still where the substantive decision happens — but the *volume* of work it absorbs drops dramatically.

## How to apply

When scoping an AI use case in an administrative procedure:

1. Look for high-volume process stages with recurring formal-error patterns.
2. Build an AI pre-check that the applicant runs voluntarily.
3. Keep the official review unchanged — the AI value is in input quality, not in changing the review.

## See also

- [[building-permits]] — canonical case.
- [[fadp-art-21]] — the legal constraint that shapes the pre-check framing.
- [[rule-based-beats-generative-for-defined-logic]] — pre-checks are mostly rule-based; AI is for unstructured-input handling.
