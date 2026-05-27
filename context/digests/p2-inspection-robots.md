# Autonomous Inspection Robots — Approaches to the AI Act and EU Machinery Legislation

**Phase**: II (2024–2026)
**Topic**: EU regulatory compliance strategy for autonomous robotic inspection of critical infrastructure
**Published**: November 2025
**Source**: reports/en/p2-inspection-robots.pdf (English and German parallel)
**Length**: ~40 pages — the most legally dense report in the bundle

## Problem & context
Energy, oil/gas, electricity and chemical facilities require frequent inspection; specialist labour is scarce (ILO: ~395M workers/year sustain non-fatal occupational injury, many in hazardous environments). Autonomous inspection robots offer continuous, hazard-free, around-the-clock monitoring fed into digital twins. But since the EU AI Act came into force, Swiss robotics companies face overlapping and partially contradictory EU regimes — AI Act, EU Machinery Directive 2006/42/EC, the new EU Machinery Regulation 2023/1230 (binding from 20 January 2027), Data Act, Cyber Resilience Act. Switzerland's Mutual Recognition Agreement (MRA) with the EU has not been updated since Switzerland rejected the framework agreement, so for the new Machinery Regulation, Swiss manufacturers will need EU notified-body certification directly.

## Approach & methodology
Pure regulatory analysis (no real-world testing — no public test partner available). Centred on **ANYmal**, the four-legged inspection robot from Swiss company **ANYbotics**. Two parallel workstreams: (1) Systematic legal classification analysis: "Should ANYmal be classified as a *high-risk AI system (HRAIS)* or not?", developed as a decision tree with two scenarios and three options each (1: not HRAIS via no-safety-component + no-critical-infrastructure-safety-component + Art. 6(3) preparatory-activity exemption + Art. 111 transitional provisions; 2: HRAIS classification with integrated EU AI Act + EU Machinery Regulation conformity assessment). (2) Practical pilot of **ISO/IEC 42001** AI management system, jointly with **Modulos AG** as the AI governance platform — covering all Annex A controls except A.5.5 (societal impact assessment).

## Key findings & recommendations
- **Inspection robots will usually qualify as machinery** regardless of autonomy level → Swiss Machinery Ordinance (transposing EU Machinery Directive) and from 20 Jan 2027 the new EU Machinery Regulation apply.
- **From 20 January 2027**: Annex I Part A point 6 of the Machinery Regulation requires notified-body conformity assessment for "machinery with embedded systems with fully or partially self-evolving behaviour using machine learning approaches ensuring safety functions" — self-declaration / internal production control no longer possible.
- **Three conformity assessment routes**: EU type-examination (most suitable for stable models), full quality assurance (for series production; involves unannounced audits), unit verification (only viable for one-off/highly specialised robots).
- **Sandbox team's recommended path**: classify as HRAIS, go through the EU Machinery Regulation conformity assessment (EU type-examination on the on-board computer specifically) — this simultaneously satisfies most EU AI Act high-risk obligations, avoids the not-yet-established AI Act conformity assessment procedure, gives lower uncertainty.
- **Only the on-board computer needs external certification** (where safety-relevant AI sits — obstacle avoidance, inspection intelligence, locomotion); body / legs / housing can stay under internal production control.
- **EU AI Act key dates**: prohibited practices Art. 5 in force 2 Feb 2025; general-purpose AI / governance / transparency 2 Aug 2025; high-risk obligations 2 Aug 2026; transitional grace for pre-existing high-risk systems until 2 Aug 2027 (until 2 Aug 2030 for high-risk in public authorities).
- **"Substantial modification" trap**: per Art. 3(23) and Recital 128, even OS or software-architecture changes count; algorithm/performance changes that occur automatically during operation and were foreseen in the conformity assessment do *not*. In practice authorities will interpret strictly.
- **SME simplifications** under the EU AI Act: <250 employees + ≤€50M turnover or ≤€43M balance sheet → reduced documentation, lower conformity-assessment fees, priority/free regulatory-sandbox access.
- **The MRA tail risk**: if the MRA isn't updated, Swiss machinery manufacturers lose mutual recognition for new conformity-assessed products and must engage EU notified bodies directly.
- **ISO/IEC 42001 lessons** from ANYbotics + Modulos: build on existing information-security management; quick wins maintain momentum; risk analysis comes first to focus resources; medium-risk classification was driven by complex regulatory environment + autonomous use + technical complexity. **10 critical risks** identified, prioritised top-3 as: AI system reliability/robustness, AI governance gaps, AI-specific security vulnerabilities.
- **General principle**: integrate regulation into product development from day one; for safety-critical functions, smart use of EU AI Act flexibilities (Art. 6(3) exemptions, transitional provisions, role-transfer to EU legal entity) can substantially reduce compliance cost.

