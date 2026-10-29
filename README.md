<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# nist-sp-800-218

NIST SP 800-218 Secure Software Development Framework (SSDF) version 1.1 (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/nist-sp-800-218](https://lmodel.github.io/nist-sp-800-218)

## What it models

The Secure Software Development Framework (SSDF) version 1.1, which the National Institute of Standards and Technology (NIST) defines in [Special Publication (SP) 800-218](https://doi.org/10.6028/NIST.SP.800-218) of February 2022:

* **Practice groups** (`SsdfPracticeGroup`): the four groups that hold the practices, Prepare the Organization (PO), Protect Software (PS), Produce Well-Secured Software (PW) and Respond to Vulnerabilities (RV).
* **Practices** (`SsdfPractice`): the nineteen practices, each an outcome with an identifier such as `PO.1`.
* **Tasks** (`SsdfTask`): the forty-two actions that may be needed to perform a practice, each with an identifier such as `PO.1.1`. A task that version 1.1 moved keeps its former identifier.
* **Notional implementation examples** (`SsdfImplementationExample`): the 198 examples of tools, processes or methods that could help implement a task.
* **References** (`SsdfReference`): the 528 pointers from a task to the parts of an established secure development document. The enum `SsdfReferenceDocument` names the 29 documents.
* **The framework** (`SsdfFramework`): one SSDF version as a single document that holds all of these.

The schema header's `version` is the SSDF version, 1.1.0, as NIST's Cybersecurity and Privacy Reference Tool numbers it (`SP_800_218_1_1_0`). Its `source` is the publication's digital object identifier (DOI). NIST also publishes the framework as a catalog in the Open Security Controls Assessment Language (OSCAL). [src/nist_sp_800_218/schema/oscal-content/](src/nist_sp_800_218/schema/oscal-content) holds that catalog as usnistgov/oscal-content released it in v1.6.0, matched to the release by git object hash. `tests/test_upstream.py` derives the whole framework from the copy, validates it, and holds it to the counts above. A weekly workflow opens an issue when NIST registers the next final edition, changes the catalog, or the copy drifts.

NIST published SP 800-218 Revision 1, which defines SSDF version 1.2, as an initial public draft in December 2025. The schema follows final editions, so it does not model the draft. Release tags number the schema's versions.

## Influences

None beyond SP 800-218 itself: the schema renders one publication, and its release asset and governance files follow [lmodel/slsa](https://github.com/lmodel/slsa).

## Mappings

The schema crosses to two kinds of vocabulary and borrows from neither.

* **OSCAL**: NIST's catalog renders a practice group as an OSCAL group, a practice and a task as controls, an example as a part and a reference as a link. Each class names its counterpart in [lmodel/oscal](https://github.com/lmodel/oscal) in `broad_mappings`, because the OSCAL class is the more general one.
* **The documents SP 800-218 references**: `SsdfReferenceDocument` names the 29 documents that the SSDF maps its tasks to, at the editions it cites, with each document's address. They include NIST SP 800-53 Revision 5, the NIST Cybersecurity Framework 1.1 and Executive Order 14028. A reference's `mapped_items` holds the identifiers within the document, such as the control `SA-4` of SP 800-53.

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

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle, in the Linked Open Knowledge Format (LOKF). Its domain schema is `.lokf/nist-sp-800-218.yaml`, which `lokf adapt` writes from `src/nist_sp_800_218/schema/nist_sp_800_218.yaml`. Edit the source, never the copy. A release carries the copy as `schema-<tag>-nist-sp-800-218.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

`just lokf-adapt` rewrites the copy, and `just lokf-adapt-check` says when it is stale. `project.justfile` names the classes the copy roots on `Concept`, and a concept may name any of them as its `type`. In Obsidian, add these classes to the KTL Registrar and KTL Curator plugins' *Known LOKF types* setting:

```text
SsdfPracticeGroup, SsdfPractice, SsdfTask
```

A concept writes the SSDF identifier in `group_id`, `practice_id` or `task_id`. A task's concept names its practice's concept in `isPartOf`, and a practice's concept names its group's. A name and a description are the concept's own `title` and `description`.

A host imports the copy beside LOKF's schema, `lokf.yaml`, and beside other adapt copies. LinkML merges them into one namespace, where the last definition of a name wins silently. So no class, enum or type shares a name with LOKF's or with the copies of slsa, github-actions and oscal. A slot shares a name only where it carries LOKF's meaning and Internationalized Resource Identifier (IRI), as `title` and `description` do, so `lokf adapt` folds the two into LOKF's and renames nothing. The copy shares no other key with the three neighbours, and `tests/test_schema_rules.py` fails on a new shared name.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)).

SP 800-218 is a work of the United States Government and is not subject to copyright in the United States. The schema's descriptions are this project's own words. NIST's catalog in [src/nist_sp_800_218/schema/oscal-content/](src/nist_sp_800_218/schema/oscal-content) keeps NIST's licence beside it: see [NOTICE](NOTICE).

This is not an official NIST project, and its use implies no endorsement by NIST.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
