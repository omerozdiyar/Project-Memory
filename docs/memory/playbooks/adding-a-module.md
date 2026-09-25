---
type: playbook
module: global
updated: 2026-07-27
---

# Playbook: Adding a Module

Goal: every new module (service, package, layer) is born with standard memory.

## Steps

1. Copy `docs/memory/_module-template/` to `docs/memory/<module-name>/` (keep the template itself). This includes the module's own `changelog.md`.
2. Fill in the module's `index.md`: description, source of requirements, "not in this module".
3. Write `architecture.md` (directory layout, key flows, data/state model) and `conventions.md` (style, patterns, prohibitions). Use `module: <module-name>` in the frontmatter.
4. Record every interface this module has with other modules as contracts in `contracts.md`.
5. Add a row to the Modules table in the root `index.md`.
6. Write an ADR ("added <module-name> module": why it exists, why this technology). Adding a whole module is a global-scope change → log it in the **root** `changelog.md`. From here on, changes *inside* the module go in `<module-name>/changelog.md`.

## Rules

- If the module boundary is unclear (separate module vs. part of an existing one), ask the user.
- Never write cross-module calls without a contract — contract first, code second (constitution rule 8).
