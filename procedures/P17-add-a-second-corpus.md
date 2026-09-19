# P17 - Add a second corpus (successor, fork, sibling)

**Effort:** M · **Needs:** P08 · **Opt out when:** one project only

## Purpose
Analyse a related project with the same structure and vocabulary in the same repository, so findings can be compared and cross-referenced.

## Steps
1. In `project.json` set `secondary` to the other repository name.
2. `python3 tools/threads.py list --corpus z2` (writes `data/issues-list-z2.json`), then `fullfetch --corpus z2 <numbers>` (P03); clone the repository (P04).
3. `python3 tools/pz.py bootstrap --corpus z2 --issues data/issues-list-z2.json --clone ../<name2>`. Records go to `records/z2/issues|commits`, with `repo: z2` in the frontmatter.
4. Extend the taxonomy with the new project's components and any successor-specific values (`engine` values for its programs, for instance). Keep every existing value; do not fork the vocabulary.
5. Refs in batches carry a prefix: `z2i75`, `z2c1a2b3c`. Issue numbers collide across corpora, so never omit it. `pz.py next --repo z2`, `pz.py status` and `index` are per corpus.
6. Do the mechanical commits by rule (P07) first, then issues (small corpora fit `full` from the start), then commits (P11).
7. Update the repository README (section "Corpora") and the coverage document.

## Outputs
A second set of records, `indexes/stats-z2.md`, status per corpus.

## Verification (done when)
`pz.py status` lists both corpora with totals equal to their lists; a batch mixing `i…` and `z2i…` refs applies.

## Pitfalls
- Pull requests are records too in the second corpus (the first run's list contained 38 PRs among 115 items); their state comes from the merged flag.
- More than two corpora needs code changes (`REPOS`, `rec_dir` in `pz.py`).
- The successor's own issue tracker may be small because the maintainer deletes off-topic threads; numbering gaps are normal.

## Related
P03, P04, P06, P13.
