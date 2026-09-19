# P05 - Design the taxonomy

**Effort:** M · **Needs:** P00 · **Opt out when:** you reuse an existing taxonomy unchanged (then still read the "evolve" step)

## Purpose
The vocabulary decides what the dataset can answer. It has to be small enough to apply consistently and rich enough that grouping by it teaches something.

## Steps
1. **Derive facets from the goals.** For every question in `00-scope.md` ask "which tag would let me count this?". Generic facets nearly every project needs are in the starter taxonomy: `kind` (issues), `ctype` (commits), `outcome`, `conf`, `os`, `impact`. Domain facets you must invent: where the problem sits (`layer`), why it happened (`cause`), which component (`engine`), plus anything the goal implies (protocol, target service, constraint type, automation potential, status in a successor).
2. **Single or multi?** Facets with exactly one truthful answer (`kind`, `ctype`, `outcome`, `conf`) are single-valued; the rest are multi-valued. The tool rejects two values for a single-valued facet.
3. **Sample before you fix values.** Read 100 titles (spread over the whole time range) and list the recurring things. Start with 5-12 values per facet, each with a one-line meaning in `facets.json`. Always include `unknown` in `cause`: an honest "not established" beats a guess.
4. **Add the confidence facet** (`conf`: stated / reported / inferred). It is what lets you separate a maintainer's explanation from your reading of it.
5. **Optional special facets**, each only if a goal needs it:
   - `constraint`: a rule a validator would have to enforce (illegal combination, phase order, capability required, parameter range, engine-only, scope limit). It feeds P14.
   - `auto`: could a tool detect and/or handle this automatically (detect+handle, detect-only, manual-only, n/a).
   - a **successor status** facet (`carried` / `changed` / `superseded` / `unverified` / `na`) if you will compare with another version (P13).
5b. **A symptom facet** (what the reporter saw: stall after N bytes, connection reset, service will not start, ...) is worth adding early: mechanism facets (`layer`, `cause`) describe why, symptoms describe what a person can observe, and support triage needs the second. It can be filled by keyword rules (`textrules.py`); measure the precision (P24).
6. **Problem classes** (`taxonomy/classes.json`): coarse buckets with ids like `M3` (letter = area, number = problem) linked to a heading in an analysis document. They are built *from* the narrative documents (P15): headings `## M3 - title` become classes (`pz.py classes-build`). You may start with none. Class links are **data carried by batches**, not something derived from documents (P24); machine-suggested classes go in a separate `classes_inferred` field.
7. Run `python3 tools/pz.py validate` (all records must still validate after every vocabulary edit).

## Evolving the vocabulary (do this as you read)
- **Adding a value** is cheap: add it to `facets.json` with its meaning; existing records are unaffected.
- **Renaming or merging values** needs a sweep script over the records plus a `replay` proof (P21); avoid it by choosing names carefully.
- **Never delete a value** that any record uses.
- Add a facet late only if it is genuinely new; a facet added late means re-reading records for it.
- Keep a value's meaning stable. If two readers would tag the same item differently, tighten the definition in `facets.json`.

## Outputs
`taxonomy/facets.json`, optionally `taxonomy/classes.json`; a page listing facets and their purpose (see [`reference/taxonomy-example.md`](../reference/taxonomy-example.md) for the first run's).

## Verification (done when)
Pick 20 random items and tag each with the vocabulary in five minutes each; if you keep wanting a value that is not there, extend it before the big run.

## Pitfalls
- **Replace semantics:** a line that mentions `cause:` replaces *all* previous causes of that record. Adding one cause means restating the others (see `pz.py check` warnings).
- Facets designed around a hypothesis you have not tested tend to stay empty. Prefer a wide `cause` list over a clever hierarchy.
- Do not encode judgement in tag names ("bad-design"); encode observable things and put judgement in summaries.

## Related
P00, P06, P14, P15, [`reference/data-model.md`](../reference/data-model.md).
