# P06 - Bootstrap the records

**Effort:** S · **Needs:** P03 and/or P04, P05 · **Opt out when:** never (core)

## Purpose
Create one stub record per issue/PR/commit so that every item exists as a file and progress can be counted.

## Steps
1. Make sure `project.json` names the repository and `data/issues-list.json` exists (P03) and the clone exists (P04).
2. Run: `python3 tools/pz.py bootstrap --corpus z1 --issues data/issues-list.json --clone ../<name>`.
   - Issues/PRs get `status: stub`, `depth: title`, state from the API (`closed/completed`, `pr-merged`, ...).
   - Commits get sequence ids from `git log --reverse`, file and line counts and the `#N` references found in the subject.
   - Default `--heuristics none`: tags stay empty. The option `--heuristics zapret` applies the first project's keyword rules (title patterns to `kind`/`cause`/`target` tags) and is only an example: those keywords and values belong to that project's taxonomy. Write your own rules only if titles are reliable enough to save time, and label them `tagged_by: heuristic` (the tool does).
3. `python3 tools/pz.py validate && python3 tools/pz.py status`. The totals must equal the list and clone counts.
4. Commit `records/` and `data/` ("bootstrap").

## Outputs
`records/issues/*.md`, `records/commits/*.md` (or the `records/z2/` equivalents for the secondary corpus).

## Verification (done when)
`status` shows `total` equal to the API list count (issues + PRs) and to the commit count; `validate` prints ok.

## PR-heavy trackers
In a project where most records are pull requests (69% in the trial), the outcome is in the record's `state` (`pr-merged`, `pr-closed`, `pr-open`, `closed/completed`, ...). Use `rulegen.py --with-state` so rules can match `[pr-merged]`, and keep `kind` for what the PR proposes (feature, fix, docs), not for whether it merged.

## Pitfalls
- Bootstrap is idempotent and never touches existing records. That makes "refresh" (goal G8) cheap: list again, bootstrap again, read only what is new.
- Heuristic tags are a head start, not knowledge: a record is only `analyzed` after a manual batch.

## Related
P07, P08, P17.
