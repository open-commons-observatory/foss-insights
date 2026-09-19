# Pitfalls (numbered; each cost real time in the first run)

Format: **symptom** - cause - fix - where it is handled.

## Data acquisition
1. **A third of the maintainer text was missing from constraint threads** - the issue list and thread cache had been scraped from HTML, which returns only the first ~15 comments - use the REST API (complete, paged) from the start - P03, P10.
2. **Maintainers who joined late were invisible** (three threads had zero maintainer replies in the cache, one with 263 comments) - first page only - compare `ncomments` from the API with the cached count - P10.
3. **The brief reader hid text** (first 160 characters of the post, first two maintainer replies cut at 200) - a reading window chosen for speed - measure the hidden text per issue and read it (audit) - P10.
4. **A reply cap silently discards content** - caps are lossy - measure what a cap loses before choosing it (1,000 characters kept 94%, 600 kept 87%) and state the cap - P09, P22.
5. **The command died after 300 seconds** - one shell command has a time limit - fetch in chunks of ~150 threads, cache per thread, use `timeout 240` - P01, P03.
6. **The public clone's history began late** - the project's public history was truncated - check the first commit date against the project's creation; state the range - P04.
7. **Discussions and forum threads were never read** - not in the REST issues API and not in scope - decide in P00, list as a limit - P00, P22.
8. **Numbering gaps and PRs sharing numbers** - deleted items, PRs and issues share one sequence - normal; keep PRs as records - P03, P17.

## Tool use and shell
9. **Directory literally named `{a,b}`** - `/bin/sh` does no brace expansion - write explicit `mkdir -p` lines - P01.
10. **A rejected batch still produced a commit whose message claimed the changes** - `pz.py apply ... | tail` returns `tail`'s exit status, so the failure was invisible - run `apply` alone, or `set -o pipefail`, and read the output - P08, P18.
11. **Session-entry script crashed after partial work** - the title contained `830/830` and `/` is a path separator - sanitise titles, write the file first, then append README and log, then verify - P20.
12. **Invalid UTF-8 in tool output** - `cut -c1-N` split a multi-byte character - cap text inside Python - P01.
13. **`time` not found** - the shell has no such builtin - measure with `date +%s` or Python - P01.
14. **A token appeared in a conversation** - pasted by the owner - never store or repeat it, read it from the environment, scan the repo before every push, advise rotation - P01, P19.
15. **Tool outputs disappeared from context** - long sessions clear old tool results - write the batch for what you just read *before* reading more - P08, P23.

## Batches and records
16. **Stray letters in refs** (`i1127b`, `i643b`, `i770b`, `i1260b`) - typed by hand - the atomic rejection caught them; use `pz.py check` before `apply` - P08.
17. **An analysed record's summary was overwritten** - a new line re-tagged an already analysed record without `+` - `check` warns; use `+ text` to append - P08, P18.
18. **A multi-valued facet lost values** - replace semantics: mentioning `cause:` replaced all causes - restate every value that still holds; `check` warns - P05, P08.
19. **`unknown class D9`** - the class did not exist - define classes early or use `-`; the atomic rejection protects the data - P05, P08.
20. **Records tagged by a title heuristic looked "done"** - `triaged` is not `analyzed` - only manual tags count in statistics - P06.
21. **Depth was defined late** (`full` and `source` added mid-way) - the first depth ladder had only `title/thread/source` - define the ladder before tagging - P05, P09.
22. **A successor-status facet added late** meant re-reading 82 records - the goal changed mid-run - decide in P00 whether a comparison will happen - P00, P13.
23. **Heuristic keyword rules did not transfer** - they encode one project's vocabulary - default `--heuristics none` in a new project - P06.
24. **Rules by subject text were unsafe** - subjects lie - only automate rules stated in one sentence and sample the matches - P07.

## Interpretation
25. **Wrong causal stories from brief reads** (one packet-counter explanation, one queue-ordering claim) - the full thread contradicted them - the correction protocol: record, every document, log - P18.
26. **Inference stated as fact** - a link inferred from commit timing - keep `conf:inferred` until the maintainer says it; then upgrade and say so - P09, P18.
27. **"Not found" reported as "does not exist"** - grep negatives are weak - write "found no X (searched A, B)" - P13.
28. **Claims about another version from its manual alone** - the manual may lag the source - check the source and name the function - P13.
29. **Nothing was executed** - conclusions from reading only - state it in every summary of results - P13, P22.
30. **Speculation recorded as evidence** (motives, budgets, politics) - it appears in long threads - leave it out or flag it unverified - P09.
31. **A rule without its mechanism** - copied from a thread without the reason - record the maintainer's stated mechanism - P14.

## Reporting and operations
32. **Numbers quoted from memory** ("about 160 remain"; the computed figure was 209) - compute from `pz.py status` or a script - P22.
33. **Backlog filed in the wrong repositories twice** - an org-wide notes folder, then another project's folder - keep the backlog in the analysis repo - P20.
34. **Similar project names were conflated** (a CLI library and the tool that uses it) - keep boundaries in the scope document and ask when unsure - P00.
35. **Rounds too big lost detail; rounds too small wasted calls** - 12 threads per round (full) and 36-40 items (brief) worked - P08, P23.
36. **Corrections left stale claims in documents** - a record was corrected but analysis documents still cited it - `grep -rn "#N" analysis/` on every correction - P18.
37. **Derived files were stale at push** - `index`/`status --write` not rerun - run them before the closing commit - P16, P19.

## Meta
38. **"Complete" without a depth** - a count of analysed records hid that many were read shallowly - always give depth counts and limits together - P22.
39. **Scope expanded silently** (a second corpus) - fine when asked for, but record the decision in the entry - P17, P20.
40. **The playbook itself:** if a procedure here disagrees with what works, fix the playbook in the same session and add the lesson here.
