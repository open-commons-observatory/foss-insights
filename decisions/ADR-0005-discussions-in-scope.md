# ADR-0005: GitHub Discussions are in scope

Status: accepted (2026-09-20). Corrects an earlier scope decision.

**What was wrong.** The first scope document for the input-remapper analysis listed GitHub Discussions as *out of scope: not in the REST issues API; too sparse to justify*. Nobody had counted.
Measured on 2026-09-20: 221 discussions with 212 comments and 238 replies. It is a support channel comparable in size to a quarter of the issue tracker, and the project's contribution guide itself
tells helpers to "answer questions in Discussions".

**Decision.** `fi acquire` fetches Discussions by default through the GraphQL API (needs `GITHUB_TOKEN`; skipped with a message otherwise) into the `discussion` table
(number, title, author, date, comment count, answered flag). Their text is not stored. Reading them at depth is a separate, optional phase.

**Why metadata only.** It is enough for responsiveness metrics (discussions with no reply per year) and for finding threads worth reading, and it avoids storing other people's text.

**Rule for the future.** A scope note may list a channel as out of scope only with the number that justifies it.