## Legal & regulatory points
- **EU AI Act** — Articles 5 (prohibited practices), 6(1) and 6(2) (HRAIS classification), 6(3) (exemptions for preparatory-activity AI), 8–20 (HRAIS requirements: risk management, data governance, technical documentation, logging, transparency, human oversight, accuracy/robustness/cybersecurity), Art. 3(14) (safety component definition), Art. 3(23) (substantial modification), Art. 16 (provider obligations), Art. 17 (QMS), Art. 47 (declaration of conformity), Art. 48 (CE marking), Art. 72 (post-market monitoring), Art. 73 (serious-incident reporting), Art. 79 (regulatory verification), Art. 111 (transitional periods); Annex I (Union harmonisation legislation list), Annex III point 2 (critical infrastructure as HRAIS area). Recital 128 (substantial modification interpretation).
- **EU Machinery Regulation 2023/1230** — Annex I Part A point 6 (embedded self-evolving systems with safety functions), Annex III Part B point 1.1.9 (protection against corruption), Annex III Part B point 3.2.4 (monitoring functions), Art. 25(2) (Annex I Part A conformity assessment regime), three conformity routes (EU type-examination, full QA, unit verification). Binding from 20 January 2027; replaces EU Machinery Directive 2006/42/EC.
- **Swiss Machinery Ordinance (Maschinenverordnung)** — transposes the current EU Machinery Directive.
- **EU General Product Safety Regulation Art. 13(3)** — referenced for interpretation of "substantial modification".
- **EU Data Act** — data portability, access rights, B2B and B2G data sharing for connected products.
- **EU Cyber Resilience Act** — horizontal cybersecurity requirements (security-by-design, vulnerability management, security updates throughout product lifecycle); affects all digital products with connected functionality.
- **Accessibility Directives (EU) 2016/2102 and (EU) 2019/882** — websites/products accessibility (HRAIS Art. 16(l) obligation).
- **Market Surveillance Regulation (EU) 2019/1020** — referenced via AI Act Art. 79.
- **ISO/IEC 42001:2023** (Swiss SN ISO/IEC 42001:2025) — international AI management system standard; first standard specifically for responsible AI use.
- **Switzerland–EU Mutual Recognition Agreement (MRA)** — currently covers EU Machinery Directive; status unclear post-2027 for the new Regulation.
- **CE marking** — required after successful conformity assessment.

## Data, models, infrastructure
- **ANYmal** (ANYbotics) — four-legged quadruped robot, in production use in >20 countries. Multimodal sensor stack: **360° LIDAR** for **SLAM** mapping/navigation; depth + zoom cameras for visual detection; thermal imaging camera; acoustic + vibration sensors. Three integrated AI components processed locally on on-board CPU/GPU: **reinforcement learning** for locomotion, self-learning navigation for obstacle avoidance, **supervised learning** for inspection analysis. Wi-Fi / 5G / edge-computing comms. Automatic charging station. **ATEX-certified** variant (ANYmal X) for explosive atmospheres. Quarterly update cycles. Deployed in chemical plants (120+ inspection points/mission), offshore platforms, data centres.
- **Modulos AG** — Zurich-based AI governance platform; partnered with ANYbotics to pilot the ISO/IEC 42001 management system.

## Stakeholders & partners
**Authors**: Stephanie Volz (ITSL, University of Zurich), Raphael von Thiessen (AI Sandbox, Canton Zürich), Sven Kohlmeier (Specialist Attorney for IT Law, Wicki Partners AG). **Project partner / case study**: **ANYbotics** (Dr. Christian Gehring co-founder + Sr. Director Robotics & AI; Kateryna Portmann Sr. Product Manager; Marcel Fehr Sr. Certification Manager). **AI governance partner**: **Modulos AG** (Elena Maran Global Head of Responsible AI; Kevin Schawinski co-founder + CEO). **Expert support**: Dr. Ann-Katrin Michel (Head of Technology, Swissmem), Barbara Mullis (Standardisation Expert, Electrosuisse), Dr. Clara Guerra (Director Office for Digital Innovation, Principality of Liechtenstein), Jonas Büchel (Legal Advisor, Wicki Partners), Yvonne Finger (Head of Unit, Bundesnetzagentur — Germany's federal network agency). Cross-border: first sandbox project to engage with non-Swiss regulators directly.

## Cross-references
- [Build & Share overview, Phase II] — flagship example of EU market-access focus; ISO/IEC 42001 pilot; cross-border collaboration.
- [Bridge Monitoring, Phase II] — adjacent infrastructure-inspection automation, but with Swiss-law-only framing (interesting contrast: cantonal-scale sensors → Swiss CO; international robotics → EU AI Act).
- [Autonomous Systems, Phase I] — direct predecessor / regulatory continuation; the Phase I report's agricultural-vehicle re-certification example is reused as a lesson here.
- [Building Permits, Phase II] — opposite legal end of Phase II (cantonal administrative law); same legal author team (Volz/ITSL).
- [Medical Documentation, Phase II] — also pure regulatory analysis with no real-world testing; both share the "no test partner found / regulatory blockers" framing.
- [Eye Clinic, Phase II] — adjacent topic (AI in safety-critical domain with notified-body conformity assessment), but under MDR instead of EU Machinery Regulation.

## Why someone planning a new AI pilot would read this specifically
This is the corpus's reference document for **EU market access**. It contains the only explicit decision tree for HRAIS classification, the only side-by-side mapping of EU AI Act vs. EU Machinery Regulation obligations (with article numbers), and the only worked example of ISO/IEC 42001 implementation in a Swiss AI company. Any Swiss AI product targeting EU customers should treat this as a checklist.

## Notable quotes
- "EU regulations often have a less drastic impact on companies than expected — those who make smart use of flexibilities and analyse risks pragmatically can develop a suitable strategy." — Sven Kohlmeier, IT Law specialist, Wicki Partners, p. 25.
- "Those who systematically embed AI governance create security, reduce risks and secure long-term market access." — Elena Maran, Global Head of Responsible AI, Modulos AG, p. 29.
