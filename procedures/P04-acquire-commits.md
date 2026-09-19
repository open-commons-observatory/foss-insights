# P04 - Acquire commits (local clone)

**Effort:** S · **Needs:** P02 · **Opt out when:** issues-only goal

## Purpose
Get every commit with its files and line counts from a full clone.

## Steps
1. `git clone <url> ../<name>` (full history, not `--depth`).
2. Check completeness: `git rev-list --count HEAD`, `git log --reverse --format='%h %ad %s' --date=short | head` and compare the first commit date with the project's creation date. In the first run one clone's public history began well after the project did; the analysis had to state that.
3. The bootstrap (P06) reads `git log --reverse --numstat --format=@@%H|%h|%ad|%s` itself; you only need the clone path.
4. Note merges vs squashes: the project's PR workflow decides whether PR numbers appear in subjects (`refs` in the record collects `#N` from subjects).

## Outputs
A full clone next to the analysis repo; a one-line note of the history range in `analysis/00-scope.md`.

## Verification (done when)
Commit count in the clone equals the count in `records/commits/` after P06.

## Pitfalls
- Sequence ids (`0001-hash.md`) come from `--reverse` order. If the project rewrites history, ids shift; the hash in the filename is the stable anchor.
- Commit subjects can mislead; P11/P12 say how deep to go.

## Related
P06, P11, P12.
