---
type: SsdfPracticeGroup
id: https://w3id.org/lmodel/nist-sp-800-218/knowledge/practice-groups/produce-well-secured-software
title: Produce Well-Secured Software
description: "The SSDF practice group PW, Produce Well-Secured Software: the organization produces software with few security vulnerabilities in its releases. It holds eight practices, PW.1, PW.2 and PW.4 to PW.9, and sixteen tasks."
group_id: PW
resource: src/nist_sp_800_218/schema/oscal-content/NIST_SP800-218_ver1_catalog.json
definedBy:
  - https://w3id.org/lmodel/nist-sp-800-218/knowledge/references/sp-800-218
relatedTo:
  - https://w3id.org/lmodel/nist-sp-800-218/knowledge/glossary/practice-group
sources:
  - id: nist_sp800-218_ver1_catalog.json
    resource: src/nist_sp_800_218/schema/oscal-content/NIST_SP800-218_ver1_catalog.json
    title: the group PW
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:21:05Z"
status: draft
---

# Produce Well-Secured Software (PW)

The catalog's overview of the group says that an organization should produce well-secured software with minimal security vulnerabilities in its releases.[^nist_sp800-218_ver1_catalog.json] The group holds 8 practices and 16 tasks in SSDF version 1.1:

- `PW.1` Design Software to Meet Security Requirements and Mitigate Security Risks: 3 tasks
- `PW.2` Review the Software Design to Verify Compliance with Security Requirements and Risk Information: 1 task
- `PW.4` Reuse Existing, Well-Secured Software When Feasible Instead of Duplicating Functionality: 3 tasks
- `PW.5` Create Source Code by Adhering to Secure Coding Practices: 1 task
- `PW.6` Configure the Compilation, Interpreter, and Build Processes to Improve Executable Security: 2 tasks
- `PW.7` Review and/or Analyze Human-Readable Code to Identify Vulnerabilities and Verify Compliance with Security Requirements: 2 tasks
- `PW.8` Test Executable Code to Identify Vulnerabilities and Verify Compliance with Security Requirements: 2 tasks
- `PW.9` Configure Software to Have Secure Settings by Default: 2 tasks

The catalog holds no practice `PW.3`. It marks task `PW.1.3` as formerly `PW.4.3`, and the tasks of `PW.4` are `PW.4.1`, `PW.4.2` and `PW.4.4`.

[^nist_sp800-218_ver1_catalog.json]: src/nist_sp_800_218/schema/oscal-content/NIST_SP800-218_ver1_catalog.json, the group PW
