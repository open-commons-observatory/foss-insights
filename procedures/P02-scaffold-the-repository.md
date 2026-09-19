# P02 - Scaffold the analysis repository

**Effort:** S · **Needs:** P01 · **Opt out when:** you continue an existing analysis repo

## Purpose
Start from a tested skeleton so tooling is not re-invented per project.

## Steps
1. Copy [`reference-implementation/`](../reference-implementation/) into a new directory; that directory becomes the analysis repo.
2. Edit `project.json`: `owner`, `primary` (repo name), `secondary` (optional successor/fork), `maintainers` (logins whose replies count as maintainer statements).
3. `git init -b main`, create a private repository under your organisation (`POST /orgs/<org>/repos` with `{"name": "...", "private": true}`), add the remote, first commit.
4. Confirm the layout below and the CI workflow (`.github/workflows/validate.yml`).
5. Copy `templates/plan.md` to `PLAN.md` and tick your procedures.

## Layout (what each path is for)
```
records/issues/NNNN.md            one file per issue (primary corpus)
records/commits/SEQ-hash.md       one file per commit
records/z2/issues|commits/        the secondary corpus (P17)
taxonomy/facets.json              controlled vocabulary (P05)
taxonomy/classes.json             problem classes linked to analysis docs
batches/NNNN-name.tsv             every manual tagging pass; replayable (P21)
analysis/                         narrative documents by class (P15)
indexes/                          GENERATED: by-class, by-facet, worklist, constraints, STATUS, stats
brainstorms/                      dated session entries (P20)
data/                             API lists (issues-list*.json)
tools/pz.py  tools/threads.py     the CLI and the API thread tool
project.json  STATE.json  LOG.md
```

## Outputs
A committed skeleton that passes `python3 tools/pz.py validate` (zero records is valid).

## Verification (done when)
`python3 tools/pz.py status` runs; CI passes on the first push.

## Pitfalls
- Two corpora are supported (primary at `records/`, secondary at `records/z2/`). More than two needs a change to `REPOS` and `rec_dir` in `pz.py`.
- Keep the thread cache (`.cache/`) out of git; it is large and derived.

## Related
[`reference/cli.md`](../reference/cli.md), P19.
