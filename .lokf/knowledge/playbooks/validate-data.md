---
type: Playbook
id: https://w3id.org/lmodel/nist-sp-800-218/knowledge/playbooks/validate-data
genre: how-to
title: Validate data against the schema
description: "How to validate SSDF data with `linkml-validate` before loading it into the generated Python models, which check less: the dataclasses check no pattern, and the Pydantic models miss the identifier types' patterns. No check covers the nesting of identifiers or a repeated one."
resource: docs/index.md
about:
  - https://w3id.org/lmodel/nist-sp-800-218/knowledge/datasets/nist-sp-800-218-linkml-schema
sources:
  - id: docs-index.md
    resource: docs/index.md
    title: the Validating data section
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:21:05Z"
status: draft
---

# Validate data against the schema

Run `linkml-validate -s src/nist_sp_800_218/schema/nist_sp_800_218.yaml -C SsdfTask task.yaml`, naming the class the file holds. It checks the file against the JSON Schema the validator generates from the schema, and `tests/test_data.py` holds every example to the same check.[^docs-index.md]

Validate a file before loading it into either model in `src/nist_sp_800_218/datamodel/`. The page says that the models LinkML 1.10.0 generates check less:

- the dataclasses check required fields and enum values, but no pattern;
- the Pydantic models also check the patterns a field carries itself, such as the form of `ssdf_version`, but not the patterns of the four identifier types.

No check covers three rules: that each identifier starts with the identifier of what holds it, that a list never repeats an identifier, and that a former task identifier is one SP 800-218 retired. `tests/test_upstream.py` checks the first two over NIST's catalog of version 1.1.

[^docs-index.md]: docs/index.md, Validating data
