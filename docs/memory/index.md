---
type: moc
module: global
updated: YYYY-MM-DD
---

# Project Memory — Root Map

> Agents: read [[constitution]] for the rules first, then descend into the module relevant to your task.
> Change history is never kept in index files → global [[changelog]] + each module's own changelog.

## Project Summary

<!-- 2-3 sentences: what the project is, the tech stack, how to run it -->

## Core Files

| File | Contents |
|---|---|
| [[constitution]] | Non-negotiable working rules (project-independent) |
| [[activeContext/README\|activeContext/]] | One file per contributor: current work + locks. Read the folder to detect conflicting locks. |
| [[contracts]] | Contracts between modules |
| [[changelog]] | Global-scope changes only (constitution, contracts, tooling). Module changes live in each module's own changelog. |

## Modules

| Module | Description |
|---|---|
| <!-- [[module-name/index\|module-name]] --> | <!-- one-sentence description --> |

## Playbooks (recipes for recurring tasks)

[[playbooks/health-check|health check]] · [[playbooks/adding-a-module|adding a module]] · [[playbooks/writing-adrs|writing ADRs]] · [[playbooks/spec-process|spec process]]

## Global Folders

- `decisions/` — dated decision records (ADRs); linked from the relevant changelog (unique dated filenames never conflict)
- `notes/` — analysis findings and scan reports; linked from the relevant changelog
- `specs/` — acceptance-criteria plans for big work; active ones linked from the owner's `activeContext/<name>.md`
- `activeContext/` — one file per contributor (current work + locks); see [[activeContext/README]]

## Root Files

Agent entry points: [[CLAUDE]] / [[AGENTS]] (identical content)
