#!/usr/bin/env python3
"""Self-check of the playbook: every procedure file appears in README's table, goals.md and templates/plan.md,
and every relative markdown link resolves. Exit 1 on any problem."""
import glob, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
problems = []

def read(p):
    return open(os.path.join(ROOT, p), encoding='utf-8').read()

procs = sorted(os.path.basename(p) for p in glob.glob(os.path.join(ROOT, 'procedures', 'P*.md')))
ids = [re.match(r'(P\d+)', p).group(1) for p in procs]
readme, goals, plan = read('README.md'), read('goals.md'), read('templates/plan.md')
for pid, fn in zip(ids, procs):
    if 'procedures/' + fn not in readme: problems.append('README table misses %s' % fn)
    if not re.search(r'\|\s*%s ' % pid, goals): problems.append('goals.md misses %s' % pid)
    if not re.search(r'- \[ \] %s ' % pid, plan): problems.append('templates/plan.md misses %s' % pid)
rows = re.findall(r'^\| ☐ \| \[(P\d+)\]', readme, re.M)
if rows != ids: problems.append('README table order/ids differ from procedures/: %s vs %s' % (rows, ids))

link = re.compile(r'\]\(([^)#]+)(#[^)]*)?\)')
for path in glob.glob(os.path.join(ROOT, '**', '*.md'), recursive=True):
    if os.sep + 'reference-implementation' + os.sep in path and not path.endswith('README.md'): continue
    for m in link.finditer(open(path, encoding='utf-8').read()):
        target = m.group(1)
        if re.match(r'[a-z]+:', target): continue
        full = os.path.normpath(os.path.join(os.path.dirname(path), target))
        if not os.path.exists(full): problems.append('%s: broken link %s' % (os.path.relpath(path, ROOT), target))

print('\n'.join(problems) if problems else 'playbook ok: %d procedures, links resolve' % len(ids))
sys.exit(1 if problems else 0)
