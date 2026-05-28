---
title: Auftragsdatenbearbeitung (Commissioned Data Processing)
type: concept
slug: auftragsdatenbearbeitung
canonical_source: null
related: [data-access, pseudonymisation]
appears_in: [machine-translation, smart-parking, ai-in-education, building-permits]
created: 2026-05-28
updated: 2026-05-28
---

# Auftragsdatenbearbeitung — Commissioned Data Processing

The Swiss legal-technical pattern for letting a third-party AI service touch protected data on behalf of a data controller. A contractually-bound processor handles the data under the controller's authority and remains subject to the controller's data-protection obligations.

## Where the Swiss legal stack sits

Per the canonical Phase I framing (see [[machine-translation]] and [[smart-parking]] for canonical instances):

1. **Cantonal IDG** ([[idg-zh]]) — when a public body is the data controller.
2. **Federal FADP/DSG** ([[dsg-fadp]]) — when a private provider is the controller.
3. **Auftragsdatenbearbeitung contracts** — when *either* controller engages a third-party AI tool.

This three-layer stack appears in every Phase I project report. It is the canonical pre-EU-AI-Act Swiss framing for AI deployments in administrative contexts.

## When you need this

Any time:
- A public administration uses a commercial AI service (cloud LLMs, MT services, image-recognition APIs).
- A third party processes data on behalf of a controller.
- Data crosses an organisational boundary but the controller retains responsibility.

## Practical implications

- The contract must specify processing purposes, security measures, sub-processor permissions, data return/deletion terms.
- The controller remains liable to data subjects; cannot delegate fundamental responsibility to the processor.
- Auditability of processor compliance is typically required by the [[data-protection-officer]].

## See also

- [[dsg-fadp]] / [[idg-zh]] — the underlying statutes.
- [[machine-translation]] — canonical Phase I source for the legal stack.
- [[pseudonymisation]] — frequently combined with Auftragsdatenbearbeitung to reduce the data-protection surface.
