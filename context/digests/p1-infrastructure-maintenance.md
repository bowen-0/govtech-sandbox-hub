# Automated Infrastructure Maintenance — Drone Inspections with Computer Vision

**Phase**: I (2022–24)
**Topic**: AI-based crack/defect detection from drone imagery for civil infrastructure
**Published**: November 2023
**Source**: reports/en/p1-infrastructure-maintenance.pdf
**Length**: ~29 pages

## Problem & context
Switzerland has 84,000 km of roads, 40,000+ bridges, 200+ major dams (highest dam density worldwide) — and most inspections are still manual: time-consuming, inconsistent, dangerous, and poorly documented. Cracks identified roughly on a clipboard rarely produce a defect map that can drive maintenance decisions. AI-based image recognition combined with drone capture can produce digital-twin documentation systematically.

## Approach & methodology
**IBM Research Zürich** entered the sandbox in spring 2022 to extend its bridge-pillar inspection work to airport runways. The sandbox provided access to **Dübendorf Air Base** as data partner and engaged **pixmap gmbh** as third-party drone flight provider. Three drone missions over a 200 × 40 m runway section on 13 May 2023 collected imagery at three resolutions; IBM Research processed the data with a custom foundation model for crack detection and presented results in IBM's OCL (One-Click-Learning) tool. The runway was closed during flights; flight altitude limited to 10 m max.

## Key findings & recommendations
- Three-mission comparison: **M1** at 0.25 mm/pixel GSD (~11,500 images, 120 min flight, 0.7 m/s); **M2** at 0.75 mm/pixel (~1,200 images, 10 min, 4.2 m/s) — 10× faster, 9× less data; **M3** at 0.60 mm/pixel photogrammetric orthophoto. **M2 detected 15.2% fewer high-confidence cracks than M1** but captured all significant defects — the sweet spot for scaling to entire runways.
- Whole runway capture (2.8 km) is feasible in half a day at M2 settings — semi-annual inspection cycle achievable.
- RTK-GPS (1 cm accuracy) is essential for stitching sub-millimetre imagery; standard metre-accurate GPS fails at this resolution.
- Annotated civil-infrastructure datasets are extremely scarce; IBM used a 3-stage pipeline — self-supervised pre-training on generic images → SSL pre-training on civil-infrastructure images → supervised fine-tuning on crack-labelled images. Foundation model uses **vision transformer** architecture with self-attention.
- Image stitching at sub-cm precision required a custom algorithm (clustering by GPS proximity, divide-and-conquer at 200-image batches, 14 merged blocks). 332,520 image pairs reduced to 19,023 by GPS clustering.
- Output stack: IBM OCL platform offers image viewer, prediction viewer (pixel-accurate segmentation masks with crack length attributes), overview viewer, statistical viewer, reporting functionality with GPS-referenced defect detail.
- Open-data publication of this kind of inspection dataset is a key recommendation for ecosystem benefit — currently almost no public annotated civil-infrastructure imagery exists.

## Legal & regulatory points
This is a technical/operational report; legal coverage is light. Key points raised:
- EU/EASA drone regulations effective 1 January 2023 — stricter than before; operating licence must cover both Ground Risk and Air Risk.
- Federal Office of Civil Aviation (**FOCA / BAZL**) is the relevant Swiss authority; Drone Industry Association Switzerland mentioned for advocacy.
- No specific data-protection issues raised since the runway is a closed military area without public access.
- No EU AI Act citations.

## Data, models, infrastructure
- **Drone**: high-end quadcopter with full-frame 36×24 mm sensor, 40–100 MP resolution, short 0.7 s trigger interval, RTK-GNSS positioning (1 cm accuracy), autonomous waypoint flight.
- **GSD targets**: 0.25 mm/pixel (M1), 0.75 mm/pixel (M2), 0.60 mm/pixel (M3 orthophoto via Pix4Dmapper).
- **AI architecture**: vision transformer foundation model, 1024×1024 pixel tiles, hierarchical pre-training pipeline (SSL on ImageNet-style → SSL on civil-infrastructure → supervised fine-tune on crack-annotated). Few-shot/transfer/self-supervised learning leveraged due to scarce labels.
- **Defect classes detected**: Crack, Crack with precipitation, Crack (net-crack), Algae, Rust, Spalling.
- **Software**: pixmap operated the drone; IBM ran processing on GPU compute; **IBM OCL** (One-Click-Learning) platform for visualisation, with a custom tile server for the 200 m × 40 m orthophoto views.
- **Data volumes**: M1 dataset > 10,000 files, 14 blocks × ~824 images each.

## Stakeholders & partners
- **IBM Research Zürich** (Rüschlikon) — AI development. Authors: Florian Scheidegger.
- **pixmap gmbh** — drone flights. Author: Reto Weiss (CEO).
- **Dübendorf Air Base** — site / data partner (military facility).
- **Office for Economy Canton Zürich** — sandbox lead.
- No academic institution beyond IBM Research listed for this project.

## Cross-references
- [Phase II Bridge Monitoring] — direct successor; same infrastructure-maintenance theme, but sensor-based instead of image-based, addressing the same M1-vs-M2 scalability question with a different sensing modality.
- [Smart Parking] — shares image-recognition stack but in a public-space privacy-sensitive context; together they show how the same CV pipeline adapts to different regulatory environments (closed military airfield → no DPA work; public car park → 5-layer privacy-by-design).
- [Autonomous Systems] — drones explicitly excluded from that guide's scope ("Ground contact" criterion) but EU/EASA regulatory thinking is parallel.
- [Phase I overview Play & Learn] — the project the German bundle is missing; only EN version exists, making this report a "missing-but-important" anchor for any taxonomy.

## Why someone planning a new AI pilot would read this specifically
The only Phase I report with detailed quantitative ML benchmarking — concrete GSD trade-offs, dataset sizes, model architecture choices, and a real cost/quality curve (M1 vs M2). Reference for any project that involves drone-based or high-resolution visual inspection of public assets. Also the only report with a third-party-drone-provider partnership pattern worth copying.

## Notable quotes
- "The data captured for the Dübendorf runway is the first dataset of its kind that provides three different mission types for the same test area." (p. 26)
- "Every project in which AI applications are successfully used adds to the assurance that the developed foundation models... operate reliably in a broad context." (p. 14)
