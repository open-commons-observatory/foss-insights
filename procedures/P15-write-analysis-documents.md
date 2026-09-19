# P15 - Write analysis documents by class

**Effort:** M · **Needs:** P08 · **Opt out when:** the dataset alone is the deliverable

## Purpose
Turn tagged records into narrative that someone can read: what goes wrong, why, and what follows. The documents are the human interface to the dataset; the records stay the evidence.

## Structure that worked
```
analysis/00-method-and-coverage.md   what was read, how, limits, claims to re-verify
analysis/01-timeline.md              dated events and design turns
analysis/10-...md  20-...md  ...     one document per problem area, sections per class
analysis/90-...md                    synthesis (for example a detector/handler matrix)
analysis/<topic>-vs-<target>.md      comparison documents (P13)
```
Inside a document each class is a heading `## X3 - short title`. The class id (a letter for the area, a number for the problem) is what `classes.json` and the records link to.

## Steps
1. After a few hundred analysed records, group them by tag combinations (`pz.py index` writes `by-facet.md`); write one section per recurring problem.
2. In each section cite records as `#1836 [R]` (issues; `R` = read in full, `T` = title/brief) and commits as backticked 7-character hashes (`` `c187aff` ``). The tool links cited records back to the class.
3. State the claim, the mechanism and the confidence; keep quotes out (P09).
4. Run `python3 tools/pz.py classes-build` (headings become `taxonomy/classes.json`) and `python3 tools/pz.py backfill-docs` (records receive class ids and `cited_in`).
5. Write `00-method-and-coverage.md` last: depth counts (computed), truncation, what was not read, the list of claims that should be re-verified.
6. When a record is corrected, correct every document that cites it (P18).

## Once a registry exists (P24)
The documents stop being hand-maintained: they become generated views of the registry, so evidence tags cannot rot and findings stay separate from proposals. Write them by hand only until P24, then migrate them once (`registry.py import-docs`).

## Outputs
Documents, `classes.json`, records linked to classes.

## Verification (done when)
Every class has at least one supporting record; every cited record exists; the coverage document's numbers match `pz.py status`.

## Pitfalls
- Documents written from memory drift from the records; write from the index and re-open the records you cite.
- A retraction in a record with the claim still standing in a document is worse than no retraction (P18).

## Related
P16, P18, P22.
