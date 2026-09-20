# ADR-0004: Structure the analysis with ITIL 4, ISO/IEC/IEEE 14764, ISO/IEC 25010:2023 and CHAOSS

Status: accepted (2026-09-20). Details and sources: [methodology](../playbook/methodology.md).

**Question.** The method could record problems only. The owner asked to analyse also features, expansion and refactoring, and to base the structure on a proper methodology
"like ITIL 4 but for software", taking the best of it.

**Options considered.**
1. *Adopt ITIL 4 wholesale.* Rejected: it assumes a service provider, customers, SLAs and a service desk, none of which exist in a public FOSS project, and it has no software-change taxonomy.
2. *ITIL 4's structure plus software standards (chosen).* ITIL 4 for the shape (evidence apart from problems apart from changes; known error; one improvement register; four dimensions);
   ISO/IEC/IEEE 14764:2022 for classifying changes; ISO/IEC 25010:2023 for quality; CHAOSS for project health.
3. *Numeric prioritisation (RICE, WSJF).* Rejected: needs reach and cost data we do not have; three-level `value`, `effort`, `risk` instead.
4. *Static-analysis debt scoring (SQALE).* Rejected as out of scope for a history-based method; debt is recorded as a `preventive` improvement.

**Decisions.**
- One `register` replaces the problems-only tables (migration 001, existing data carried over). Types: problem, request, improvement, risk. Status `known-error` requires a workaround.
- New facets: `change_type` (5 values), `quality` (9), `dimension` (4), `value`, `effort`, `risk`. Register entries use the same vocabulary and the same foreign-key enforcement as item tags.
- Register batches are YAML (`fi apply x.yaml`): prose-heavy entries are unreadable as SQL, and YAML lets the tool validate everything before writing (evidence exists, values in the vocabulary,
  single-valued facets, known-error has a workaround).
- Activity data (migration 002): comments (author, item, date, review or not; **never the text**), releases, discussions, a maintainer list from `fi.yaml`. A generated `health.md` reports the
  CHAOSS starter metrics with bots excluded and aggregates only.
- Numbered **migrations** (`db/migrations/`) replace the single schema file so instances upgrade in place. Tested: an old-schema database with data is upgraded with its data intact.

**Consequences.** Instances must run `fi db init` after taking the update, and add the new facets to their own `taxonomy.yaml`. The pages `problems.md` and `problems/<id>.md` became `register.md` and `register/<id>.md`.
Old links break; nothing else references them.

**Known limits.** Health metrics cannot tell a busy maintainer from a departed one; `value` and `effort` are analyst judgement; ISO 14764 is a fee-based standard, so this relies on published summaries of it
and on the standard's own front matter, not on a full reading of its clauses.
