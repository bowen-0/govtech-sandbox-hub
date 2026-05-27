# Build & Share — A Sandbox to Enable the AI Ecosystem

**Phase**: II (2024–2026) — Phase II overview
**Topic**: Strategic framing of Phase II — ecosystem enablement, regulatory learning, real-world testing
**Published**: 2026 (final phase report)
**Source**: reports/de/00-overview-phase2-build-and-share.pdf — **GERMAN-ONLY** (English version not yet published by Canton Zürich)
**Length**: ~28 pages

## Problem & context
After Phase I ("Play & Learn", 2022–2024) proved the sandbox model worked, Canton Zürich's *Standortförderung* (location promotion office, in the *Amt für Wirtschaft* / Office of Economic Affairs) needed to evolve it from a pilot instrument into a structural component of the Swiss AI ecosystem. Phase II's brief: deepen regulatory clarity, broaden into new sectors (notably healthcare), and engage with the now-actionable EU AI Act. Where Phase I focused on *computer vision*, Phase II deliberately shifted toward *generative AI* — timed after the first wave of chatbot hype had passed, so applications could be reflective rather than reactive.

## Approach & methodology
Phase II followed a portfolio approach: 8 projects initiated, 5 implemented in parallel (lightly staggered) over 9–12 months each within an 18-month window. The team kept the Phase I success formula — sector-open calls, no financial compensation for participants, no regulatory exemptions (everything within existing law), strong public communication — and added: (a) pre-application contact with interested parties to vet relevance early, (b) tighter networking via events/workshops, (c) entry into new sectors (especially health), (d) explicit engagement with EU regulation for market-access questions. Five role types around each project: test partner, mandated experts, technical implementation partner, sparring partner, supervisory authority.

