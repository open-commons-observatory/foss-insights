# P00 - Define goals and scope

**Effort:** S (30-60 minutes) · **Needs:** nothing · **Opt out when:** never

## Purpose
Decide what decision the dataset will feed, which items are in it and how deeply each kind is read. The dataset is exhaustive by construction, but *depth* is a budget, and goals decide the taxonomy. A vague goal produces a vocabulary that answers nothing.

## Use when / skip when
Always. Skipping it is how a taxonomy gets designed twice.

## Steps
1. Write the **decision or deliverable** in one paragraph (for example "a typed strategy layer must refuse illegal option combinations" or "compare how a successor changed the failure modes").
2. Pick one or more presets in [`goals.md`](../goals.md). The preset fixes which procedures you will tick.
3. Write the **questions** the dataset must answer (5-15 sentences). Each later facet must serve at least one question.
4. Decide the **item types**: issues, pull requests, commits, and explicitly the sources you leave out (discussions, forum threads, wikis, mailing lists, chat). Out-of-scope sources are written down, because the analysis will otherwise be read as covering them.
5. Decide the **depth budget** per item type using the ladder in [`reference/data-model.md`](../reference/data-model.md): for example issues to `full`, commits to `title`, constraint-related commits to `source`.
6. Decide the **honesty checks** you will run at the end (P10 audit, P18 QA, P22 statement).
7. Timebox: number of rounds you are willing to spend. Reading is the cost driver (see P08 and P09).

## Outputs
`analysis/00-scope.md` in the analysis repo (goal, questions, item types, out-of-scope list, depth budget, timebox) and the ticked plan ([`templates/plan.md`](../templates/plan.md)).

## Verification (done when)
Someone can read `00-scope.md` and say which questions the dataset will and will not answer.

## Pitfalls
- Scope creep into Discussions/forums halfway through: decide now; in the first run they were never read and had to be listed as a limit.
- A goal like "understand the project" is not a goal. Ask what will be built or decided from it.
- Two goals with conflicting facets: list the union of facets now (P05).

## Related
P05 (taxonomy from goals), P22 (limits statement repeats the out-of-scope list).
