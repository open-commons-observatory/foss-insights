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

## Pattern-rule batches (the fast way, once the subjects are readable)
When commit subjects are regular (a project that writes `component: what`), do not type hashes. Read a slice with `pz.py next --kind commit -n 120`, then write a **rules file** and let `tools/rulegen.py` build the batch:
```python
# rules_0073.py: first match wins, specific rules first
R = [
  (r'AI (inspired )?fix',        'ctype:fix layer:parser engine:main',        'Small fixes prompted by AI-assisted review (the subject names no specific change).'),
  (r'timer|lua-gc',              'ctype:feature layer:parser engine:main',     'A timer API with fixes; the --lua-gc default was corrected from 60 ms to 60 s.'),
  (r'pie experiment|dynamicbase','ctype:build layer:dist os:windows',          'Hardening of built binaries: PIE, ASLR, dynamic base.'),
]
```
```
python3 tools/rulegen.py rules_0073.py --corpus z2 --n 120 --out batches/0073-commits-jan-2026.tsv --header "commits 366..475, Jan 2026"
python3 tools/pz.py check batches/0073-commits-jan-2026.tsv && python3 tools/pz.py apply batches/0073-commits-jan-2026.tsv && python3 tools/pz.py validate
```
- The tool prints every commit no rule matched (`UNMATCHED`): add a rule or write those lines by hand.
- The rules are copied into the batch header as comments: the archive shows how each tag was assigned.
- Run `check && apply && validate` **without pipes** (P08).
- Order matters: put narrow rules (a specific fix you know from an issue) before broad ones (`optimize|cleanup`), and finish with a broad `maintenance` rule so nothing is silently left out.
- Sample 10 records per rule set against their subjects. Rules assign tags from subjects only, so the batch stays `depth: title`.
- In the first run, hand-typed hash lists produced a typo in nearly every second batch (`dc0fe0f` for `dc0fe70`, `cb85262a` for `cb85f6e`); generated batches produced none.

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
