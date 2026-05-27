# Autonomous Systems — Guidelines for Regulatory Questions

**Phase**: I (2022–24)
**Topic**: Regulatory guide for manufacturers of autonomous ground vehicles (non-transport)
**Published**: July 2023
**Source**: reports/en/p1-autonomous-systems.pdf
**Length**: ~25 pages

## Problem & context
Swiss law has no dedicated framework for autonomous systems that operate commercially on the ground but aren't passenger/freight vehicles — e.g. agricultural tractors, professional lawnmowers, cleaning robots, security patrollers. Manufacturers (often small start-ups) face a fragmented patchwork of product safety, road traffic, data protection and liability law, with no entry point. The Road Traffic Act revision is underway but not yet in force.

## Approach & methodology
Two start-ups — **Lonomy** (autonomous tractor for fruit-growing/viticulture) and **Ronovatec** (self-driving professional lawnmower) — entered the sandbox in spring 2022 with overlapping regulatory questions. Rather than testing a product, the sandbox bundled their cases into a single legal guide written by Stephanie Volz (ITSL UZH) with input from FEDRO, SUVA, TÜV Süd, SNV, Zurich Insurance and academics. Ronovatec went bankrupt mid-collaboration; guidelines were finalised using Lonomy plus expert interviews. Output is a Q&A reference book, NOT a tested prototype.

## Key findings & recommendations
- Use the existing legal stack proactively — Swiss Ordinance on Machine Safety (MaschV) covers most autonomous ground systems by treating them as "machines"; sectoral special rules (chemicals, foodstuffs) take precedence over the Federal Law on Product Safety.
- CE marking is not legally required for Swiss-only market, but is strategically advisable if EU sale is planned later — and most relevant EN/CEN-CENELEC standards are EU-derived anyway.
- "Already authorised in EU = automatically authorised in Switzerland" — true for machines (Swiss ordinance directly references the EU machinery directive); for vehicles, mutual recognition with EU applies via FEDRO homologation.
- Pavements and walkways qualify as public roads under SVG — autonomous systems crossing them legally must do so on a trailer or as a "dual mode" vehicle manually steered across.
- Pilot-test exception (SVG Art. 106 para. 5) — the Federal Council can grant exemption permits for automated vehicle tests; conditions are documentation of insights, mitigation of legal gaps, and proportionality of residual risk.
- Lidar can still capture personal data (silhouettes, gait) — privacy-by-design also applies to non-camera sensors.
- Recommendation: introduce a "no-person-data" camera label so the public can distinguish surveillance cameras from inspection ones.
- Animal welfare is under-regulated for animal-machine interactions — manufacturers should adopt own measures (ML thermographic cameras for animal detection) ahead of regulation.
- Liability stack: Product Liability Act (PrHG) for personal injury/property damage to third parties; Code of Obligations Art. 55 (employer liability), Art. 41 (general fault-based), Art. 58 (property-owner); SVG Art. 58 strict motor-vehicle liability if road-authorised.

## Legal & regulatory points
- **Federal Law on Product Safety (PrSG)** — baseline product safety obligations.
- **Ordinance on Machine Safety (MaschV)** — primary regime for autonomous machines; conformity assessment required.
- **Federal Energy Efficiency Ordinance** — applies generally.
- **Swiss Road Traffic Act (SVG)** — Art. 1 (public road definition includes pavements, meadows, frozen waterways), Art. 58 (motor-vehicle strict liability), Art. 87 (no disclaiming liability), Art. 106 para. 5 (pilot test exception). FEDRO/ASTRA is the homologation body.
- **Product Liability Act (PrHG)** — Art. 8 (no disclaiming), CHF 900 deductible.
- **Swiss Code of Obligations (OR)** — Art. 41 (fault), Art. 55 (employer), Art. 58 (property owner).
- **Federal Act on Data Protection (FADP)** — in force from 1 Sep 2023; introduces privacy-by-design and privacy-by-default principles into Swiss law.
- **Cantonal data protection (IDG ZH)** — applies when public administration deploys the system.
- **Animal Welfare Act** — relevant for ML detection systems near livestock.
- **EU AI Act (AI-E)** — Art. 5 (prohibited), Art. 6–51 (high-risk), Art. 52, Art. 69. **AI Liability Directive**, **Machinery Regulation 2023** (updates 2006/42/EC), **Cybersecurity regulation for products with digital elements**, **Product Liability Directive** — all influence Swiss manufacturers selling into EU.
- Bodies cited: **SNV** (Swiss Association for Standardization), **SUVA**, **TÜV Süd**, **OFCOM** (radio licences), **FEDRO/ASTRA**, **SAVV** (Swiss Automobile Association).

## Data, models, infrastructure
This is a non-technical guide — no models, datasets or deployment infrastructure are documented. The two case studies (Lonomy tractor, Ronovatec lawnmower) are mentioned only as legal-question generators. Technical references include lidar sensors, edge computing, GPS, and thermographic ML cameras as illustrative privacy-by-design measures.

## Stakeholders & partners
- **Lonomy** (autonomous tractor, fruit/viticulture) — Swiss start-up.
- **Ronovatec** (autonomous lawnmower, professional greenkeeping) — bankrupt mid-project.
- **Office for Economy Canton Zürich** (sandbox lead).
- **ITSL University of Zürich** — Dr. iur. Stephanie Volz (lead author).
- **Expert interviewees**: Benno Nager (FEDRO/ASTRA), Dr. Martin Saerbeck (TÜV Süd), Prof. Oliver Bendel (FHNW), Patrick Graber (Zurich Insurance), Prof. Thomas Probst (University of Fribourg / SAAM), David Schaltegger (SNV).

## Cross-references
- [Phase II Inspection Robots] — direct successor; that report applies EU AI Act + EU Machinery Regulation to a concrete robot deployment, so this guide's open questions get tested there.
- [Smart Parking] — shares the privacy-by-design vocabulary (low resolution, masking, edge computing) but for fixed cameras instead of mobile systems.
- [Infrastructure Maintenance] — drone (airborne autonomous system) — explicitly out of scope here ("Ground contact" criterion) but uses the same EU/EASA regulatory thinking.
- [Phase I overview Play & Learn] — exemplifies the "regulatory consulting" axis with NO data provisioning needed.

## Why someone planning a new AI pilot would read this specifically
This is the most legally dense Phase I report — a 16-question Q&A that any Swiss start-up putting a moving machine into a semi-public space should treat as a checklist. Particularly valuable for the gap between "machine on private property" and "vehicle on public road" — the practical middle ground (sports fields, fields with crossings, pavement transit) where most innovation happens.

## Notable quotes
- "The regulatory frameworks and standards will continually change in the future. Manufacturers must closely monitor these developments." — David Schaltegger, SNV (p. 8)
- "In many cases, manufacturers can avoid the generation of personal data." — Stephanie Volz, ITSL UZH (p. 15)
