# ADR-0006: The repository is its own operating manual for AI agents

Status: accepted (2026-09-20).

**Context.** The work is done across many sessions by an AI with no memory of the earlier ones. At the end of a long session a separate hand-off document was written outside the repository. The owner pointed out
that the repository is itself the manual: it was written by the AI, for the AI, and should be the context of every session: read in full, kept up to date, with decisions only ever added.

**Options considered.**
1. *A separate hand-off document, rewritten each time* (what was done first). Rejected: not versioned, drifts from the repository, easy to lose, and not the file a new session opens by reflex.
2. *The chat tool's own memory or project notes.* Rejected as the source of truth: private, unversioned, not reviewable by the owner, not part of an open project. Useful only as a pointer to the repository.
3. *The repository as the manual (chosen).* Versioned, public, reviewable, and it travels with the template into every FI repository created from it.

**Decision.**
- `AGENTS.md` at the root is the entry point: read the repository in full, in a stated order, at the start of every session; update it in the same commit as the change that taught something; decision records are append-only and are superseded, never edited; start and end checklists.
- `playbook/agent-manual.md` holds the environment, procedures and checks; `ROADMAP.md` holds the plan and the staged tasks of the repository; lessons and decision records hold the reasons.
- FI repositories inherit `AGENTS.md` and the manual through the template, take updates through the documented procedure (which now includes `AGENTS.md`), and keep their own `ROADMAP.md`, `SCOPE.md` and decision records.
- The token is never stored in the repository; the owner supplies it each session.

**Consequences.** A session that does not update the repository has not finished. Anything only said in a chat is considered lost. The stand-alone hand-off file remains only as a bootstrap for a first session and points here.

**Unverified.** Whether a future agent follows the reading order in full is not testable here; the start checklist asks it to report differences between the repository's claims and reality, which is the visible sign that it read them.
