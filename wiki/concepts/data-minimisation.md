---
title: Data Minimisation
type: concept
slug: data-minimisation
canonical_source: null
related: [pseudonymisation, data-access]
appears_in: [smart-parking, ai-in-education, digital-eye-clinic]
created: 2026-05-28
updated: 2026-05-28
---

# Data Minimisation

The privacy-by-design principle of collecting and processing only the data strictly necessary for the AI system's purpose. Part of the **canonical Phase I privacy-by-design lexicon** — alongside *low resolution*, *masking*, *edge computing*, *instant deletion*, and [[pseudonymisation]] — first articulated in [[smart-parking]] and reused across the Phase I corpus.

## Concrete forms in the corpus

| Project | Form of minimisation |
|---|---|
| [[smart-parking]] | Low-resolution cameras incapable of capturing identifying detail; masking of bystander faces; instant deletion after parking-state inference. |
| [[ai-in-education]] | Limiting student-data processing to the AI-task scope; not retaining inputs beyond the immediate query. |
| [[digital-eye-clinic]] | Sharing only retinal images strictly needed for diagnostic inference; no broader patient-record access. |

## Legal anchor

Built into the Swiss data-protection regime — both [[dsg-fadp]] (federal) and [[idg-zh]] (cantonal) require that data processing be limited to what is necessary for the stated purpose. Failure to minimise is a common compliance gap; auditability of minimisation choices is a recurring [[data-protection-officer]] requirement.

## See also

- [[pseudonymisation]] — companion technique.
- [[smart-parking]] — canonical Phase I source for the privacy-by-design lexicon.
- [[dsg-fadp]] — federal legal anchor.
