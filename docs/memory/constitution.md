---
type: constitution
module: global
updated: 2026-07-27
---

# The Constitution — Non-Negotiable Working Rules

This file is project-independent: it applies regardless of language, framework, or architecture.
Project-specific knowledge does NOT live here — it lives in the memory map (`index.md`) and the module files.

## 1. Sync first, then read memory

Before anything else, if the project has a git remote and the working tree is clean, sync: `git pull origin main` — and when starting a new task, branch from the freshly pulled `main`. Never pull over uncommitted changes; ask the user instead. Stale memory is worse than no memory: it makes you confidently build against yesterday's contracts.

Then read `docs/memory/index.md`, then the index of the relevant module, then its area files. Scan code files only when memory is not enough.

## 2. Update memory with every meaningful change

When code, file structure, env, data model, or a contract changes, update the relevant **state file to reflect the new reality** (the old state lives in git history). Record the **why** as a dated ADR under `decisions/`. ADRs are never deleted; their body is never edited — only the `status` field may be updated to `superseded → [[new-adr]]`.

## 3. Memory and code ship in the same commit

A commit that contains code changes must also contain the related memory update. (Enforced locally by `tools/hooks/pre-commit` and on PRs by `.github/workflows/memory-check.yml`.)

## 4. Reachability and the changelog (partitioned by owner — no shared append file)

Every memory file must be reachable from the index chain (`index.md` → module index → file) via `[[wiki-links]]`; change lists are never written into index files. Enforced by `tools/check-links.py`.

Changelogs are **split by module so parallel contributors never fight over one file**:

- A change scoped to a module → one dated, linked line in **that module's** `<module>/changelog.md`. The module owner writes only there.
- A change with global scope (constitution, contracts, tooling, adding a whole module) → one line in the root `changelog.md`. These are rare and go through review, so contention is a non-issue.

Rationale: the memory is already federated by module and each module has one owner, so a per-module changelog gives every contributor their own file (zero cross-member merge conflicts) while keeping a module's whole story in one place. We partition by module rather than by person because modules outlive team changes.

## 5. Source of requirements

Each module's source of requirements is declared in that module's index. If a request contradicts the requirements, ask the user.

## 6. File findings back into memory

Save reusable findings (bug root causes, performance analyses, behavioral discoveries) as dated notes under `notes/`, linked from the relevant changelog (the module's, or the root one if global). Do not open notes for routine work.

## 7. Health checks

When the user asks (or proactively every few tasks), validate memory against the code: stale facts, contradictions, unreachable files, missing ADRs. Procedure: [[playbooks/health-check]]. Never touch ADRs.

## 8. Contracts are sacred

Every interface between modules (API, data schema, event, error format) is defined in `contracts.md`. A contract change requires an ADR and must be reflected in the state files of every affected module.

## 9. Write down the present and take a lock (one file per contributor)

Each contributor keeps their own file `activeContext/<your-name>.md` — you write only yours, so no shared file to conflict on. When starting a task, write your intent and your **lock** (module, branch, scope) there. **Before locking a module, read all files in `activeContext/`**; if someone else holds an active lock on the same module, ask the user before starting. When done, record the outcome, release your lock, and clear finished items — this file shows *your* "now"; leave nothing stale.

(activeContext is split by person, not module, because "who is doing what right now" is inherently personal; reading the directory still gives the full coordination picture.)

## 10. Size limit

No state file may exceed ~200 lines. Split oversized files by topic and link the parts from the module index.

## 11. Frontmatter standard

Every memory file starts with this YAML frontmatter:

```yaml
---
type: moc | state | adr | note | contract | constitution | playbook | spec
module: global | <module-name>
updated: YYYY-MM-DD
---
```

(ADRs use `date` instead of `updated`, and it is never changed afterwards.)

## 12. Follow the playbooks

Recipes for recurring tasks live under `playbooks/`. If a playbook matches your task, follow it; if you find yourself doing a procedure manually for the third time, propose a playbook for it.

## 13. Spec before big work

For a new module, a contract change, or a feature spanning many files, first write a spec with acceptance criteria under `specs/` and get user approval; code starts only after approval. Procedure: [[playbooks/spec-process]].

## ADR Format

Filename: `YYYY-MM-DD-short-title.md`, location: `decisions/` — details: [[playbooks/writing-adrs]]

```markdown
---
type: adr
module: <affected module or global>
date: YYYY-MM-DD
status: accepted | superseded → [[new-adr]]
---

# Title
- **Decided by:** (person/agent)

## Context (why was this needed?)
## Decision (what was done?)
## Consequences (what does it affect?)
```
