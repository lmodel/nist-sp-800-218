---
type: Explanation
id: https://w3id.org/lmodel/nist-sp-800-218/knowledge/explanations/element-names
genre: explanation
title: Element names and the shared namespace
description: "How the schema names its elements so that its adapt copy can sit beside LOKF's schema and the slsa, github-actions and oscal copies: classes with the `Ssdf` prefix, NIST's identifiers and reference labels kept as written, `title` and `description` carrying LOKF's IRIs, and no other key shared, which `tests/test_schema_rules.py` checks."
resource: docs/about.md
about:
  - https://w3id.org/lmodel/nist-sp-800-218/knowledge/datasets/nist-sp-800-218-linkml-schema
sources:
  - id: about.md
    resource: docs/about.md
    title: the naming paragraphs
  - id: readme.md
    resource: README.md
    title: the Knowledge Trust Ladder (KTL) section
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: SHARED_WITH_NEIGHBOURS and the name tests
  - id: linkmllint.yaml
    resource: .linkmllint.yaml
    title: the standard_naming setting and its comment
generated:
  by: process:ktl-librarian
  at: "2026-10-30T09:17:17Z"
status: draft
---

# Element names and the shared namespace

Element names are the schema's own. Classes carry the `Ssdf` prefix, such as `SsdfPractice`, so that they can be imported beside other vocabularies. Slots are snake_case, and the identifiers keep the form NIST gives them, such as `PO.1.1`.[^about.md] Every element is in the `nist_sp_800_218:` namespace, `https://w3id.org/lmodel/nist-sp-800-218/`.

The values of `SsdfReferenceDocument` keep the labels SP 800-218 gives its references, such as `BSAFSS` and `SP80053`, so that a reference compares with NIST's catalog without translating. `.linkmllint.yaml` therefore asks the `standard_naming` rule for permissible values in upper case, and keeps the rule at error level.[^linkmllint.yaml]

## Beside other schemas

A host imports the adapt copy beside LOKF's `lokf.yaml` and other adapt copies, and LinkML merges them into one namespace, where the last definition of a name wins silently. The README says that no class, enum or type therefore shares a name with LOKF's or with the copies of slsa, github-actions and oscal. A slot shares a name only where it carries LOKF's meaning and IRI, as `title` and `description` do, so `lokf adapt` folds the two into LOKF's and renames nothing.[^readme.md]

`tests/test_schema_rules.py` checks the copy against `lokf.yaml` and the schema assets of slsa v0.7.0, github-actions v0.2.1 and oscal v0.1.0. Its list of keys shared with each neighbour is empty, so a new shared key fails the test, and it checks that every `oscal:` mapping names a class of the oscal copy, by the IRI a renamed class keeps.[^test_schema_rules.py]

[^about.md]: docs/about.md, the paragraph on element names
[^linkmllint.yaml]: .linkmllint.yaml, the comment and the standard_naming rule
[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
[^test_schema_rules.py]: tests/test_schema_rules.py, NEIGHBOURS and SHARED_WITH_NEIGHBOURS
