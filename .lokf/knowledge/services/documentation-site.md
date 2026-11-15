---
type: Service
id: https://w3id.org/lmodel/nist-sp-800-218/knowledge/services/documentation-site
genre: reference
title: Documentation site
description: "The Hugo site in `website/`, for <https://lmodel.github.io/nist-sp-800-218>: the README as its home page, the pages of `docs/`, the schema's element pages, a page per concept of this bundle with its trust label, and the bundle's exports, built and published by Knowledge website."
resource: website
endpoint: https://lmodel.github.io/nist-sp-800-218
documentation: website/README.md
sources:
  - id: site.toml
    resource: website/site.toml
    title: the site's address, title and redirects
  - id: website-readme.md
    resource: website/README.md
    title: what each page is built from and how to build it
generated:
  by: process:ktl-librarian
  at: "2026-11-15T03:07:08Z"
status: draft
---

# Documentation site

`website/` holds a Hugo site. `website/site.toml` gives the site's address, `https://lmodel.github.io/nist-sp-800-218/`, its title, `nist-sp-800-218`, and the repository, `https://github.com/lmodel/nist-sp-800-218`. It sends `/about` to the page built from `docs/about.md`. It sends twenty old element addresses, such as `/elements/Control`, to the page of the class that succeeds each or, where none does, to the schema's index. It names no logo, so the site shows the Knowledge Trust Ladder logo.[^site.toml]

The README is the home page. The site has a page for each page under `docs/`, a page per release of `CHANGELOG.md`, and a page for each class, slot, enumeration and type that LinkML's `gen-doc` writes from the schema, each also at `elements/<Name>/`. `scripts/build.sh`, run from `website/`, writes the site to `dist/` with its search index, then checks every link between its pages.[^website-readme.md] [Knowledge website](../workflows/knowledge-website.md) builds the site on each change to its sources and publishes it once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.

[^site.toml]: website/site.toml, the site's address, title and redirects
[^website-readme.md]: website/README.md, what each page is built from and how to build it
