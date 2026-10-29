# About nist-sp-800-218

This page is for anyone reading the [LinkML](https://linkml.io) schema's
elements: it says how they are named and what the model leaves out.

The Secure Software Development Framework (SSDF) defines four elements for each
practice. A practice has a name, an identifier and an explanation. A task is an
action that may be needed to perform it. A notional implementation example
suggests a way to implement a task. A reference points from a task to an
established secure development document. The schema gives each a class, and
holds them under one of four practice groups.

Element names are the schema's own. Classes carry the `Ssdf` prefix
(`SsdfPractice`, `SsdfTask`) so they can be imported beside other vocabularies.
Slots are snake_case. The identifiers keep the form that the National Institute
of Standards and Technology (NIST) gives them, such as `PO.1.1`.
The permissible values of `SsdfReferenceDocument` keep the labels the
publication gives its references, such as `BSAFSS` and `SP80053`. Every element
is in the `nist_sp_800_218:` namespace
(`https://w3id.org/lmodel/nist-sp-800-218/`).

The descriptions are this project's own words. NIST's own text of each
practice, task and example stays in NIST's catalog, which the repository keeps
beside the schema.

## What is left out

The schema models the practices and tasks of the version, not the practice and
tasks that version 1.1 retired, which NIST's catalog also leaves out. A moved
task records its former identifier. The schema holds none of the publication's prose
outside the table, and no community profile, such as Special Publication
800-218A for generative artificial intelligence models.

## Reference

- [Special Publication 800-218 on NIST's site](https://csrc.nist.gov/pubs/sp/800/218/final)
- [The SSDF project](https://csrc.nist.gov/projects/ssdf)
- [NIST's SSDF catalog in the Open Security Controls Assessment Language](https://github.com/usnistgov/oscal-content/tree/v1.6.0/nist.gov/SP800-218/ver1)
