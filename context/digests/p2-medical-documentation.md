# AI in Medical Documentation — Data Protection, Professional Secrecy and Medical-Device Classification

**Phase**: II (2024–2026)
**Topic**: Regulatory guide for LLM-based medical documentation in Swiss healthcare
**Published**: November 2025
**Source**: reports/en/p2-medical-documentation.pdf (English and German parallel)
**Length**: ~40 pages — the most legally detailed health-sector report in the bundle

## Problem & context
Documentation is one of the highest time burdens on Swiss clinicians; LLMs (speech-to-text dictation, report drafting, summarisation, retrieval over patient files) promise major efficiency gains. But health data is the most sensitive personal-data category, professional secrecy is criminally enforced, public hospitals operate under cantonal law (IDG ZH) layered on federal law (FADP), and any software that "analyses, interprets or influences" medical content can become a regulated medical device. The originally-anchored sandbox project (**MPAssist**, a Zurich SME with a clinical documentation tool) could *not* be operationally tested — data-protection requirements blocked use of patient data in the public-hospital test partner. The report is therefore pure regulatory analysis with eight worked use-case scenarios.

## Approach & methodology
Pure desk research + an institutionalised roundtable. The ITSL team plus an external attorney (Raphael von Thiessen as co-author) built (a) a decision-tree-style **data-protection FAQ** with a published figure on p. 12 covering source-of-data, processing purpose, lawful basis, on-premise vs. cloud, US-cloud risk, and outsourcing; (b) a parallel **medical-device classification framework** built on MedDO/IvDO + EU MDR/IVDR + Swissmedic guidance + MDCG 2019-11 + the new EU AI Act; (c) **eight use-case scenarios** each paired with a regulatory perspective sidebar (see findings); (d) a **13-point best-practice list + 7 strategic ideas** for the future; (e) a roundtable with 10+ start-ups and the cantonal data-protection authority.

## Key findings & recommendations
- **The "medical purpose" line is everything**. Pure transcription = administrative tool, not a medical device. Once the software *summarises, interprets, ranks, generates differential diagnoses, decides on requests, or aggregates with medical conclusions*, it becomes a medical device and the full MedDO/IvDO + MDR/IVDR regime kicks in.
- **Eight use cases benchmarked**: (I) dictation transcription — usually not a medical device; (II) report optimisation/translation — borderline because rewording can shift meaning; (III) ambient clinical intelligence (recording doctor-patient conversation) — medical device if it summarises; (IV) multi-source report aggregation — medical device if it draws medical conclusions; (V) chatbot over patient records — medical device when it formulates diagnoses/recommendations; (VI) AI-suggested **differential diagnoses** — clearly a medical device, **MDR Class IIa+**; (VII) *automatisierte Abrechnung* (automated billing with ICD codes) — non-medical unless it influences treatment; (VIII) automatic patient appointment requests — medical device if the AI evaluates content rather than running on fixed schedules.
- **Classification consequences**: Annex VIII MDR Rule 11 → Classes I, IIa, IIb, III based on (significance of information × state of patient condition). High-significance + critical = **Class III**; medium + serious = **Class IIb**; everything that informs but doesn't drive treatment = Class IIa typically.
- **In-house manufacture exception** (Art. 9 MedDO / Art. 9 IvDO + Art. 18 MedDO / Art. 10 IvDO) — healthcare facilities can manufacture and use medical devices internally without full MDR compliance, but must notify and meet essential safety/performance requirements; MDCG 2023-1 guidance applies.
- **Generic LLMs are strongly discouraged for medical use**: OpenAI/Anthropic terms of use exclude health applications. Use medically-specialised LLMs (**Med-PaLM 2**, **BioGPT**, or the Swiss open-source **Meditron** from EPFL) plus **retrieval-augmented generation** for institutional grounding.
- **End-to-end encryption beats anonymisation** — anonymising by stripping names/dates rarely succeeds for clinical text; encryption + access control is the more defensible path.
- **Confidential computing + HSM + double key encryption + CASB** are flagged as the forward-looking stack to keep cloud providers blind to patient data.
- **13 best practices**: (1) early product qualification; (2) early collaboration with specialist regulatory advisors; (3) modular architecture so only medical modules get registered; (4) ISO 13485 QMS certification; (5) avoid shadow use by giving staff sanctioned tools; (6) transparency via **model cards**; (7) traceability + human-in-the-loop; (8) verify LLM-vendor terms of use; (9) **predetermined change control plans** for continuous learning (FDA model, likely echoed by EU AI Act Art. 43(4)); (10) end-to-end encryption over anonymisation; (11) confidential computing; (12) shared reference architectures (Association of Zurich Hospitals working on this); (13) institutionalised stakeholder round tables.
- **7 strategic ideas**: open ecosystems with standardised interfaces; **joint cantonal data-protection standards** (privatim + cantonal health depts); ethical bias monitoring + human-by-design; new value-creation/financing models; sandboxes as pre-submission dossiers; **adaptive AI regulation beyond rigid approvals**; medical report itself may transform as structured data interoperability improves.

