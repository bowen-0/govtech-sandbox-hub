# Smart Parking — Best Practices for Image Recognition

**Phase**: I (2022–24)
**Topic**: Camera-based image recognition for public parking occupancy
**Published**: January 2024
**Source**: reports/en/p1-smart-parking.pdf
**Length**: ~22 pages

## Problem & context
Swiss cities lack reliable data on outdoor public parking occupancy, fuelling unproductive debate between de-paving advocates and parking-retention groups, and producing traffic from drivers hunting free spaces. Frauenfeld has 14 public car parks (~500 spaces in the pilot scope); the city wanted occupancy data without installing one in-ground sensor per space.

## Approach & methodology
ETH spin-off Parquery AG submitted a proposal in spring 2022; the Innovation Sandbox paired it with the city of Frauenfeld as data/site partner. Cameras at 5 car parks captured a still image every 2 minutes (not video); images were converted to numerical occupancy data and deleted immediately. The pilot ran from August 2022; the production system has been live since November 2023, integrated into Frauenfeld's "Regio" app and exposed via the Parkopedia interface to car navigation systems. Live data also flows to an open-data dashboard.

## Key findings & recommendations
- Cameras beat in-ground sensors for cost-per-space at outdoor sites — one camera covers many spaces and supports analyses (vehicle type, duration) sensors cannot.
- Non-AI obstacles dominated: powering cameras 24/7 (battery + off-peak grid), gaining property-owner consent, and coordinating with electricity suppliers ate most of the timeline.
- "Privacy-by-design stack" combines: low resolution, high bird's-eye camera angle, digital masking of pedestrian zones/ATMs/entrances, instant deletion after numerical conversion, edge or Swiss-cloud processing. No single measure suffices — combine them.
- Snapshot every 2 min is sufficient for occupancy and reduces re-purposing risk (e.g. for gait analysis) vs. continuous video.
- Open-data publication (ISO/APDS standard, MODI federal infrastructure) future-proofs the dataset for navigation apps and downstream analyses.
- Dummy/visible cameras still create perceived surveillance — communicate intent via on-site QR codes and FAQs even when no personal data is recorded.
- Get the political mandate explicit (Regierungsbeschluss / city council resolution) BEFORE installation — citizens will demand information rights regardless of whether personal data is technically processed.

## Legal & regulatory points
- Cantonal IDG (Gesetz über die Information und den Datenschutz) — applies because Frauenfeld is a public body; legitimate basis required for image processing even when output is anonymous.
- Federal FADP (DSG) — applies if the AI provider processes data for its own purposes.
- Commissioned data processing ("Auftragsdatenbearbeitung") — Parquery as third-party processor requires a written contract per IDG Zürich. Same applies to cloud providers.
- Re-purposing of data needs a separate legal basis or data-subject consent (purpose limitation principle); police access to camera data possible only via specific federal/cantonal authorisations.
- GDPR-derived "privacy by design" and "privacy by default" principles applied even though Switzerland is non-EU.
- Data export outside Switzerland: only to countries on Annex 1 of the Ordinance on Data Protection (DPO) — EU/UK yes, USA no.
- Right to information (Auskunftsrecht) applies even if no personal data is recorded — prepare a standing response.

## Data, models, infrastructure
Vendor: **Parquery AG** (ETH spin-off). Camera model not specified — any device with SIM/wireless/wired transmission works. Software runs on-premise, edge, or Swiss SaaS cloud. Still images every 2 min → numerical occupancy data → dashboard (live + historical reports with parking duration distributions). Specific ML architecture not disclosed beyond "AI-based image recognition that learns by example." Integration with Frauenfeld's "Regio" app and Parkopedia. Open-data publication planned via APDS (Alliance for Parking Data Standards ISO).

## Stakeholders & partners
- **Parquery AG** (ETH spin-off, vendor)
- **City of Frauenfeld** — Office for Communications and Business Development (Peter Koch)
- **Parking Zürich AG** (Georg Spycher, interviewee)
- **Office for Economy Canton Zürich** (sandbox lead)
- **ITSL University of Zürich** (Stephanie Volz, legal expertise)
- **Ausschuss Digitalisierung des Verbands ParkingSwiss**, **MODI** (Federal Office of Transport), **APDS** (international standard) — referenced as standards bodies for data harmonisation.

## Cross-references
- [Phase II Bridge Monitoring] — also public-infrastructure image recognition; informative comparison on sensors vs. cameras (Bridge Monitoring uses sensors precisely because they avoid the personal-data risk Smart Parking had to engineer around).
- [Infrastructure Maintenance] — second image-recognition project in Phase I; covers airborne (drone) capture in a closed environment, whereas Smart Parking covers fixed cameras in public space — together they bracket the privacy-risk spectrum.
- [Autonomous Systems] — same privacy-by-design vocabulary (low resolution, lidar/edge) appears there for mobile cameras.
- [Phase I overview Play & Learn] — flagship example of the "data provisioning" sandbox axis.

## Why someone planning a new AI pilot would read this specifically
The single most concrete operational playbook for installing AI image recognition in Swiss public space — every legal, technical and political bottleneck spelled out, including the political resolution path and the 5-layer privacy-by-design stack. Reusable for any city considering camera AI.

## Notable quotes
- "Our goal is to realise an efficient parking management based on intelligent technologies." — Peter Koch, City of Frauenfeld (p. 5)
- "Image recognition in public can be responsibly implemented through technical and organisational measures." — Raphael von Thiessen (p. 14)
