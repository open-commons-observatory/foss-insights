# P25 - Review and stress-test the finished dataset

**Effort:** S (the tool) + M (reading its findings) · **Needs:** P08 · **Opt out when:** the dataset is a throw-away exploration

## Purpose
Before anyone relies on the dataset (or on findings drawn from it), find out where it is thin, stale, one-sided or duplicated. The first run did this by hand-written scripts at the end and it changed the plan; this procedure makes it a tool (`review.py`) plus a reading checklist. Run it once when the main reading is done, again after big structural changes, and before publishing conclusions.

## Steps
1. **Run the tool:** `python3 tools/review.py --maintainers <login,login> --clone1 ../<repo1> [--clone2 ../<repo2>]`. It writes `indexes/review.md` (generated; never edit) with an **ATTENTION list** at the top and these sections: coverage and depth, facet population, class coverage and redundancy with a facet, citation coverage, time concentration, confidence and outcomes, corrections, uncited constraint records, duplicated summaries, maintainer behaviour (from the thread caches) and authorship concentration (from the clones).
2. **Decide per ATTENTION item** one of: *fix* (do the missing work), *accept and state* (write it into the limits statement, P22), or *not applicable* (add the facet to `--sparse-ok`). Do not leave an item undecided.
3. **Read what the tool cannot check** (about an hour):
   - re-open five records of each kind against their threads (P18);
   - grep the analysis documents for claims that later evidence contradicts (retractions, successor status, corrected mechanisms);
   - look at the three biggest classes and the three smallest: are the small ones thin because they are rare or because nobody read for them?
4. **Judge the structure.** Ask: which questions can the dataset answer (mechanism, symptom, decision, time), and which lens has no facet? Missing lenses become new facets or registry views (P05, P24).
5. **Rank the possible uses** by value, feasibility and strength of evidence, and write them into the session entry (P20). The first run's list (rule catalogue, preflight checklist, support decision tree, probe test suite, regression corpus, design-boundary catalogue, event log) is a starting point.
6. **Record the review** in the session entry: the ATTENTION list, what was decided, and the follow-ups done.

## What the metrics mean (calibration from the first run)
| ATTENTION | first run | What it told us / what was done |
|---|---|---|
| commits at title depth | 94% / 98% | expected; stated in every summary; 82 constraint-related diffs read (P12) |
| a facet on under 15% of records | `auto` 3%, commit `os`/`impact` ~0-9% | `auto` moved to the registry entry (P24); the rest accepted |
| class letters predictable from `layer` | 83% | top-level letters duplicate a facet; the numbered classes carry the information |
| classes with fewer than three records | A2, D1, D3, D4 | adversary-behaviour entries rest on documentation and source, not threads; said so |
| one half-year holds a third or more of issues | 2024H2 = 49% | one episode dominates every "typical" statistic; stated |
| most records rest on a maintainer statement | 81% `stated` | single-source knowledge, never tested by experiment; stated |
| issues without a visible resolution | 23% | mostly unanswered threads and PRs |
| threads never answered by the maintainer | 29% / 33% | support burden is not fully served; useful for triage design |
| one person wrote most commits | 94% / 99% | the corpus is one expert's model; bus factor 1 |
| records share their summary opening | 75% | group-tagged lines give many records the same text: summaries are group-level evidence |
| uncited constraint records | 72% before the rule catalogue, 31% after | write the deduplicated rules (P14) |

## Outputs
`indexes/review.md`, a decision per ATTENTION item, the ranked uses.

## Verification (done when)
Every ATTENTION item has a decision recorded; the limits statement (P22) mentions each accepted one.

## Pitfalls
- Treating the thresholds as truth: they are heuristics; a sparse facet may be sparse by design.
- Reviewing only the numbers: the contradiction check against documents needs a reader.
- Skipping the maintainer-behaviour section because it needs the thread caches: keep `.cache/` until the review is done.

## Related
P16, P18, P20, P22, P24.
