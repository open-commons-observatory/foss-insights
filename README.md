# prior-art-playbook

How to build an **exhaustive, normalised, tagged prior-art analysis** of an open-source project: every issue, pull request and commit becomes one small record with controlled tags, a confidence level and a "how deeply was this read" marker. Written for my future self, from the first run of this method (an analysis of `bol-van/zapret` and `bol-van/zapret2`, kept in `sync-dot-mesh/zapret-prior-art`).

The result is not a report. It is a **dataset** (one file per issue/commit, controlled vocabulary, derived indexes and statistics) from which many different reports can be produced. That is why the playbook is split into small procedures you opt in and out of according to the goal.

## How to use this playbook

1. Read [`principles.md`](principles.md) (5 minutes). They are the rules that kept the first run honest.
2. Pick a goal in [`goals.md`](goals.md). Each preset is a checklist of procedures.
3. Copy [`templates/plan.md`](templates/plan.md) into the new analysis repo and tick the procedures you will do. Skipping is fine; the table below says what each one costs and when it is safe to omit.
4. Scaffold from [`reference-implementation/`](reference-implementation/) (tested working skeleton: CLI, thread fetcher, starter taxonomy, CI). Procedure [P02](procedures/P02-scaffold-the-repository.md) explains it.
5. Work in rounds ([P23](procedures/P23-autonomous-rounds.md)); after each round record notes as a batch immediately.
6. Read [`lessons/pitfalls.md`](lessons/pitfalls.md) once before starting and again before each big phase. Most entries cost me hours.

## Procedure overview (opt in / out)

`☐` = tick in your own copy of the plan. **Core** = the method breaks without it. Effort is relative (S = minutes, M = an hour or two, L = many rounds).

| ☐ | ID | Procedure | Needs | Yields | Effort | Safe to skip when |
|---|---|---|---|---|---|---|
| ☐ | [P00](procedures/P00-define-goals-and-scope.md) | Define goals and scope | - | goal, depth budget, deliverables | S | never (30 minutes that save days) |
| ☐ | [P01](procedures/P01-environment-credentials-safety.md) | Environment, credentials, safety | - | token in env, limits known | S | never |
| ☐ | [P02](procedures/P02-scaffold-the-repository.md) | Scaffold the analysis repository | P01 | repo with tool, CI, layout | S | you already have one |
| ☐ | [P03](procedures/P03-acquire-issues-and-prs.md) | Acquire issues and PRs (API) | P01, P02 | complete list + full thread cache | M | commits-only goal |
| ☐ | [P04](procedures/P04-acquire-commits.md) | Acquire commits (local clone) | P02 | clone, history checked | S | issues-only goal |
| ☐ | [P05](procedures/P05-design-the-taxonomy.md) | Design the taxonomy | P00 | facets, values, classes | M | you reuse an existing taxonomy |
| ☐ | [P06](procedures/P06-bootstrap-the-records.md) | Bootstrap the records | P03/P04, P05 | one stub record per item | S | never (core) |
| ☐ | [P07](procedures/P07-rule-tagging-mechanical-commits.md) | Rule-tag mechanical commits | P06 | merges/docs-only tagged | S | issues-only goal |
| ☐ | [P08](procedures/P08-the-atomic-batch-loop.md) | The atomic batch loop | P06 | manual tags + summaries | L | never (core) |
| ☐ | [P09](procedures/P09-read-issues-at-depth.md) | Read issues at depth | P03, P08 | analysed issues, depth marked | L | commits-only goal |
| ☐ | [P10](procedures/P10-audit-hidden-text.md) | Audit for hidden text and re-read | P09 | coverage measured, gaps closed | M | you used the API from the start and read in full |
| ☐ | [P11](procedures/P11-triage-commits.md) | Triage commits (subject + files) | P06, P07 | analysed commits | L | issues-only goal |
| ☐ | [P12](procedures/P12-read-commit-diffs.md) | Read commit diffs (optional, deep) | P11 | source-depth commits | L | you only need the landscape |
| ☐ | [P13](procedures/P13-verify-against-another-version.md) | Verify claims against another version | P08 | status facet, evidence | M | no successor/fork/newer version exists |
| ☐ | [P14](procedures/P14-build-a-constraints-catalog.md) | Build a constraints catalog | P08, P13 | rule catalogue | M | goal is not rule extraction |
| ☐ | [P15](procedures/P15-write-analysis-documents.md) | Write analysis documents by class | P08 | narrative docs, class links | M | dataset alone is the deliverable |
| ☐ | [P16](procedures/P16-indexes-and-statistics.md) | Generate indexes and statistics | P08 | STATUS, by-facet, stats | S | never (it is one command) |
| ☐ | [P17](procedures/P17-add-a-second-corpus.md) | Add a second corpus | P08 | second project in same repo | M | one project only |
| ☐ | [P18](procedures/P18-quality-and-corrections.md) | Quality assurance and corrections | P08 | audits, retractions | M (ongoing) | never |
| ☐ | [P19](procedures/P19-ci-and-publishing.md) | CI and publishing | P02 | pushed, CI green, no secrets | S | local-only work |
| ☐ | [P20](procedures/P20-backlog-and-session-log.md) | Backlog and session log | - | dated entries, LOG | S | never |
| ☐ | [P21](procedures/P21-rebuild-and-replay.md) | Rebuild and replay | P08 | reproducibility proof | S | you do not need a rebuild guarantee |
| ☐ | [P22](procedures/P22-honest-coverage-reporting.md) | Honest coverage reporting | any | limits statement | S | never |
| ☐ | [P23](procedures/P23-autonomous-rounds.md) | Working mode: autonomous rounds | P08 | efficient long sessions | S | short analyses |

## Reference material

| File | What it holds |
|---|---|
| [`reference/data-model.md`](reference/data-model.md) | Record format, status and depth ladders, refs, derived files |
| [`reference/batch-format.md`](reference/batch-format.md) | The batch line grammar and its rules |
| [`reference/cli.md`](reference/cli.md) | Every command of the reference implementation |
| [`reference/taxonomy-example.md`](reference/taxonomy-example.md) | The taxonomy actually used in the first run, as a model |
| [`reference/summary-style.md`](reference/summary-style.md) | How to write record summaries and notes |
| [`lessons/pitfalls.md`](lessons/pitfalls.md) | Numbered mistakes and their fixes |
| [`templates/`](templates/) | Plan checklist, session entry, batch example, record example |
| [`reference-implementation/`](reference-implementation/) | Working CLI (`pz.py`), API thread tool (`threads.py`), starter taxonomy, CI |

## What the first run produced (scale reference)

- Corpus 1: 830 issues (766 read in full, 64 also checked against source) and 974 commits at subject level. Corpus 2: 115 issues/PRs (96 full, 19 source) and 1,330 commits. Diffs were read for 82 constraint-related commits (61 in the first corpus, 21 in the second).
- 60 problem classes; a constraints catalogue of about 125 rules with a status against the successor (carried 37, changed 25, superseded 9, not applicable 10, unverified 1).
- Effort: many long sessions. Reading depth was the driver, not tooling: the first corpus took roughly 45 batches of 12-36 items; the second, the same structure at a fifth of the size, was done in a fraction of the time thanks to the API-only fetcher, `pz.py check` and `rulegen.py`.
