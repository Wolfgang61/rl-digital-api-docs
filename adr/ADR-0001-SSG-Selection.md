# ADR-0001: Auswahl eines SSG

## Status

Proposed

## Kontext

Für DIGIT-2604 soll ein geeigneter Static Site Generator
für die zentrale API-Dokumentation evaluiert werden.

## Kandidaten

- Hugo + Docsy
- MkDocs
- Docusaurus
- Sphinx

## Erfolgskriterien

- Markdown
- Suche
- Mermaid
- OpenAPI Integration
- GitHub Pages

## Status

PoC was successfully finished. The documentation portal will be  generated using Hugo Extended v0.167.0 for Linux (amd64).

## PoC Findings

The PoC can be found in https://github.com/Wolfgang61/rl-digital-api-docs-poc

### Positive

- Hugo 0.160.1 Extended successfully installed
- Hugo Modules work
- Docsy theme loads correctly
- Official Docsy Example can be downloaded and built

### Issues discovered

Current Docsy versions require:

- Hugo >= 0.160.1 Extended
- Go
- Hugo Modules
- Dart Sass
- Node.js

The setup is considerably more complex than a traditional static site generator.

During evaluation, the official Docsy Example and the
custom PoC both failed with a Dart Sass integration issue
under WSL2 despite a successful installation of Hugo,
Node.js and Dart Sass.

### Impact

Additional setup and troubleshooting effort was required
before a productive rollout can be considered. Currently all setup issues are resolved. See also https://arvato-systems-group.atlassian.net/browse/DIGIT-2604