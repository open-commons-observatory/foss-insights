# P13 - Verify claims against another version

**Effort:** M · **Needs:** P08 · **Opt out when:** no successor, fork or newer version exists, or old findings are all you need

## Purpose
Old issues describe old behaviour. When a successor (rewrite, fork, later major version) exists, each finding must say whether it still holds there. This is what turns a history into usable knowledge.

## Steps
1. **Pin the target version:** clone it and note the commit hash and date. Every status you record is "as of this commit".
2. **Select what to verify.** Start with records tagged `constraint:*`; then records with a named mechanism (a limit, a capability, an ordering rule).
3. **Find evidence** in this order, cheapest first: the manual and changelog (`grep -n` for the option or concept), the configuration defaults, the source (the function that would enforce or implement the rule), the tests. Record *where* (file and function or manual line).
4. **Classify** with a single-valued status facet (the first run called it `z2`):
   - `carried`: still holds (say where it is documented or visible in source);
   - `changed`: holds differently (semantics, defaults, mechanism);
   - `superseded`: no longer applies (removed, replaced, made automatic);
   - `unverified`: not checked; **the honest default**;
   - `na`: not a question about the target (packaging, user error, dated provider observation).
5. **Write the evidence** as an appended summary line (`+ z2 check: ...`) and set `depth=source`.
6. **Write the catalogue document** (`analysis/constraints-vs-<target>.md`): a table by rule family with the issues, the status and the evidence, plus a section "Corrections to earlier readings" and a section "Limits".
7. **Second round** for the `unverified` ones: group them by theme (platform support, payload detection, option parsing) and grep per theme; expect most to resolve, and leave the rest listed by number.

## Outputs
Status facet on every checked record; a comparison document; a count of carried/changed/superseded/unverified/na.

## Verification (done when)
Every constraint-tagged record has a status; each `carried`/`changed`/`superseded` has evidence with a location; the document states which ones remain `unverified`.

## Pitfalls
- **Absence of evidence:** "I found no X in the manual" is not "X does not exist". Write it as found-no-X, with what you searched.
- Nothing was executed in the first run. Say so ("from documentation and source at commit ..., not run").
- A rule may be `changed` in a way that creates a *new* constraint in the target (for example an option that must start at a particular packet). Add a new record or note for it.
- Do not let the newer version's docs stand in for its behaviour when the source disagrees; the source wins.

## Related
P14, P17, P18.
