---
type: playbook
module: global
updated: 2026-07-27
---

# Playbook: Spec Process

Goal: plan before code on big work. ADRs look backwards; specs look forwards.

## When Is a Spec Required?

- A new module or a change to a cross-module contract
- A feature spanning many files or multiple sessions
- Work that will be shared by more than one person/agent

Small, single-file work needs no spec.

## Steps

1. Copy `docs/memory/specs/_spec-template.md` to `specs/YYYY-MM-DD-feature-name.md` and fill it in. Acceptance criteria must be **testable** sentences (not "should be fast" but "the list loads in under 200ms").
2. Present it to the user with frontmatter `status: draft`; link it from your `activeContext/<name>.md`.
3. When the user approves, set `status: approved`. **Code starts only after this point.**
4. Implement against the spec; if you must deviate, update the spec first and ask the user.
5. When finished, verify each acceptance criterion one by one, record the results at the bottom of the spec, set `status: completed`.
6. Distill the durable knowledge: update the source of requirements and module state files, write an ADR, add a line to the relevant changelog (the module's, or root if the change was global). The spec file remains under `specs/` as historical record.

## Rules

- No code against an unapproved spec.
- A spec never replaces the source of requirements — it is distilled into it when done.
