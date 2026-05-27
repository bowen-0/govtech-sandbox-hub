# Artificial Intelligence in Education — Legal Best Practices

**Phase**: I (2022–24)
**Topic**: Data protection and copyright for AI tools in schools
**Published**: October 2023
**Source**: reports/en/p1-ai-in-education.pdf
**Length**: ~15 pages

## Problem & context
AI tools (automated correction, personalised learning, exam preparation) are already widely used in Swiss schools, but the legal framework is unclear to providers, teachers, parents and school authorities. Children's data is sensitive by default; cantonal data-protection rules vary; copyright on training data and teaching materials is unsettled. The result is uncertainty that slows adoption and creates compliance risk.

## Approach & methodology
**Herby Vision AG** entered the sandbox in spring 2022 with a smartphone-scan tool that auto-corrects handwritten primary-school maths and spelling worksheets. Direct school access was difficult; the team partnered with the **Swiss EdTech Collider** to gain primary-school testing (this still took months). Output is a legal guide aimed at EdTech providers (not directly at schools). A specific finding was that legal support pushed the start-up to redesign — they pushed personal-data-dependent features into the background and centred the product on pure automated correction, reducing regulatory complexity.

## Key findings & recommendations
- **Holistic legal analysis is non-optional** — data protection always applies, but copyright (training data, teaching materials), administrative/school law and contract law overlap in nearly every case. Identify all four early.
- **Generate as little personal data as possible** — handwritten worksheets are usually identifiable to the teacher, qualifying as personal data; design tools so the AI provider can't link sheets to children (no names, no birth dates in registration, QR-code-based session allocation). Once anonymous, much of the legal complexity vanishes.
- **Consent is a trap, not a solution** — children's consent requires guardian consent, must be truly voluntary with real choice. Better path: rely on the statutory basis already in the cantonal Volksschulgesetz, or render data non-personal.
- **Data Protection Impact Assessment (DPIA) is mandatory** in Canton Zürich for new processing activities by public bodies (schools). If the DPIA flags risk, submit to the cantonal data protection officer for **prior checking** along with an **ISDP concept** (information security and data protection).
- **Sensitive data caution**: educationally relevant diagnoses (dyslexia, dyscalculia), religious info, biometric data (voice/handwriting analysis can qualify) need explicit statutory basis from formal cantonal parliament law.
- **Reusing pupils' data for AI training is generally not permitted** without separate legal basis or full anonymisation — even though it would be commercially attractive for the provider.
- **Teaching material in AI tools triggers copyright** — Swiss copyright's classroom exception does NOT extend to commercial AI tools; author consent required.
- **Embedding LLMs via API creates uncontrolled data flow** — particular caution; data security and provider copyright risks both apply.
- **Recommendation 1**: uniform national strategy across cantons for legal security (currently fragmented).
- **Recommendation 2**: cantonal contact points for AI providers to get compliance pre-checks (one provider asking the same question of 26 cantonal schools is not scalable).

## Legal & regulatory points
- **Cantonal data protection** — In Canton Zürich, **Gesetz über die Information und den Datenschutz (IDG)** for state schools (public bodies); other cantons have parallel laws applied differently.
- **Federal Act on Data Protection (FADP)** — applies to private-sector AI providers and federal authorities.
- **Volksschulgesetz** (Zurich elementary education law) — provides statutory basis for school-related data processing; in some cases also covers sensitive data if sufficiently specific.
- **Data processing principles** — lawfulness (legal basis required), proportionality, purpose limitation, data minimisation, transparency (duty to inform).
- **Special categories of personal data** (sensitive data) — health, religion, ethnicity, biometric, criminal proceedings — require statutory basis from a formal law (parliamentary act).
- **Profiling** — falls under sensitive data rules when evaluating substantial personal aspects.
- **Copyright on training data**: **Federal Act on Copyright and Related Rights (URG) Art. 24d** — text-and-data mining exception for scientific purposes; legal uncertainty over whether this extends to commercial AI tool training. **Strong recommendation: clarify case-by-case.**
- **Copyright classroom exception** — applies only to actual classroom use, NOT to commercial AI tools using teaching materials.
- **Data Protection Impact Assessment (DPIA)** — mandatory for new data processing in Canton Zürich.
- **Prior checking** by cantonal data protection officer when DPIA flags risk; requires ISDP concept submission.
- **Commissioned data processing contracts** — minimum content prescribed by cantonal law; in Zürich, by ordinance to the IDG and GTC of the Zürich Government Council.

## Data, models, infrastructure
- **Vendor**: Herby Vision AG — image-recognition AI for automated correction of handwritten primary-school maths and spelling.
- **Delivery**: smartphone scan → AI-based image recognition → automatic correction feedback.
- **Model architecture not disclosed.**
- **Training data**: handwritten worksheets — privacy implications discussed but training dataset details not stated.
- **LLM integration**: discussed as a future risk pattern (embedding via API) but not used in the case study itself.
- **Testing infrastructure**: Swiss EdTech Collider testbed program (private testbed; replaces direct school access).

## Stakeholders & partners
- **Herby Vision AG** — vendor / case study.
- **Swiss EdTech Collider** (Verena Rohrer, Carmen Sieber) — testbed partner enabling primary-school testing.
- **Office for Elementary Education (Volksschulamt), Canton Zürich** (René Moser).
- **Educa** (Nelly Buchser, Karen Grossmann) — Swiss agency for digital education.
- **Schule Medien Informatik Zürich** (Moria Zürrer — school principal).
- **Kellerhals Carrard** (Manuel Brogli) — law firm.
- **ITSL University of Zürich** (Stephanie Volz, lead author).
- **Office for Economy Canton Zürich** (sandbox lead).

## Cross-references
- [Phase II Medical Documentation] — closest analogue: AI processing sensitive personal data in a regulated public-trust context; same DPIA / sensitive-data / consent-trap arguments apply.
- [Phase II Building Permits] — uses the same cantonal-IDG framework but for administrative procedure rather than education.
- [Machine Translation] — shares the "cantonal directives ban free online tools so build internal alternatives" pattern.
- [Smart Parking] — same FADP vs IDG split, same commissioned-data-processing contract requirement.
- [Phase I overview Play & Learn] — exemplifies the difficulty of finding implementation partners (school access took months).

## Why someone planning a new AI pilot would read this specifically
The most data-protection-dense Phase I report and the one with the clearest legal taxonomy — handles personal data, sensitive data, biometric data, profiling, copyright on training data, copyright on teaching materials, DPIA, prior checking, consent traps, and LLM-embedding risks all in 15 pages. Reusable structure for any AI pilot touching minors or other sensitive populations.

## Notable quotes
- "Due to the legal complexity of AI projects in schools, a holistic approach is recommended." — Stephanie Volz (p. 4)
- "The collection of personal data that is not strictly necessary for an AI application significantly increases legal complexity." — Stephanie Volz (p. 8)
- "The integration of Large Language Models offers great opportunities for solution providers, but also leads to legal risks that are difficult to control." — Raphael von Thiessen (p. 12)
