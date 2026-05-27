# Digital Eye Clinic — AI-supported Ophthalmology at Stadtspital Zürich

**Phase**: II (2024–2026)
**Topic**: AI diagnostics for diabetic retinopathy (and roadmap to broader ocular AI)
**Published**: November 2025
**Source**: reports/en/p2-digital-eye-clinic.pdf (English and German parallel)
**Length**: ~31 pages

## Problem & context
Switzerland has ~430,000 people with diabetes; ~25% develop *diabetic retinopathy* (DR), the leading cause of preventable blindness in working-age adults. Screening capacity is constrained by specialist shortage and growing patient volumes, and *optical coherence tomography (OCT)* and *colour fundus photography (CFP)* together generate more image data than ophthalmologists can read reliably. Stadtspital Zürich's ophthalmology department (Prof. Matthias Becker MD) and the **Werner H. Spross Foundation for the Advancement of Ophthalmology** entered the sandbox in summer 2024 to test whether AI could close the screening gap without losing clinical control.

## Approach & methodology
Two parallel tracks. **(1) Vendor assessment**: structured market scan of five commercial DR-screening solutions, scored against six criteria (Azure / on-premise deployment, OCT *and* CFP support, integration with the clinic's own AI, glaucoma + AMD coverage in addition to DR, modularity, transparency/auditability). **None of five vendors met the combined requirements**, with vendor pricing ranging USD 6,000–18,000 setup + EUR 189–1,500/month. Deal-breaker was usually inability to plug in the clinic's own models or support both imaging modalities. **(2) In-house build**: adapted Meta AI's open-source **DINOV2** *Vision Transformer* into **Block Expanded DINORET** for retinal images, ran on a local GPU PC then a CPU-only setup; wrapped it in a web-based MVP GUI on the hospital network (secure login, exam management module, AI inference pipeline, results+heatmap display, DICOM-compliant export, explicit error states). Validated against a medical second opinion per case (sensitivity, specificity, false positives/negatives, processing time, uptime) and a clinical review by treating ophthalmologists.

## Key findings & recommendations
- **No off-the-shelf solution fit the clinic** — modular, open, interoperable architecture is the only viable path for a public hospital with its own ML capability.
- **In-house Vision Transformer (DINORET) was the chosen route** — adapted from Meta's DINOV2; gives full responsibility for performance and support but eliminates vendor lock-in.
- **MVP is operational** with secure auth (username + 2FA), exam creation, AI inference for DR severity, heatmap-based explainability, dispute/confirm workflow, and DICOM export.
- **Cloud is the target state** for scalable, maintainable operation; edge/on-premise was the MVP fallback because data-protection clearance for cloud was unfinished — explicit reference to the *Medical Documentation* report for the legal detail.
- **Glaucoma module is next**, then AMD; modular back end means each new condition is a new model behind the same UI.
- **Clinician acceptance is the actual blocker, not accuracy** — codesign with doctors during prototyping was decisive for adoption.
- **Best practices**: structure the project in market-research → pilot → validation → deployment gates; insist on DICOM + FHIR + open APIs; engage regulatory experts from day one; treat the *in-house exception* under MDR/MedDO as nuanced (an internally-used AI that drives treatment decisions can still qualify as a medical device, even if not sold).

## Legal & regulatory points
- **Swiss Medical Devices Ordinance (MedDO)** + **EU MDR (Regulation 2017/745)** — Annex VIII classification; likely **Class IIa or IIb** for diagnostic support → CE marking, notified-body conformity assessment, technical documentation, risk analysis required before any external release.
- **"In-house exception"** — using a self-developed AI inside a single healthcare institution may avoid full MDR compliance, *but* if outputs drive patient treatment decisions the line is crossed; the report explicitly flags this as nuanced and recommends regulatory consulting.
- **Swiss FADP / cantonal IDG ZH** — strict on-premise handling for MVP patient data; any future cloud (Azure) deployment requires encryption, deidentification, data-processing agreements, and an assessment of US **CLOUD Act** exposure.
- **Information Security and Data Privacy (ISDS)** processes — internal Stadtspital regime that all images and data complied with.
- **EU AI Act** — implied via the cross-reference to the Medical Documentation report; medical-decision-influencing AI is high-risk.
- **Ethics**: transparent disclosure of AI use to patients, physician retains final diagnosis, bias monitoring (training-data demographic mismatch flagged as a deployment risk).

## Data, models, infrastructure
- Imaging stack: **Heidelberg Spectralis OCT** and **Zeiss Clarus** fundus camera; outputs OCT cross-sectional retinal scans + colour fundus photographs.
- Foundation model: **Meta DINOV2** → fine-tuned/extended into **Block Expanded DINORET** (Vision Transformer for retinal image analysis).
- Compute: started on a local **GPU** PC; production target is CPU-only or cloud.
- MVP stack: web app on hospital network, secure 2FA login, DICOM-compliant export, heatmap-based explainability, dispute/confirm interface.
- Standards baked in: **DICOM** for imaging, **FHIR** named as the longer-term EHR interop layer.

## Stakeholders & partners
**Project lead**: Prof. Matthias Becker MD (Head of Ophthalmology, Stadtspital Zürich). **Authors / project team**: Raphael von Thiessen (Programme Manager, AI Sandbox), Dávid Isztl (Machine Learning Engineer, Department of Ophthalmology + Spross Research Institute), Rui Santos PhD, Gábor Márk Somfai MD/PhD, Tahm Spitznagel MD, Florian Lüchinger (Foresite AG). **Legal**: Stephanie Volz (Managing Director ITSL, University of Zurich). **Additional clinical/MBA support**: Amr Saad MD/MBA; Stephanie Volz also coordinated the cross-report regulatory analysis. **Test partner**: **Stadtspital Zürich + Werner H. Spross Foundation**. **Project Steering**: Office for Economy (Zürich + Schwyz), Statistical Office Zürich, Department for Digital Administration Zürich, ETH AI Center, ITSL UZH, ZHAW entrepreneurship.

## Cross-references
- [Build & Share overview, Phase II] — flagship health-sector pilot; modular open-source diagnostics platform.
- [Medical Documentation, Phase II] — explicit footnote cross-reference (footnote 9, p. 25); medical-device classification and data-protection detail live there.
- [Inspection Robots, Phase II] — adjacent "safety-critical AI under notified-body conformity assessment" framing, but under MDR rather than EU Machinery Regulation.
- [Building Permits, Phase II] — shared ITSL legal-analysis backbone; opposite end of the regulatory complexity spectrum.
- [Phase I — no direct predecessor]; this is the first health-sector deep dive, made possible by the *digital health center Bülach (dhc)* partnership formed at Phase II launch.

## Why someone planning a new AI pilot would read this specifically
This is the corpus's reference example for **"build vs. buy" in a Swiss public hospital** when commercial vendors don't quite fit — and the only worked example of fine-tuning an open-source foundation model (DINOV2 → DINORET) inside the sandbox. The vendor-comparison table is directly reusable as a procurement template, and the MVP architecture (modular back end, DICOM/FHIR-first, heatmap explainability, dispute/confirm workflow) is the cleanest UX pattern in the bundle for clinician-in-the-loop AI.

## Notable quotes
- "Machine learning in ophthalmology paves the way for safe, accurate, and accessible ocular disease prediction." — Dávid Isztl, Machine Learning Engineer, Department of Ophthalmology and Spross Research Institute, Stadtspital Zürich, p. 22.
