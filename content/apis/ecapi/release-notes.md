---
title: "eCAPI Release Notes"
linkTitle: "Release Notes"
weight: 50
type: docs
description: >
  Release history and lifecycle information for the Electronic Consumer API (eCAPI).
---

# eCAPI Release Notes

This page provides an overview of released versions, lifecycle status, and significant changes to the Electronic Consumer API (eCAPI).

## eCAPI v2

**Status:** Active

### Overview

eCAPI v2 is the current major version of the Electronic Consumer API. It provides health insurance providers and authorized partners with secure access to Electronic Product Leaflet (ePL) information and enhanced search capabilities.

### Added

- Enhanced medicinal product search capabilities.
- Improved retrieval workflows.
- Extended API documentation and integration examples.
- Additional version metadata exposed through the API versions endpoint.

### Changed

- Updated search endpoint structure.
- Improved API documentation and examples.
- Updated OpenAPI specification.

### API Version Information

| Property | Value |
|-----------|---------|
| API Version | v2 |
| Status | Active |
| Lifecycle | Supported |

### Migration Notes

Consumers should use eCAPI v2 for new integrations and future development activities.

### Documentation

- OpenAPI Specification
- Swagger UI
- Integration Guide
- API Architecture Overview
- Versioning Policy

---

## eCAPI v1

**Status:** Deprecated

### Overview

eCAPI v1 was the initial version of the Electronic Consumer API. It provided secure access to electronic product leaflet information and search functionality for authorized consumers.

### Features

- OAuth2-based authentication
- Retrieval of ePL information by PZN
- Product search functionality
- OpenAPI specification
- Swagger UI support

### Deprecated Functionality

The original search endpoint:

```http
GET /v1/pil/search
```

has been deprecated and replaced by the enhanced search capabilities available in eCAPI v2.

### Lifecycle Status

| Property | Value |
|-----------|---------|
| API Version | v1 |
| Status | Deprecated |
| Migration Target | v2 |

### Migration Notes

Existing consumers should migrate to eCAPI v2 to benefit from enhanced search capabilities, future improvements, and continued support.

---

# Release History

| Version | Status |
|----------|---------|
| v2 | Active |
| v1 | Deprecated |

---

# Version Lifecycle

The API Versions endpoint allows consumers to discover:

- Available API versions
- Current lifecycle status
- Deprecation information
- Planned retirement dates
- Reference documentation
- Related release notes

Consumers should periodically check the API Versions endpoint and release notes to ensure continued compatibility.

---

# Support

For technical questions, integration support, or lifecycle-related inquiries, please contact the responsible API support team.