## Legal & regulatory points
- **Swiss FADP / DSG** — Art. 5(c)(2) (health data as sensitive), Art. 8 (data security), Art. 9 (commissioned processing/outsourcing), Art. 21 (automated individual decisions; right to human review), Art. 22 (data protection impact assessment / **DPIA**), Art. 23 (FDPIC consultation when DPIA shows high residual risk). Appendix 1 lists countries with adequate protection (the **Data Privacy Framework** for US).
- **IDG ZH (Cantonal Information and Data Protection Act, Zürich)** — Section 3 (scope), Section 3(3) and 3(4)(a)(2) (sensitive personal data), Section 6 (lawful basis), Section 10 (DPIA + prior checking with cantonal data-protection authority), Section 19/22/25 (outsourcing requirements).
- **IDV ZH** — implementing ordinance to IDG; commissioned processing/outsourcing rules.
- **Art. 321 Swiss Criminal Code** — professional secrecy (criminal liability for unauthorised disclosure by medical staff); the criminal-law spine of all health-data law.
- **Section 15 Health Act** (cantonal) — medical confidentiality.
- **FDPIC** — Federal Data Protection and Information Commissioner; consulted under Art. 23 FADP.
- **MedDO (Medical Devices Ordinance, Switzerland)** — Art. 9 (in-house manufacture), Art. 18 (notification), plus full conformity assessment for classes IIa+.
- **IvDO** — parallel ordinance for *in vitro* diagnostics; Art. 9 (in-house manufacture), Art. 10 (notification), Class B+ for non-trivial diagnostic software.
- **Therapeutic Products Act** — overarching statutory base.
- **Swissmedic 'Medical Device Software' information sheet** — Swiss regulatory guidance.
- **EU MDR (2017/745)** + **EU IVDR** — apply because Switzerland's MRA for medical devices was revoked in 2021; class IIa+ / Class B+ requires EU **notified body**.
- **MDCG 2019-11** — EU guideline for software classification (Annex VIII Rule 11 table reproduced in the report); **MDCG 2023-1** — in-house manufacture guidance.
- **EU AI Act** — Art. 43(4) (predetermined change control plan); medical AI is high-risk and subject to risk-management, transparency, human oversight, accuracy/robustness obligations.
- **Standards**: **SN EN ISO 13485** (QMS for medical devices), **SN EN 62304** (medical device software life cycle), **SN EN 82304-1** (health software safety), **SN EN 62366-1** (usability), **IEC 81001-5-1** (cybersecurity in medical/health IT life cycle), **ISO 27001** (information security management).
- **General Product Safety Regulation (GPSR)** — Appendix I MDR.
- **FINMA Circular 2008/7** — outsourcing supervision (banks, but cited as comparable model).
- **FOPH provisions** + **Art. 12(5) EPDV** — electronic patient record ordinance.
- **US CLOUD Act + Data Privacy Framework** — cross-border data access risk for US-based cloud providers; mitigations: confidential computing, **HSM** (hardware security module), **double key encryption (DKE)**, **CASB** (cloud access security broker).
- **MDR Annex VIII Rule 11** — software classification table (Class III / IIb / IIa) by significance × patient state.

## Data, models, infrastructure
- **MPAssist** — Swiss SME whose clinical-documentation product anchored the legal use case (no operational testing).
- **Medical LLMs**: Med-PaLM 2 (Google), BioGPT (Microsoft), **Meditron** (EPFL, open-source Swiss alternative).
- **Generic LLMs**: explicitly cautioned against (OpenAI/Anthropic exclude health use in ToS).
- **Architectural primitives**: confidential computing / TEE, HSM, double key encryption, CASB, retrieval-augmented generation, model cards, predetermined change control plans.
- **Reference architectures**: Association of Zurich Hospitals (*Verein Zürcher Krankenhäuser*) working on canton-wide patterns.

## Stakeholders & partners
**Authors**: Stephanie Volz (Managing Director ITSL, University of Zurich) + Raphael von Thiessen (AI Sandbox Programme Manager). **Expert contributors / roundtable** (named): Dr. André Baumgart (VZK — Association of Zurich Hospitals), Dr. Nadine Bienefeld (ETH Zürich), Michèle Hess (Cantonal Health Department), Dr. Rolf Kaufmann, Raffaele Lugli, Dr. Michael Neugebauer (University Children's Hospital Zurich), Corinne Spirig (**dhc — digital health center Bülach**), Sebastian Svetel, **Dr. Atanas Todorov (Chief Medical Officer, Arcondis)**, Peter Waldner. **Anchor SME**: MPAssist. **Project Steering**: Office for Economy (Zürich + Schwyz), Statistical Office Zürich, Department for Digital Administration Zürich, ETH AI Center, ITSL UZH, ZHAW entrepreneurship.

## Cross-references
- [Build & Share overview, Phase II] — named as one of two Phase II projects that could not undergo real-world testing (the other being Inspection Robots).
- [Digital Eye Clinic, Phase II] — companion health-sector report; the Eye Clinic explicitly defers to this report (footnote 9, p. 25) for medical-device-regulation and data-protection detail.
- [Inspection Robots, Phase II] — fellow "pure regulatory analysis, no operational testing" report; both share authorship by Volz/ITSL.
- [Building Permits, Phase II] — same ITSL legal-analysis backbone; shared FADP Art. 21 + DPIA framing.
- [Phase I — no direct predecessor]; health was a new sectoral focus in Phase II.

## Why someone planning a new AI pilot would read this specifically
This is the corpus's reference document for **Swiss healthcare AI legality**. It is the only place that maps the eight realistic LLM use cases against MDR Annex VIII Rule 11 (with the classification table reproduced), the only worked example of stacking FADP + IDG ZH + Art. 321 Criminal Code + MedDO + IvDO + MDR + IVDR + EU AI Act on a single artefact, and the only published Swiss inventory of medical-LLM and confidential-computing options. Anyone touching patient-data AI in a Swiss public hospital should treat this as the legal checklist; every other Phase II health discussion defers here for the detail.

## Notable quotes
- "LLMs fit into existing regulatory frameworks — provided their function is clearly defined and documentation is thorough." — Dr. Atanas Todorov, Chief Medical Officer, Arcondis, p. 32.
- "AI needs new regulatory approaches — flexible, risk-based, and beyond rigid approvals." — Raphael von Thiessen, AI Sandbox Programme Manager, Canton of Zurich, p. 38.
