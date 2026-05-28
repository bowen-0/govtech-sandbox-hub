---
title: Is AI even the right approach? — Scoping guide
type: synthesis
slug: scoping-is-ai-the-right-approach
question: "Is AI the right approach for this problem?"
audience: [administrative-staff-scoping-a-pilot, ai-providers-pre-rfp]
connects:
  - ai-is-rarely-the-primary-challenge
  - rule-based-beats-generative-for-defined-logic
  - data-access-is-the-most-powerful-lever
  - integration-matters-more-than-model-choice
  - new-ways-of-working-need-change-management
  - partner-bottleneck
  - data-access
  - 00-overview-phase2-build-and-share
created: 2026-05-28
updated: 2026-05-28
---

# Is AI even the right approach?

> **For:** administrative staff scoping a new AI pilot · AI providers pre-RFP · anyone tempted to start with "we should use LLMs for this".
>
> **TL;DR:** Probably not the way you think. Across ten sandbox projects, the AI was rarely the binding constraint. Partners, data access, integration, and governance were. Here's what the corpus actually says, and how to ask better scoping questions.

---

## What the booklet itself says

The Phase II booklet opens its insights with the same caveat ([[00-overview-phase2-build-and-share]] §04 Technology, p. 17):

> *"AI is rarely the primary challenge: in many cases, the deployed AI technologies are already available and mature (e.g. computer vision in smart parking or speech recognition for medical transcription). The more significant challenges lie in infrastructure, data access, integration, governance, and adoption in day-to-day operations."*

In other words: the **default position from the challenge owner's own publication** is that AI scoping conversations starting with model choice are starting in the wrong place.

---

## Four questions to ask before you commit to AI

### 1. Is your decision logic well-defined?

If you can describe the decision as an if/then matrix, you probably don't need generative AI. You need rule-based logic and maybe AI for unstructured-input handling at the edges.

The canonical case: [[building-permits]] — procedure determination uses pure rule-based logic (8 project types × ~20 zone/protection criteria); generative AI is reserved for unstructured document quality checks. Read [[rule-based-beats-generative-for-defined-logic]] for the full pattern.

**Signal you should use rule-based instead:** the decision is *traceable*, *legally relevant*, and you need it to be *reproducible* across runs. Generative AI fights all three — see [[probabilistic-ai-vs-administrative-reproducibility]].

### 2. Do you have data access?

Data access is the most-cited blocker in the corpus. Per the booklet: *"data access is the most powerful lever."* See [[data-access-is-the-most-powerful-lever]] and the [[data-access-patterns-and-unblocking]] theme.

**Signal data access is your real bottleneck:** you keep finding "promising approaches" that you can't execute because no one will give you the data. Don't keep iterating on model choice. Invest in unblocking access — pseudonymisation, [[auftragsdatenbearbeitung]] contracts, partner negotiation. The data is what unlocks the AI, not the other way around.

### 3. Is your bottleneck partners, integration, or governance?

[[partner-bottleneck]] is the cross-cutting failure mode — surfaced in 6 of 10 sandbox projects. [[integration-matters-more-than-model-choice]] is the production-stage equivalent. [[new-ways-of-working-need-change-management]] is the people-side equivalent.

**Signal you should stop optimising the model:** the model already works adequately in a notebook. What doesn't work is the rest of the system — getting it into the workflow, persuading the team to use it, getting the legal sign-off.

### 4. What outcome class can you realistically aim for?

The sandbox treats both **real-world testing** and **regulatory analysis only** as legitimate outcomes ([[real-world-testing]]). 3 of 5 Phase II projects achieved operational testing; 2 ([[medical-documentation]], [[inspection-robots]]) pivoted to pure regulatory analysis after partner constraints. Both contributed real value.

**Signal you should pre-plan an analysis-only fallback:** the partner-access risk is high (healthcare data, military access, EU certification), or the regulatory question is itself the point.

---

## Concrete signals from the corpus

| If you observe… | The binding constraint is probably… | Read |
|---|---|---|
| "We have access to the data, the model works in a notebook, we can't get it into production" | Integration | [[integration-matters-more-than-model-choice]] |
| "Our partner won't give us the data" | Data access / partner | [[data-access-patterns-and-unblocking]] |
| "The decision rule is well-defined but the AI gives different answers" | Wrong tool — rule-based | [[rule-based-beats-generative-for-defined-logic]] |
| "Our staff distrust the system; they keep working around it" | Change management | [[new-ways-of-working-need-change-management]] |
| "Legal flagged a problem with how we're processing data" | Regulation was engaged too late | [[integrate-regulation-early]] |
| "We need EU market access" | Cross-border regulatory clarity | [[eu-market-access-for-swiss-ai]] |

---

## What to read next, in order

1. **[[ai-is-rarely-the-primary-challenge]]** — the foundational lesson.
2. **[[data-access-is-the-most-powerful-lever]]** — the most-cited blocker pattern.
3. **[[rule-based-beats-generative-for-defined-logic]]** — when to *not* use generative AI even if you could.
4. **[[integration-matters-more-than-model-choice]]** — what makes pilots become products.
5. **[[partner-bottleneck]]** (concept) and **[[partner-pivot-is-normal]]** (lesson) — how to plan for partner risk.

If after reading these you're still convinced AI is right, the corpus has more granular guidance:

- For frontier-LLM-specific design: **[[model-selection-is-task-specific]]** and the **[[model-agnostic-architecture]]** concept.
- For benchmark methodology: **[[llm-benchmarks]]** and **[[llm-as-a-judge]]**.
- For the regulatory framing: **[[integrate-regulation-early]]**.

---

## See also

- [[00-overview-phase2-build-and-share]] — the booklet that anchors most of this synthesis.
- [[when-rule-based-beats-generative]] — companion theme, narrower question.
- [[zh-ai-ecosystem-strategy-2026-2029]] — the macro context in which "do we need AI?" decisions get made.
