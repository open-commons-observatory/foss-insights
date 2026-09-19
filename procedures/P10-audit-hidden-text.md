# P10 - Audit for hidden text and re-read

**Effort:** M · **Needs:** P09 · **Opt out when:** you used the API from the start and read every thread at `full`

## Purpose
Measure how much of each thread you did **not** see, then close the gap. Any shortcut (scraped pages, brief reads, reply caps) hides something; this procedure turns "probably fine" into a number.

## Steps
1. **Compare the list with the API** (catches missing items): fetch the list again through the API and diff the item numbers against the list you bootstrapped from.
2. **Fetch complete threads** for every issue still below `full` (P03 step 3, chunked).
3. **Compute unseen maintainer text per issue**: total maintainer characters in the full thread minus what your earlier read could have shown (first N replies, first C characters each). Rank descending. In the first run: 539 brief-depth issues, 33 KB unseen in total, 10 issues with more maintainer replies than the cache held, 45 issues with 200+ characters unseen.
4. **Read the unseen text** of the top of the ranking in full (a round per 12), record each in a batch with `+ Deep read (hidden): ...` appended summaries and `depth=full`.
5. **Close the tail**: for the rest, print exactly the unseen parts (tails of replies over your old cut, replies beyond the first N) and read them; the first run's tail was 47 issues and 6 KB and changed no conclusion.
6. **Mark everything compared as `full`** in one closure batch, and write down the audit numbers in the session entry (P20/P22).

```python
# unseen maintainer text per issue (adapt SEEN_REPLIES and SEEN_CHARS to your earlier read)
SEEN_REPLIES, SEEN_CHARS = 2, 200
rows = []
for n in brief_issue_numbers:
    full = json.load(open(f'.cache/full/{n}.json', encoding='utf-8'))
    m = [c['t'] for c in full['comments'] if c['a'] in MAINTAINERS and len(c['t']) >= 60]
    seen = sum(min(len(t), SEEN_CHARS) for t in m[:SEEN_REPLIES])
    rows.append((sum(len(t) for t in m) - seen, n))
rows.sort(reverse=True)
```

## Outputs
Closure batches; audit numbers; every issue at `full`.

## Verification (done when)
`pz.py status` shows zero issues at `thread` (or you list exactly which stay there and why).

## Pitfalls
- Do not declare the audit done by sampling; the whole point is a computed number for every item.
- Threads with hundreds of comments: the cache from a scraped page held about 15 of them. Compare `ncomments` from the API with the cached count.
- The audit found real errors of interpretation too (see P18): corrections belong in the record and in every document that repeated the claim.

## Related
P03, P09, P18, P22.
