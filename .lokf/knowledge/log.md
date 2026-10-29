# Change Log

## 2026-10-29

* **Changed**: the generators' settings moved from `config.yaml` to `.linkml/generators.yaml`.
* **Added**: nist-sp-800-218 LinkML schema, from `src/nist_sp_800_218/schema/nist_sp_800_218.yaml`, its adapt copy and the lokf-adapt recipes.
* **Added**: NIST's SSDF catalog copy, from `src/nist_sp_800_218/schema/oscal-content/`, NOTICE and the watch's pins.
* **Added**: Generated artefacts, from the justfile's recipes, `config.yaml` and `project/`.
* **Added**: Test data and tests, from `tests/`.
* **Added**: NIST SP 800-218, SSDF version 1.1, from NIST's publication pages.
* **Added**: NIST's SSDF project page, from <https://csrc.nist.gov/projects/ssdf>.
* **Added**: Scope, influences and mappings, from the README, the changelog and `docs/about.md`.
* **Added**: Element names and the shared namespace, from `docs/about.md`, the README, `.linkmllint.yaml` and the schema rules test.
* **Added**: Practice group, from NIST's SSDF project page and the class `SsdfPracticeGroup`.
* **Added**: Practice, from NIST's SSDF project page and the class `SsdfPractice`.
* **Added**: Task, from NIST's SSDF project page and the class `SsdfTask`.
* **Added**: Notional implementation example, from NIST's SSDF project page and the class `SsdfImplementationExample`.
* **Added**: Reference (SSDF), from NIST's SSDF project page and the class `SsdfReference`.
* **Added**: Prepare the Organization, the practice group PO, from NIST's catalog copy.
* **Added**: Protect Software, the practice group PS, from NIST's catalog copy.
* **Added**: Produce Well-Secured Software, the practice group PW, from NIST's catalog copy.
* **Added**: Respond to Vulnerabilities, the practice group RV, from NIST's catalog copy.
* **Added**: Regenerate and test after a schema change, from CONTRIBUTING.md and the recipes.
* **Added**: Validate data against the schema, from `docs/index.md`.
* **Added**: Update the upstream pins, from `scripts/check_upstream_release.py` and its tests.
* **Added**: Cut a release, from `.releaserc.json`, the changelog and CONTRIBUTING.md.
* **Added**: AI covenant, from `AI_COVENANT.md`.
* **Added**: License and attribution, from NOTICE, LICENSE and the README.
* **Added**: Security policy, from `SECURITY.md` and the Dependabot settings.
* **Added**: Documentation site, from `website/site.config.mjs` and `website/README.md`.
* **Added**: Build and test (main.yaml), from `.github/workflows/main.yaml`.
* **Added**: Lint & docs (lint-and-docs.yaml), from `.github/workflows/lint-and-docs.yaml`.
* **Added**: Upstream watch (upstream-watch.yaml), from `.github/workflows/upstream-watch.yaml`.
* **Added**: Semantic release (semantic-release.yml), from `.github/workflows/semantic-release.yml`.
* **Added**: Knowledge Registrar (knowledge-registrar.yaml), from `.github/workflows/knowledge-registrar.yaml`.
* **Added**: Knowledge Librarian (knowledge-librarian.yaml), from `.github/workflows/knowledge-librarian.yaml`.
* **Added**: Knowledge Release (knowledge-release.yaml), from `.github/workflows/knowledge-release.yaml`.
* **Added**: Knowledge sync (knowledge-sync.yaml), from `.github/workflows/knowledge-sync.yaml`.
* **Added**: Knowledge website (knowledge-website.yaml), from `.github/workflows/knowledge-website.yaml`.
* **Added**: Knowledge sources map, the bootstrap's map of what each source yields and how to re-check it, with the paths left out on purpose.
* **Removal**: the sidecar's two example services, which the bootstrap's concepts replace.
* **Initialization**: Scaffolded the LOKF bundle for nist-sp-800-218 with placeholder
  services. Real concepts to follow.
