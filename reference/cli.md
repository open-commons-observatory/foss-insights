# CLI reference (`tools/pz.py`, `tools/threads.py`)

Python 3 standard library only. Run from the repository root.

## threads.py (GitHub REST API; needs `GH_TOKEN` in the environment)
| Command | What it does |
|---|---|
| `threads.py list --corpus z1 [--out FILE]` | Writes every issue and PR of the corpus's repo to `data/issues-list.json` (`issues-list-z2.json` for z2): number, title, state, reason, dates, author, comment count, PR and merged flags, labels. |
| `threads.py fullfetch --corpus z1 N [N ...]` | Caches complete threads (body plus all comments, paged) in `.cache/full/N.json` (`.cache/full-z2/` for z2). Resumable; skips cached threads. About 150 threads fit one 300 s command. |
| `threads.py readfull --corpus z1 [--maint-only] [--min N] [--cap N] [--q N] [--users N] N ...` | Prints threads from the cache. `--maint-only`: only maintainer replies (`project.json` logins); `--min`: skip replies shorter than N characters; `--cap`: truncate long replies with `[..cut]`; `--q`: characters of the opening post; `--users`: characters of other participants' replies (0 = hide). |

## pz.py
| Command | What it does |
|---|---|
| `pz.py bootstrap --corpus z1\|z2 --issues FILE --clone PATH [--heuristics none\|zapret]` | Creates stub records for issues/PRs (from the list file) and commits (from `git log --reverse --numstat`). Idempotent. |
| `pz.py next [--kind issue\|commit] [--repo z1\|z2] [--status stub,triaged,read] [-n 30] [--after N] [--width 90]` | Lists the next records still to do (date, status, tags, title). |
| `pz.py show REF` | Prints one record. |
| `pz.py check BATCH` | Dry run: errors as `apply` would report, plus warnings (summary overwrite of an analysed record, facet values dropped, duplicate refs). Exit 1 on errors. |
| `pz.py apply BATCH [--name NAME]` | Validates the whole batch, then applies it and archives it under `batches/`. Exit 1 and nothing written on any error. |
| `pz.py validate` | Checks every record against the taxonomy and the ladders. |
| `pz.py status [--write]` | Counters per corpus and kind: status, depth, tagged_by, first not analysed. `--write` saves `STATE.json`. |
| `pz.py index` | Regenerates `indexes/` (by-class, by-facet, worklist, constraints, STATUS, stats, stats-z2). |
| `pz.py classes-build` | Builds `taxonomy/classes.json` from headings `## X3 - title` in `analysis/*.md`. |
| `pz.py backfill-docs` | Links records to classes and `cited_in` from citations in `analysis/*.md`. |
| `pz.py replay` | Re-applies every archived batch in order (rebuild proof, P21). |

## Exit codes that matter
`apply` and `check` return 1 on errors. Do not pipe them into `tail`/`head` if you need the status (use `set -o pipefail`).
