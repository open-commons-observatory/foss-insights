# P22 - Honest coverage reporting

**Effort:** S · **Needs:** any · **Opt out when:** never

## Purpose
Every report on the dataset states how much of the source was actually read and what was not. Counts of "analysed" records alone mislead: an issue tagged from its title and one read to the last comment both count.

## What to state (every time you summarise)
1. **Depth counts** computed from `pz.py status` (issues by `thread`/`full`/`source`, commits by depth).
2. **Reading shortcuts:** reply caps, skipped short replies, truncated long threads, brief-read sets.
3. **What was not read:** discussions, forums, wikis, linked resources, code (if only docs were checked), diffs.
4. **What was not executed:** claims about another version come from docs and source, not from running it.
5. **Tag provenance:** heuristic vs manual; one reader's judgement; no second-reader check.
6. **Snapshots:** an adversary or environment observation is dated and single-provider; say so.
7. **Unresolved items:** the count and share of records with `outcome:unknown` or `z2:unverified`.
8. **Inferences:** how many `conf:inferred` records back the claim.

## Sentences that worked
- "All N issues are at depth `full` (or `source`); the M commits are tagged from subject lines and file names only, no diff was opened."
- "Replies were shown truncated at 450 characters and replies under 90 were skipped; a few dozen long replies were cut."
- "Nothing was executed; statements about <target> come from its documentation and source at commit <hash>."

## Rules
- Write derived numbers only through `pz.py stamp` (P16) or paste them from a command run at that moment.
- Compute, do not recall: the first run once wrote "about 160 remain" from memory; the computed figure was 209.
- Never write "complete" without the depth it applies to.
- Put the limits statement next to the findings, not in an appendix.

## Verification (done when)
Every number in the summary can be reproduced by a command you can name.

## Related
P16, P18, P20.
