# P18 - Quality assurance and corrections

**Effort:** M (ongoing) · **Needs:** P08 · **Opt out when:** never

## Purpose
Keep the dataset trustworthy while it grows: catch mechanical errors before they are stored, catch interpretive errors when later evidence contradicts them, and make corrections visible.

## Mechanical checks (every batch)
1. `pz.py check batch.tsv` before `apply`: errors (would be rejected) and warnings (summary overwrite of an analysed record, facet lines that drop existing values, duplicate refs).
2. `pz.py apply` is atomic: any error rejects the whole batch. Fix the batch, do not work around it.
3. `pz.py validate` after every apply and in CI.
4. Look at the exit status of `apply` before committing (see P08); a piped `| tail` hides a rejection.

## Interpretive checks (periodically)
- **Sample re-reads:** every so often re-open five random analysed records and re-read their threads against the summary.
- **Second-pass reads** of rule-bearing records (P14) usually change something. In the first run the full reads corrected a reason that had been recorded as unknown, replaced an explanation that was wrong, and turned an inference into a stated fact.
- **Coverage audits** (P10) whenever a reading shortcut was used.

## The correction protocol
When new evidence contradicts an earlier record:
1. **Record:** append `+ Deep read (CORRECTION): ...` to the summary (or replace the summary when it is simply wrong and say so in the batch header); restate the affected facets (replace semantics); adjust `conf`.
2. **Documents:** `grep -rn "#<number>" analysis/` and fix or retract every claim that repeated it. Write retractions visibly ("Retracted (#675): the first pass inferred ...").
3. **Log:** one line in `LOG.md` and the session entry naming the record, the old claim and the reason.
4. Never quietly edit a record file by hand: replay (P21) would lose the correction.

## Inference hygiene
- `conf:inferred` stays until someone with authority states it; then upgrade and say "upgrades an earlier inference".
- Speculation in a thread (about motives, budgets, politics) is not evidence: leave it out or flag it unverified.

## Outputs
Corrections recorded in three places; an audit trail in `batches/`.

## Verification (done when)
`grep` for a retracted claim finds only the retraction; `pz.py check` shows no unexplained warnings on the latest batches.

## Pitfalls
- Correcting the record but not the documents that cite it.
- An "improvement" batch that silently changes many summaries (the check warns; read the warnings).

## Related
P08, P10, P15, P21.
