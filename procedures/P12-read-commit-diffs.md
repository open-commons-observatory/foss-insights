# P12 - Read commit diffs (optional, deep)

**Effort:** L · **Needs:** P11 · **Opt out when:** you only need the landscape or issue-level knowledge

## Status of this procedure
Exercised on **82 commits** in the first run: the 75 that carried a constraint tag or a key constraint cause (61 in the first corpus, 14 in the second) plus seven second-corpus commits tied to issues recorded earlier. All other commits (about 2,200) stayed at subject level. Reading the 75 took about ten rounds of 8-16 diffs each (one `git show` helper call per round, one batch per one or two rounds).

What it showed:
- Diffs **refine** claims rather than contradict them: a reload guard keeps the in-memory list only for files that cannot be *opened* (a comment says a backup copy would double RAM on small devices), narrower than "keeps the last good list"; a queue-limit fix degrades to *no reassembly*; a timestamp-fooling fix explains the exact bug (an option area lengthened even without a timestamp).
- **Code comments carry the reasons.** Several enforcement points state the mechanism the issues only hinted at: the server-side race behind "seqovl only on the first part", the ICMP reason a low TTL cannot be used in a conntrack workaround, why a mark filter is mandatory (ordering and deadlock).
- Small diffs (1-50 changed lines) are cheap and prove the mechanism; large ones (200+ lines: new facilities) need only the stat and the subject, and are recorded as "a large change adding X" without claiming details.
- Selecting by tag ("commit carries a `constraint:*` tag or key cause") plus "commit fixes an issue I already recorded" is efficient because you know what to look for.

The helper used (not part of the reference implementation; it is twenty lines): for each hash print `git show --stat` and the changed lines of the diff with `-U0`, blank and brace-only lines dropped, capped per commit.

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
