---
type: Policy
id: https://w3id.org/lmodel/nist-sp-800-218/knowledge/policies/ai-covenant
genre: explanation
title: AI covenant
description: "The repository's rules for work done with artificial intelligence (AI): you own what you submit, an element under the schema renders SP 800-218 in the project's own words and cites it, NIST's catalog copy is never edited, and the scheduled librarian proposes changes only through reviewed pull requests."
resource: AI_COVENANT.md
sources:
  - id: ai_covenant.md
    resource: AI_COVENANT.md
    title: the core principle, the project note and the section on agent automation
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:21:05Z"
status: draft
---

# AI covenant

`AI_COVENANT.md` says that everything a person contributes is theirs, whatever tools helped make it, and that they answer for it in review.[^ai_covenant.md] Its note for this project says that the repository models someone else's framework, so a practice, task or rule a model invented would read as what the SSDF says. It sets three rules:

- every class, slot and enum under `src/nist_sp_800_218/schema/` renders an element of SP 800-218 at the pinned version, in the project's own words, and the pull request cites the section or table;
- `src/nist_sp_800_218/schema/oscal-content/` holds NIST's catalog as published and is never edited;
- everything the schema defines lives under `nist_sp_800_218:`, and the SSDF's own identifiers appear only as values.

The covenant also covers the scheduled `knowledge-librarian` agent. It commits as a labelled bot, proposes every change as a pull request a person approves, runs with no write credential, and never records a person's verdict for them. It discourages AI co-authorship lines in commit messages.

[^ai_covenant.md]: AI_COVENANT.md, the core principle, the project note and Repository-Owned Agent Automation
