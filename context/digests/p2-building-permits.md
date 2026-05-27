# AI for Building Permits — Use Cases, Prototypes and Practical Insights

**Phase**: II (2024–2026)
**Topic**: AI-supported pre-checks for building/planning permit applications
**Published**: April 2026 (most recent Phase II report)
**Source**: reports/en/p2-building-permits.pdf (English and German parallel)
**Length**: ~33 pages

## Problem & context
Swiss building-permit procedures are highly fragmented: federal/cantonal/municipal jurisdictions overlay each other, requirements vary by zone, building type and project type, and a large share of applications arrive incomplete or formally incorrect — driving queries, suspensions and prolonged proceedings. Canton Zürich is mid-digitalisation: from 1 April 2027, all applications must run through the *eBaugesucheZH* platform. The Cantonal Parliament's postulate "AI in the building permit procedure" provides the political backdrop; this Sandbox project supplies the evidence base.

## Approach & methodology
Two-track: (1) **Systematic AI capability benchmark**: 3,336 controlled tests across eight frontier LLMs (gpt-5-mini, gpt-5.1, o3, gemini-3-pro-preview, gemini-2.5-flash, gemini-2.5-flash-lite, claude-opus-4.5, claude-sonnet-4.5) on real building applications from Stadt Kloten, scored 0–10 against expert reference answers, evaluated via *LLM-as-a-Judge*. Five capability dimensions: information extraction, counting, measuring/calculating, spatial understanding, context understanding. Each query repeated three times to measure consistency. (2) **Working prototype** developed with Nokema (project submission), Byte Studio (technical implementation), Gossweiler Ingenieure (specialist support) and the city of Kloten — narrowed to the **notification procedure** (Meldeverfahren) for solar panels, heat pumps and charging stations because complexity is bounded.

## Key findings & recommendations
- **Full end-to-end automation is unrealistic today** — AI value lies in clearly defined, modular sub-tasks.
- **Model performance is wildly heterogeneous**: best model 60.2% accuracy on perfect answers, average 37.9%, worst 18.5%. Speed: best 3.2s, worst 41.7s. Consistency (reproducibility across 3 runs): 86.8% best, 78.8% worst. Cost: best USD 0.0001 per query, worst USD 0.033 — **a full preliminary check on one application runs under CHF 2**.
- **Different models win on different metrics** — no single best provider; model-agnostic architecture is mandatory.
- **What works well today**: information extraction (area specs, roof shapes, scales, simple metadata), context understanding (green-space vs. road vs. building), counting with clear markings.
- **What fails today**: complex measurement/calculation (especially summing partial masses), counting unmarked elements (windows in complex façades), distance measurement (inconsistent interpretation of reference points/scales).
- **Rule-based beats generative AI when decision logic is clear** (process matrix → 8 project types × ~20 zone/protection criteria → if/then) — the prototype uses pure rule-based logic for procedure determination, generative AI only for unstructured document quality checks.
- **Greatest leverage is pre-submission quality improvement** — catching the recurring formal deficiencies (wrong scales, missing drawings) before they enter the formal proceeding.
- **System integration matters more than model choice**: isolated AI bolted onto a paper workflow creates media discontinuity and increases errors. The prototype is designed for integration with *eBaugesucheZH* and the GIS-Browser.
- **Probabilistic AI fights administrative reproducibility**: 95% vs 99% reliability is a substantive question requiring political decision.

## Legal & regulatory points
- **Planning and Building Act (PBG)** — Canton Zürich; primary statutory basis.
- **General Building Ordinance (ABV)** — Canton Zürich.
- **Construction Procedures Ordinance (BVV)** — Canton Zürich; specifically §§ 2a (notification procedure scope), 3 (completeness check), 4 (formal review), 14 (procedural review).
- **Cantonal Parliamentary postulate KR no. 226/2023** — "AI in the building permit procedure".
- **EMBAG (Federal Act on the Use of Electronic Means)** — SR 172.019, 17 March 2023; regulates e-government source-code disclosure, administrative data publication.
- **IDG ZH (Cantonal Information and Data Protection Act)** — currently being revised to add a transparency register for *Algorithmische Entscheidungsfindungssysteme (AES)* / algorithmic decision systems with fundamental-rights impact.
- **Swiss FADP Art. 21** — automated individual decisions; right to human review. Fully automated rejection of an application would likely breach.
- **Art. 29 BV** — constitutional right to be heard; AI-assisted decisions must be comprehensible and explainable, not "black box".
- **Principles of administrative law**: legality, equal treatment, proportionality, prohibition of arbitrariness, duty to give reasons — all apply equally to rule-based and generative AI systems.
- **Procurement law**: location of data centres in Switzerland and geo-redundancy may matter when procuring AI models (cited Federal Administrative Court ruling B-3238/2021, 20 October 2021 on "public clouds").
- **State liability**: for AI-induced unlawful decisions, liability lies with the public body, not the software provider; recourse against the provider is contractual/internal only. Authority cannot delegate responsibility — even technical errors are attributed to the authority.
- **Voluntary AI pre-check tools may still trigger state liability** under "protected trust" if users reasonably rely on them — must be clearly labelled non-binding.

