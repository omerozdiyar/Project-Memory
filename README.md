# memory-template

A **git-versioned, Obsidian-readable, tool-agnostic project memory** template for AI-assisted (vibe coding) development.

## Problems it solves

- Lock-in to a single AI tool: memory is plain Markdown, portable across Claude Code, Antigravity, Cursor, etc. (`CLAUDE.md` + `AGENTS.md`).
- No shared context in teams: memory lives in the same repo, same commit, same PR as the code; even with frontend/backend written by different people, everyone reads the same map.
- Merge conflicts on shared memory: changelogs are split per module (each owner writes their own) and active-work files are split per contributor, so parallel branches don't collide on one append-only file.
- Token waste: agents read memory first (`index.md` → module) and scan code only when needed.

## Quick start

To install into an existing project: **[SETUP.md](SETUP.md)** — copy, give the bootstrap prompt to an agent, review, wire up git.

## Structure

```
CLAUDE.md / AGENTS.md            agent entry files (thin, identical in every project)
tools/hooks/pre-commit           blocks code commits without a memory update
tools/check-links.py             broken wiki-link / orphan detection
tools/check-coverage.py          report of code areas without memory
.github/workflows/memory-check.yml   the same checks on PRs (CI)
docs/memory/
  constitution.md                non-negotiable working rules (13 rules)
  index.md                       root map (router)
  activeContext/                 one file per contributor (current work + locks) — no shared file
  contracts.md                   contracts between modules
  changelog.md                   GLOBAL-scope changes only; each module has its own changelog
  playbooks/                     task recipes (health check, module, ADR, spec)
  specs/                         acceptance-criteria plans for big work
  decisions/                     ADRs (never edited)
  notes/                         analysis findings, scan reports
  _module-template/              skeleton for new modules (index, architecture, conventions, changelog)
```

## Conflict-free by construction

Two things every contributor touches — the change log and the "what am I working on now" file — are partitioned so parallel branches never fight over them:

- **Changelog is per module.** A module's changes go in `docs/memory/<module>/changelog.md`; only its owner writes there. The root `changelog.md` is reserved for rare global changes (constitution, contracts, tooling). Partitioned by module (not person) because modules outlive team changes.
- **Active context is per contributor.** Each person keeps `docs/memory/activeContext/<name>.md`. To detect a conflicting lock, read the folder — you never edit anyone else's file.
- ADRs and notes are already one-file-per-entry with unique dated names, so they never conflict either.

## Core principles

Read memory first · update memory with every change · memory and code ship in the same commit · the "what" stays current in state files, the "why" accumulates in ADRs · spec before big work · periodic health checks validate memory against code.

Details: [docs/memory/constitution.md](docs/memory/constitution.md)
