# ADR-0003: Rename `oco-atlas` to `foss-insights` (short: `fi`)

Status: accepted (2026-09-20). Supersedes the name in [ADR-0002](ADR-0002-oco-atlas-name-and-rewrite.md); the rest of ADR-0002 stands.

**Why.** "Atlas" said what shape the output has (a map) but not what it does. The owner proposed **FOSS Insights**, in the sense of *business insights* (BI) applied
to free and open-source software, `fi` for short: it says the domain (FOSS) and the product (insights), and it is not tied to problems alone, which matters now that the
method is being widened to features, expansion, refactoring and project health.

**What changed.**
- Repositories: template `oco-atlas` -> `foss-insights`; every analysis is `<project>-fi` (first one: `input-remapper-oco-atlas` -> `input-remapper-fi`).
- Tool and config: `tools/atlas.py` -> `tools/fi.py`, `atlas.yaml` -> `fi.yaml`, environment `ATLAS_*` -> `FI_*`, local cache `~/.cache/foss-insights/<name>`,
  database name `atlas` -> `fi`, commands `atlas ...` -> `fi ...` (run as `python tools/fi.py ...`). Vocabulary: "an atlas" -> "an FI repository".
- Kept as history: ADR-0001 and ADR-0002 (they describe decisions under the names they were made with), the v1 files, tag `v1-markdown-records`.

**Consequences observed (measured, not assumed).**
- Git URLs of the old names redirect, so existing clones keep working. The **old GitHub Pages address does not redirect** (HTTP 404); the new address serves. Any link to
  `.../input-remapper-oco-atlas/` is dead. The GitHub Pages configuration itself survived the rename.
- The database stores its GitHub remote URL. `fi db push` now compares it with `fi.yaml` and repairs a stale one instead of leaning on the redirect.
- The documented update-from-template procedure copies files but cannot remove files the template deleted (a rename deletes `tools/atlas.py`, `atlas.yaml`).
  [Operate](../playbook/09-operate.md) now lists the extra `git rm` step. Instances must rename their own config (`atlas.yaml` -> `fi.yaml`) and set `database: fi`.

**Not renamed on purpose.** `input-remapper-prior-art` (the v1 analysis) and `dolt-pipeline-scratch` (the storage experiment) are not FI repositories.
