---
type: GlossaryTerm
id: https://w3id.org/lmodel/nist-sp-800-218/knowledge/glossary/ssdf-reference
genre: reference
title: Reference (SSDF)
description: In the SSDF, a pointer from a task to an established secure development practice document and to the parts of it the task maps to. The schema renders one as `SsdfReference`, with the document in `reference_document` and the parts in `mapped_items`.
definition: A pointer to an established secure development practice document and its mappings to a particular task.
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
    title: the class SsdfReference
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:21:05Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T09:17:17Z"
---

# Reference (SSDF)

NIST's project page defines a reference as a pointer to an established secure development practice document and its mappings to a particular task.[^ssdf] The schema renders one as `SsdfReference`, with the document in `reference_document`, a value of the enum `SsdfReferenceDocument`, and the parts of the document in `mapped_items`, such as `ID.GV-3` for the NIST Cybersecurity Framework. The enum holds the 29 documents SP 800-218 references.[^nist_sp_800_218.yaml]

[^ssdf]: <https://csrc.nist.gov/projects/ssdf>, the SSDF Practices section
[^nist_sp_800_218.yaml]: src/nist_sp_800_218/schema/nist_sp_800_218.yaml, the class SsdfReference
