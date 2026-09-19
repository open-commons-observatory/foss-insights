# P12 - Read commit diffs (optional, deep)

**Effort:** L · **Needs:** P11 · **Opt out when:** you only need the landscape or issue-level knowledge

## Status of this procedure
Designed, **not exercised in the first run**: all 2,300 commits there stayed at subject level. Treat the steps as a plan to try on a small selection first.

## Purpose
Establish what a change really did, verify a maintainer's explanation against code, and find design decisions that no issue explains.

## Selection rule (choose one, do not read everything)
- Commits linked to a `constraint:*`-tagged issue or record (the rule's enforcement point).
- `ctype:fix` commits whose subject names no cause.
- Commits that touch a core file heavily (`adds + dels` large) or that other records cite.
- Commits within a date window around a major redesign.

Query: iterate `pz.all_records('commit')` and filter on tags, `refs` and size; write the selection into `analysis/commit-diff-queue.md`.

## Steps
1. Show stats first: `git -C ../<clone> show --stat <hash> | head -40`.
2. Read the diff of the relevant files only: `git -C ../<clone> show <hash> -- <path>`. For huge diffs read the hunks around function names in the subject.
3. Write the finding as an appended summary: `+ Diff read: <what the change does>; the subject said <...>` and set `depth=source`.
4. Cross-check with the issue thread that motivated the commit; note disagreements explicitly.
5. If the diff establishes a root cause the thread lacked, add `cause:` and `conf:stated` only if the code itself proves it; otherwise `inferred`.

## Outputs
`depth: source` commit records; an updated constraint catalogue where relevant.

## Verification (done when)
Every commit in the selection is at `source`; a sample of five summaries survives a re-read of the diff.

## Pitfalls
- Diffs are expensive to read: cap each round and record after every round (P08).
- Reading the diff of the *fix* does not prove the *report* was correct; keep the two claims separate.

## Related
P11, P13, P14.
