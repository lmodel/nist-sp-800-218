# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change bumps the minor version. See [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers).

## [Unreleased]

### Added

- **The upstream watch reports more, and always writes its report.** It names a release that changes or drops a pinned file, the licence included, or the catalog's folder, a moved tag and a file NIST adds; a check that cannot reach doi.org or GitHub becomes a line of the report.
- **Dependabot watches the website's npm packages**, beside the actions and the two Python locks.
- **`.github/release/package-lock.json`, which pins semantic-release and every package it pulls in.** The release job installs from it with `npm ci`, and Dependabot keeps it current.

### Changed

- **The generated artefacts, the Python models and `docs/schema/nist_sp_800_218.yaml` are regenerated with linkml 1.12.1.** Pull request #18 locked 1.12.1 without regenerating them, so they still carried metamodel 1.7.0.
- **The upstream watch sends its GitHub token to the API alone, never on to a redirect.**
- **Every job of `main.yaml`, `lint-and-docs.yaml`, `semantic-release.yml` and `upstream-watch.yaml` has a timeout, and `main.yaml` installs `just` 1.59.0, the version `.lokf/` pins.** The release title check names rebase and merge, since `main` refuses merge commits.
- **Six packages in `uv.lock` move past published advisories**: idna, pygments, pytest, requests, urllib3 and the certificate bundle.
- **A blank mapped item fails alike under the validator and the Pydantic models**, and each counter-example names where it must fail.
- **The old mkdocs class pages redirect to their successors' pages** on the knowledge website.
- **SECURITY.md says that a ruleset on `main` blocks deletion and force-pushes and keeps the history linear.** Required reviewers on `release` and secret scanning are still not in force.

## [0.1.0] - 2026-10-29

### Added

- **A LinkML schema of the Secure Software Development Framework (SSDF) version 1.1**, which the National Institute of Standards and Technology (NIST) defines in Special Publication (SP) 800-218. It holds the practice groups, practices and tasks, each task's notional implementation examples, and its references to 29 secure development documents.
- **A copy of NIST's SSDF catalog from usnistgov/oscal-content v1.6.0, and a weekly upstream watch.** A test derives the whole framework from the copy and holds it to the validator and to the publication's counts, and the watch also asks doi.org whether NIST has published the next final edition.
- **`.lokf/nist-sp-800-218.yaml`, the schema's `lokf adapt` copy, rooted on the practice group, the practice and the task.** The knowledge release attaches it as `schema-<tag>-nist-sp-800-218.yaml`, and tests hold its names apart from those of the Linked Open Knowledge Format (LOKF) and of the slsa, github-actions and oscal copies, with which it shares no key.
- **An example of each class and a counter-example for each constraint**, held to the validator by `just test`.
- **The repository's Knowledge Trust Ladder (KTL) knowledge bundle and its sidecar automation**, from the KTL v0.59.0 templates with the lokf floor at 0.9.0, and a knowledge website that replaces the mkdocs site.

### Changed

- **The schema models the SSDF's own elements, not a copy of a catalog in the Open Security Controls Assessment Language (OSCAL).** The OSCAL-shaped classes shared names with LOKF's and lmodel/oscal's, and their `class_uri: linkml:Any` let a catalog with any keys validate.
- **The schema's name is `nist_sp_800_218`, as its file and package are, and the Python project's name is `nist-sp-800-218-linkml`.** PyPI publishing stays off.

### Removed

- **The PyPI publishing workflow and the mkdocs site and its preview.** The knowledge website replaces the site.
