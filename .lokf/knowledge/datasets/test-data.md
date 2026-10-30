---
type: Dataset
id: https://w3id.org/lmodel/nist-sp-800-218/knowledge/datasets/test-data
genre: reference
title: Test data and tests
description: "The schema's tests: seven valid examples and nineteen counter-examples under `tests/data/`, `tests/test_data.py`, which holds each to the validator, `tests/test_upstream.py`, which derives the framework from NIST's catalog, `tests/test_watch.py`, which runs the upstream watch against a stubbed upstream, and `tests/test_schema_rules.py`, which holds the adapt copy apart from LOKF and the slsa, github-actions and oscal copies in `tests/neighbours/`."
resource: tests
sources:
  - id: data
    resource: tests/data
    title: the valid and invalid examples
  - id: test_data.py
    resource: tests/test_data.py
    title: the data tests
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: the derivation and the counts
  - id: test_watch.py
    resource: tests/test_watch.py
    title: the watch against a stubbed upstream
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: the neighbours and their checksums
  - resource: tests/neighbours
    title: the three released adapt copies
  - resource: tests/data/README.md
    title: the naming rule
generated:
  by: process:ktl-librarian
  at: "2026-10-30T09:17:17Z"
status: draft
---

# Test data and tests

`tests/data/valid/` holds seven examples, one for each class and two for `SsdfTask`, and `tests/data/invalid/` holds nineteen counter-examples, each invalid for one reason.[^data] A file's class is the part of its name before the first hyphen, such as `SsdfTask-identifier-only.yaml`, and a counter-example's first line, `# Fails at:`, names the place in the data where it breaks the schema. The counter-examples break each constraint the schema states:

- a missing required field;
- an identifier of the wrong form;
- an unknown practice group;
- a reference to a document SP 800-218 does not cite;
- blank mapped items;
- a key the class does not declare.

`tests/test_data.py` loads each valid example into the dataclasses, holds each to the validator, which must pass a valid example and fail a counter-example at the place its first line names, and checks that every class has an example.[^test_data.py] `tests/test_upstream.py` derives the whole of version 1.1 from NIST's catalog copy and holds it to the validator and to the publication's counts, as [NIST's SSDF catalog copy](ssdf-catalog-copy.md) says.[^test_upstream.py] `tests/test_watch.py` runs `scripts/check_upstream_release.py` against answers it builds itself, with no network: a release that drops the catalog's folder, a network failure, a file NIST adds, a moved tag and a changed licence.[^test_watch.py]

`tests/test_schema_rules.py` checks the adapt copy against LOKF's `lokf.yaml` and three neighbours: the schema assets of lmodel/slsa v0.7.0, lmodel/github-actions v0.2.1 and lmodel/oscal v0.1.0, each pinned by its SHA-256 checksum.[^test_schema_rules.py] No class, enum, type or subset may share a name, and the copy shares no key with a neighbour. The test also checks that the copy roots exactly the three concept classes, that every mapping uses a prefix the copy binds, and that every `oscal:` mapping names a class of lmodel/oscal's copy. `just test` runs the tests, generates the project into `tmp/`, and runs the examples through `linkml-run-examples`.

[^data]: tests/data, valid/ and invalid/
[^test_data.py]: tests/test_data.py, the four tests
[^test_upstream.py]: tests/test_upstream.py, the tests and COUNTS
[^test_watch.py]: tests/test_watch.py, the stubbed upstream and its six tests
[^test_schema_rules.py]: tests/test_schema_rules.py, NEIGHBOURS and the tests
