# Wiki Index

> Auto-navigable inventory of every page in the wiki. Organised by retrieval priority first, then by type, phase, and sector.
>
> **Maintenance**: hand-edited for now. Will be regenerated from frontmatter by a ~30-line script once the wiki exceeds ~100 pages and hand-maintenance becomes painful.

---

## ★ Start here — Cross-cutting Phase II principles

For general queries (*"what are the key lessons?"*, *"how do I scope an AI pilot?"*, *"what should I know before doing this?"*), the highest-priority entry point is:

- **[[phase-2-cross-cutting-principles]]** ★ — the booklet's 17 general principles consolidated across Technology / Legal / Organisation, with links to atomic lesson pages. **Retrieve this first** for general guidance queries; the case-study-specific findings live one layer deeper.

The principles themselves are split across the 14 lessons tagged `cross_cutting: true` (see [Lessons section](#lessons-14-cross-cutting--7-case-study-specific) below).

---

## Themes — guided synthesis pages for specific user questions

Six synthesis pages organised as persona-questions, each with a reading path:

- **[[phase-2-cross-cutting-principles]]** — *"What are the booklet's general principles?"* (priority retrieval target — see above.)
- **[[scoping-is-ai-the-right-approach]]** — *"Is AI even the right approach for my problem?"*
- **[[when-rule-based-beats-generative]]** — *"Should I use rule-based logic or generative AI?"*
- **[[data-access-patterns-and-unblocking]]** — *"How do I unblock data access for my pilot?"*
- **[[eu-market-access-for-swiss-ai]]** — *"What's the EU market access pathway for my Swiss AI product?"*
- **[[partner-roles-around-a-pilot]]** — *"Who do I need around my AI pilot, and what do they each do?"*
- **[[zh-ai-ecosystem-strategy-2026-2029]]** — the 4-pillar Canton-of-Zurich macro context.

---

## By type

### Projects (10) — one per sandbox pilot

> Project slugs drop the `p1-`/`p2-` prefix (phase is frontmatter, not filename). Source slugs *keep* the prefix to match PDF filenames. So `[[smart-parking]]` = the project page; `[[p1-smart-parking]]` = its source PDF page.

#### Phase I (2022–2024)
- [[smart-parking]] — Best practices for image recognition. *Mobility.*
- [[autonomous-systems]] — Regulatory guide for autonomous machinery. *Autonomous Systems.*
- [[infrastructure-maintenance]] — Drone inspections with computer vision (IBM Research → Hugging Face dataset). *Autonomous Systems.*
- [[machine-translation]] — MT for public administration. *Public Administration.*
- [[ai-in-education]] — Legal best practices for AI in classrooms. *Education & Work.*

#### Phase II (2024–2026)
- [[bridge-monitoring]] — Sensor data + AI for infrastructure maintenance (SOB rail bridge). *Mobility.*
- [[digital-eye-clinic]] — Open-source AI diagnostics for diabetic retinopathy. *Healthcare.*
- [[inspection-robots]] — EU AI Act + Machinery Regulation compliance (ANYbotics, ISO/IEC 42001). *Autonomous Systems.* `analysis-only`
- [[medical-documentation]] — Legal foundations for AI medical notes (MPAssist, Swissmedic). *Healthcare.* `analysis-only`
- [[building-permits]] — Working prototype + 3,336-evaluation benchmark. *Construction.*

### Concepts (16)

#### From the booklet glossary (canonical definitions, p.26)
- [[computer-vision]] · [[deepfakes]] · [[frontier-models]] · [[generative-ai]] · [[intrapreneurship]] · [[large-language-models]] · [[llm-benchmarks]] · [[real-world-testing]]

(The 3 booklet-glossary terms that are also regulations — [[eu-ai-act]], [[iso-iec-42001]], [[machinery-regulation]] — live in `regulations/` only.)

#### Derived from cross-cutting corpus patterns
- [[data-access]] — the most powerful lever; cross-project chokepoint table.
- [[pseudonymisation]] — privacy-by-design technique.
- [[partner-bottleneck]] — recurring failure mode (6 of 10 projects).
- [[auftragsdatenbearbeitung]] — Swiss commissioned-data-processing contracts.
- [[llm-as-a-judge]] — domain-specific LLM evaluation methodology (from [[building-permits]]).
- [[regulatory-roundtable]] — multi-party knowledge-transfer format (from [[medical-documentation]]).
- [[model-agnostic-architecture]] — swappable-model design pattern.
- [[data-minimisation]] — privacy-by-design lexicon.

### Regulations (8)

#### Swiss
- [[dsg-fadp]] — Federal Act on Data Protection.
- [[idg-zh]] — Cantonal Information and Data Protection Act, Zurich.
- [[fadp-art-21]] — Automated individual decisions; right to human review.
- [[ai-convention-ch-implementation]] — Swiss implementation of the Council of Europe AI Convention.
- [[embag]] — Federal Act on the Use of Electronic Means; open-source default for administrative software.

#### EU
- [[eu-ai-act]] — Risk-based EU AI regulation.
- [[machinery-regulation]] — EU Machinery Regulation 2023/1230.

#### Standards
- [[iso-iec-42001]] — International AI management-system standard.

### Stakeholders (13)

#### People — Canton of Zurich sandbox programme
- [[raphael-von-thiessen]] — Programme Lead AI, Canton of Zurich. Constant institutional anchor.
- [[lukas-willi]] — Project Lead AI, Canton of Zurich. **Challenge owner at the hackathon.**
- [[stephanie-volz]] — Managing Director ITSL, UZH. Legal author/co-author on every sandbox project.

#### Organisations — Canton + academic
- [[amt-fuer-wirtschaft-zh]] — coordinating body.
- [[itsl-uzh]] — academic legal partner.

#### Test partners + implementation partners
- [[mpassist]] — medical-documentation AI provider (Phase II).
- [[anybotics]] — autonomous-robotics vendor (Phase II).
- [[modulos]] — AI-governance platform provider (Phase II).
- [[ibm-research]] — drone-inspection partner (Phase I).
- [[irmos-technologies]] — sensor-based monitoring vendor (Phase II).
- [[sob]] — Schweizerische Südostbahn; bridge-monitoring test partner.
- [[stadt-kloten]] — building-permits test partner.

#### Supervisory authorities
- [[swissmedic]] — Swiss medical-products supervisor.

### Lessons (14 cross-cutting + 7 case-study-specific)

**Cross-cutting principles** (`cross_cutting: true`) — boost these for general queries:

- [[ai-is-rarely-the-primary-challenge]] (Technology §04)
- [[rule-based-beats-generative-for-defined-logic]] (Technology §04)
- [[ai-extends-beyond-large-language-models]] (Technology §04)
- [[model-selection-is-task-specific]] (Technology §04)
- [[combine-frontier-and-open-source-strategically]] (Technology §04)
- [[data-access-is-the-most-powerful-lever]] (Technology §04)
- [[integrate-regulation-early]] (Legal §04)
- [[interdisciplinary-legal-issues-are-the-norm]] (Legal §04)
- [[continuous-regulatory-learning-beats-rigid-approval]] (Legal §04)
- [[strong-stakeholder-engagement-is-decisive]] (Organisation §04)
- [[value-must-be-clearly-articulated]] (Organisation §04)
- [[domain-expertise-tech-interface-is-critical]] (Organisation §04)
- [[integration-matters-more-than-model-choice]] (Organisation §04)
- [[new-ways-of-working-need-change-management]] (Organisation §04)

**Case-study-specific lessons** — apply when query context matches:

- [[probabilistic-ai-vs-administrative-reproducibility]] (Building Permits)
- [[pre-submission-quality-is-the-leverage]] (Building Permits)
- [[open-source-as-procurement-alternative]] (Digital Eye Clinic / Building Permits)
- [[partner-pivot-is-normal]] (Bridge Monitoring / Inspection Robots / Medical Documentation)
- [[cross-border-collab-unlocks-eu-access]] (Inspection Robots)
- [[regulatory-roundtable-is-high-leverage]] (Medical Documentation)
- [[data-reuse-multiplies-pilot-impact]] (Infrastructure Maintenance → IBM/Hugging Face)

### Sources (12)

#### Phase overviews
- [[00-overview-phase1-play-and-learn]] — Phase I overview ("Play & Learn"). DE + EN.
- [[00-overview-phase2-build-and-share]] — Phase II overview ("Build & Share"). DE + EN. **The current authoritative snapshot.** `priority: high`

#### Phase I project reports
- [[p1-smart-parking]] · [[p1-autonomous-systems]] · [[p1-infrastructure-maintenance]] (EN only) · [[p1-machine-translation]] · [[p1-ai-in-education]]

#### Phase II project reports
- [[p2-bridge-monitoring]] · [[p2-digital-eye-clinic]] · [[p2-inspection-robots]] · [[p2-medical-documentation]] · [[p2-building-permits]] `priority: high`

### Synthesis (7 — cross-cutting patterns + themes)

- [[phase-2-cross-cutting-principles]] ★ — `priority: high`. The 17 general principles, the priority retrieval surface.
- [[scoping-is-ai-the-right-approach]] — broadest scoping theme.
- [[when-rule-based-beats-generative]] — rule-based-vs-generative decision guide.
- [[data-access-patterns-and-unblocking]] — partner-bottleneck mitigations.
- [[eu-market-access-for-swiss-ai]] — EU regulatory pathway.
- [[partner-roles-around-a-pilot]] — the 5-role taxonomy applied.
- [[zh-ai-ecosystem-strategy-2026-2029]] — the 4-pillar macro context.

---

## By phase (project pages, not source pages)

**Phase I** (computer vision, mostly Swiss law):
[[smart-parking]] · [[autonomous-systems]] · [[infrastructure-maintenance]] · [[machine-translation]] · [[ai-in-education]]
(source: [[00-overview-phase1-play-and-learn]])

**Phase II** (generative AI, EU law enters, healthcare focus):
[[bridge-monitoring]] · [[digital-eye-clinic]] · [[inspection-robots]] · [[medical-documentation]] · [[building-permits]]
(source: [[00-overview-phase2-build-and-share]])

---

## By sector (from the booklet's 7-bucket taxonomy)

- **Mobility**: [[smart-parking]], [[bridge-monitoring]]
- **Autonomous Systems**: [[autonomous-systems]], [[infrastructure-maintenance]], [[inspection-robots]]
- **Public Administration**: [[machine-translation]]
- **Education & Work**: [[ai-in-education]]
- **Healthcare**: [[digital-eye-clinic]], [[medical-documentation]]
- **Construction**: [[building-permits]]
- **Other**: *(submitted-but-not-executed projects listed here per booklet figure 1)*

---

## Retrieval-priority quick reference (for the future chatbot)

When a query lands, prefer in this order:

1. **General / scoping queries** → [[phase-2-cross-cutting-principles]] + relevant theme synthesis pages → cross-cutting lessons.
2. **Specific case-study queries** → the relevant project page → that project's source + case-study-specific lessons.
3. **Legal queries** → the relevant regulation page → relevant cross-cutting lesson(s) → specific project examples.
4. **Partner / process queries** → [[partner-roles-around-a-pilot]] + relevant stakeholder pages.
5. **Outcome / strategy queries** → [[zh-ai-ecosystem-strategy-2026-2029]] + [[phase-2-cross-cutting-principles]].

This is a heuristic for the *generator*, not a constraint on browsing — users navigating the wiki freely should find paths from anywhere to anywhere via wikilinks.

---

## Open areas (gaps the wiki currently doesn't cover)

These are deliberate stubs — places where the team could extend during the hackathon.

- **Concepts** — `edge-computing`, `bias-audit`, `auftragsdatenbearbeitung` (✓ now exists), additional sector-specific concepts from individual reports.
- **Stakeholders** — remaining named test/implementation partners + specialist support people: spross-stiftung, stadtspital-zuerich-augenklinik, nokema, byte-studio, gossweiler-ingenieure, gogymi, bundesnetzagentur-de, li-digital-innovation, plus the FHNW/HSG specialist support people from [[building-permits]] (Walzer, Meyer, Klingler, Jost, Hüppin, Baldwin, Louis, Späti, Schneider, Arnold, Polach).
- **Lessons** — case-study-specific lessons not yet extracted: e.g. cost-per-application economics from Building Permits, regulatory-roundtable-as-format details from Medical Documentation, intrapreneurship-as-procurement-path from Digital Eye Clinic.
- **Regulations** — sector-specific instruments: MDR, IVDR, ÖREB cadastre framework, sectoral healthcare law, federal admin-law principles (BV Art. 29).
- **Synthesis** — additional themes: `healthcare-pilot-scoping`, `real-world-testing-vs-analysis-only` (sandbox outcome class chooser), `intrapreneurship-as-public-sector-procurement`.

If you pick up one of these, link your PR to issue tag `wiki:expansion`.
