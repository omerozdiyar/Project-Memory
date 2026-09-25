---
type: playbook
module: global
updated: 2026-07-27
---

# Playbook: Memory Health Check

Goal: catch silent drift between memory and code before it grows.

## Steps

1. **Mechanical pre-check:** run `python3 tools/check-links.py` (broken links/orphans) and `python3 tools/check-coverage.py` (code areas without memory). Add the output to your findings.
2. **Module validation:** verify every claim in each module's `architecture.md` and `conventions.md` against the code: stale facts, missing features, wrong descriptions.
3. **Contract validation:** compare every contract in `contracts.md` with the code on both sides.
4. **Present-tense check:** read every file in `activeContext/` — any stale locks or finished items left behind by anyone?
5. **Fix:** update state files to the new reality. Never touch ADR bodies. Delete rather than update measurements that go stale quickly (file sizes, line counts, etc.).
6. **Report:** save findings and fixes as `notes/YYYY-MM-DD-health-check-N.md`; add a line to the root `changelog.md` (a health check is global-scope).

## Rules

- Never make a fix you are not sure about; ask the user.
- Feature ideas discovered during the scan go into the report as "candidates" — do not touch code.
