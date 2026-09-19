# P09 - Read issues at depth

**Effort:** L · **Needs:** P03, P08 · **Opt out when:** commits-only goal

## Purpose
Turn each thread into a tagged record whose summary says what happened and who said it, at a depth you can state honestly.

## The depth ladder
| depth | Meaning | Use for |
|---|---|---|
| `title` | only the title (bootstrap) | items you deliberately skip |
| `thread` | opening post plus the first maintainer replies (truncated) | landscape goals (G1); noise; items with no maintainer reply |
| `full` | the whole thread read from the complete API comment list | the default for an exhaustive dataset |
| `source` | additionally checked against code, docs or a newer version | rules you will rely on (P13, P14) |

With the API there is no reason to start at `thread` for a project with a few hundred threads: read at `full` from the beginning. Use `thread` only when the volume forces it, and then run P10.

## Steps (one round, 6-12 threads)
1. Read: `python3 tools/threads.py readfull --corpus z1 --maint-only --min 60 --cap 700 N ...`
   - `--maint-only` prints only maintainer replies (login list in `project.json`); drop it when the reporter's post matters, and add `--q 400 --users 200` to see the opening post and other participants.
   - `--min` skips one-liners ("thanks", "fixed"); `--cap` truncates very long replies and marks `[..cut]`.
   - Choose `--cap` by **measuring** what it discards (snippet below); 1,000 characters kept 94% of the text in the first run, 600 kept 87%.
2. For each thread decide, in this order: **what is the report** (`kind`), **how did it end** (`outcome`), **what is the root cause and who established it** (`cause` + `conf`), **where does it sit** (`layer`, `engine`, `proto`, `os`, `target`), **what rule does it imply** (`constraint`), **what would detect it** (`auto`).
3. Write the record (batch line). Summary style: [`reference/summary-style.md`](../reference/summary-style.md). Include numbers, versions, mechanisms and the maintainer's stated reason; leave out politics and speculation, or mark it unverified.
4. Mark `depth=full` in the batch line. Big threads (hundreds of comments): read the maintainer replies, the opening post and the most-replied comments; state that in the summary if it limits the claim.

## Deciding `conf`
- `stated`: the maintainer or an authoritative participant said it.
- `reported`: a user said it.
- `inferred`: you concluded it (for example from commit timing). Upgrade to `stated` only when someone states it, and say so in the summary ("upgrades an earlier inference").

## Measure what a cap loses (snippet)
```python
import json, os
tot = 0; kept = {600: 0, 1000: 0, 1500: 0}
for f in os.listdir('.cache/full'):
    o = json.load(open('.cache/full/' + f, encoding='utf-8'))
    for c in o['comments']:
        if c['a'] != 'MAINTAINER_LOGIN' or len(c['t']) < 60: continue
        tot += len(c['t'])
        for cap in kept: kept[cap] += min(len(c['t']), cap)
print({cap: round(100 * v / tot) for cap, v in kept.items()})
```

## Choosing what to read first
Chronological order gives a natural timeline; **descending maintainer text** finds the most informative threads first (the first run's constraint-tagged threads held 77 KB of maintainer text in 82 threads). Combine: chronological for coverage, then a second pass by volume for depth.

## Outputs
Analysed issue records with `depth=full`; a growing set of summaries.

## Verification (done when)
`pz.py status` shows the issue depth counts you planned; sampling five records against their threads finds no misattributed statement.

## Pitfalls
- Reading only the first two maintainer replies hides later explanations; the audit (P10) found 33 KB hidden in the first run.
- Attributing a user's guess to the maintainer: check `M[...]` vs `u:` lines.
- Long quotations in summaries: paraphrase; short quoted phrases only when the exact wording matters.
- Pull requests: tag them like issues (`kind`, `outcome` from the merged flag); a PR's discussion is often the design rationale.

## Related
P08, P10, P13, P14.
