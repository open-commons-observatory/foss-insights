# P07 - Rule-tag mechanical commits

**Effort:** S · **Needs:** P06 · **Opt out when:** issues-only goal, or you want every commit read

## Purpose
In the first run 553 of 1,330 commits (and 301 of 974 earlier) were merges or documentation-only. Reading them adds nothing; tagging them by an explicit rule saves time and stays auditable.

## Rules that were safe
- **Merge commits:** subject starts with `Merge `: `ctype:maintenance`.
- **Documentation-only:** every touched path is under `docs/` or ends in `.md`, and the subject does not describe a fix: `ctype:docs layer:docs engine:docs`.
Both rules are stated in one sentence. If a rule needs two sentences, it is a judgement: do not automate it.

## Steps
1. Write a small script (or use the pattern below) that finds commits matching a rule and writes a **batch file** whose header comments state the rule.
2. Sample 20 matches by hand across the date range; if any is wrong, tighten the rule.
3. `python3 tools/pz.py check batches/NNNN-rules.tsv && python3 tools/pz.py apply batches/NNNN-rules.tsv`.
4. Commit the batch file. It is the audit trail: the rule is in the file, the matches are its lines.

```python
import sys; sys.path.insert(0, 'tools'); import pz
docs, merges = [], []
for kind, path in pz.all_records('commit'):
    fm, summary, notes = pz.parse(path)
    if fm['title'].startswith('Merge '): merges.append(fm['hash']); continue
    # heuristic ctype must be docs AND no engine other than docs:
    eng = {t.split(':')[1] for t in fm['tags'] if t.startswith('engine:')}
    if 'ctype:docs' in fm['tags'] and eng <= {'docs'} and 'ctype:fix' not in fm['tags']: docs.append(fm['hash'])
# then write lines: "c<hash>,c<hash>,... | - | ctype:docs layer:docs engine:docs | Documentation-only change."  (12 refs per line)
```
(The snippet relies on heuristic tags. With `--heuristics none` derive "docs-only" from the file list instead: re-run `git show --name-only` per commit or extend bootstrap to store the file list.)

## Outputs
One batch file per rule; records at `status: analyzed`, `depth: title`, `tagged_by: manual`.

## Verification (done when)
`pz.py status` shows the expected number analysed; sampled records are truly mechanical.

## Pitfalls
- A "docs-only" commit can carry a behaviour change described only in docs (a new option documented first). If the goal depends on design history (G5), leave docs commits for a skim instead.
- Do not extend a rule to "small commits" or "typo" subjects: subject text lies.

## Related
P11, P18.
