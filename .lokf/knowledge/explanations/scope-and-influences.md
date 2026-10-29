---
type: Explanation
id: https://w3id.org/lmodel/nist-sp-800-218/knowledge/explanations/scope-and-influences
genre: explanation
title: Scope, influences and mappings
description: "What the schema renders and what it leaves out: the SSDF version 1.1 of SP 800-218 and nothing beyond it, with lmodel/slsa as its one influence on layout. It maps its classes to lmodel/oscal's, as NIST's catalog renders them, and names the 29 documents SP 800-218 references; it models neither the retired identifiers, SP 800-218A nor the draft of version 1.2."
resource: README.md
about:
  - https://w3id.org/lmodel/nist-sp-800-218/knowledge/datasets/nist-sp-800-218-linkml-schema
sources:
  - id: readme.md
    resource: README.md
    title: the What it models, Influences, Mappings and Not modelled here sections
  - id: changelog.md
    resource: CHANGELOG.md
    title: the Changed entries
  - id: about.md
    resource: docs/about.md
    title: the section on what is left out
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:21:05Z"
status: draft
---

# Scope, influences and mappings

The schema renders one publication, SP 800-218, at one final edition, SSDF version 1.1. The README's Influences section says that nothing beyond SP 800-218 shaped it, and that its release asset and governance files follow lmodel/slsa.[^readme.md]

## Why the SSDF's own elements

The schema models the practice group, the practice, the task, the notional implementation example and the reference, which [the glossary](../glossary/index.md) defines. The changelog says that it replaced classes copied from the shape of an OSCAL catalog. Those classes shared names with LOKF's and lmodel/oscal's, and their `class_uri: linkml:Any` let a catalog with any keys validate.[^changelog.md] NIST's catalog in OSCAL stays in the repository as the upstream copy that the tests read.

## Mappings

The README says that the schema crosses to two kinds of vocabulary and borrows from neither. NIST's catalog renders a practice group as an OSCAL group, a practice and a task as controls, an example as a part and a reference as a link, so each class names its lmodel/oscal counterpart in `broad_mappings`. The OSCAL class is the more general one. The enum `SsdfReferenceDocument` names the 29 documents SP 800-218 maps its tasks to, at the editions it cites, and a reference's `mapped_items` holds the identifiers within such a document, such as the control `SA-4` of SP 800-53.

## Not modelled here

- the practice `PW.3` and the tasks version 1.1 retired, except as a moved task's former identifier, since NIST's catalog leaves them out;
- SP 800-218A and the other SSDF community profiles;
- the draft of SSDF version 1.2;
- the publication's prose outside its table.[^about.md]

[^readme.md]: README.md, the Influences, Mappings and Not modelled here sections
[^changelog.md]: CHANGELOG.md, the Changed entries under Unreleased
[^about.md]: docs/about.md, What is left out
