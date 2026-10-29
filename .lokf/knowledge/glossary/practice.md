---
type: GlossaryTerm
id: https://w3id.org/lmodel/nist-sp-800-218/knowledge/glossary/practice
genre: reference
title: Practice
description: "In the SSDF, a secure software development practice: a named outcome with a unique identifier, such as PO.1, and a short explanation of what it is and why it helps. The schema renders a practice as `SsdfPractice`, with its identifier in `practice_id`."
definition: "A secure software development practice: a name and a unique identifier, then a short explanation of what it is and why it is beneficial."
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
    title: the class SsdfPractice
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:21:05Z"
status: draft
---

# Practice

NIST's project page says that a practice is defined by its name and a unique identifier, then a short explanation of what it is and why it helps.[^ssdf] The schema renders a practice as `SsdfPractice`, with its identifier in `practice_id`, such as `PO.1`, and may hold its tasks in `practice_tasks`.[^nist_sp_800_218.yaml]

[^ssdf]: <https://csrc.nist.gov/projects/ssdf>, the SSDF Practices section
[^nist_sp_800_218.yaml]: src/nist_sp_800_218/schema/nist_sp_800_218.yaml, the class SsdfPractice
