# Success Criteria — Sandbox Knowledge Hub

> Light-touch requirements checklist derived from [`challenge/brief.md`](challenge/brief.md). Designed to be **re-scored at midday Thursday and again Friday morning** so it drives prioritization, not decoration. Companion to [`README.md`](README.md), [`architecture-route.md`](architecture-route.md), [`frontend-route.md`](frontend-route.md), [`team-handout.md`](team-handout.md).

---

## How to use

- **Status legend**: `✓` done · `◐` partial · `☐` planned, not started · `✗` punted (with reasoning)
- **Hard constraints** are non-negotiable for a credible submission. If any sit at `☐` Friday midday, escalate to the team.
- **Bonus items** improve jury score but aren't make-or-break.
- **User-impact items** are what the brief says should be true *after* the system exists. They're how we know we built the right thing, not just the thing we said we'd build.
- **Differentiators** are our chosen risk-budget. If they slip, scope down — don't fake them.

---

## Hard constraints (from brief §3 + §Einschränkungen)

| # | Criterion | Source quote | Our approach | Status |
|---|---|---|---|---|
| H1 | **Non-technical audience** | *"Die Lösung soll für nicht-technische Nutzerinnen und Nutzer verständlich sein."* | Wikipedia-shaped UI; generator outputs plain-language briefing with concrete next-step artifacts (checklists, stakeholder chips) — no graph viz for its own sake, no chat-only fallback. | ☐ |
| H2 | **Traceability — every claim → source paragraph** | *"Die Inhalte müssen nachvollziehbar bleiben; Aussagen sollten auf konkrete Berichtsinhalte zurückgeführt werden können."* | Frontmatter `sources:` field on every wiki page with `#para-N` anchors; PDF slideover renders the cited paragraph highlighted. Components reject empty `sources` structurally. | ☐ |
| H3 | **No unsupported claims (anti-hallucination)** | *"Die Lösung soll sich eng an den tatsächlich vorhandenen Informationen orientieren und keine unbelegten Aussagen erzeugen."* | Generator components take wiki slugs as props, not raw prose — the LLM picks WHICH components to render and WHICH pages they reference; content comes from disk, not generation. | ☐ |
| H4 | **Sensitive / legal info handled with care** | *"Der Umgang mit sensiblen Informationen und potenziell rechtlich relevanten Aussagen erfordert Sorgfalt."* | Prose hedges naturally ("according to Report X…"); explicit "not legal advice" disclaimer in footer + at top of generator output; book the **Fri 10:00 BK legal Q&A slot**. | ☐ |
| H5 | **Currency — flag stale, easy to update** | *"Eine weitere Herausforderung ist auch die Aktualität der Inhalte … muss sichergestellt werden, dass die Informationen korrekt (d.h. nicht veraltet) sind und … es relativ einfach möglich sein, Informationen zu aktualisieren."* | `freshness:` field per wiki page; "as-of YYYY-MM" badge on every card; pre-2024 content gets a soft-warning chip ("Regulation may have evolved — check current"); Admin re-ingest flow is the live demo of "easy to update." | ☐ |
| H6 | **Practical utility > technical complexity** | *"Der Fokus liegt auf praktischem Nutzen und nicht auf technischer Komplexität um ihrer selbst willen."* | Generator artifact is a concrete checklist + stakeholders list + regulations list — things a civil servant copies into their internal memo. No technique demos disconnected from user value. | ☐ |

## Bonus items the brief explicitly named

| # | Criterion | Source quote | Our approach | Status |
|---|---|---|---|---|
| B1 | **Embeddability on the AI Innovation Sandbox website** | *"Falls möglich und im zeitlichen Rahmen ist eine mögliche Einbettung auf der Webseite der AI Innovation Sandbox zu berücksichtigen."* | Wiki Reader uses Next.js `output: 'export'`; `?embed=1` chrome-stripping mode; verify exact CMS integration requirements with Lukas Thu 09:30. | ☐ |
| B2 | **Sustainability — continuable post-hackathon** | *"Der Hackathon soll … konkrete Ansätze sichtbar machen, die das Potenzial haben, nach dem Anlass weiterverfolgt, vertieft oder in angepasster Form übernommen zu werden."* | Markdown wiki = trivially handed off (any editor); `CLAUDE.md` documents schema and conventions; ingest scripts open-source; no proprietary infra; clear "what we punted and why" notes in route docs. | ☐ |
| B3 | **Short-video integration** *(brief mentions per-report videos exist)* | *"Was bereits verfolgt wird: Zur Unterstützung der Wissensvermittlung wurden auch Kurzvideos für jeden Bericht erstellt."* | `<VideoSummary slug="…" />` component in the registry. If videos are available (asking Lukas), real embed; if not, polished placeholder showing the integration intent. | ☐ |

