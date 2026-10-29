---
type: SsdfPracticeGroup
id: https://w3id.org/lmodel/nist-sp-800-218/knowledge/practice-groups/protect-software
title: Protect Software
description: "The SSDF practice group PS, Protect Software: the organization protects every component of its software from tampering and unauthorized access. It holds the practices PS.1 to PS.3 and four tasks."
group_id: PS
resource: src/nist_sp_800_218/schema/oscal-content/NIST_SP800-218_ver1_catalog.json
definedBy:
  - https://w3id.org/lmodel/nist-sp-800-218/knowledge/references/sp-800-218
relatedTo:
  - https://w3id.org/lmodel/nist-sp-800-218/knowledge/glossary/practice-group
sources:
  - id: nist_sp800-218_ver1_catalog.json
    resource: src/nist_sp_800_218/schema/oscal-content/NIST_SP800-218_ver1_catalog.json
    title: the group PS
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:21:05Z"
status: draft
---

# Protect Software (PS)

The catalog's overview of the group says that an organization should protect all components of its software from tampering and unauthorized access.[^nist_sp800-218_ver1_catalog.json] The group holds 3 practices and 4 tasks in SSDF version 1.1:

- `PS.1` Protect All Forms of Code from Unauthorized Access and Tampering: 1 task
- `PS.2` Provide a Mechanism for Verifying Software Release Integrity: 1 task
- `PS.3` Archive and Protect Each Software Release: 2 tasks

Task `PS.3.2` is about collecting, safeguarding, maintaining and sharing the provenance data of every component of a release.

[^nist_sp800-218_ver1_catalog.json]: src/nist_sp_800_218/schema/oscal-content/NIST_SP800-218_ver1_catalog.json, the group PS
