# FOSS Insights

**Turn a project's public history into an evidence-backed, versioned map of its problems, and a queue of fixes.**

A *FOSS Insights* repository (an *FI*) takes the issues, pull requests and commits of an open-source project, records what each one says against a controlled
vocabulary in a version-controlled Postgres-compatible database, groups them into recurring problems, and publishes the result as
Markdown and a website. Every claim links to its source thread and says how it is known and how deeply it was read.

This repository is the **template**. Each analysis is its own repository created from it and named `<project>-fi`,
for example `input-remapper-fi`.

```
GitHub API ──acquire──▶  Doltgres database  ──render──▶  Markdown + website
(issues, PRs, commits)   facets, items, analyses,        (coverage, triage, problems,
                         tags, problems                   one page per facet value)
                         │ every batch = one commit
                         └─ stored in this repo's hidden ref refs/dolt/data
```

## Quick start

```bash
# 1. Use this template -> name it <project>-fi, then edit fi.yaml (repo, source.repo, title)
pip install -r requirements.txt
tools/install-doltgres.sh
export GITHUB_TOKEN=...                       # environment only, never committed
python tools/fi.py db init                 # server + schema + vocabulary
python tools/fi.py acquire                 # fetch the corpus
python tools/fi.py next                    # what to read first
python tools/fi.py read 1 2 3
python tools/fi.py apply batches/0001.tsv  # tag a batch; validated whole, written atomically
python tools/fi.py render                  # pages from SQL + templates
python tools/fi.py db push                 # the database into GitHub
```

Self-test of the whole pipeline on a small fixture: `bash tests/run.sh` (CI runs it on every push).

## What is in here

| Path | What |
|---|---|
| [`playbook/`](playbook/README.md) | the method: nine phases, principles, lenses, lessons |
| `fi.yaml`, `taxonomy.yaml` | your project's configuration and controlled vocabulary |
| `db/migrations/` | the database schema as numbered migrations (Postgres dialect); `fi db init` applies the pending ones |
| `tools/fi.py`, `tools/render.py` | the command line tool and the page generator |
| `docs/pages.yaml`, `docs/queries/`, `docs/templates/` | what to render: SQL feeds Jinja templates |
| `batches/` | applied batch files: the readable audit log (in FI repos) |
| `data/`, `docs/generated/` | CSV export and rendered pages, regenerated from the database (in FI repos) |
| [`decisions/`](decisions/) | decision records: options considered, evidence, why |
| `.github/workflows/` | `self-test.yml` (this template) and `docs.yml` (publishes an FI repository) |

## Why a database

The first version kept one markdown file per record. It worked for one project and hurt at scale: no constraints (a typo in a tag
passed validation), hand-rolled indexes, and state that could go stale. A real database gives constraints, SQL, history, and
diffs at the row level. [ADR-0001](decisions/ADR-0001-data-store-and-tooling.md) records what was tested and why Doltgres won.

## Status and limits

Working end to end and self-tested. Not yet supported: analysing commits (they are acquired and stored), multiple corpora in one
fi (successor comparison), and a private-repository CI path. See [lenses](playbook/lenses.md). Built on Doltgres 1.x and
Zensical 0.0.x, both young: versions are pinned.

## FI repositories built from this template

| FI repository | Analyses | Site |
|---|---|---|
| [input-remapper-fi](https://github.com/open-commons-observatory/input-remapper-fi) | [sezanzeb/input-remapper](https://github.com/sezanzeb/input-remapper) | https://open-commons-observatory.github.io/input-remapper-fi/ |

To take template fixes into an FI repository, see [operate](playbook/09-operate.md#updating-an-fi-repository-from-the-template).

## Lineage

Successor to `sync-dot-mesh/prior-art-playbook` (markdown records; preserved here as tag `v1-markdown-records`).
