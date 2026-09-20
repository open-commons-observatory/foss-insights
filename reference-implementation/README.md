# Reference implementation (the tested skeleton)

Copy this directory to start an analysis repository (procedure P02). Everything here uses only the Python 3 standard library.

```
project.json                 owner, primary/secondary repo names, maintainer logins   <- edit first
tools/pz.py                  the CLI (bootstrap, next, check, apply, validate, status, index, replay, ...)
tools/threads.py             GitHub REST API thread fetcher and reader (list, fullfetch, readfull)
tools/rulegen.py             batches from subject-pattern rules (no hand-typed hashes)
tools/textrules.py           multi-label keyword tagging (weak labels such as symptom)
tools/review.py              health review with an ATTENTION list (P25); `pz.py stamp FILE` fills computed status blocks
tools/registry.py            problem registry: generate pages, index, by-symptom view and document views (import-docs is a one-time migration)
taxonomy/facets.json         STARTER vocabulary: replace the domain facets (layer, cause, engine)
taxonomy/classes.json        problem classes ({} at the start)
.github/workflows/validate.yml   CI: validate records and batch syntax
registry/source/             problems.json and links.json (empty; see P24)
batches/  analysis/  brainstorms/  data/  LOG.md     empty, ready to use
```

## First commands
```
export GH_TOKEN=...                                  # from your secret store; never commit it
python3 tools/threads.py list --corpus z1            # data/issues-list.json
python3 tools/threads.py fullfetch --corpus z1 $(python3 -c "import json;print(' '.join(str(x['n']) for x in json.load(open('data/issues-list.json'))[:150]))")
git clone https://github.com/OWNER/REPO ../REPO
python3 tools/pz.py bootstrap --corpus z1 --issues data/issues-list.json --clone ../REPO
python3 tools/pz.py validate && python3 tools/pz.py status
```

## Tests
`python tests/test_reference.py` (offline, no token, 16 checks; mutation-tested). See ../MATURITY.md for what is and is not covered.

## Tested
The skeleton was smoke-tested end to end against a live repository: list, fullfetch, readfull, bootstrap of both corpora, a batch with a deliberately bad ref (rejected atomically), a valid batch, validate, index, status.

## Things to adapt for a new project
- `project.json` (names and logins).
- `taxonomy/facets.json`: the generic facets transfer, the domain facets do not (P05).
- `pz.py`: the `heur_issue`/`heur_commit` keyword rules and the rule tables above them are the *first project's* (opt in with `--heuristics zapret`; default is none). Write your own only if titles are reliable enough to help.
- More than two corpora: change `REPOS` and `rec_dir` in `pz.py`.
- The first project's corpus ids are `z1` (primary) and `z2` (secondary); they are only labels in this tool. Renaming means editing `REPOS`, `rec_dir`, `repo_of`, `refname`, `label` and the parser choices.
