# ADR-0004: Manage Docsy as a Hugo Module

## Status

Accepted

## Context

The repository referenced Docsy through a Gitlink under `themes/docsy` without
a corresponding `.gitmodules` configuration. A clean checkout therefore could
not restore the theme reliably, and local theme files could influence builds.

The platform requires reproducible local and GitHub Actions builds without a
manually prepared theme directory.

## Decision

Docsy is imported as a versioned Hugo Module and pinned in `go.mod`. Hugo
verifies downloaded module content against `go.sum`.

Docsy's Bootstrap and Font Awesome assets are provided by its Hugo Module
imports. The project keeps only its own PostCSS toolchain in the root NPM
lockfile and installs it with `npm ci`; upstream theme-development dependencies
are not copied into the project.

## Consequences

- A clean checkout can restore Docsy using Go and Hugo alone.
- Builds do not depend on a local `themes/docsy` checkout.
- Docsy upgrades are explicit changes to `go.mod` and `go.sum`.
- Contributors need network access when the pinned module is not already in
  their Go module cache.
