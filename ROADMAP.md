# Roadmap of the template

Kept up to date by whoever works on the template (see `AGENTS.md`). Decisions behind items are in `decisions/`. An FI repository has its own `ROADMAP.md` for its analysis.

## Staged (agreed, not started): Conventional Commits and release-plz in CI

The owner asked for this, using `sync-dot-mesh/core` (public, Rust) as the model, "with minor adjustments". Nothing is built yet. **Confirm the decision points with the owner first, then record them as a new decision record.**

What the reference does: a PR-title check (`amannn/action-semantic-pull-request@v5`; types feat, fix, perf, refactor, docs, style, test, build, ci, chore, revert; optional scope; lowercase subject), a `release-plz` workflow on every push to `main` (full history, `MarcoIeni/release-plz-action@v0.5`, no registry token), `release-plz.toml` (tag and GitHub Release on, `publish = false`, changelog from `cliff.toml`), a git-cliff changelog template with a `User-Facing` footer, `CONTRIBUTING.md` (squash-merge, the PR title is the commit, the always-open Release PR), and dependabot.

Decision points:
1. **release-plz is a Rust tool and this repository has no `Cargo.toml`.** Test a minimal "version carrier" crate (`publish = false`, an empty lib target) on a scratch repository in the organization first. Fall back to a Python-native tool (release-please `simple`, or python-semantic-release) only with the owner's agreement.
2. **Direct pushes to `main`.** The PR-title check does not see them. Choose: conventional messages required on push (commit lint), or protect `main` and work through pull requests. Do not enable protection unasked.
3. Squash-merge settings so the PR title becomes the commit (`squash_merge_commit_title=PR_TITLE`, `squash_merge_commit_message=PR_BODY`).
4. Release PRs made by the workflow's own token do not trigger other workflows, and "Allow GitHub Actions to create and approve pull requests" must be on. Accept, or use a PAT or app token.

Adjustments: guard every new workflow with `if: github.repository == 'open-commons-observatory/foss-insights'` so FI repositories do not inherit it; scopes `tool db render taxonomy playbook decisions docs tests ci deps release`; anchor the changelog tag pattern (`^v[0-9]+\.[0-9]+\.[0-9]+$`) because the reference's `v[0-9]*` would also match the legacy tag `v1-markdown-records`; use the changelog as the upgrade guide for FI repositories (mark schema migrations and breaking changes with `!` or `BREAKING CHANGE:`); adapt `CONTRIBUTING.md` and `dependabot.yml` (`github-actions`, `pip`, prefix `chore(deps)`). **Write template commits as Conventional Commits from now on.** Do not merge a Release PR without the owner's say.

## Next
- LICENSE: not chosen (suggest MIT or Apache-2.0; ask the owner).
- Commit analysis (schema extension); multiple corpora for successor comparison; private-repository CI path.
- A `fi update-from-template` command (today it is a documented manual procedure).
- Cosmetic: the template site title reads "FOSS Insights - FOSS Insights".
- Archive `input-remapper-prior-art` and `dolt-pipeline-scratch` with a pointer (ask first).
- A second FI repository on another project (the prior-art lens).
