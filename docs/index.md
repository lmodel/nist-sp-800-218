# nist-sp-800-218

This project is a LinkML model of the Secure Software Development Framework
(SSDF) version 1.1, which the National Institute of Standards and Technology
(NIST) defines in Special Publication (SP) 800-218. It covers the practice
groups, practices and tasks, the notional implementation examples of each task,
and the references that map each task to other secure software development
documents.

- [Schema documentation](elements/index.md), generated from the schema
- [About](about.md): how the elements are named and what the model leaves out
- [`nist_sp_800_218.yaml`](schema/nist_sp_800_218.yaml): the schema

## Validating data

`linkml-validate -s src/nist_sp_800_218/schema/nist_sp_800_218.yaml -C SsdfTask task.yaml`
checks a file against the JSON Schema generated from the schema, and
`tests/test_data.py` holds every example to it.

Validate a file before loading it into either model in
`src/nist_sp_800_218/datamodel/`. LinkML 1.10.0 generates models that check
less:

- The dataclasses check required fields and enum values, but no pattern.
- The Pydantic models also check the patterns a field carries itself, such as
  the form of `ssdf_version`. They do not check the patterns of the four
  identifier types, so a group, practice, task or example identifier goes
  unchecked.

No check covers these rules:

- that a practice's identifier starts with its group's, a task's with its
  practice's, and an example's with its task's;
- that a list never repeats an identifier;
- that a former task identifier is one that SP 800-218 retired.

`tests/test_upstream.py` checks the first two over NIST's catalog of version
1.1.
