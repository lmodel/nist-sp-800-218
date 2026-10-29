---
type: GlossaryTerm
id: https://w3id.org/lmodel/nist-sp-800-218/knowledge/glossary/practice-group
genre: reference
title: Practice group
description: "In the SSDF, one of the four groups its practices are organized into: Prepare the Organization (PO), Protect the Software (PS), Produce Well-Secured Software (PW) and Respond to Vulnerabilities (RV). The schema renders a group as `SsdfPracticeGroup`, with its two letters in `group_id`."
definition: One of the four groups the SSDF organizes its practices into, each named by two letters.
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
    title: the class SsdfPracticeGroup
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:21:05Z"
status: draft
---

# Practice group

NIST's project page names the four groups.[^ssdf] The schema renders a group as `SsdfPracticeGroup`, with its two letters in `group_id`, and may hold the group's practices in `group_practices`.[^nist_sp_800_218.yaml] In a knowledge bundle a practice names its group with `isPartOf` instead. The bundle describes each group under [practice groups](../practice-groups/index.md).

[^ssdf]: <https://csrc.nist.gov/projects/ssdf>, the SSDF Practices section
[^nist_sp_800_218.yaml]: src/nist_sp_800_218/schema/nist_sp_800_218.yaml, the class SsdfPracticeGroup
