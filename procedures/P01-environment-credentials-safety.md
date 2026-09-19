# P01 - Environment, credentials and safety

**Effort:** S · **Needs:** nothing · **Opt out when:** never

## Purpose
Make the working environment predictable and make sure no secret ever lands in a file, a log, a commit or a memory store.

## Steps
1. **Token.** Use a GitHub token from the environment variable `GH_TOKEN`. Reading public repositories needs no special scope; pushing to your analysis repo needs contents write (a fine-grained token limited to that repo is best). Never write the token into a file, a batch, a log, a commit message, a URL or a chat summary.
2. **Rate limits.** Authenticated REST calls: 5000 per hour (`X-RateLimit-Remaining` header). Unauthenticated: 60 per hour, useless for this. A full thread costs two calls (the issue plus its comments, paged by 100).
3. **Command time limit.** In the working environment a single shell command dies after about 300 seconds. Fetch in chunks (150 threads fit), rely on the on-disk cache, wrap long commands in `timeout 240`.
4. **Shell.** The shell was `/bin/sh` (dash): no brace expansion (`mkdir -p a/{b,c}` creates a directory literally named `{b,c}`), no `time` builtin, `printf` over `echo -e`. In pipelines `cmd | tail` returns tail's exit status, so a failing `apply` is invisible: use `set -o pipefail`, or run the command alone and check its exit code.
5. **Encoding.** Do not cut text with `cut -c` (it splits multi-byte characters and the tool output becomes invalid UTF-8). Cap text inside Python instead.
6. **Tools.** Python 3 standard library only; git; curl is not needed.
7. **If a token appears in plain text in a conversation**, tell the user it should be rotated. Do not repeat it in summaries.
8. **Secret scan before every push:** `grep -rnE "github_pat_[A-Za-z0-9]{10}|ghp_[A-Za-z0-9]{10}" . --exclude-dir=.git --exclude-dir=.cache` must print nothing.
9. **Pushing** without putting the token in a URL: `B64=$(printf 'x-access-token:%s' "$GH_TOKEN" | base64 -w0); git -c http.extraheader="Authorization: Basic ${B64}" push origin main 2>&1 | sed "s/${B64}/***/g" | tail -1`.

## Outputs
A shell where `echo ${GH_TOKEN:+set}` prints `set`, and a written note of the limits above in your working notes.

## Verification (done when)
`curl -s -H "Authorization: Bearer $GH_TOKEN" https://api.github.com/rate_limit` shows 5000; the secret scan is clean.

## Pitfalls
- The first run began with HTML scraping and ended with a repair audit (see P10 and [`lessons/pitfalls.md`](../lessons/pitfalls.md)).
- A memory or notes system may persist what you write: keep secrets out of anything durable.

## Related
P03 (uses the token), P19 (push and scan).
