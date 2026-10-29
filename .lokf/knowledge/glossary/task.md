---
type: GlossaryTerm
id: https://w3id.org/lmodel/nist-sp-800-218/knowledge/glossary/task
genre: reference
title: Task
description: In the SSDF, an action that may be needed to perform a practice, with an identifier such as PO.1.1. The schema renders a task as `SsdfTask`, with its identifier in `task_id`, its examples, its references and any identifier it had before version 1.1.
definition: An action that may be needed to perform a practice.
resource: https://csrc.nist.gov/projects/ssdf
definedBy:
  - https://w3id.org/lmodel/nist-sp-800-218/knowledge/references/ssdf-project
relatedTo:
  - https://w3id.org/lmodel/nist-sp-800-218/knowledge/datasets/nist-sp-800-218-linkml-schema
sources:
  - id: ssdf
    resource: https://csrc.nist.gov/projects/ssdf
    title: the SSDF Practices section, read on 2026-10-29
  - id: nist_sp_800_218.yaml
    resource: src/nist_sp_800_218/schema/nist_sp_800_218.yaml
    title: the class SsdfTask
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:21:05Z"
status: draft
---

# Task

NIST's project page defines a task as an action that may be needed to perform a practice.[^ssdf] The schema renders a task as `SsdfTask`, with its identifier in `task_id`, such as `PO.1.1`. A task holds its notional implementation examples in `implementation_examples`, its references in `task_references`, and in `former_task_ids` the identifier it had before version 1.1 moved it.[^nist_sp_800_218.yaml]

[^ssdf]: <https://csrc.nist.gov/projects/ssdf>, the SSDF Practices section
[^nist_sp_800_218.yaml]: src/nist_sp_800_218/schema/nist_sp_800_218.yaml, the class SsdfTask