## Key findings & recommendations
- **24 applications received** (vs. 21 in Phase I); selection process unchanged (written submission → 30-min validation interview → Steering Committee prioritisation).
- **Real-world testing in 3 of 5 projects** (Digital Eye Clinic, AI in Building Permits, Sensor-based Bridge Monitoring); the other two (Medical Documentation, Autonomous Inspection Robots) were limited to regulatory analysis — Medical Documentation because data-protection requirements blocked operational use of patient data in a public hospital, Inspection Robots because no suitable test partner was found.
- **Rule-based systems beat generative AI when decision logic is well-defined** (e.g. completeness checks in building permits); generative AI shines on unstructured input (summaries, transcription, plausibility pre-checks).
- **Model choice is task-specific**: no single "best" model exists across heterogeneous use cases with mixed image/text inputs; architecture should be **model-agnostic** so models can be swapped and continuously benchmarked.
- **Frontier vs. open-source is a deliberate mix**: combine cloud commercial frontier models with locally-run open-source models depending on privacy/cost/scale (especially in health).
- **Data access is the biggest lever**: even apparently trivial datasets (e.g. drone images of an airfield) yield outsized value when made publicly accessible — they let multiple providers train, validate and compare.
- **AI providers should integrate regulation into product development from the start**; late-stage regulatory fixes drive flawed business models (e.g. autonomous agricultural vehicles required full re-certification when retrofitted).
- **Continuous regulatory learning is essential**: classical licensing logics hit limits with dynamic learning systems; formats like *Regulatory Roundtables* matter beyond rigid approval logic.
- **Scaling fails on integration, not on model performance**: the pilot-to-production gap is usually missing integration into existing systems, processes and governance — not a weak model.
- **Three impact levels**: (1) direct project value for AI providers + public partners, (2) ecosystem know-how transfer (publications, prototypes like Digital Eye Clinic platform opened to third parties, Regulatory Roundtables, international networking with DE/LI/EU/NA/SA/Asia), (3) systemic anchoring (input to the Federal Council's *Bundesratsentscheid zur KI-Regulierung* / AI regulation decision, the *KI im Baubewilligungsverfahren* parliamentary postulate, sector transfer to *Educa* (education), *Swissmedic* (health), *MODI* (mobility)).

## Legal & regulatory points
- **EU AI Act** — central to the Autonomous Inspection Robots project; risk-based classification, high-risk obligations, transparency duties.
- **EU Machinery Regulation 2023/1230** (*EU-Maschinenverordnung*) — examined jointly with the AI Act for inspection-robot market access; the dynamic interdependence between the two regulations was a particular challenge.
- **ISO/IEC 42001** — AI management system standard; piloted with Modulos as an AI governance platform for the inspection-robot use case.
- **Swiss implementation of the Council of Europe AI Convention** — flagged as expanding the existing legal framework, especially where AI touches fundamental rights.
- **Swiss FADP/DSG** — central blocker in Medical Documentation (data processing of patient records).
- **Federal Council decision on AI testing environments** (*KI-Testumgebungen*) — sandboxes were specifically named as innovation-promotion instrument.
- **Cantonal Government Council Decision** (*Regierungsratsbeschluss*) on strengthening the AI location 2026–2029 — directly built on sandbox findings, anchoring four pillars: (I) AI Sandbox, (II) AI startup promotion, (III) AI adoption by SMEs, (IV) population dialogue.

## Data, models, infrastructure
The overview itself is non-technical, but it names: **MPAssist** (medical documentation provider whose use case anchored the legal guide), **ANYbotics** (Swiss inspection-robot vendor), **Modulos** (AI governance platform for ISO/IEC 42001), **irmos technologies** (sensor bridge monitoring), **Nokema / Gossweiler Ingenieure / Byte Studio** (Building Permits implementation), **IBM Research** (annotated drone-inspection dataset for infrastructure, published on **Hugging Face** as a public benchmark). The Digital Eye Clinic project produced an **open-source modular AI diagnostics platform** because no commercial product met public-hospital requirements. References to: *generative AI*, *LLMs*, *frontier models*, *computer vision*, *LLM-as-a-judge* (used for evaluating the building-permits prototype across thousands of test runs).

## Stakeholders & partners
**Publisher**: *Standortförderung Kanton Zürich* (location promotion office, *Amt für Wirtschaft* / Office of Economic Affairs), *Verein Metropolitanraum Zürich*, *Innovation Zurich*. **Authors**: Raphael von Thiessen (Programmleiter KI-Standort), Lukas Willi (Projektleiter KI). **Project Steering**: Amt für Wirtschaft (Zürich + Schwyz), *Staatskanzlei Kanton Zürich* (Cantonal Chancellery), *Metropolitanraum Zürich*, *ETH AI Center*, *Center for Information Technology, Society, and Law (ITSL) Universität Zürich*, *swissICT*, *ZHAW entrepreneurship*. **Specialist advisors**: Dr. Aurelia Tamò-Larrieux (UNIL), Dr. Clara Guerra (Liechtenstein digital innovation), Demian Niemeyer (appliedAI Institute), Ivo Ruckstuhl (Swiss Centre for Responsible AI), Melhem Daoud (digitalswitzerland), Dr. Sebastian Singler (PwC), Yvonne Finger (Bundesnetzagentur, Germany). **Test partners** named: digital health center Bülach (dhc), Stadtspital Zürich Augenklinik, Spross Stiftung für Augenheilkunde, Schweizerische Südostbahn (SOB), Stadt Kloten, Stadt Frauenfeld, Kanton Schwyz, GoGymi, IBM Research.

## Cross-references
- [Play & Learn (Phase I overview)] — the predecessor; Build & Share is the direct continuation and explicitly references its strategic framing.
- [Smart Parking, Phase I] — cited as a Phase I roll-out success (Frauenfeld production deployment, scaled to multiple cantons).
- [Machine Translation, Phase I] — cited as another Phase I roll-out success (commercial register, scaled with Kanton Schwyz).
- [Automated Infrastructure Maintenance, Phase I] — IBM Research dataset legacy, now publicly available; explicit lineage with Phase II Bridge Monitoring.
- [Autonomous Systems, Phase I] — its example of agricultural vehicles needing full re-certification when retrofitted is reused here as the canonical "integrate regulation early" lesson.
- [Sensor-based Bridge Monitoring, Phase II] — pivoted to SOB rail bridge after the original municipal footbridge partner withdrew.
- [Digital Eye Clinic, Phase II] — flagship health-sector pilot; modular open-source diagnostics platform.
- [Autonomous Inspection Robots, Phase II] — flagship EU market-access pilot; cross-border collaboration with Bundesnetzagentur (DE) and Liechtenstein.
- [AI in Medical Documentation, Phase II] — pure regulatory analysis (no real-world testing possible).
- [AI in Building Permits, Phase II] — flagship working prototype; fed directly into a Cantonal Parliament postulate.

## Why someone planning a new AI pilot would read this specifically
This is the single most strategic document in the corpus — it explains what the sandbox *is now*, how it changed from Phase I, and the four-pillar 2026–2029 location strategy it now anchors. Without reading this, you can't speak credibly about where the sandbox is heading.

## Notable quotes
- "Our sandbox approach deliberately uses the strengths of the Swiss AI ecosystem: collaboration, openness and a clear practical focus." (*«Unser Sandbox-Ansatz nutzt gezielt die Stärken des Schweizer KI-Ökosystems: Kollaboration, Offenheit und klarer Praxisfokus.»*) — Raphael von Thiessen, p. 4.
- "Precisely in healthcare, you need protected test spaces to effectively bring regulatory requirements and progress together." (*«Gerade im Gesundheitswesen braucht es geschützte Testräume, um regulatorische Anforderungen und Fortschritt effektiv zusammenzubringen.»*) — Stefan Lienhard, CEO digital health center Bülach, p. 7.

## Three biggest deltas vs. Phase I (Play & Learn)
1. **Generative AI replaced computer vision as the technological centre of gravity**, but only after the team deliberately waited out the initial chatbot wave so they could test it reflectively.
2. **Healthcare became a deliberate sectoral focus** (4 of 24 applications), driven by partnership with digital health center Bülach. Two of five executed projects (Eye Clinic, Medical Documentation) were health, plus active regulatory work with Swissmedic.
3. **EU regulation moved from peripheral to central** — the Autonomous Inspection Robots project was framed entirely as an EU-AI-Act + EU-Machinery-Regulation market-access exercise, and the sandbox engaged cross-border with Germany's Bundesnetzagentur and Liechtenstein for the first time. Phase I's regulatory work was almost entirely Swiss law.

## Translation notes
- *Standortförderung* — rendered as "location promotion" (or sometimes "regional economic development"); literally the office charged with making Canton Zürich an attractive economic site. There is no clean English equivalent.
- *Befähigung des KI-Ökosystems* — "enabling the AI ecosystem"; "Befähigung" connotes both empowerment and capacity-building.
- *Regulatorisches Lernen* — "regulatory learning"; a sandbox-specific term of art meaning the iterative co-development of regulation through observed practice rather than purely top-down rulemaking.
- *Aufsichtsbehörden* — "supervisory authorities" / "regulators"; used broadly to cover both sector regulators (e.g. Swissmedic) and data-protection authorities.
- *Frontier-Modelle* — kept as "frontier models"; the German report uses the English term directly.
- *Real-World-Testing* — also kept in English in the German original.
- *Regierungsratsbeschluss* — "Cantonal Government Council decision"; the executive-branch resolution of Canton Zürich.
- *Postulat* — Swiss parliamentary instrument requesting the executive to examine a question; rendered "postulate" but a non-Swiss reader should understand it as a formal legislative motion.
- *Bundesratsentscheid zur KI-Regulierung* — "Federal Council decision on AI regulation"; the Swiss federal-level decision (Feb 2025) on how Switzerland implements the Council of Europe AI Convention.
