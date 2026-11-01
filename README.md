<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# nist-sp-800-218

NIST SP 800-218 Secure Software Development Framework (SSDF) version 1.1 (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/nist-sp-800-218](https://lmodel.github.io/nist-sp-800-218)

## What it models

The schema models the Secure Software Development Framework (SSDF) version 1.1, which the National Institute of Standards and Technology (NIST) defines in [Special Publication (SP) 800-218](https://doi.org/10.6028/NIST.SP.800-218) of February 2022. The schema holds the four practice groups (`SsdfPracticeGroup`), nineteen practices (`SsdfPractice`) and forty-two tasks (`SsdfTask`), with the implementation examples and the references to secure development documents that each task carries.

[src/nist_sp_800_218/schema/oscal-content/](src/nist_sp_800_218/schema/oscal-content) holds NIST's catalog of the framework in the Open Security Controls Assessment Language (OSCAL), from usnistgov/oscal-content v1.6.0, and `tests/test_upstream.py` derives the whole framework from it. A weekly workflow opens an issue when NIST registers the next final edition, changes the catalog, or the copy drifts. The schema follows final editions, so it does not model the December 2025 draft of SP 800-218 Revision 1.

## Mappings

* **OSCAL**: each class names its counterpart in [lmodel/oscal](https://github.com/lmodel/oscal) in `broad_mappings`: a practice group is a group, a practice and a task are controls, and an example is a part.
* **Referenced documents**: `SsdfReferenceDocument` names the 29 documents the SSDF maps its tasks to, and a reference's `mapped_items` holds the identifiers within one, such as the control `SA-4` of SP 800-53.

## Not modelled here

* The practice and the tasks that version 1.1 retired, such as `PW.3`, except as a moved task's former identifier. NIST's catalog leaves them out.
* SP 800-218A, the SSDF community profile for generative artificial intelligence (AI) and dual-use foundation models, and the other community profiles.
* The draft of SSDF version 1.2.
* The rules no pattern can check, which [docs/index.md](docs/index.md) lists.

## Repository Structure

* [docs/](docs/): the website's pages, with the generated schema pages in [elements/](docs/elements/)
* [examples/](examples/): usage examples
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the upstream watch
* [src/nist_sp_800_218/schema/](src/nist_sp_800_218/schema): the LinkML schema, `nist_sp_800_218.yaml` (edit this), and NIST's catalog copy
* [src/nist_sp_800_218/datamodel/](src/nist_sp_800_218/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data in [data/](tests/data) and the neighbours' adapt copies in [neighbours/](tests/neighbours)
* [website/](website/): the Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Run `just` to list the project's [just](https://github.com/casey/just/) recipes.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle. Its domain schema, `.lokf/nist-sp-800-218.yaml`, is the copy `just lokf-adapt` writes from `src/nist_sp_800_218/schema/nist_sp_800_218.yaml`, and `just lokf-adapt-check` says when it is stale. Edit the source, never the copy. A release carries the copy as `schema-<tag>-nist-sp-800-218.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

The copy roots these classes on `Concept`, so a concept may name any of them as its `type`. In Obsidian, add them to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins:

```text
SsdfPracticeGroup, SsdfPractice, SsdfTask
```

A concept writes the SSDF identifier in `group_id`, `practice_id` or `task_id`. A task's concept names its practice's concept in `isPartOf`, and a practice's concept names its group's.

No class, enum or type of the copy shares a name with LOKF's schema or with another lmodel copy, and `tests/test_schema_rules.py` fails on a new shared name.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)), and the knowledge bundle in `.lokf/knowledge/` is under CC BY 4.0.

SP 800-218 is a work of the United States Government and is not subject to copyright in the United States. The schema's descriptions are this project's own words, and NIST's catalog keeps NIST's licence beside it: see [NOTICE](NOTICE). This is not an official NIST project, and its use implies no endorsement by NIST.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
