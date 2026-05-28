# Wiki Index

> Auto-navigable inventory of every page in the wiki. Organised by type, then by phase / sector. Designed so an LLM (or a person) can scan the whole knowledge base in one read without opening every file.
>
> **Maintenance**: hand-edited for the seed batch (2026-05-28). Will be regenerated from frontmatter by a ~30-line script once the corpus is large enough that hand-maintenance is painful (~50+ pages).

---

## By type

### Projects (10) — one per sandbox pilot

> Project slugs drop the `p1-`/`p2-` prefix (phase is frontmatter, not filename). Source slugs *keep* the prefix to match PDF filenames. So `[[smart-parking]]` = the project page; `[[p1-smart-parking]]` = its source PDF page.

#### Phase I (2022–2024)
- [[smart-parking]] — Best practices for image recognition (camera-based free-parking detection). *Mobility.*
- [[autonomous-systems]] — Regulatory guide for autonomous machinery (drones, agricultural systems). *Autonomous Systems.*
- [[infrastructure-maintenance]] — Drone inspections with computer vision (IBM Research dataset, now on Hugging Face). *Autonomous Systems.*
- [[machine-translation]] — Recommendations for public administration adopting machine translation. *Public Administration.*
- [[ai-in-education]] — Legal best practices for AI in classrooms. *Education & Work.*

#### Phase II (2024–2026)
- [[bridge-monitoring]] — Data capture + AI predictions for infrastructure maintenance (SOB rail bridge). *Mobility.*
- [[digital-eye-clinic]] — Open-source AI diagnostics platform for diabetic retinopathy screening. *Healthcare.*
- [[inspection-robots]] — EU AI Act + EU Machinery Regulation compliance for autonomous inspection (ANYbotics, ISO/IEC 42001). *Autonomous Systems.* `analysis-only`
- [[medical-documentation]] — Legal foundations for AI-generated medical notes (MPAssist, Swissmedic). *Healthcare.* `analysis-only`
- [[building-permits]] — Working prototype + 3,336-evaluation benchmark (Nokema, Byte Studio, Kloten). *Construction.*

### Concepts (seeded from booklet glossary p.26)

- [[computer-vision]] — Visual data analysis (object detection, classification, damage identification).
- [[deepfakes]] — AI-generated or manipulated audio/image/video of individuals or events.
- [[eu-ai-act]] — *(canonical page lives in [regulations/](regulations/)).* Risk-based EU regulation of AI systems.
- [[frontier-models]] — Large-scale state-of-the-art AI models trained on extensive data.
- [[generative-ai]] — Systems generating new text/image/code/audio based on pre-trained models.
- [[intrapreneurship]] — Entrepreneurial activity within established organisations.
- [[iso-iec-42001]] — *(canonical page lives in [regulations/](regulations/)).* International AI management-system standard.
- [[large-language-models]] — Neural-network-based language models, foundation of generative AI.
- [[llm-benchmarks]] — Standardised tests for evaluating LLM performance; limited explanatory power.
- [[machinery-regulation]] — *(canonical page lives in [regulations/](regulations/)).* EU framework for machinery safety, relevant to AI in autonomous/safety-critical systems.
- [[real-world-testing]] — Evaluation of an AI system under real operating conditions with actual data.

Plus a few derived concepts from cross-cutting patterns in the digests:
- [[data-access]] — The "most powerful lever" per the booklet; partner bottleneck pattern.
- [[pseudonymisation]] — Recurring privacy-by-design technique (Smart Parking, Education, Eye Clinic, Building Permits).
- [[partner-bottleneck]] — Pattern where partner access (property owners, schools, hospitals) blocks more than the AI itself.

### Regulations

