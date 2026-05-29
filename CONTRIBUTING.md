# Contributing to the Sandbox Knowledge Hub

Welcome. This guide is optimised for someone joining the team **cold** during the hackathon. Read top-to-bottom in <5 minutes.

---

## TL;DR

1. **Read** [`wiki/README.md`](wiki/README.md) (3 min) and [`wiki/CONVENTIONS.md`](wiki/CONVENTIONS.md) (5 min). They define the substrate.
2. **Browse** [`wiki/index.md`](wiki/index.md) to see what already exists.
3. **Pick** an open area (see end of `wiki/index.md` for current gaps).
4. **Branch** off `main` with a slug-style branch name (`add-lesson-procurement-trap`, `expand-concepts-edge-computing`).
5. **Write** the page following the conventions. Every claim has a `[[wikilink]]` or a citation.
6. **Open a PR.** The PR template will ask you to confirm citations + frontmatter + at least one wikilink.

If you're unsure where a page should live, **open an issue** with the "Propose a new concept/tag" template — better to discuss it than to commit a misplaced page that has to be moved later.

---

## The three things you can do most often

### 1. Add a new source

A new source can be a PDF, a URL, a paper, a video, a transcript, a podcast, or just a personal note. They're all first-class.

**For a file** (PDF, paper, transcript):
- Drop the file into `wiki/pdfs/<lang>/` (or another sensible folder).
- Create `wiki/sources/<slug>.md` matching the [source schema](wiki/CONVENTIONS.md#sources--citation-backbone). Required: `type: source`, `source_type:`, `path:`, `language:`, `year:`.
- For PDFs that the team wants to cite paragraph-level, leave `paragraphs: []` — the future ingest pipeline will populate it.

**For a URL** (article, blog, official policy document):
- Don't download. Use `url:` instead of `path:`.
- Cite with anchor fragments where available (e.g. `https://example.gov/policy#section-3`).

**For non-Canton-Zurich sources** (academic papers, EU policy, news articles):
- These are first-class. The wiki is not limited to the original 13 PDFs.
- Use `source_type: paper | url` and set `publisher:` accurately so the citation surface looks credible.

### 2. Add a lesson

A *lesson* is the highest-leverage page type. It's an **atomic, transferable claim** — something a person planning a new pilot can actually use.

A good lesson:
- States the claim in the title (declarative, ~10 words). Example: "Rule-based systems outperform generative AI when decision logic is well-defined."
- Has at least one source citation with paragraph anchor.
- Links to ≥2 projects via `project[]` (lessons that only apply to one project are usually not transferable enough).
- Tags `concept[]`, `regulation[]`, `stakeholder[]` so the future generator can filter on them.
- Sets `confidence: high | medium | low` honestly. `low` is fine and useful — it tells future readers the claim needs more evidence.
- Includes a "How to apply" section so the lesson is *actionable*, not just descriptive.

See [`wiki/lessons/rule-based-beats-generative-for-defined-logic.md`](wiki/lessons/rule-based-beats-generative-for-defined-logic.md) as a working example.

### 3. Add or expand a concept

A *concept* is a reusable idea or term. Some come from the official booklet glossary (use `canonical_source:` to point at the booklet paragraph — these are authoritative). Others are derived from reading the corpus as a whole (`canonical_source: null` is fine).

Before adding, **search for existing concepts**:

```bash
ls wiki/concepts/
grep -ri "your term" wiki/
```

If you find a similar concept, consider extending it rather than creating a new one.

---

## Conventions you might miss

1. **English body, German verbatim quotes.** Wiki prose is English (Bowen and most teammates don't read German). When you quote a German report, quote it *verbatim* in italics inside `«…»` guillemets — and translate in the surrounding English sentence. Never machine-translate a source quote.
2. **Wikilinks are by slug, not folder.** `[[building-permits]]` resolves uniquely across the whole `wiki/`. Slugs must be unique across all seven folders.
3. **Citations cite paragraphs, not pages.** Format: `<source-slug>#para-N`. Page-level (`#page-12`) is a fallback when paragraph anchors slip.
4. **Frontmatter is open.** If you need a new field, just add it. If 3 other pages add the same field, codify it in `wiki/CONVENTIONS.md` §2.
5. **`[!tension]` callouts are valuable**, not bad. When two sources disagree, surface the disagreement explicitly — it's load-bearing for the credibility of the wiki overall.

---

## Workflow

### Branch + PR

```bash
git checkout -b add-concept-edge-computing
# … edits …
git add wiki/concepts/edge-computing.md
git commit -m "Add edge-computing concept page"
git push -u origin add-concept-edge-computing
# Open a PR via gh pr create or the GitHub web UI
```

PR titles use the shape: `<verb> <type> <slug>` — e.g. `Add lesson rule-based-beats-generative`, `Expand stakeholder anybotics`, `Fix broken wikilinks in concepts/data-access`.

### Reviews

Reviewers should check:

- [ ] Frontmatter `type:` matches the folder.
- [ ] At least one citation with `<source>#para-N` or `<source>#page-N`.
- [ ] At least one `[[wikilink]]` to another wiki page.
- [ ] No broken wikilinks (referenced slugs exist).
- [ ] If the page introduces a new frontmatter field, the PR description names it.
- [ ] If the page introduces a new taxonomy value (e.g. a new `sector`), the PR description names it and a `[follow-up: codify in CONVENTIONS]` task is added.

### Commits

Small, atomic, descriptive. Body of the commit should explain *why*, not *what* (the diff shows the what).

---

## Stuck?

- Wrong type? Open an issue with the "Propose a new concept/tag" template.
- Missing source? Open an issue with the "Add a source" template.
- Schema feels wrong? Update `wiki/CONVENTIONS.md` in the same PR as your content edit. Conventions evolve.

When in doubt, write the page first and we'll figure out where it lives in review. Better to have content than to wait for taxonomy clarity.
