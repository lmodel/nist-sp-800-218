---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: https://w3id.org/lmodel/nist-sp-800-218/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: nist-sp-800-218 Knowledge Bundle
description: NIST SP 800-218 Secure Software Development Framework (SSDF) version 1.1 (LinkML)
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Person
  id: https://w3id.org/lmodel/nist-sp-800-218/knowledge/person/noel-mcloughlin
  name: Noel McLoughlin
---

# nist-sp-800-218 Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for nist-sp-800-218. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

# Services

* [Documentation site](services/documentation-site.md) - The Astro Starlight site in `website/`, for <https://lmodel.github.io/nist-sp-800-218>: the README as its home page, the pages of `docs/`, the schema's element pages, a page per concept of this bundle with its trust label, and the bundle's exports, built and published by Knowledge website.

# Datasets

* [nist-sp-800-218 LinkML schema](datasets/nist-sp-800-218-linkml-schema.md) - The LinkML schema of the Secure Software Development Framework (SSDF) version 1.1, `src/nist_sp_800_218/schema/nist_sp_800_218.yaml` (schema id `https://w3id.org/lmodel/nist-sp-800-218`, version 1.1.0): six classes, one enum of reference documents and four identifier types. Its `lokf adapt` copy `.lokf/nist-sp-800-218.yaml`, rooted on the practice group, the practice and the task, is the bundle's domain schema.
* [NIST's SSDF catalog copy](datasets/ssdf-catalog-copy.md) - NIST's catalog of SP 800-218 version 1.1 in the Open Security Controls Assessment Language (OSCAL), copied with NIST's licence from usnistgov/oscal-content v1.6.0 into `src/nist_sp_800_218/schema/oscal-content/` and matched to that release by git object hash. The tests derive the whole framework from it.
* [Generated artefacts](datasets/generated-artefacts.md) - What the LinkML generators and `lokf adapt` write from the schema: `project/` (JSON Schema, OWL, SHACL, ShEx, JSON-LD, GraphQL, protobuf, SQL, TypeScript, Excel and Java), the Python dataclasses and Pydantic models in `src/nist_sp_800_218/datamodel/`, `docs/schema/` and `docs/elements/`, and `.lokf/nist-sp-800-218.yaml`. None is edited by hand.
* [Test data and tests](datasets/test-data.md) - The schema's tests: seven valid examples and nineteen counter-examples under `tests/data/`, `tests/test_data.py`, which holds each to the validator, `tests/test_upstream.py`, which derives the framework from NIST's catalog, and `tests/test_schema_rules.py`, which holds the adapt copy apart from LOKF and the slsa, github-actions and oscal copies in `tests/neighbours/`.

# References

* [NIST SP 800-218, SSDF version 1.1](references/sp-800-218.md) - NIST Special Publication 800-218, Secure Software Development Framework (SSDF) Version 1.1 (February 2022, <https://doi.org/10.6028/NIST.SP.800-218>), the final edition the schema renders. SP 800-218 Revision 1, which defines SSDF version 1.2, is an initial public draft of December 2025.
* [NIST's SSDF project page](references/ssdf-project.md) - NIST's project page for the SSDF, <https://csrc.nist.gov/projects/ssdf>: it defines the four elements of each practice (the practice, the task, the notional implementation example and the reference) and names the four practice groups.

# Explanations

* [Scope, influences and mappings](explanations/scope-and-influences.md) - What the schema renders and what it leaves out: the SSDF version 1.1 of SP 800-218 and nothing beyond it, with lmodel/slsa as its one influence on layout. It maps its classes to lmodel/oscal's, as NIST's catalog renders them, and names the 29 documents SP 800-218 references; it models neither the retired identifiers, SP 800-218A nor the draft of version 1.2.
* [Element names and the shared namespace](explanations/element-names.md) - How the schema names its elements so that its adapt copy can sit beside LOKF's schema and the slsa, github-actions and oscal copies: classes with the `Ssdf` prefix, NIST's identifiers and reference labels kept as written, `title` and `description` carrying LOKF's IRIs, and no other key shared, which `tests/test_schema_rules.py` checks.

# Glossary

* [Practice group](glossary/practice-group.md) - In the SSDF, one of the four groups its practices are organized into: Prepare the Organization (PO), Protect the Software (PS), Produce Well-Secured Software (PW) and Respond to Vulnerabilities (RV). The schema renders a group as `SsdfPracticeGroup`, with its two letters in `group_id`.
* [Practice](glossary/practice.md) - In the SSDF, a secure software development practice: a named outcome with a unique identifier, such as PO.1, and a short explanation of what it is and why it helps. The schema renders a practice as `SsdfPractice`, with its identifier in `practice_id`.
* [Task](glossary/task.md) - In the SSDF, an action that may be needed to perform a practice, with an identifier such as PO.1.1. The schema renders a task as `SsdfTask`, with its identifier in `task_id`, its examples, its references and any identifier it had before version 1.1.
* [Notional implementation example](glossary/notional-implementation-example.md) - In the SSDF, a notional example of the types of tools, processes or other methods that could help implement a task; no example is required, and the examples are not the only options. The schema renders one as `SsdfImplementationExample`.
* [Reference (SSDF)](glossary/ssdf-reference.md) - In the SSDF, a pointer from a task to an established secure development practice document and to the parts of it the task maps to. The schema renders one as `SsdfReference`, with the document in `reference_document` and the parts in `mapped_items`.

# Practice-groups

* [Prepare the Organization](practice-groups/prepare-the-organization.md) - The SSDF practice group PO, Prepare the Organization: the organization readies its people, processes and technology for secure software development. It holds the practices PO.1 to PO.5 and thirteen tasks.
* [Protect Software](practice-groups/protect-software.md) - The SSDF practice group PS, Protect Software: the organization protects every component of its software from tampering and unauthorized access. It holds the practices PS.1 to PS.3 and four tasks.
* [Produce Well-Secured Software](practice-groups/produce-well-secured-software.md) - The SSDF practice group PW, Produce Well-Secured Software: the organization produces software with few security vulnerabilities in its releases. It holds eight practices, PW.1, PW.2 and PW.4 to PW.9, and sixteen tasks.
* [Respond to Vulnerabilities](practice-groups/respond-to-vulnerabilities.md) - The SSDF practice group RV, Respond to Vulnerabilities: the organization finds the vulnerabilities left in its releases, responds to them and prevents similar ones. It holds the practices RV.1 to RV.3 and nine tasks.

# Playbooks

* [Regenerate and test after a schema change](playbooks/regenerate-and-test.md) - How to change the schema and check it: `uv sync --group dev`, edit `src/nist_sp_800_218/schema/nist_sp_800_218.yaml`, then `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and the pre-commit hooks before a pull request.
* [Validate data against the schema](playbooks/validate-data.md) - How to validate SSDF data with `linkml-validate` before loading it into the generated Python models, which check less: the dataclasses check no pattern, and the Pydantic models miss the identifier types' patterns. No check covers the nesting of identifiers or a repeated one.
* [Update the upstream pins](playbooks/update-upstream-pins.md) - What to do when the weekly upstream watch reports that NIST registered the next final edition of SP 800-218, released a changed SSDF catalog in usnistgov/oscal-content, or that the copy drifted: replace the copy whole from one release, move the pins in `scripts/check_upstream_release.py` and the schema header, and run the tests.
* [Cut a release](playbooks/release.md) - How a release is made: Conventional Commits on `main`, an `## [Unreleased]` changelog section, the `v0.0.0` baseline tag that keeps the first release at 0.1.0, and `semantic-release.yml`, which tags the release and dispatches Knowledge Release to attach `schema-<tag>-nist-sp-800-218.yaml` once `KNOWLEDGE_RELEASE_ENABLED` is true.
* [Knowledge sources map](playbooks/knowledge-sources.md) - The librarian's scrape map: every repository location and external page this bundle derives concepts from, the concepts each yields, how to re-check each on a refresh run, and the paths left out on purpose.

# Policies

* [AI covenant](policies/ai-covenant.md) - The repository's rules for work done with artificial intelligence (AI): you own what you submit, an element under the schema renders SP 800-218 in the project's own words and cites it, NIST's catalog copy is never edited, and the scheduled librarian proposes changes only through reviewed pull requests.
* [License and attribution](policies/license-and-attribution.md) - The repository's licences: Apache 2.0 for the schema and the code, NIST's public-domain and CC0 terms for the SSDF catalog copy, NIST's statement that SP 800-218 is not subject to copyright in the United States, MIT for the copier template's scaffolding, and Apache 2.0 for the KTL sidecar and website templates.
* [Security policy](policies/security-policy.md) - How to report a vulnerability (GitHub's private vulnerability reporting), which release receives fixes (the latest), what executes in the repository and what holds each surface, and the three repository settings that are not yet in force.

# Workflows

* [Build and test (main.yaml)](workflows/main.md) - The Build and test workflow, `.github/workflows/main.yaml`: on a push to main and on every pull request, its test job runs `just test` on Python 3.10 to 3.14, and on 3.13 also `just lint` and `just lokf-adapt-check`, the check that `.lokf/nist-sp-800-218.yaml` is current.
* [Lint & docs (lint-and-docs.yaml)](workflows/lint-and-docs.md) - The Lint & docs workflow, `.github/workflows/lint-and-docs.yaml`: on a push to main, every pull request, a Monday 06:00 UTC schedule and by hand, four jobs run ShellCheck, actionlint, the word budgets of CONTRIBUTING.md (1000) and SECURITY.md (900), and markdownlint, lychee and codespell over the Markdown.
* [Upstream watch (upstream-watch.yaml)](workflows/upstream-watch.md) - The Upstream watch workflow, `.github/workflows/upstream-watch.yaml`: every Monday at 07:00 UTC and by hand, its ssdf-catalog job runs `scripts/check_upstream_release.py` against NIST's editions and usnistgov/oscal-content, and on a finding opens or updates the issue titled Upstream watch: NIST's SSDF has changed.
* [Semantic release (semantic-release.yml)](workflows/semantic-release.md) - The Semantic release workflow, `.github/workflows/semantic-release.yml`: on a pull request into main, its plan job checks that the commits, the changelog and the title would release and previews the release; on a push to main, its release job in the release Environment tags vX.Y.Z, publishes the GitHub release and dispatches Knowledge Release.
* [Knowledge Registrar (knowledge-registrar.yaml)](workflows/knowledge-registrar.md) - The Knowledge Registrar workflow, `.github/workflows/knowledge-registrar.yaml`: the gate on the knowledge bundle, run on pull requests that touch `.lokf/` or `knowledge_bundle/`, every Monday at 06:00 UTC and by hand; it validates the bundle and its relation targets against the domain schema, runs the conventions script, and checks that each new confirmation by a person is backed by an approval or a signed commit.
* [Knowledge Librarian (knowledge-librarian.yaml)](workflows/knowledge-librarian.md) - The Knowledge Librarian workflow, `.github/workflows/knowledge-librarian.yaml`: every Monday at 05:00 UTC and by hand, once `KNOWLEDGE_LIBRARIAN_ENABLED` is true, it runs an agent with the ktl-librarian skill (pinned by `TRUST_LADDER_SKILLS_REF` at v0.59.0) in a read-only job and opens a review pull request from a separate job that runs no agent.
* [Knowledge Release (knowledge-release.yaml)](workflows/knowledge-release.md) - The Knowledge Release workflow, `.github/workflows/knowledge-release.yaml`: dispatched with a release's tag, or started by a published release once `KNOWLEDGE_RELEASE_ENABLED` is true, it attaches the bundle zip, the domain schema as `schema-<tag>-nist-sp-800-218.yaml` with its checksum, and the Copilot skills to the release, when the bundle or the schema changed or `force` is set.
* [Knowledge sync (knowledge-sync.yaml)](workflows/knowledge-sync.md) - The Knowledge sync workflow, `.github/workflows/knowledge-sync.yaml`: every Monday at 04:10 UTC and by hand, it moves the sidecar's copies and the skills pin to the newest Knowledge Trust Ladder release through one pull request, opened with the `KNOWLEDGE_SYNC_TOKEN` secret, and holds the workflow changes for a person to approve.
* [Knowledge website (knowledge-website.yaml)](workflows/knowledge-website.md) - The Knowledge website workflow, `.github/workflows/knowledge-website.yaml`: on pushes and pull requests that touch the site's sources, every Monday at 05:23 UTC and by hand, its build job builds `website/` and checks its links read-only, and its deploy job publishes the default branch's build to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is true.
