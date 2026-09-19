# P08 - The atomic batch loop (the core cycle)

**Effort:** L · **Needs:** P06 · **Opt out when:** never

## Purpose
Turn reading into stored, validated, replayable data in small safe steps, so that any interruption loses nothing.

## The cycle
```
next N items  ->  read them  ->  write ONE batch file  ->  check  ->  apply  ->  validate  ->  commit  ->  next
```
1. **Pick the next N items.** `python3 tools/pz.py next --kind issue -n 12` (or your own queue, e.g. largest maintainer text first). N = 6-12 for threads read in full, 30-40 for brief reads or commit subjects. Bigger rounds lose detail; smaller ones cost tool calls.
2. **Read** with `python3 tools/threads.py readfull --corpus z1 --maint-only --min 60 --cap 700 N1 N2 ...` (see P09 for the options and depth rules).
3. **Write the batch immediately.** File `batches/NNNN-short-name.tsv`, one line per record or per group of records with identical tags (grammar in [`reference/batch-format.md`](../reference/batch-format.md)):
   `i1836 | M1,S2 | kind:bug cause:byte-cutoff layer:probe conf:stated outcome:workaround depth=full | Own-words summary.`
   Group refs that share tags and a summary (`i12,i57,i94 | - | ...`); write a unique summary only where the item adds information.
4. **Check:** `python3 tools/pz.py check batches/NNNN-name.tsv`. Errors mean the batch would be rejected. Warnings are the mistakes that cost time: an overwritten summary, dropped facet values, duplicate refs.
5. **Apply:** `python3 tools/pz.py apply batches/NNNN-name.tsv`. The whole batch is validated first; on any error *nothing* is written. The batch file is archived under `batches/` automatically (a copy outside `batches/` is added with the next number).
6. **Validate and commit:** `python3 tools/pz.py validate && git add -A && git commit -m "batch NNNN: <what>"`.
7. **Regenerate derived files** (`pz.py index`, `pz.py status --write`) at the end of a session, not after every batch.

## Rules for lines
- `status` defaults to `analyzed`, `depth` to `thread` (issues) or `title` (commits). Set `depth=full` or `depth=source` explicitly when true. Depth only ever moves up.
- Tags of a facet **replace** that facet's previous values. Use a `+ text` summary to **append** without overwriting.
- Never re-tag an analysed record with a full summary unless you mean to replace it.
- A ref is `i<number>`, `c<hash prefix>` (and `z2i<n>`, `z2c<hash>` for the secondary corpus). A typo such as `i1127b` is rejected, and the rejection is atomic.

## Working discipline
- **Write notes into the batch as soon as you have read the items.** Tool output can be cleared from context; the batch file cannot.
- Check the exit status. `pz.py apply ... | tail -3 && next` hides a rejection because the pipeline returns `tail`'s status; run `apply` without a pipe, or use `set -o pipefail`.
- One batch = one commit; the commit message names the item range.

## Outputs
One archived batch per round; records at `status: analyzed`.

## Verification (done when)
`pz.py status` counts move as expected; `validate` is ok; `git log` shows one commit per batch.

## Pitfalls
See [`lessons/pitfalls.md`](../lessons/pitfalls.md): unknown class rejected but commit created anyway, stray ref suffixes, replace-semantics surprises, invalid filenames in session entries.

## Related
P09, P11, P18, P21, P23.
