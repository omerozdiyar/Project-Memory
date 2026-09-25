# Memory System Setup Guide (for an Existing Project)

## 1. Copy the template

Copy the contents of this folder (except SETUP.md and README.md) into your project root:
`CLAUDE.md`, `AGENTS.md`, `docs/memory/`, `tools/`, `.github/`

Add to `.gitignore`: `.obsidian/`

If the project already has a CLAUDE.md or AGENTS.md, merge the contents (memory rules go on top).

## 2. Bootstrap: have an agent fill the memory

Give this prompt to your AI tool (Claude Code, Antigravity, Cursor, etc.):

```
This project will use persistent project memory under docs/memory/. First read
docs/memory/constitution.md and follow its rules. Your task is to bootstrap the
memory from the existing codebase:

1. Scan the codebase and identify sensible modules (e.g. frontend, backend, db).
2. For each module create docs/memory/<module>/ with index.md (map),
   architecture.md (directory layout, key flows, data/state model),
   conventions.md (code style, patterns, prohibitions) and changelog.md
   (that module's own change log). Use _module-template/ as the example;
   keep the template folder when you're done.
3. Where present: write the database schema, env variables (their NAMES and
   purposes — never values), and the authorization flow into the relevant module.
4. Record cross-module interfaces in docs/memory/contracts.md.
5. Fill in the project summary and module table in the root docs/memory/index.md.
6. Write the first ADR under decisions/ ("memory system installed"). Add
   separate ADRs for major architectural decisions you can read from the code,
   marked as "retroactive record".
7. Inspect git history but DISTILL, don't copy: extract only significant
   decisions from git log (major direction changes, reverts = abandoned
   approaches, library/architecture migrations). Write each as a separate
   "retroactive record" ADR citing the relevant commit hashes as evidence.
   Add a short report on the most frequently changed files (fragile spots)
   under notes/. If a commit message doesn't explain WHY, never invent it:
   ask me or skip it. No records for routine commits (fix, refactor, typo).
8. Add the installation line to the ROOT changelog.md (installing the system is
   global-scope). Module-scoped changes from here on go in each module's own
   changelog.md. Replace every YYYY-MM-DD placeholder in frontmatter with today's date.

Never fabricate anything you are not sure about; ask me about whatever you
cannot verify from the code.
```

## 3. Review

Bootstrap is never perfect on the first pass. Read `docs/memory/` yourself:
misunderstood architecture, missing modules, fabricated facts?
Have them fixed. This investment determines the quality of every future task.

## 4. Wire up git

```
git add -A
git commit -m "Install project memory"
git config core.hooksPath tools/hooks     # memory enforcement hook
git push
```

(No repo yet? `git init` first and create a remote.)

On GitHub, `.github/workflows/memory-check.yml` activates with the push:
every PR gets the memory check, link integrity, and coverage report.
Manual local checks: `python3 tools/check-links.py` and `python3 tools/check-coverage.py`

## 5. Connect Obsidian (optional, for humans)

Obsidian → "Open folder as vault" → select the project root.
In graph view, confirm everything is connected to the index chain.

## 6. Onboard the team

- Everyone clones the repo and runs `git config core.hooksPath tools/hooks`.
- One team rule: no code PR is accepted without a memory update.
- AGENTS.md is already there for people using other tools.
- Each person creates their own `docs/memory/activeContext/<name>.md` (copy `_contributor-template.md`) and logs module work in that module's own changelog — this is what keeps parallel branches conflict-free.

## 7. Watch the loop on the first task

Give an agent a small task and check: did it read memory first, update the
state file and add an ADR afterwards, add a changelog line? If something is
missed, retry with "Read AGENTS.md first and follow it" at the top of the prompt.

## 8. Routine maintenance

Every few tasks ask for a health check: "Run a memory health check per
constitution rule 7." Stale facts get cleaned up; the report lands in notes/.
