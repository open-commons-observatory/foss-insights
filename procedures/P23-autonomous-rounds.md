# P23 - Working mode: autonomous rounds

**Effort:** S · **Needs:** P08 · **Opt out when:** short analyses (do it interactively)

## Purpose
Long analyses are hundreds of small rounds. When the owner says "go on" or "sequence the rounds yourself", chain them without asking for permission each time, safely.

## The loop (2 tool calls per round)
```
call A:  record the batch for the items just read  ->  check -> apply -> validate -> commit  ->  compute the next queue slice  ->  read it
call B:  (same, for the next slice)
...
last:    session entry + LOG + index + status --write  ->  commit  ->  secret scan  ->  push  ->  CI check
```
Reading and recording are combined in one call: the batch for round k and the read for round k+1. Housekeeping (indexes, entry, push) happens **once at the end of the session**, not per round.

## Rules
1. **Record before you read more.** Tool outputs may be cleared from context; only the batch file persists.
2. **Round size:** 12 threads (full read) or 36-40 commits/brief items; cap displayed replies (P09).
3. **Queue:** compute it once (`/tmp/queue.txt`) and slice it; recompute from the records (`depth`/`status`) after every batch so you never re-read.
4. **Check exit statuses.** Never pipe `apply` into `tail`.
5. **Stay inside command limits** (300 s): chunk fetches, use the cache.
6. **Stop conditions:** the queue is empty, an error you cannot fix from the message, a scope question that needs the owner, or the context budget is nearly used. Then write the entry and say exactly where you stopped and what is next.
7. **Progress numbers in every reply** come from `pz.py status`.
8. **Do not expand scope silently** (new corpus, new facet family): ask, or record the decision in the entry.
9. **A correction found mid-loop** is applied immediately (P18) and mentioned in the next summary.

## Skeleton of a round (shell)
```
python3 tools/pz.py check batches/NNNN-x.tsv && python3 tools/pz.py apply batches/NNNN-x.tsv   # no pipe
python3 tools/pz.py validate && git add -A && git commit -q -m "batch NNNN: items a-b"
python3 tools/threads.py readfull --corpus z1 --maint-only --min 90 --cap 450 $(next 12 numbers)
```


## Machine-readable session state: CHECKPOINT.json (improvement from input-remapper run)

When rounds span multiple sessions or context windows, a `CHECKPOINT.json` file at the repo root acts as a durable cursor that any session can read to resume instantly without parsing LOG.md or batch filenames.

```json
{
  "schema": 1,
  "session": 3,
  "last_batch": 12,
  "last_issue_analyzed": 180,
  "issues_analyzed": 144,
  "issues_total": 1099,
  "taxonomy_locked": false,
  "fetch_cache_watermark": 400,
  "notes": "One line on where things stand and any notable finding.",
  "next_steps": ["fetch threads 400-600", "read round 13"]
}
```

**Rules:**
- Update after every batch `apply` and at end of every session, before the final commit.
- Keep `next_steps` as a short list; it is the first thing the next session reads.
- `fetch_cache_watermark` tracks how many threads are cached, so the next session knows what to fetch before reading.
- Commit CHECKPOINT.json separately from the batch commit (or add it to the batch commit); never leave a round without updating it.
- The file is data, not instructions: never put executable commands or token references in it.

## Verification (done when)
Each round produced one archived batch and one commit; the session entry lists the batch range and the remaining queue.

## Related
P08, P20, P22.
