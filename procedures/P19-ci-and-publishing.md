# P19 - CI and publishing

**Effort:** S · **Needs:** P02 · **Opt out when:** you never publish

## Purpose
Every push is validated by a machine, and nothing secret leaves the machine.

## CI (already in the skeleton)
`.github/workflows/validate.yml` runs on push and pull request: `python tools/pz.py validate` (every record against the taxonomy) and a syntax/vocabulary check of every archived batch. A broken vocabulary edit therefore fails CI instead of poisoning replay.

## Publishing sequence (end of a round or session)
```
python3 tools/pz.py index && python3 tools/pz.py status --write
git add -A && git commit -m "<what was done>"
grep -rn "github_pat_\|ghp_" . --exclude-dir=.git --exclude-dir=.cache      # must print nothing
B64=$(printf 'x-access-token:%s' "$GH_TOKEN" | base64 -w0)
git -c http.extraheader="Authorization: Basic ${B64}" push origin main 2>&1 | sed "s/${B64}/***/g" | tail -1
sleep 25
curl -s -H "Authorization: Bearer $GH_TOKEN" "https://api.github.com/repos/<owner>/<repo>/actions/runs?per_page=1" \
  | python3 -c "import sys,json;r=json.load(sys.stdin)['workflow_runs'][0];print('CI:',r['name'],r['status'],r['conclusion'])"
```
Expect `CI: validate completed success`. If `in_progress`, wait and check again.

## Rules
- Push to the analysis repository only. Session entries and backlog about this analysis live *in it*, never in other projects' repositories (P20).
- The token is used through `http.extraheader`, never in the remote URL, never printed (the `sed` masks it).
- Branch protection on other repositories may require pull requests and green checks; follow it there.
- Keep the repository private unless you have decided otherwise: records quote issue text (paraphrased) and may include personal handles.

## Verification (done when)
The push line shows the new hash, CI is green, the secret scan is empty.

## Pitfalls
- A commit message that promises more than the commit contains (a script failed halfway but the chain still committed). Use the exit status and read the output.
- Pushing with stale derived files: run `index` and `status --write` first.

## Related
P01, P20.
