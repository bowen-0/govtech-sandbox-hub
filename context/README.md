# GovTech Hackathon 2026 — Context Hub

Personal working index for the **AI Innovation Sandbox Knowledge Hub** challenge.
Hackathon dates: **Thu 28 — Fri 29 May 2026** · FOITT, Eichenweg 3, Zollikofen (Bern).

---

## 1. The challenge in one paragraph

The Canton of Zürich runs an *Innovation-Sandbox für Künstliche Intelligenz* — a regulatory + technical playground where public administration, businesses and researchers pilot AI applications under real conditions. Since 2022 the sandbox has completed **10 pilots across two phases** and produced detailed PDF reports for each, plus two umbrella reports. The hard-won knowledge (legal frameworks, data access, organisational prerequisites, technical learnings, lessons learned) is locked inside ~12 static PDFs.

> **Our job at the hackathon:** make that knowledge *discoverable, applicable, and citable* for non-technical people planning a new AI project — typically administrative staff starting a new AI pilot.

Source: [`challenge/brief.md`](challenge/brief.md) (the full challenge text from govtech.digisus-lab.ch/project/11) and [`challenge/slides.pdf`](challenge/slides.pdf) (the challenge owner's deck).

## 2. What the challenge owner explicitly named

From `challenge/slides.pdf`, slide 4 — the most authoritative single statement of expectations:

| | What |
|---|---|
| **Primary goal** | Structuring / preparing the data foundation — e.g. **Knowledge Graph** or **LLM-Wiki** |
| **Secondary goal** | Audience-specific applications on top — e.g. **Guideline Generator**, **GraphRAG search engine** |
| **Available data** | All sandbox + project reports (this `reports/` folder) |
| **Out of scope** | Production system, new data collection, full legal review, access to other government data |

**Challenge owner contact:** Lukas Willi, Projektleiter KI, Amt für Wirtschaft, Kanton Zürich (Volkswirtschaftsdirektion).

## 3. Hard constraints (from the challenge brief)

These directly shape any architectural decision. Treat as acceptance criteria.

- **Non-technical audience.** Verwaltungsmitarbeitende must be able to use it.
- **Traceability / no hallucinations.** Every claim must link back to a specific report; "die Aussagen werden mit Verweisen auf die zugrunde liegenden Berichte nachvollziehbar gemacht."
- **Currency.** Reports span 4 years; AI legal landscape shifts fast. The system must make it *easy to update* and clearly flag stale content.
- **Sensitivity.** Legal claims and sensitive content need careful handling.
- **Bonus: embeddability** on the AI Innovation Sandbox website (zh.ch/innovation-sandbox / innovationsandbox.ai).

## 4. Resources index

### 4.1 Hackathon meta — `govtech-hackathon-2026-main/`
The downloaded organiser repo.
- `README.md` — full programme schedule (check-in times, mentoring sessions, meals, pitch slot).
- `hackathon-handbook.md` — format, roles, dribdat platform, pitch structure, IP rules (everything open-source).

### 4.2 Challenge brief — `challenge/`
- `brief.md` — full German text from the challenge platform. Problem, available data, expected impact, hackathon goal, possible approaches, constraints, sustainability.
- `brief.en.md` — **English translation** of `brief.md` for reading prep. Use the German `brief.md` when citing the challenge owner's exact wording.
- `slides.pdf` — Lukas Willi's pitch deck. Most concise statement of primary/secondary goals.

### 4.3 Sandbox reports — `reports/en/` (English, for your prep) + `reports/de/` (German, for prototype citations)

**How to read these.** Canton Zürich publishes both German and English versions of most reports. The English PDFs in `reports/en/` are your primary prep material — read them directly. The German PDFs in `reports/de/` are what the **prototype's RAG/KG should cite** at inference time, since the target users are German-speaking Swiss administrators and they expect to land on authoritative original-language text. Treat the two languages as parallel corpora, not as alternatives.

**Read order:** start with the Phase I overview (`00-overview-phase1-play-and-learn.pdf`), then skim the project reports.

| # | Topic | Phase | EN file | DE file | Report focus |
|---|---|---|---|---|---|
| **0a** | **Play & Learn** (sandbox overview) | I | `en/00-overview-phase1-play-and-learn.pdf` | `de/00-overview-phase1-play-and-learn.pdf` | Why the sandbox exists, its goals (regulatory learning, innovation, knowledge transfer, regulatory input), the 2-axis sandbox typology (*regulatory advice* × *data provision*), application/selection process, governance. **Best single entry point.** |
| **0b** | **Build & Share** (Phase II overview) | II | `en/00-overview-phase2-build-and-share.pdf` | `de/00-overview-phase2-build-and-share.pdf` | Phase II strategic framing — ecosystem-enablement, four-pillar 2026–2029 ZH ecosystem strategy, 7-sector submission taxonomy, 5 partner-role types, 11-term glossary, hyperlink graph into other Phase II reports. **The authoritative current snapshot of where the sandbox is now**; pair with Play & Learn for the full arc. |
| 1 | Smart Parking | I | `en/p1-smart-parking.pdf` | `de/p1-smart-parking.pdf` | Best practices for image recognition — operational/technical playbook for camera-based free-parking detection. |
| 2 | Autonomous Systems | I | `en/p1-autonomous-systems.pdf` | `de/p1-autonomous-systems.pdf` | **Regulatory guide** for autonomous machinery (drones, agricultural systems). |
| 3 | Automated Infrastructure Maintenance | I | `en/p1-infrastructure-maintenance.pdf` | *(not in the bundle the challenge owner shipped; EN-only)* | Drone inspections with computer vision. **Important context** — this was the "missing" Phase I project. |
| 4 | Machine Translation | I | `en/p1-machine-translation.pdf` | `de/p1-machine-translation.pdf` | **Recommendations for public administration** when adopting MT for official documents. |
| 5 | AI in Education | I | `en/p1-ai-in-education.pdf` | `de/p1-ai-in-education.pdf` | **Legal best practices** for AI in classrooms / educational settings. |
| 6 | Sensor-based Bridge Monitoring | II | `en/p2-bridge-monitoring.pdf` | `de/p2-bridge-monitoring.pdf` | Data capture + AI predictions for infrastructure maintenance. Successor to project #3. |
| 7 | Digital Eye Clinic | II | `en/p2-digital-eye-clinic.pdf` | `de/p2-digital-eye-clinic.pdf` | Introducing AI diagnostics into clinical practice. |
| 8 | Autonomous Inspection Robots | II | `en/p2-inspection-robots.pdf` | `de/p2-inspection-robots.pdf` | **Compliance with the EU AI Act + EU Machinery Regulation** — a legal manual disguised as a project report. |
| 9 | AI in Medical Documentation | II | `en/p2-medical-documentation.pdf` | `de/p2-medical-documentation.pdf` | **Legal foundations + recommendations** for auto-generating medical notes from consultations. |
| 10 | AI in Building Permits | II | `en/p2-building-permits.pdf` | `de/p2-building-permits.pdf` | **Use cases, a working prototype** ("AI pre-check in the notification procedure") **and practical lessons.** Most recent + most concrete. |

`★ Pattern across the bundle:` Phase I reports lean *technical/operational*. Phase II reports lean *legal/governance* — AI Act, sectoral law, data-protection. Any taxonomy you build needs both dimensions.

### 4.4 Digests — `digests/` (English, ~50 min total read)

One 600–1000-word structured digest per report. Same schema for every file: *Problem & context → Approach → Findings → Legal points → Data/models → Stakeholders → Cross-references → Why-read-this*. **This is your fastest path to coverage** — skim all 12 in under an hour, then read the underlying PDFs only for the 2–3 most relevant to your team's angle.

The digests also double as **seed structured data for the prototype's knowledge layer** — every section maps cleanly to KG node types (Project, Regulation, Partner, Model, Lesson) with explicit cross-references already wired.

### 4.5 Cross-cutting patterns extracted from the digests

These shape prototype design — surfaced by reading all 12 reports as a corpus, not visible from any single report.

**1. Institutional spine.** Stephanie Volz (ITSL University of Zurich) is the legal author/co-author across every project; Raphael von Thiessen is Programme Manager on all of them; the Amt für Wirtschaft Kanton Zürich coordinates. This three-node institutional core appears in every report — make it a first-class entity in any KG.

**2. Swiss legal stack (consistent across Phase I).** Three frameworks recur in *every* Phase I report:
- Cantonal IDG (when a public body is the data controller)
- Federal FADP/DSG (when a private provider is the controller)
- Commissioned-data-processing contracts (*Auftragsdatenbearbeitung*) for any third-party tool

Treat as a canonical sub-vocabulary.

**3. Phase I → Phase II regulatory centre of gravity shifted.** Phase I is almost entirely Swiss law. Phase II adds EU regulation as the new dominant frame — AI Act, Machinery Regulation 2023/1230, MDR, IVDR, Data Act, CRA, GPSR. Encode as **two distinct legal families**, not one continuous "legal" facet.

**4. "No real-world testing" is a legitimate sandbox outcome.** Two of five Phase II projects (Medical Documentation, Inspection Robots) pivoted to pure legal analysis after hitting regulatory blockers — the sandbox treats this as a successful output. Your prototype must handle "legal-analysis-only" reports gracefully: not every report describes a deployed system.

**5. Privacy-by-design vocabulary repeats verbatim.** Smart Parking, Autonomous Systems, AI in Education, Eye Clinic all use the same lexicon: low resolution, masking, edge computing, instant deletion, data minimisation. Canonical privacy sub-taxonomy.

**6. Implementation partners — not AI — are the bottleneck.** Recurring blockers: property owners (Smart Parking), school IT access (AI in Education), military base access (Infrastructure Maintenance), hospital data agreements (Eye Clinic). A "**what partner access did this need?**" facet would be a uniquely useful KG filter for someone planning a new pilot.

**7. Rule-based vs. generative AI tension is universal in Phase II.** Building Permits (best LLM accuracy 60.2% → hybrid rule-based + generative for <CHF 2/application), Bridge Monitoring (data-driven complements standards-based), Inspection Robots (deterministic safety logic vs. self-evolving ML). Don't treat AI as monolithic in your taxonomy.

**8. Healthcare became a deliberate Phase II sectoral focus.** 4 of 24 Phase II applications were health-sector; 2 of 5 executed projects (Eye Clinic, Medical Documentation); active regulatory work with Swissmedic; deep cross-references between the two health reports. **Strongest single sectoral demo angle** if you want to narrow your prototype's narrative.

## 5. Programme highlights — the moments that actually matter

From `govtech-hackathon-2026-main/README.md`:

| Time | Event | Why it matters |
|---|---|---|
| **Thu 09:30** | Challenge presentations | Lukas Willi pitches the challenge — bring questions about Phase I "Automatisierte Infrastrukturwartung", embeddability requirements, and update-cycle expectations. |
| **Thu 10:45** | Team building | 3–8 person teams. Find domain (legal, public-sector, info architecture) + tech (RAG, graph DB, UX) complementary skills. |
| **Thu 15:00–16:00** | **Mentoring sessions (optional)**: Human Centred Design (BIT), LINDAS (BAR), Renku (SDSC), LOMAS (BFS) | LINDAS = Swiss Linked Data service — directly relevant if knowledge-graph route. Renku = SDSC's data-science platform. |
| **Thu 18:00 / 22:00** | Snacks / hard stop | Plan the day-1 milestone before snacks; don't try to push past 22:00. |
| **Fri 10:00–10:30** | **Legal Q&A (BK)** | Critical if any output makes legal claims — book this slot. |
| **Fri 16:00** | Final pitches | ~5 min + Q&A. Slides + screen recording uploaded to dribdat. |

Platform: **dribdat** (`dribdat.cc/usage`) — you join the project, post progress, upload slides, sync demo.

## 6. Strategic notes for the prototype

These are opinions, not constraints. Verify with the challenge owner before betting on them.

1. **The corpus is tiny and bounded** (~12 PDFs, ~25 MB total). Embeddings + RAG are trivially cheap; quality lives in *chunking strategy*, *metadata enrichment*, and *citation UX*.
2. **The owner literally said "Knowledge Graph or LLM-Wiki".** Picking one and doing it well > inventing something orthogonal. A graph over `{Project, Topic, Regulation, Stakeholder, Lesson, Risk}` connecting back to *paragraph-level PDF anchors* would directly match the brief.
3. **Demonstrate the "guideline generator" loop**: user describes a planned AI project → system surfaces the 3–5 most relevant lessons + a checklist + the citing paragraphs. That's the "Was wäre wenn"-impact story.
4. **Update-flow is differentiating.** A simple admin UI to flag a chunk as outdated or upload a new report (with re-indexing) directly addresses the brief's "Aktualität" concern and signals production-readiness thinking.
5. **Language orientation.** Three orthogonal axes: (a) **development UI = English** so the dev feedback loop works for non-German-readers on the team; (b) **report content stays German** — citations quote source PDFs verbatim, no machine translation of source material; (c) **shipped UI = bilingual via i18n** (next-intl), with the demo-time default language deferred. See [`frontend-route.md`](frontend-route.md) "Language orientation" for the full split.
6. **Don't build a chat-only UI.** "Verständlich" for Verwaltung means structured: checklists, side-by-side report comparisons, filterable topic facets — not just a chat box.
7. **Show the source.** Every output card should preview the cited PDF paragraph. Make "trace to source" a one-click action.

## 7. Source URLs and filename mapping

### English PDFs (downloaded from zh.ch)
All under base `https://www.zh.ch/content/dam/zhweb/bilder-dokumente/themen/wirtschaft-arbeit/wirtschaftsstandort/dokumente/` — see canonical landing page at <https://www.zh.ch/en/wirtschaft-arbeit/wirtschaftsstandort/innovation-sandbox.html>.

| Local file | Source filename on zh.ch | Published |
|---|---|---|
| `reports/en/00-overview-phase1-play-and-learn.pdf` | `sandbox_en.pdf` | Sep 2024 |
| `reports/en/p1-smart-parking.pdf` | `smart_parking_EN.pdf` | Jan 2024 |
| `reports/en/p1-autonomous-systems.pdf` | `leitfaden_autonome_systeme_en_v2.pdf` | Jul 2023 |
| `reports/en/p1-infrastructure-maintenance.pdf` | `sandbox_ibm_research_infrastructure_maintenance_en.pdf` | Nov 2023 |
| `reports/en/p1-machine-translation.pdf` | `maschine_translation_kzh_sandbox_report.pdf` | Feb 2024 |
| `reports/en/p1-ai-in-education.pdf` | `best_practices_ki_bildung_EN.pdf` | Oct 2023 |
| `reports/en/00-overview-phase2-build-and-share.pdf` | `052026-1-Innovation-Sandbox-Booklet-A4-EN.pdf` | May 2026 |
| `reports/en/p2-bridge-monitoring.pdf` | `sensorbasierte_brueckenueberwachung_en.pdf` | Feb 2026 |
| `reports/en/p2-digital-eye-clinic.pdf` | `digital_eye_clinic_en.pdf` | Dec 2025 |
| `reports/en/p2-inspection-robots.pdf` | `autonome_inspektionsroboter_en.pdf` | Nov 2025 |
| `reports/en/p2-medical-documentation.pdf` | `medizinische_dokumentation_en.pdf` | Dec 2025 |
| `reports/en/p2-building-permits.pdf` | `InnovationSandbox_AI_for_building_permits.pdf` | Apr 2026 |

### German PDFs (renamed from challenge-platform UUIDs)
Originals available via the S3 URLs in `challenge/brief.md`.

| Local file | Original UUID name |
|---|---|
| `reports/de/00-overview-phase1-play-and-learn.pdf` | `sandbox_de.pdf` |
| `reports/de/00-overview-phase2-build-and-share.pdf` | `IE85U0OS.pdf` |
| `reports/de/p1-smart-parking.pdf` | `3WA7IZVY.pdf` |
| `reports/de/p1-autonomous-systems.pdf` | `E6XDSMXU.pdf` |
| `reports/de/p1-machine-translation.pdf` | `87MXEKJ3.pdf` |
| `reports/de/p1-ai-in-education.pdf` | `ACKRXKWG.pdf` |
| `reports/de/p2-bridge-monitoring.pdf` | `1Z71YRRF.pdf` |
| `reports/de/p2-digital-eye-clinic.pdf` | `XRQ98GZD.pdf` |
| `reports/de/p2-inspection-robots.pdf` | `NRFS5YOL.pdf` |
| `reports/de/p2-medical-documentation.pdf` | `3X6I8GB6.pdf` |
| `reports/de/p2-building-permits.pdf` | `I89H6B1C.pdf` |
| `challenge/brief.md` | `challenge-context.md` |
| `challenge/slides.pdf` | `challenge-context-pdf.pdf` |

### Asymmetries
- **No DE** for `p1-infrastructure-maintenance.pdf` — wasn't in the challenge-platform bundle; only the EN version was fetchable. (A German version likely exists on the zh.ch German page; fetch on demand if needed for prototype citations.)
- ~~**No EN** for `00-overview-phase2-build-and-share.pdf`~~ — **resolved 2026-05-28**: the EN booklet was shared by the challenge owner and now lives at `reports/en/00-overview-phase2-build-and-share.pdf`. Corpus is now symmetrically bilingual for both phase overviews.

## 8. Pre-event checklist

- [ ] Read sections 1–4 of this README — challenge framing + cross-cutting patterns (~15 min).
- [ ] Read all 12 digests in `digests/` (~50 min). This is the fastest path to corpus-wide understanding; reading order: `00-overview-phase1-play-and-learn.md` → `00-overview-phase2-build-and-share.md` → projects (any order; sort by relevance to your angle).
- [ ] *Optional but recommended*: read the 2–3 source PDFs in `reports/en/` most relevant to your team's angle for depth.
- [ ] Decide pre-event: **knowledge graph route** vs **LLM-wiki / RAG route** vs **hybrid**. Sketch a 1-page rough architecture before Thursday. → see [`architecture-route.md`](architecture-route.md) (current recommendation: wiki-first with KG-shaped frontmatter; kill-switches + Thu Q-list inside).
- [ ] Pre-bake a Q-list for Lukas Willi (Thu 09:30):
  - **Embeddability.** Concrete requirements for the zh.ch CMS — iframe, web component, plain HTML drop-in?
  - **Refresh cadence + maintainer.** Expected update frequency post-hackathon; who owns it.
  - **Phase II overview EN.** Is the Build & Share English version shareable as draft?
  - **Data access.** Can teams access the `eBaugesucheZH` platform from the Building Permits report? Does a sandbox data-availability matrix (project × data type × access) exist anywhere?
  - **Persona lifecycle stage** *(new)*. Where in the AI-pilot lifecycle is the typical "administrative staff starting a pilot" user — pre-idea exploration, validating a chosen approach, or already scoping procurement? Load-bearing for what artifact the generator outputs.
  - **Short videos** *(new)*. Are the per-report short videos (mentioned in brief §Lösungsansätze) available to teams — embed URLs, hosting, license? One-per-report? Considered citation-authoritative or supplementary?
  - **LINDAS expectation.** Is there a downstream pull to connect to LINDAS / cantonal Linked Data infrastructure? (Kill-switch for substrate decision — see [`architecture-route.md`](architecture-route.md).)
  - **Existing Sandbox design language / brand.** Anything we should align to or visibly diverge from for the embedded experience?
- [ ] Pre-event docs to skim morning-of: [`team-handout.md`](team-handout.md) (the one-pager for the kickoff), [`success-criteria.md`](success-criteria.md) (the checklist that drives prioritization).
- [ ] Confirm dribdat account is set up before Thursday 09:00.