#### Swiss
- [[dsg-fadp]] — Federal Act on Data Protection (FADP/DSG). Central across all Phase I projects.
- [[idg-zh]] — Cantonal Information and Data Protection Act, Canton of Zürich.
- [[ai-convention-ch-implementation]] — Swiss implementation of the Council of Europe AI Convention.
- [[postulate-ai-building-permits]] — Cantonal Parliament postulate KR no. 226/2023.
- [[bundesratsentscheid-ki-regulierung]] — Federal Council decision on AI regulation.

#### EU
- [[eu-ai-act]] — EU regulation governing AI systems (risk-based).
- [[machinery-regulation]] — EU Machinery Regulation 2023/1230.
- [[gdpr-related]] — GDPR-equivalent considerations under FADP for cross-border data.

#### Standards
- [[iso-iec-42001]] — AI management-system standard.

### Stakeholders

#### People
- [[raphael-von-thiessen]] — Programme Lead AI, Canton of Zurich. Author of both phase overviews.
- [[lukas-willi]] — Project Lead AI, Canton of Zurich. **Challenge owner** at the hackathon.
- [[stephanie-volz]] — Managing Director ITSL, University of Zurich. Legal author/co-author across every Phase I + II project.

#### Organisations
- [[itsl-uzh]] — Center for Information Technology, Society, and Law, University of Zurich.
- [[amt-fuer-wirtschaft-zh]] — Office for Economic Affairs, Canton of Zurich. Coordinating body.

### Lessons (seed examples)

- [[lesson-rule-based-beats-generative-for-defined-logic]] — Cross-cutting pattern from Phase II. *Phase II.*
- [[lesson-data-access-is-the-most-powerful-lever]] — From Build & Share booklet, p.17. *Phase I + II.*

### Sources (13)

#### Phase overviews
- [[00-overview-phase1-play-and-learn]] — Phase I overview ("Play & Learn"). DE + EN.
- [[00-overview-phase2-build-and-share]] — Phase II overview ("Build & Share"). DE + EN. **The current authoritative snapshot.**

#### Phase I project reports
- [[p1-smart-parking]] — DE + EN.
- [[p1-autonomous-systems]] — DE + EN.
- [[p1-infrastructure-maintenance]] — EN only (no DE in the bundle).
- [[p1-machine-translation]] — DE + EN.
- [[p1-ai-in-education]] — DE + EN.

#### Phase II project reports
- [[p2-bridge-monitoring]] — DE + EN.
- [[p2-digital-eye-clinic]] — DE + EN.
- [[p2-inspection-robots]] — DE + EN.
- [[p2-medical-documentation]] — DE + EN.
- [[p2-building-permits]] — DE + EN.

### Synthesis (cross-cutting patterns)

- [[zh-ai-ecosystem-strategy-2026-2029]] — The four-pillar strategy following from Phase II (Sandbox · Startup Support · SME Adoption · Public Dialogue) per the Government Council decision.

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
- **Other**: *(none in the executed projects; the booklet lists submitted-but-not-executed projects here)*

---

## Open areas (gaps the wiki currently doesn't cover)

These are deliberate stubs — places where the team could add content during the hackathon.

- **Concepts** — `auftragsdatenbearbeitung` (commissioned data processing), `llm-as-a-judge`, `edge-computing`, `bias-audit`, `data-minimisation` (all repeating in the corpus).
- **Stakeholders** — most named test partners, technical implementation partners, and mandated experts from the booklet still need pages: MPAssist, ANYbotics, Modulos, irmos technologies, SOB, Spross Stiftung, Stadt Kloten, GoGymi, IBM Research, plus the named specialist support people (Walzer, Meyer, Klingler, Jost, Hüppin, Baldwin, Louis, Späti, Schneider, Arnold, Polach).
- **Lessons** — only 2 examples seeded. Reading each digest carefully yields 4-8 atomic lessons. Target: ~30-50 by hackathon end.
- **Regulations** — sector-specific regulation pages from individual reports (e.g. MDR, IVDR, EMBAG, sectoral laws referenced in Building Permits).

If you pick up one of these, link your PR to issue tag `wiki:expansion`.