## Data, models, infrastructure
- **Eight LLMs benchmarked**: gpt-5-mini, gpt-5.1, o3 (OpenAI); gemini-3-pro-preview, gemini-2.5-flash, gemini-2.5-flash-lite (Google); claude-opus-4.5, claude-sonnet-4.5 (Anthropic). 3,336 evaluations, scored via *LLM-as-a-Judge*.
- **Working prototype** (test access available from sandbox team) — 4-step UX: (1) address capture with map view (Leaflet/OpenStreetMap), (2) project-type selection from 8 reportable circumstances → rule-based procedure determination + GIS API lookups, (3) document upload with AI-supported pre-checks per document type (e.g. solar-datasheet against "low reflectivity", "module illustrations present"), (4) downloadable result summary.
- Plans are processed as PDF or pre-converted to high-resolution images depending on model.
- Architecture: modular, multi-level, model-agnostic; integration target *eBaugesucheZH* (interface not yet implemented).
- *Building Information Modelling (BIM)* and structured digital plans named as the longer-term substrate that would make AI evaluation easier; today, 2D PDF + AI is the bridge.
- *ÖREB cadastre* (Register of Restrictions on Ownership under Public Law) — referenced data source, but flagged as incomplete (e.g. municipal monument-protection inventories not consolidated).

## Stakeholders & partners
**Authors**: Stephanie Volz (Managing Director ITSL, University of Zurich), Raphael von Thiessen (AI Sandbox Programme Manager). **Project partners**: **NOKEMA GmbH** (project submission; ETH architect Marcel Muri), **Byte Studio GmbH** (technical implementation; founders Noah Chavannes + Yves Rutishauser), **Gossweiler Ingenieure AG** (specialist; Richard König), **Stadt Kloten** (test data provider — real building applications). **Specialist support** (named on p. 4): Dr. Alexander N. Walzer (FHNW Institute of Virtual Design and Construction), Benjamin Meyer (Head of Spatial Planning, Building Department Canton Zürich), Prof. Dr. Désirée Klingler (Asst. Prof. Public Law, University of St. Gallen), Evelyne Jost (FHNW), Marcel Hüppin + Maria-Luise Baldwin + Dr. Patrik Louis + Urs Späti (Canton of Zürich Building Department), Prof. Oliver Schneider (FHNW), Patrick Arnold (Wüest Partner), Tomas Polach (CTO and co-founder, onprem.ai). **Project Steering**: Office for Economy Canton Zürich, Statistical Office Canton Zürich, Department for Digital Administration Canton Zürich, Office for Economy Canton Schwyz, Metropolitanraum Zürich, ETH AI Center, ITSL Universität Zürich, swissICT, ZHAW entrepreneurship.

## Cross-references
- [Build & Share overview, Phase II] — flagship example for rule-based ≥ generative AI when decision logic is clear; cited explicitly as the canonical real-world-testing pilot.
- [Bridge Monitoring, Phase II] — same "data + AI cannot eliminate the need for human expertise" framing; both report into the cantonal political discourse.
- [Inspection Robots, Phase II] — opposite end of the legal spectrum (EU regulation-heavy vs. cantonal-administrative-law-heavy); both use ITSL legal analysis.
- [Smart Parking, Phase I] — image recognition on physical environment; building permits extends this to plan-document understanding (a different visual modality, much harder).
- [Machine Translation, Phase I] — fellow "AI in administrative procedures" report; both share the FADP Art. 21 + Art. 29 BV automated-decision framing.

## Why someone planning a new AI pilot would read this specifically
This is the corpus's only **working prototype with deployed code and a published evaluation pipeline**, and it answers two recurring administrative-AI questions head-on: (a) what's the actual capability ceiling of frontier LLMs today on structured Swiss government tasks (with numbers), and (b) how do you split work between rule-based logic and generative AI in a way that survives administrative-law scrutiny. For the hackathon prototype specifically, the multi-model LLM-as-a-judge evaluation harness is the most reusable engineering artifact in the bundle.

## Notable quotes
- "The greatest leverage of AI currently lies in improving the quality and completeness of building applications before submission." — Raphael von Thiessen, p. 7.
- "AI can support building authorities, but the justification and responsibility for decisions remain with humans." — Stephanie Volz, ITSL, p. 25.
