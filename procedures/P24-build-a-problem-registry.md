# P24 - Build a problem registry

**Effort:** M · **Needs:** P08 (and P15 if narrative documents already exist) · **Opt out when:** the dataset alone, or a handful of free-form documents, is enough

## Purpose
Records answer "what happened in issue 1836". A **problem registry** answers "what recurring problems does this project have, what do we know about each, and where is the evidence". One entry per problem; hand-written narrative (findings, proposals) kept apart; **evidence, status in a successor, symptoms and counts generated from the records**; the analysis documents become generated views. This is the layer that keeps prose, tags and records coherent.

## Design (what the first run ended with)
```
taxonomy/classes.json          problem ids = class ids (60: M1..M9, S1..S9, D1..D8, A1..A4, P1..P8, R1..R5, L1..L8, U1..U4, O1..O5)
records[].classes              cited by hand (human)             records[].classes_inferred   suggested by a model (never mixed)
registry/source/problems.json  hand-written text per problem: findings, proposals, first-pass evidence note
registry/source/links.json     problem -> rule ids
registry/<ID>.md               GENERATED page: text + evidence table + counts by depth, status, symptom, outcome
registry/README.md, by-symptom.md   GENERATED index (with a rules-to-problems table and a thin-evidence list) and the symptom view
analysis/NN-*.md               GENERATED document views (findings, proposals kept apart, generated evidence per problem)
```
Never edit generated files: edit `registry/source/` and run `python3 tools/registry.py generate`.

## Steps
1. **Decide the problems.** Use the headings of your analysis documents (P15) or cluster tags; keep ids stable (`X<number>`), titles short. Ids are the class ids in `classes.json`.
2. **Freeze class links as data before touching any document.** If classes came from parsing documents (`backfill-docs`), write them into a batch (`refs | C1,C2 | |`) first; otherwise regenerating the documents silently changes the rebuild. Then `backfill-docs` only links `cited_in`.
3. **Migrate the narrative** into `registry/source/problems.json`. If your documents use `## X1 - title` entries with bullets, `registry.py import-docs` does it once: it separates proposals (bullets that start with Auto-catch, Auto-handle, notes for a consumer) from findings, strips outdated evidence tags for issues, keeps the first-pass evidence note, and copies the originals to `analysis/first-pass/`. **Verify** the migration: compare the word multiset of every entry with the original (snippet below); the first run matched all 60 entries exactly.
4. **Assign classes to the rest with provenance.** Train a naive-Bayes model on the tags of the human-classified records; measure **leave-one-out** precision by posterior threshold; add eligibility rules (skip noise, docs-only and maintenance commits, records without a cause or layer tag); **spot-check 15-20 predictions by hand** in any corpus the model has not seen. Apply with `~C` in the class column (stored in `classes_inferred`). First run: 81% (issues) and 89% (commits) leave-one-out at posterior 0.7, about 70% in the manual spot check on the second corpus.
5. **Add a symptom facet** (what the reporter saw, separate from the mechanism) with `textrules.py`: multi-label keyword rules over the title and the first 240 characters of the summary. **Measure precision on a random sample before applying** (first run: 60-65%, then tightened) and write the estimate into the batch header. Treat as a search aid, not a measurement.
6. **Link rules** (`links.json`), run `registry.py generate`, read the **thin-evidence list** (problems with fewer than three hand-cited records) and the by-symptom view. Thin entries rest on little data, or on documentation/source instead of tracker threads: say which.
7. **Documents are now views.** Edit the source text, regenerate, commit source and output together.
8. **Prove the rebuild** (P21): bootstrap, `classes-build`, `backfill-docs`, replay must reproduce every record.

```python
# word-multiset check of a migration (per entry)
import collections, re
o = collections.Counter(clean(original_body).split())
g = collections.Counter(' '.join(p['findings'] + p['proposals'] + p['first_pass_evidence']).split())
assert o == g
```

## Automation field
Each entry gets `automation` computed from its proposals (`detect+handle`, `detect-only`, `handle-only`, `none`). It is a property of the *proposal*, not of the evidence: do not copy it onto records (the first run's per-record `auto` facet stayed on 30 records for that reason).

## Outputs
`registry/` (pages, index, by-symptom), regenerated documents, classes as data (human and inferred), symptom tags, links to rules.

## Verification (done when)
Every problem has a page; the word-multiset check passes; `pz.py validate` is ok; the rebuild proof shows zero differing records; the thin-evidence list is read and acted on or explained.

## Pitfalls
- Regenerating documents that were the only home of a data relationship breaks the rebuild (pitfall 47).
- A generator that omits a block (the first version dropped the evidence notes from the document views) is found by the rebuild diff (pitfall 48).
- Inferred classes look like evidence once mixed with human ones: keep a separate field and show them apart (pitfall 51).
- Leave-one-out accuracy is optimistic when the training set is the problem-rich subset (pitfall 50).

## Related
P05, P08, P14, P15, P21.
