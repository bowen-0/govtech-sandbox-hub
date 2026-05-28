---
title: How to unblock data access for your pilot — Patterns from the corpus
type: synthesis
slug: data-access-patterns-and-unblocking
question: "How do I unblock data access for my AI pilot?"
audience: [administrative-staff-scoping-a-pilot, ai-providers-pre-rfp, partner-org-leads]
connects:
  - data-access-is-the-most-powerful-lever
  - data-reuse-multiplies-pilot-impact
  - partner-pivot-is-normal
  - data-access
  - partner-bottleneck
  - pseudonymisation
  - data-minimisation
  - auftragsdatenbearbeitung
  - infrastructure-maintenance
  - 00-overview-phase2-build-and-share
created: 2026-05-28
updated: 2026-05-28
---

# How to unblock data access for your pilot

> **For:** AI providers, public-administration product owners, sandbox project leads who have hit a data-access wall.
>
> **TL;DR:** The booklet calls data access the *"most powerful lever."* The corpus's 10 projects each have a different blocker — but the unblocking patterns are surprisingly consistent.

---

## The booklet's own framing

From [[00-overview-phase2-build-and-share]] §04 Technology, p. 17:

> *"Data access is the most powerful lever: even seemingly simple datasets can generate substantial value for the development and optimisation of AI systems. When made accessible, they enable a wide range of providers to train, validate, and improve their models."*

This is the explicit ranking of priorities: data access *above* model choice, integration, or governance.

---

## The blocker taxonomy

Every project in the corpus has a different data-access blocker. Naming yours is the first step.

| Blocker type | Example | Where in the corpus |
|---|---|---|
| **Property / physical access** | Camera mounts; military base permissions | [[smart-parking]]; [[infrastructure-maintenance]] |
| **Institutional gatekeeping** | School-IT access; hospital data agreements | [[ai-in-education]]; [[digital-eye-clinic]] |
| **Regulatory blocker** | Patient-record protection; commercial data confidentiality | [[medical-documentation]] |
| **Partner withdrawal** | Original implementation partner walks away | [[bridge-monitoring]] |
| **No suitable test partner exists** | Specialised use case with no production-ready partner | [[inspection-robots]] |

See [[partner-bottleneck]] for the concept; the pattern recurs in 6 of 10 sandbox projects.

---

## Four unblocking patterns

### 1. Pseudonymisation + commissioned-data-processing contracts

The Phase I default. Combine [[pseudonymisation]] (data-subject identifying attributes replaced) with [[auftragsdatenbearbeitung]] (third-party AI service contracted under the controller's authority). Together they take a non-trivial fraction of "we can't share this data" cases into "we can share an anonymised version under contract."

**When it works:** the data has identifying attributes that can be removed without destroying the use case. *Most* image data, *most* text data, *most* tabular data.

**When it doesn't:** the data's value is precisely in the identifying detail (rare in administrative use cases, but applies in some health-record scenarios).

### 2. Partner relationship work (more than the AI work)

The corpus has six projects where partner-relationship work was the load-bearing input. The booklet's framing ([[00-overview-phase2-build-and-share]] §04 Organisation, p. 19, "Strong stakeholder engagement is decisive"):

> *"Successful projects are characterised by committed implementation partners who contribute time, resources, networks, and domain expertise."*

**How to apply:** identify the partner-access dependency at intake, not during execution. Pre-define acceptable pivot directions if access slips. Treat partner-management as a first-class workstream, not a contingency.

### 3. Pivot to analysis-only (when access cannot be unblocked)

The booklet treats this as a legitimate outcome class. 2 of 5 Phase II projects pivoted ([[medical-documentation]], [[inspection-robots]]). Both delivered substantial value via regulatory analysis, supervisory-authority engagement, and best-practice documentation.

**How to apply:** see [[partner-pivot-is-normal]] for the playbook. The key is recognising the pivot opportunity early — before the team has spent its budget chasing inaccessible data.

### 4. Publishing derived datasets (so the next pilot doesn't hit the same wall)

The canonical case: [[infrastructure-maintenance]] → IBM Research dataset on Hugging Face. The sandbox's investment in data collection becomes a public benchmark, multiplying impact beyond the engagement. See [[data-reuse-multiplies-pilot-impact]].

**How to apply:** at intake, plan the derived dataset's downstream publication. Design pseudonymisation, annotation quality, and licensing to enable reuse.

---

## A diagnostic checklist

Before you escalate to "we can't get the data":

- [ ] Have you identified the **specific** blocker (property / institutional / regulatory / partner)?
- [ ] Have you tried [[pseudonymisation]] + [[auftragsdatenbearbeitung]] as the legal-technical pattern?
- [ ] Have you engaged the [[data-protection-officer]] *as a partner*, not as a gatekeeper?
- [ ] Have you considered scoping down to a **subset** of the data the partner could share (per [[data-minimisation]])?
- [ ] Is there an **alternative partner** in the same problem space (the [[bridge-monitoring]] pivot pattern)?
- [ ] Could the project pivot to **regulatory analysis** as a primary outcome ([[partner-pivot-is-normal]])?
- [ ] If you do collect data, can it be published downstream to enable future pilots ([[data-reuse-multiplies-pilot-impact]])?

---

## What to read next

1. **[[data-access-is-the-most-powerful-lever]]** — the foundational lesson.
2. **[[partner-bottleneck]]** — the cross-cutting concept this theme operationalises.
3. **[[partner-pivot-is-normal]]** — what to do when access can't be unblocked.
4. **[[pseudonymisation]]** + **[[data-minimisation]]** + **[[auftragsdatenbearbeitung]]** — the legal-technical pattern.
5. **[[data-reuse-multiplies-pilot-impact]]** — the long-term play.

## See also

- [[scoping-is-ai-the-right-approach]] — broader scoping theme.
- [[partner-roles-around-a-pilot]] — companion theme on partner-side success factors.
