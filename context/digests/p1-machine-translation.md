# Machine Translation — Recommendations for Public Administration

**Phase**: I (2022–24)
**Topic**: Machine translation tools for Swiss public administration
**Published**: February 2024
**Source**: reports/en/p1-machine-translation.pdf
**Length**: ~25 pages

## Problem & context
Switzerland has four official languages plus high migration; administrative offices (commercial registers, migration offices, courts, labour market offices) face constant translation demand. Free tools like DeepL and Google Translate are convenient but route sensitive data outside Switzerland and don't know Swiss administrative jargon. Specialised Swiss providers exist but adoption is fragmented and per-office. Policy question: should administrations translate official content at all? If yes, into which languages, and with what tools?

## Approach & methodology
Two Swiss translation start-ups entered the sandbox in spring/summer 2022 with overlapping cases — the team bundled them into a comparative study. **Neur.on** worked with the **Commercial Register of Canton Schwyz** to build a German→English (then French/Italian) translation model fine-tuned on 20,000 commercial-register entries. **Textshuttle** (University of Zürich spin-off) worked with the **Integration Unit of Canton Zürich** on a tool with stored public-administration terminology in English, French, Italian and Polish. A blind benchmarking compared DeepL Pro, Textshuttle, and certified human translation across 6 criteria (accuracy, text flow, terminology, grammar, completeness, cultural appropriateness) on the "Welcome to Canton Zürich" text — 12 total evaluations.

## Key findings & recommendations
- **Specialist models beat generic tools on terminology** — Textshuttle with 119–139 stored admin terms outperformed DeepL Pro on Italian admin texts (Italian DeepL rated negatively on terminology/cultural appropriateness).
- **Human translation is NOT consistently top** in blind tests — across English/French/Italian, automated tools matched or beat human; human only clearly won on Polish (complex language, less training data).
- **DeepL Pro excelled on English/French/Polish grammar and text flow**; struggled on Italian. Polish was particularly hard for Textshuttle.
- **Regularity is the key adoption signal** — commercial-register excerpts have structured, repeated terminology; ideal for fine-tuning. Free-form content (e.g. "Purpose" field describing a company's activity) saw the highest error rate.
- **Specific models drift on legislative change** — Neur.on's model needs retraining when underlying legal language updates.
- **Mandatory output labelling** — every machine-translated document must be marked "machine-generated translation" with a disclaimer that the source-language version is binding (e.g. "The German version is binding"). The Integration Unit's email template is a reusable artefact.
- **Swiss data residency matters** — Neur.on is ISO-27001 certified with documented Swiss dataflows; this is the differentiator from international cloud providers regardless of translation quality.
- **Use cases split into 3 tiers**: (1) Legally binding/certified — keep human translation; (2) standardised admin docs (commercial register excerpts, fact sheets) — specialised MT with human review; (3) informal correspondence/general info — MT acceptable with disclaimer.
- **Switching tools breaks workflow** — integration into the existing admin application is essential for adoption; standalone MT tools see employees revert to free online services.

## Legal & regulatory points
- **Federal Act on Data Protection (FADP)** and cantonal data protection laws — apply when administrative documents leave the internal server for translation.
- **Confidentiality classifications** — "confidential" and "secret" documents require either on-premise installation OR an ISO 27001 certified external solution with audited data flows.
- **Liability/reputation risk** — public bodies have an obligation to provide correct public information; MT errors without clear labelling create liability exposure.
- **Transparency duty** — users must be informed when text was MT-generated; binding source language must be stated.
- **Cantonal directives** often prohibit use of freely available online services (DeepL free, ChatGPT free) for internal documents; tool integration is the practical solution.
- The report does NOT cite specific article numbers — its legal framing is principles-based rather than article-specific.

## Data, models, infrastructure
- **Neur.on**: legal-tech start-up, ISO 27001 certified, Swiss cloud GPU infrastructure. Custom translation model fine-tuned on 20,000 commercial-register entries; DE→EN first, FR/IT planned. Output integrated as direct download from the Commercial Register website with per-document "machine-generated" label. Product name **CorreXT**.
- **Textshuttle**: University of Zürich spin-off, business solution with stored public-admin terminology (119–139 terms per language across EN/FR/IT/PL). Used in production by the Integration Unit for English/French/Spanish email correspondence.
- **Compared against**: DeepL Pro, Google Translate, ChatGPT (referenced but not benchmarked formally).
- **Methods named**: neural networks, transformer models, fine-tuning, LLMs (referenced as future direction).

## Stakeholders & partners
- **Neur.on** (Paula Reichenberg) — translation start-up specialised in law/tax/banking.
- **Textshuttle** (Mara Bertamini) — UZH spin-off, customised translation systems.
- **Commercial Register of Canton Schwyz** (Othmar Aeschi) — data partner for Neur.on case.
- **Integration Unit of Canton Zürich** (Nadia Sambuco) — deployment partner for Textshuttle case.
- **Office for Economy Canton Zürich** (sandbox lead).
- **ITSL University of Zürich** (Stephanie Volz, legal expertise).

## Cross-references
- [Phase II Medical Documentation] — same "AI on administrative free-text in a sensitive language context" pattern; medical context has stricter health-data rules but same data-residency, terminology-fine-tuning, and human-review themes.
- [Phase II Building Permits] — also Swiss-administration text processing; permits build on the "specialist model for narrow domain" lesson from commercial registers.
- [AI in Education] — shares the cantonal-directive vs federal-FADP framing, plus the "consent / legal basis is rarely the right route" finding.
- [Phase I overview Play & Learn] — example of bundling two parallel use cases for comparative insight, exemplifying the "sector-independent" approach.

## Why someone planning a new AI pilot would read this specifically
The only Phase I report with a side-by-side comparison of commercial AI tools (DeepL Pro vs Textshuttle vs human) across multiple languages — the benchmarking methodology, the criteria, and the per-language quirks (Polish ≠ Italian ≠ English) are directly reusable for any procurement decision. Also the most polyglot-relevant for any multilingual federation.

## Notable quotes
- "Machine translation must be used responsibly and with a differentiated approach." — Raphael von Thiessen (p. 7)
- "Machine translation can pose reputational and liability risks for public administration. A clear and transparent indication of the possibility of errors is thus an important requirement." — Stephanie Volz (p. 8)
