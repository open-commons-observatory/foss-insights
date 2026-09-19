# P16 - Generate indexes and statistics

**Effort:** S · **Needs:** P08 · **Opt out when:** never (one command)

## Purpose
Turn the records into counts and lists you can read: progress, distribution by every facet, the work queue.

## Commands
```
python3 tools/pz.py index              # indexes/: by-class.md, by-facet.md, worklist.md, constraints.md, STATUS.md, stats.md (+ stats-z2.md)
python3 tools/pz.py status             # counters per corpus and kind; depth and tagged_by breakdown
python3 tools/pz.py status --write     # also writes STATE.json (the snapshot the README quotes)
```
Generated files are never edited by hand and are safe to delete and regenerate. Run them at the end of a session, before the commit that closes it.

## Using the data (queries)
Every record is a markdown file with JSON-valued frontmatter, so plain tools work:
- Count by tag: `grep -l '"cause:byte-cutoff"' records/issues/*.md | wc -l`.
- Python: `import pz; for kind, path in pz.all_records('issue'): fm, summary, notes = pz.parse(path)` then filter `fm['tags']`, `fm['classes']`, `fm['depth']`, `fm['date']`.
- Cross-tabulate two facets (for example `kind` by year, `cause` by `outcome`) in a few lines; the built-in `stats.md` already gives per-facet counts and issues by year and kind.

## Outputs
`indexes/*`, `STATE.json`.

## Verification (done when)
Totals equal the number of records; the analysed count equals what your batches applied.

## Pitfalls
- Multi-valued facets sum to more than the record count.
- Statistics over a sample of failing users describe *reports*, not usage; say so when you quote a ratio.
- Heuristic-tagged records are excluded from statistics by design (only manual tags count).

## Related
P08, P22.
