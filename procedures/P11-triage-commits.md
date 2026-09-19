# P11 - Triage commits (subject and file level)

**Effort:** L · **Needs:** P06, P07 · **Opt out when:** issues-only goal

## Purpose
Tag every commit from its subject, touched files and size, in date order, so change history can be grouped and counted. This is a `depth: title` reading: honest but shallow.

## Steps
1. Skip what P07 already tagged.
2. In date order, in rounds of 30-40: `python3 tools/pz.py next --kind commit -n 40` (shows date, subject and heuristic tags). For an unclear subject open the file list: `git -C ../<clone> show --stat --format=%s <hash> | head -30`.
3. Tag each commit: `ctype`, `engine` (from touched paths), `layer`, `cause` when the subject states one, `proto`/`os` when named, `constraint` when the change adds a check or restriction, plus `classes` when it belongs to a known problem class. Link the commit to an issue through `refs` (bootstrap collected `#N` from subjects).
4. Write one line per commit or per group with the same tags; one sentence summary in your own words that says *what changed and why, if the subject says why*.
5. Record uncertainty: if the subject is vague, tag what is observable (files, size) and use `conf:inferred` or leave `cause:unknown`. Do not upgrade a guess to a fact.
6. Apply, validate, commit (P08).

## Outputs
Commit records at `analyzed`, `depth: title`.

## Verification (done when)
Every commit is `analyzed`; the noise ratio (docs, merges, typos) is known; the statistics table by `ctype` and `engine` (P16) looks plausible against the project's history.

## Pitfalls
- Subject lines lie ("fix", "cleanup"): do not assign root causes from a subject alone; P12 exists for that.
- Large commits (initial import, vendored code, generated files) distort counts: tag them `ctype:maintenance` and note the size.
- Version bumps and release commits carry the changelog; the changelog is a better source than the diff for what shipped.

## Related
P07, P12, P16.
