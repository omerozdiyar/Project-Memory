---
type: contract
module: global
updated: YYYY-MM-DD
---

# Contracts Between Modules

Every interface between modules (API, data schema, event, error format) is defined here.
A contract change requires an ADR and must be reflected in the state files of every affected module (see [[constitution]] rule 8).

## Active Contracts

<!-- filled during bootstrap -->

## Contract Template

```markdown
### <contract-name> (<producer-module> → <consumer-module>)
- **Interface:** (endpoint / function / event / file)
- **Request / Input:** (schema, types, required fields)
- **Response / Output:** (schema, types)
- **Error cases:** (codes, formats, behavior the consumer must expect)
- **Decision record:** [[related-adr]]
```
