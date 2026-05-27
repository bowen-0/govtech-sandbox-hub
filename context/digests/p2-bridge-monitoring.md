# Sensor-based Bridge Monitoring — Data Collection and Forecasting for Infrastructure Maintenance

**Phase**: II (2024–2026)
**Topic**: Sensor + AI monitoring of railway bridge structural condition
**Published**: February 2026
**Source**: reports/en/p2-bridge-monitoring.pdf (English available; German parallel exists)
**Length**: ~16 pages

## Problem & context
Switzerland operates ~40,000 bridges, many built between the 1950s–1980s and now nearing end of designed service life, while loads (heavier trains, denser timetables, more freight) and climate stress (heatwaves, flooding, frost-thaw) keep rising. Today's bridge assessment relies on visual inspection plus standards-based structural reassessment under conservative assumptions, producing costly precautionary reinforcements or replacements. The Morandi collapse (Genoa 2018, 43 dead) and Carolabrücke partial collapse (Dresden 2024) are cited as evidence of how fast safety-relevant defects can emerge.

## Approach & methodology
Schweizerische Südostbahn AG (SOB) and irmos technologies instrumented the 5-metre Reidholz railway bridge on the Wädenswil–Einsiedeln line (Canton Zürich; built 1910, converted from steel to concrete slab in 1953, shotcrete-reinforced in 1990). They installed a "lean" sensor network — accelerometers (dynamic response), strain gauges (stress variations), a temperature sensor (seasonal correction), a data acquisition unit, plus cameras to validate train type/speed/composition. Over several months, real-world traffic-induced loads were captured. AI-assisted analysis identified patterns and calibrated engineering models, with all metrics visible on a cloud-based dashboard. The original sandbox partner (a municipal pedestrian-footbridge owner) had withdrawn, prompting the pivot to SOB's rail bridge.

## Key findings & recommendations
- **Even short measurement campaigns** (months, not years) yield robust conclusions about fatigue and stiffness — but results must be interpreted with safety margins because seasonal coverage is incomplete and long-term historical load data is absent.
- **Service life extension is plausible**: SOB explicitly asked whether the bridge could be operated safely for 20 years instead of 10; sensor data + calibrated models supported a less conservative answer than standards-based methods.
- **Dynamic amplification factors and assumed stiffness** — both inputs to standards-based assessment — were verifiable against measurement reality, often showing the standard assumptions were over-conservative.
- **Scenario simulation tool** built: combines historical data with assumptions about future train types/frequencies/loads to project remaining service life under "conservative" vs "optimistic" assumptions (damage accumulation projected out to 2045/2055).
- **Portfolio-scale leverage**: similar age/construction across the bridge fleet means the methodology scales beyond the individual asset.
- **Data-driven monitoring complements, not replaces, existing standards-based evidence** — explicit warning against parallel-structure proliferation.
- **Only collect data that supports a clear operational decision** — data collection is not an end in itself.

## Legal & regulatory points
- **Swiss Code of Obligations** (*Obligationenrecht*) — governs contractual liability between operator and technical provider; non-contractual liability toward third parties if obviously-wrong measurements lead to damage.
- **Swiss product liability law** — applies to personal injury caused by faulty sensor systems.
- **SIA 261.008 (Eurocode 1, Part 2)** — Swiss/European standard for traffic loads on bridges; the baseline against which data-driven methods are compared.
- **Swiss FADP/DSG** — applies only to camera footage that could identify individuals (faces, licence plates, employee clothing); pure sensor data (temperature, strain, acceleration) is *not* personal data and falls outside FADP scope. Mitigations recommended: on-site signs, restricted camera angles, pixelation/automatic obliteration of individuals/plates, swift deletion of raw footage after validation.
- **Federal Office of Transport (BAV) service agreements** — define objectives/indicators; relevant to who pays for what investments over which period.
- **MODI** (federal Mobility Data Infrastructure) — emerging national framework for data-driven infrastructure policy.
- Liability is allocated by role: operator responsible for access to the structure; technical provider for safe assembly and regular maintenance. Provider liable for grossly negligent analysis; cannot contractually exclude wilful/grossly-negligent conduct.

## Data, models, infrastructure
- Sensor stack: accelerometers, strain gauges, temperature sensor, data acquisition unit, cameras for train classification.
- Vendor: **irmos technologies** — proprietary cloud-based dashboard showing global health status, traffic condition, temperature, daily max deflection, current stiffness, axle loads per bogie, train count by type, speed and passage frequency over the full measurement period.
- **AI methods**: pattern recognition, anomaly identification, model adaptation to real-world data; specific model architectures are not named.
- Output artifact: a function/tool that combines historical + projected loads to simulate remaining service life under varying assumptions.

## Stakeholders & partners
- **Schweizerische Südostbahn AG (SOB)** — regional railway operator; test partner; technical lead Stephan Zürcher (Technology Manager Infrastructure).
- **irmos technologies** — Zurich-based sensor + AI vendor; Dr Panagiotis Martakis (Founder & CEO).
- **Stadt Frauenfeld** / municipal pedestrian-bridge partner — original test partner that withdrew before the pivot to SOB.
- **Innovation Sandbox** / *Standortförderung Kanton Zürich* — Raphael von Thiessen, Programme Manager.
- **ITSL Universität Zürich** — Stephanie Volz (Managing Director) led the legal analysis.
- **Federal Office of Transport (BAV)** — implicated via service agreements (named in conclusions).

## Cross-references
- [Automated Infrastructure Maintenance, Phase I] — direct predecessor; that project used drone+CV for visual inspection, while this one adds *sensor-based dynamic monitoring*. The two methods are explicitly framed as complementary (visual vs. continuous structural).
- [Smart Parking, Phase I] — another image-recognition-on-infrastructure pilot; same operator-vs-provider liability framing applies.
- [Build & Share overview, Phase II] — names this as one of three "real-world testing" pilots.
- [Autonomous Inspection Robots, Phase II] — another infrastructure-inspection automation use case but with much heavier EU regulatory framing.
- [AI in Building Permits, Phase II] — shares the "rule-based assessment vs. data-driven model" tension.

## Why someone planning a new AI pilot would read this specifically
This is the cleanest case study in the corpus for "how to introduce continuous-monitoring AI into a safety-critical legacy domain without displacing existing engineering judgement" — and the only Phase II pilot where Swiss Code of Obligations liability framing is worked through in detail.

## Notable quotes
- "Data-driven monitoring does not replace existing evidence, but complements it with measurement data from live operations." — Raphael von Thiessen, p. 6.
- "Data-driven monitoring systems support operations, but they do not shift the responsibility for safety-related decisions from the operator to the technology." — Stephanie Volz, ITSL University of Zurich, p. 13.
