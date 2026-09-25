---
type: playbook
module: global
updated: 2026-07-27
---

# Playbook: Writing ADRs

Goal: never lose the "why". ADRs look backwards; they preserve **why** something happened, not what.

## When to Write an ADR

- Architectural direction change, library/technology choice or replacement
- A contract change (`contracts.md`)
- An approach that was tried and abandoned (revert) — the most valuable ADR type; prevents repeating mistakes
- Deliberate constraints ("localStorage was not used because...")

Routine work (fix, refactor, typo) gets no ADR; a changelog line (in the relevant module's changelog) is enough.

## How to Write One

1. File: `decisions/YYYY-MM-DD-short-title.md`, format per the constitution template.
2. In **Context**, capture the situation at decision time: what problem existed, which options were considered.
3. In **Consequences**, list affected files/modules and warnings for future agents ("any change touching function X must preserve this record").
4. Add a linked line to the relevant changelog: the affected module's `<module>/changelog.md`, or the root `changelog.md` if the decision is global (constitution, contracts, tooling).

## Superseding

When a decision changes, the old ADR is never deleted and its body is never edited. Write a new ADR; update only the old ADR's frontmatter `status` field: `superseded → [[new-adr]]`.

## Retroactive Records

Decisions distilled from git history are written with a "retroactive record" note and evidence commit hashes. If the reason is unknown, never invent it — ask the user or skip.
