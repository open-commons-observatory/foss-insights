# How to write summaries and notes

A summary is one or two sentences (three at most for a rule-bearing thread) that would let a reader decide whether to open the record.

## Content, in order of priority
1. **What happened**, with the numbers, versions and dates that identify it.
2. **Why**, in the maintainer's words *paraphrased*, with who said it implicit in `conf` (or explicit: "maintainer states ...", "the reporter suspects ...").
3. **How it ended** (fixed in a version, workaround, declined, no resolution visible).
4. **A rule or limit** if the thread proves one.

## Style
- Your own words; no copied passages. A short quoted phrase only when the exact wording carries meaning.
- Present the mechanism, not the mood. "A stalled stream after 16 KB with a healthy handshake" beats "the site does not work".
- Attribute uncertainty: "the maintainer suspects", "the reporter believes", "not confirmed".
- Numbers are exact when stated (KB, versions, kernel numbers) and absent when not.
- Leave out speculation about motives, politics and budgets; if it matters, say "speculation, not recorded as fact".
- Correct in place: append `+ Deep read (CORRECTION): ...` rather than rewriting silently.
- For depth upgrades, append `+ Deep read: ...` (idempotent) and keep the first summary as the anchor.

## Examples (paraphrased from the first run)
Good:
> Oct 2025 byte-count blocks: the handshake succeeds and the stream stalls after about 16 KB, so a probe that only checks the connection or a short response reports the site as available. The maintainer says only crafted fakes help and that testing must be manual; a later change made the probe fetch a large object.

Good (a rule):
> Phase-0 methods act before any hostname exists, so a hostlist or L7 filter removes them; the maintainer's workaround in the successor is to cache the hostname from DNS answers, which does not help with DoH.

Too vague:
> Not working on Windows.

Overclaiming:
> The DPI blocks everything after 16 KB (root cause: whitelist). *(One user's capture; state it as reported.)*

Bad (copies text):
> "I would not support this because ..." *(paste of a maintainer paragraph)*

## Notes section
Usually empty. Use it for links to other records, for open questions and for anything that is not a claim.
