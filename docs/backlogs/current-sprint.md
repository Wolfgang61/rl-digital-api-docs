# Current Sprint

## Sprint Information

**Sprint Name:** Foundation & Build Reproducibility

**Date Range:** YYYY-MM-DD to YYYY-MM-DD

**Goal**

Establish a reproducible and maintainable foundation for the API documentation platform.

---

# Scope

This sprint focuses on:

- Build reproducibility
- Hugo/Docsy foundation
- OpenAPI-first architecture
- CI/CD preparation

Out of scope:

- Content migration
- Advanced search
- Governance processes

---

# Active Backlog Items

## BL-001 Make Docsy dependency reproducible

### Priority

P1

### Status

Done

### Acceptance Criteria

- Docsy managed via Hugo Modules
- Clean checkout builds successfully
- Build instructions documented
- GitHub Actions build succeeds

### Notes

Docsy v0.12.0 is pinned as a Hugo Module. The local theme Gitlink was removed,
the root NPM lockfile contains only the project build toolchain, and the build
was verified with the Node.js and Hugo versions used by CI.

---

## BL-002 Create Build Documentation

### Priority

P1

### Status

Not Started

### Acceptance Criteria

- README updated
- Development setup documented
- Build process documented

### Notes

Documentation must allow onboarding on a clean workstation.

---

## BL-003 Validate OpenAPI Architecture

### Priority

P1

### Status

Not Started

### Acceptance Criteria

- OpenAPI source locations documented
- Integration approach reviewed
- ADR created if necessary

---

# Technical Tasks

## TASK-001

Review current Hugo configuration.

Owner: Wolfgang

Status: In Progress

---

## TASK-002

Review current Docsy integration.

Owner: Wolfgang

Status: Not Started

---

## TASK-003

Review GitHub Actions workflow.

Owner: Wolfgang

Status: Not Started

---

# Risks

## Risk-001

Current build process may rely on local environment settings.

### Mitigation

Perform clean checkout validation.

---

# Decisions Needed

## DEC-001

Theme management strategy

Options:

- Hugo Modules
- Git Submodule

Preferred Option:

- Hugo Modules

Status:

Accepted

---

# Sprint Deliverables

At the end of this sprint the following should exist:

- Reproducible build process
- Working Hugo setup
- Working Docsy integration
- Updated README
- Initial ADRs
- Basic CI/CD validation

---

# Sprint Review Checklist

- [ ] Clean clone succeeds
- [ ] Hugo build succeeds
- [ ] Local development documented
- [ ] GitHub Actions build succeeds
- [ ] No undocumented dependencies exist
- [ ] Architecture documentation updated

---

# Copilot Guidance

When working on this sprint:

1. Focus only on sprint backlog items.
2. Prefer Hugo Modules over Git submodules.
3. Follow all instructions in `.github/copilot-instructions.md`.
4. Use OpenAPI as source of truth.
5. Avoid introducing custom JavaScript unless required.
6. Keep solutions maintainable and production-ready.
7. Update documentation whenever code or configuration changes.