## Expected user impact (brief §Erwarteter Nutzen)

These are the user-facing wins the brief says should be true after the system exists. They're the "did we build the right thing?" check, separate from "did we build the thing right?".

| # | Outcome | Source quote | Demonstrated by | Status |
|---|---|---|---|---|
| U1 | Findings easier to find | *"Erkenntnisse aus früheren Projekten werden leichter auffindbar"* | Faceted left-rail nav + Pagefind search + generator's similar-pilots section | ☐ |
| U2 | Recurring challenges identified earlier | *"wiederkehrende Herausforderungen werden früher erkannt"* | Cross-pilot pattern surfacing on every project page; `⚠ Tension` callouts where reports contradict | ☐ |
| U3 | Legal/organisational questions raised earlier | *"wichtige rechtliche, organisatorische und technische Fragen können früher berücksichtigt werden"* | Generator's "Regulations" and "Stakeholders" sections; "Open questions" footer in canvas | ☐ |
| U4 | New projects better prepared | *"neue KI-Projekte können fundierter vorbereitet werden"* | The Readiness Checklist artifact — concrete next steps drawn from prior pilot lessons | ☐ |
| U5 | Sandbox knowledge has impact beyond individual reports | *"das in der Sandbox aufgebaute Wissen entfaltet mehr Wirkung über einzelne Projekte hinaus"* | Backlinks + cross-references + atomic `wiki/lessons/` pages that transcend any single project | ☐ |

## Self-imposed differentiators (our risk-budget)

Not in the brief — choices we make to elevate the submission beyond baseline expectations.

| # | Item | Why | Status |
|---|---|---|---|
| D1 | Three "moments" land cleanly in the demo | Streaming canvas + PDF slideover + live re-ingest — the three things the jury will remember | ☐ |
| D2 | Pick 2 from `frontend-route.md` exploration menu | Current vote: contradiction surface (`[!tension]`) + Admin diff view | ☐ |
| D3 | English-dev / German-content / bilingual-shipped is named openly | Honest framing of language choice = trust signal, not weakness | ☐ |

## Risk register

| Risk | Mitigation | Owner |
|---|---|---|
| Generator hallucinates a claim | Components only render from wiki slugs; no free-text prose generation in canvas. Lint catches empty `sources`. | All |
| PDF chunking loses paragraph-anchor stability across re-ingests | Lock chunker version; deterministic chunking; checksum on `#para-N` resolution. | TBD |
| Admin live re-ingest crashes on stage | Pre-record a fallback video of the flow; smoke-test 30 min before pitch. | TBD |
| German source content + English UI feels off in demo | Name it as the design intent ("citation in source language is the point — we don't pretend translation is the citation"). | Narrator |
| Demo machine offline / WiFi flaky | Pre-cache `localhost` deployment + run from laptop; no cloud-only dependencies. | TBD |
| Two surfaces are great, third one is broken | Scope-cut Admin to pre-recorded video by Thu end-of-day if not stable. | All |

## What we are explicitly NOT promising

(Quoted from brief §"Nicht im Fokus stehen" — making these explicit in the pitch deflects scope creep questions from the jury.)

- Production-ready system
- Full new data collection
- Complete legal review of all content
- Access to arbitrary additional government data beyond bundled material
- Machine translation of report content into English (source German is preserved as authoritative)

## Review cadence

- [ ] **Thu midday (~13:00)** — re-score every row above. Anything still `☐` that's a hard constraint → escalate.
- [ ] **Thu end-of-day (~18:00)** — scope decision: cut/keep Admin? Confirm Day 2 plan with team.
- [ ] **Fri midday (~12:00)** — final differentiator pick lock-in. No new features after this.
- [ ] **Fri 14:00** — full demo path rehearsal, fallback video recorded.
- [ ] **Fri 16:00** — pitch.

---

## Notes log

| Date | Note |
|---|---|
| 2026-05-27 | Initial doc. All items at `☐`. Highest-risk hard constraint: H2 (PDF paragraph-anchoring) — needs day 1 spike. Highest-leverage bonus: B1 (embeddability) — confirm CMS requirements with Lukas Thu 09:30 before committing render mode. |
