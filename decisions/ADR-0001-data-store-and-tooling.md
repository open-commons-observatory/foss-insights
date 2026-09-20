# ADR-0001: Where the analysis data lives, and what tooling sits on it

Status: **proposed** (investigated 2026-09-20; not yet adopted; owner decides)
Context session: input-remapper run, session 3.

## Question
The playbook is hand-rolled ETL (Python tools) over markdown-with-frontmatter records. The owner asked: is this
classical technical-BA tooling, what open tools exist, and can the data live in a real database (Postgres) that the
agent can edit in its sandbox and sync via GitHub?

## What the playbook is, in BA terms
Elicitation (acquire issues) -> controlled vocabulary (taxonomy = data dictionary) -> relational model
(records, tags, links) -> validation (pz.py) -> traceability (registry links) -> generated reports (indexes, registry).
Mature open tools exist for each stage; the parts we hand-rolled are acquisition, validation, diffing and reporting.

## Measured in the sandbox (2026-09-20; sandbox = root, Ubuntu 24, network on)
| Fact | Result |
|---|---|
| Real PostgreSQL 16 | `apt-get install postgresql` works; start with `pg_ctlcluster` (no systemd). Full SQL, constraints, dumps OK |
| Dolt 2.3.5 | installs from release script; cell-level diff, branch, merge OK |
| Doltgres 1.3.3 (Postgres dialect, 1.0 GA 2026-08-06) | runs; stock `psql` connects (reports PG 15.5); CHECK constraints enforced; dolt_diff/branch/merge via SQL OK |
| Dolt AND Doltgres -> Git remote | push / clone round trip through a plain Git repo works (local bare repo). Requirement: repo must already have a commit |
| Where Dolt puts data in Git | hidden ref `refs/dolt/data` + a branch `__dolt_remote_info__`; contents are opaque chunk files. NOT browsable or reviewable in the GitHub UI |
| Diff noise, 12 scattered row edits, 2000 rows | pg_dump --inserts: 14+/14- lines. PK-sorted CSV export: 12+/12-. After VACUUM FULL with no data change: pg_dump 2+/2-, sorted CSV 0 |
| DuckDB over the existing batch files | `pip install duckdb`; loaded 192 analysed records and produced triage queries in one script |
| Background servers | a server started in one tool call was gone in the next (connection refused). Restart inside each call. Filesystem also resets between tasks, so the repo must be the source of truth |
| pkill/pgrep -f | self-match the calling shell when the pattern is in the command line; use `pkill -x name` |

GitHub limits (docs.github.com, repository limits): single object recommended <=1 MB, enforced 100 MB; repo ideally <1 GB;
push rate recommended <=6/min/repo. Fine for us; relevant if a binary DB file were committed.

## Options
1. **Postgres + canonical text export in Git (recommended base).** Schema as `schema.sql`; each table exported as
   PK-sorted CSV/NDJSON; sandbox and CI restore into real Postgres (or query with DuckDB). Reviewable diffs in PRs, real
   constraints, standard tooling. Cost: export/restore discipline; no cell-level merge.
2. **Doltgres/Dolt as the store, Git repo as remote.** DB-level branch/diff/merge. Cost: data invisible in GitHub UI unless
   also exported to text; young ecosystem; a Feb-2026 report (dolthub/dolt#10537) measured 45-80 s per push to GitHub
   (issue now Closed, reported on Dolt 1.82.2; current speed against real GitHub NOT verified by me).
3. **SQLite/DuckDB file(s).** Binary SQLite is opaque in diffs; use sqlite-diffable text dumps, or DuckDB directly over
   CSV/Parquet in the repo (no server, runs anywhere incl. CI).
4. **BA-as-code requirement tools (StrictDoc, Doorstop, Sphinx-Needs, OpenFastTrace, TRLC, quarto-needs).** Built for
   engineering requirements with typed links, not for a ~1000-record externally sourced corpus with facets. Useful on the
   OUTPUT side (PR specs traced to problem-registry entries), not as the analytical store.
5. **Report layer:** Evidence.dev (SQL+Markdown -> static site; DuckDB engine over CSV/Parquet), Datasette (browse/JSON API;
   github-to-sqlite already implements the acquisition we hand-rolled), Quarto/MkDocs for prose.

## Proposed direction (pending owner decision)
Option 1 as the source of truth, DuckDB for ad-hoc analysis, Evidence or Quarto for published reports, CI restores into a
Postgres service container and runs the constraint suite. Keep Doltgres as a phase-2 option if DB-level merge is wanted.

## Evidence this matters (found in our own data)
- Two malformed tags (`conf=stated`) passed the current validator ("all records valid"); a CHECK/enum constraint rejects them.
- 89 of 192 analysed records have pr_potential=unknown (46%): a NOT NULL / no-default rule would force a decision.

## Not verified
Real GitHub HTTPS push/clone speed for Dolt(gres); a full GitHub Actions run of restore+validate+report; Doltgres extension
coverage; pg_dump diff behaviour beyond ~2000 rows.
