---
type: Dataset
id: https://w3id.org/lmodel/nist-sp-800-218/knowledge/datasets/nist-sp-800-218-linkml-schema
genre: reference
title: nist-sp-800-218 LinkML schema
description: "The LinkML schema of the Secure Software Development Framework (SSDF) version 1.1, `src/nist_sp_800_218/schema/nist_sp_800_218.yaml` (schema id `https://w3id.org/lmodel/nist-sp-800-218`, version 1.1.0): six classes, one enum of reference documents and four identifier types. Its `lokf adapt` copy `.lokf/nist-sp-800-218.yaml`, rooted on the practice group, the practice and the task, is the bundle's domain schema."
resource: src/nist_sp_800_218/schema/nist_sp_800_218.yaml
version: 1.1.0
license: Apache-2.0
derivedFrom:
  - https://w3id.org/lmodel/nist-sp-800-218/knowledge/references/sp-800-218
  - https://w3id.org/lmodel/nist-sp-800-218/knowledge/datasets/ssdf-catalog-copy
sources:
  - id: nist_sp_800_218.yaml
    resource: src/nist_sp_800_218/schema/nist_sp_800_218.yaml
    title: the header, the classes, the enum and the types
  - id: readme.md
    resource: README.md
    title: the What it models and Knowledge Trust Ladder (KTL) sections
  - id: project.justfile
    resource: project.justfile
    title: the lokf-adapt recipes and their roots
  - id: nist-sp-800-218.yaml
    resource: .lokf/nist-sp-800-218.yaml
    title: the notes lokf adapt wrote
  - resource: .lokf/justfile
    title: the schema line
  - resource: .lokf/pyproject.toml
    title: the tool.lokf table
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:21:05Z"
status: draft
---

# nist-sp-800-218 LinkML schema

`src/nist_sp_800_218/schema/nist_sp_800_218.yaml` is the schema, titled "Secure Software Development Framework (SSDF) version 1.1". Its header gives `version: 1.1.0`, the SSDF version, and `source: https://doi.org/10.6028/NIST.SP.800-218`, the digital object identifier of NIST Special Publication (SP) 800-218.[^nist_sp_800_218.yaml] Its annotations name the identifier NIST's Cybersecurity and Privacy Reference Tool gives the version, `SP_800_218_1_1_0`, the publication date `2022-02`, and the usnistgov/oscal-content tag `v1.6.0` and commit `f0de6d8d8c059d374f15e0ae07508d82e370fc1d` of the catalog copy. A comment says that `scripts/check_upstream_release.py` reads the same pins, and that the release tags are the schema's own versions. The schema declares the prefix `nist_sp_800_218:` as `https://w3id.org/lmodel/nist-sp-800-218/` and the license Apache-2.0, and it imports only `linkml:types`.

## Classes

- **`SsdfFramework`** is the tree root: one SSDF version as a whole. It requires `ssdf_version`, two numbers such as `1.1`, and `practice_groups`.
- **`SsdfPracticeGroup`** is one of the four practice groups. It requires `group_id`, two letters out of `PO`, `PS`, `PW` and `RV`, and it may hold its practices in `group_practices`.
- **`SsdfPractice`** is a practice. It requires `practice_id`, such as `PO.1`, and it may hold its tasks in `practice_tasks`.
- **`SsdfTask`** is a task. It requires `task_id`, such as `PO.1.1`, and it may hold `former_task_ids`, `implementation_examples` and `task_references`.
- **`SsdfImplementationExample`** is a notional implementation example. It requires `example_id`, such as `PO.1.1.1`, and a `description`.
- **`SsdfReference`** points from a task to a document. It requires `reference_document`, a value of the enum, and `mapped_items`, the parts of the document the task maps to.

The enum `SsdfReferenceDocument` holds the 29 documents SP 800-218 references, each by the label the publication gives it, such as `BSAFSS` or `SP80053`, with the document's title and address. Four types hold the forms of the identifiers: `ssdf_group_identifier`, `ssdf_practice_identifier`, `ssdf_task_identifier` and `ssdf_example_identifier`, each with a pattern. The schema's slots `title` and `description` carry the IRIs `schema:name` and `schema:description`.

## Mappings

Each class but the framework names a class of lmodel/oscal in `broad_mappings`: `oscal:Group` for the practice group, `oscal:Control` for the practice and the task, `oscal:Part` for the example and `oscal:Link` for the reference. A comment in the header says that NIST's catalog renders the elements that way. [Scope, influences and mappings](../explanations/scope-and-influences.md) says more.

## As the bundle's domain schema

A LOKF domain schema is a LinkML schema that imports LOKF's own `lokf.yaml` and adds a host's classes and keys, so that `lokf validate` checks the concepts typed with them. The README says that this bundle's domain schema is `.lokf/nist-sp-800-218.yaml`, which `lokf adapt` writes from the schema. Edit the source, never the copy.[^readme.md] The `schema :=` line of `.lokf/justfile` and the `[tool.lokf]` table of `.lokf/pyproject.toml` both name the copy.

`project.justfile` passes three roots to `lokf adapt`: `SsdfPracticeGroup`, `SsdfPractice` and `SsdfTask`. Its comment says that these are the three elements that SP 800-218 gives an identifier and that other documents cite, and that an example and a reference stay inlined in their task.[^project.justfile] The copy's notes say that `lokf adapt` re-rooted the three classes on `lokf:Concept` and folded `title` and `description` into LOKF's slots.[^nist-sp-800-218.yaml] The copy renames nothing, and `SsdfFramework` is no longer a tree root in it. The concepts under `practice-groups/` in this bundle are typed `SsdfPracticeGroup`.

The generated models, `project/` and the adapt copy come from this file: see [Generated artefacts](generated-artefacts.md). [Element names and the shared namespace](../explanations/element-names.md) says why no class, enum or type shares a name with LOKF's or a neighbour's.

[^nist_sp_800_218.yaml]: src/nist_sp_800_218/schema/nist_sp_800_218.yaml, the header and the classes
[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
[^project.justfile]: project.justfile, the knowledge bundle recipes
[^nist-sp-800-218.yaml]: .lokf/nist-sp-800-218.yaml, the notes
