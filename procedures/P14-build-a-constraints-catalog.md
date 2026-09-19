# P14 - Build a constraints catalogue

**Effort:** M · **Needs:** P08 (better with P13) · **Opt out when:** the goal is not rule extraction

## Purpose
Extract from the tagged corpus the rules a validator, wrapper or guard would have to enforce: things the project says (or proves) you must not do, must do first, or need a capability for.

## Steps
1. **Define the constraint types** in `facets.json` (the first run: `illegal-combo`, `phase-order`, `needs-cap`, `param-range`, `engine-only`, `scope-limit`) with one-line meanings. Keep them observable.
2. **Tag as you read** (P09). A record is `constraint:*` only if the thread or commit states or shows the rule; a user's guess is not a rule.
3. **Read every constraint-tagged thread in full** (the first run: 82 threads, 77 KB of maintainer text, several summaries corrected). Rules are precisely the thing a brief read distorts.
4. **Generate the catalogue:** `python3 tools/pz.py index` writes `indexes/constraints.md` (grouped by constraint type, one summary line per record with its successor status).
5. **Write each rule once** in your own document (`analysis/rules.md`): one-sentence rule, evidence records, confidence, successor status, and what a validator would check. Keep the rule separate from the evidence.
6. **Deduplicate and merge**: many records support one rule (in the first run, the mark-filter deadlock appeared in six threads).
7. **Verify** against the newer version (P13) before encoding any rule.

## Format that worked (one entry per rule family)
```
## R05 - seqovl
- Rule:      one sentence a checker can test
- Why:       the mechanism (stated by the maintainer, or shown in code)
- Evidence:  #issue, z2#issue, `commit`, `z2:commit` ... and the confidence (stated / shown / reported)
- Status:    carried / changed / superseded / unverified in the successor
- Checker:   what a validator or run-time check would verify
- Test idea: a reproducer
```
A table at the top lists id, short rule and successor status. In the first run **134 constraint-tagged records collapsed into 15 rules**; most were duplicates of one finding attached to many threads (a similarity clustering over summary words, tags and constraint type showed about a dozen families before the hand-written dedupe).

**Verify every reference programmatically** before committing the catalogue: extract `#N`, `z2#N`, `` `hash` `` and `` `z2:hash` `` and check each against the records (five hashes lacked the successor prefix in the first draft). Link each rule to registry entries (P24) and put the rule numbers in `registry/source/links.json`.

## Outputs
`indexes/constraints.md` (generated), `analysis/rules.md` (hand-written), a rule count by type.

## Verification (done when)
Every rule cites at least one record read at `full`; each has a status against the target version or is marked unverified.

## Pitfalls
- A rule read from a thread without its reason is a superstition. Record the maintainer's stated mechanism.
- Constraints from an old version may be wrong for the new one (see P13); never ship them unlabelled.
- Do not count records as rules: 125 records in the first run were far fewer distinct rules.

## Related
P05, P09, P13, P15.
