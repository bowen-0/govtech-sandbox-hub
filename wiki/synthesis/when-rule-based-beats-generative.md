---
title: When rule-based systems beat generative AI — A decision guide
type: synthesis
slug: when-rule-based-beats-generative
question: "Should I use rule-based logic or generative AI for this decision?"
audience: [administrative-staff-scoping-a-pilot, ai-providers-pre-rfp, public-sector-architects]
connects:
  - rule-based-beats-generative-for-defined-logic
  - probabilistic-ai-vs-administrative-reproducibility
  - generative-ai
  - building-permits
  - 00-overview-phase2-build-and-share
created: 2026-05-28
updated: 2026-05-28
---

# When rule-based systems beat generative AI

> **For:** anyone choosing between rule-based logic, ML models, and generative AI for a Swiss-public-sector decision system.
>
> **TL;DR:** Generative AI is for *unstructured input*. Rule-based logic is for *traceable, legally-relevant, reproducible decisions*. The corpus is unusually unambiguous on this — and the consequences are administrative-law-shaped, not engineering-shaped.

---

## The booklet's own framing

From [[00-overview-phase2-build-and-share]] §04 Technology, p. 17:

> *"Rule-based systems outperform generative AI for well-defined decision logic: generative models demonstrate strengths in processing unstructured information, such as summarisation, transcription, information structuring, or preliminary checks (e.g. medical documentation or pre-checks in building permit procedures). However, they reach their limits in clearly defined, traceable, and legally relevant decision processes. In such cases, rule-based approaches deliver more robust and transparent results."*

---

## A decision tree

```
                    Is the decision rule definable as
                    a finite if/then matrix?
                              │
                ┌─────────────┴─────────────┐
                │                           │
              YES                          NO
                │                           │
                ▼                           ▼
        Use rule-based logic.       Are the inputs unstructured
        AI may handle unstructured  (text, images, audio)?
        sub-inputs at the edges.            │
                              ┌─────────────┴─────────────┐
                              │                           │
                            YES                          NO
                              │                           │
                              ▼                           ▼
                      Generative AI is        Reconsider — most
                      a fit. Frame outputs    "AI-shaped" problems
                      as suggestions, not     fall in one of the
                      decisions. See          two yes-branches.
                      [[fadp-art-21]].
```

---

## Three reasons rule-based wins for administrative decisions

### 1. Reproducibility

Swiss administrative law assumes that the same case gets the same outcome — *equal treatment* and *prohibition of arbitrariness* are core principles. Generative AI fights this by construction: ask the same question three times and get three slightly different answers. The [[building-permits]] benchmark measured consistency-across-3-runs at 86.8% (best) to 78.8% (worst) — meaning a non-trivial fraction of cases would receive *different* AI assessments from the same model run twice. See [[probabilistic-ai-vs-administrative-reproducibility]].

### 2. Traceability

A rule-based system can explain *exactly* why it gave the answer it did. A generative model can produce a plausible-sounding explanation that doesn't necessarily reflect the actual computation. For administrative-law contexts — where [[fadp-art-21]] requires human review of automated decisions, and *Art. 29 BV* requires that decisions be comprehensible — rule-based explainability is structurally easier to defend.

### 3. Cost stability

A rule-based check on a building application costs essentially zero (one IF-statement evaluation). A frontier-LLM check on the same application costs CHF 0.0001 — CHF 0.033 per query and runs in 3.2 — 41.7 seconds. For high-volume processes, the cost difference matters at the budget level.

---

## When generative AI does win

It's not always wrong. Generative AI is the right tool for:

- **Unstructured input parsing** — extracting structured data from documents, transcribing speech, summarising free text (e.g. [[medical-documentation]] transcription, [[building-permits]] plan-document understanding).
- **Pre-checks and quality improvement** — voluntary, non-binding pre-screening that an applicant runs before submission. See [[pre-submission-quality-is-the-leverage]].
- **Cases where reproducibility doesn't matter** — exploratory queries, draft suggestions, document discovery.

The discipline is to keep generative AI **out of the deterministic decision step** while letting it do the work it's actually good at.

---

## The hybrid pattern (the corpus's recommended default)

The [[building-permits]] prototype is the canonical hybrid:

```
[Applicant submits documents]
        │
        ▼
[Rule-based logic determines which procedure applies]   ← 8 project types × ~20 criteria
        │
        ▼
[Generative AI parses uploaded plans and datasheets]    ← unstructured input handling
        │
        ▼
[Rule-based completeness check]                         ← deterministic decision
        │
        ▼
[Human reviews; AI output is advisory]                  ← FADP Art. 21 compliance
```

Result: predictable cost, traceable decisions, AI doing the work it's good at, regulatory compliance built in.

---

## What to read next

1. **[[rule-based-beats-generative-for-defined-logic]]** — the underlying atomic lesson with quantitative support.
2. **[[building-permits]]** — the canonical case study; read for the hybrid pattern in production.
3. **[[probabilistic-ai-vs-administrative-reproducibility]]** — the lesson on why reproducibility matters in admin law.
4. **[[fadp-art-21]]** — the legal anchor that constrains "AI decides" patterns.
5. **[[pre-submission-quality-is-the-leverage]]** — where generative AI does add value in admin processes.

## See also

- [[scoping-is-ai-the-right-approach]] — the broader scoping theme.
- [[generative-ai]] — concept definition.
