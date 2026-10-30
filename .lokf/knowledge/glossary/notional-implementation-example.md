---
type: GlossaryTerm
id: https://w3id.org/lmodel/nist-sp-800-218/knowledge/glossary/notional-implementation-example
genre: reference
title: Notional implementation example
description: In the SSDF, a notional example of the types of tools, processes or other methods that could help implement a task; no example is required, and the examples are not the only options. The schema renders one as `SsdfImplementationExample`.
definition: A notional example of the types of tools, processes, or other methods that could be used to help implement a task.
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
    title: the class SsdfImplementationExample
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:21:05Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T09:17:17Z"
---

# Notional implementation example

NIST's project page defines a notional implementation example as a notional example of the types of tools, processes or other methods that could help implement a task. It adds that no example or combination of examples is required, and that the examples are not the only feasible options.[^ssdf] The schema renders one as `SsdfImplementationExample`, with the identifier NIST's reference data gives it in `example_id`, such as `PO.1.1.1`, and its text in `description`.[^nist_sp_800_218.yaml]

[^ssdf]: <https://csrc.nist.gov/projects/ssdf>, the SSDF Practices section
[^nist_sp_800_218.yaml]: src/nist_sp_800_218/schema/nist_sp_800_218.yaml, the class SsdfImplementationExample
