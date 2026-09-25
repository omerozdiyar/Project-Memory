---
type: state
module: global
updated: YYYY-MM-DD
---

# Active Context — Now (one file per contributor)

This folder holds the **present-tense** state: what each person/agent is working on right now, and their active locks.

## How it works (constitution rule 9)

- Each contributor keeps their own file here: `activeContext/<your-name>.md` (copy `_contributor-template.md` to start).
- You write **only your own file** — so there is no shared file to cause merge conflicts.
- **Before locking a module, read every file in this folder.** If someone else holds an active lock on the same module, ask the user before starting.
- When a task is done, clear it from your file and release the lock. This folder shows "now" — leave nothing stale.

## Why per-person (and not per-module)?

"Who is doing what right now" is inherently personal and short-lived. Splitting it per person means nobody edits anybody else's file, yet reading the whole folder still gives the full coordination picture. (Durable history is the opposite: it is split per *module* — see the module changelogs.)

## Active contributors

<!-- optional: list contributor files for humans, e.g. -->
<!-- - [[activeContext/omer]] -->
<!-- - [[activeContext/oguz]] -->
