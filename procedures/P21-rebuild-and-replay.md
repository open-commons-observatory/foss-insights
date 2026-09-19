# P21 - Rebuild and replay

**Effort:** S · **Needs:** P08 · **Opt out when:** you do not need a reproducibility guarantee

## Purpose
Prove that the dataset is exactly what the archived batches say, so nothing depends on an undocumented hand edit.

## Steps
1. In a scratch copy: delete `records/`, keep `taxonomy/`, `analysis/`, `batches/`, `data/`.
2. Rebuild: `bootstrap` for each corpus (P06/P17), then `classes-build` and `backfill-docs` (P15), then `python3 tools/pz.py replay` (re-applies every archived batch in numeric order).
3. Compare with the original: `diff -r records <scratch>/records` (empty output means byte-identical).
4. Fix any difference at its source (a missing batch, a hand-edited record) and repeat.

## When to run
After a tooling change that touches parsing, after a vocabulary rename, and once before you call the analysis finished. The first run verified a byte-identical rebuild once mid-way; later batches were not re-verified, so re-run it.

## Rules
- Never edit a record file by hand. Anything that is not in a batch (or in `bootstrap`/`backfill-docs`) does not survive a replay.
- Batches are immutable once applied; a correction is a new batch.
- `replay` order is the file number; keep numbering monotonic.

## Verification (done when)
The `diff` is empty.

## Pitfalls
- Depth and status only move up, so replaying in a different order can change results if batches conflict; keep the archive order.
- Heuristic tags come from bootstrap; if you changed heuristics, the rebuild differs on untagged records only.

## Related
P08, P18.
