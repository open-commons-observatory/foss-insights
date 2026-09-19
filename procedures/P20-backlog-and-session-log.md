# P20 - Backlog and session log

**Effort:** S · **Needs:** nothing · **Opt out when:** never

## Purpose
Leave a dated, readable trace of what each session did, found and left open, so the next session (a different context, possibly a different reader) can continue without re-deriving anything.

## Two artefacts
- **`LOG.md`**: append-only, one or two lines per session, machine-oriented (batch ranges, counts, tool changes).
- **`brainstorms/YYYY-MM-DD HH-MM - Subject.md`** plus an index row in `brainstorms/README.md`: the narrative entry.

## Entry template ([`templates/session-entry.md`](../templates/session-entry.md))
```
# <date time> - <subject>
<one line: what project, standing instructions>
## Done            what was read/tagged (ranges, counts computed from the tool)
## Findings        what is now known that was not; corrections; retractions
## Limits and open what was skipped, truncated, unverified; what comes next
```

## Rules
1. **Write the entry at the end of every session**, even a short one. Numbers come from `pz.py status` (P22), not from memory.
2. **Filenames must not contain `/`.** A title such as "830/830" is a path separator: the script crashed halfway and the first attempt left the README and log un-updated while a commit message claimed otherwise. Use "830 of 830".
3. **Write the entry file first**, then append the index row and the log line; check that the file exists.
4. Keep the backlog **in the analysis repository**. Another project's notes folder is the wrong place (in the first run the entries were filed twice in the wrong repositories before the owner corrected it).
5. State standing rules the owner gave ("use the API", "backlog here") at the top of the entry so they survive.
6. Corrections go in the entry too (P18).

## Outputs
A new entry, an updated index, a `LOG.md` line.

## Verification (done when)
`ls brainstorms | tail -2` shows the new file; the README row links to it; `git status` is clean after the commit.

## Related
P18, P19, P22.
