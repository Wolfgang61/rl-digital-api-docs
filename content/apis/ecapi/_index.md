---
title: "eCAPI"
weight: 20
cascade:
  toc: true
---

# eCAPI

The Electronic Consumer API (eCAPI) enables the search and retrieval of electronic product information within the EPL platform.

## Verfügbare Versionen

| Version | Status |
|----------|----------|
| v1 | Active |
| v2 | Active |

## Dokumentation

- [Version 1](v1/)
- [Version 2](v2/) (recommended)
- [Release Notes](release-notes/)

## Funktionen

- Retrieve product information
- Provide search capabilities
- Provide product metadata


```mermaid
sequenceDiagram
    actor Client as Health insurance provider
    participant EC as Consumer API v2
    participant IDX as SSearch index
    participant STORE as Document Repository

    Client->>EC: GET /products/{productId}/documents
    EC->>IDX: Search Published Documents
    IDX-->>EC: Document Metadata
    EC->>STORE: Request Signed Download URL
    STORE-->>EC: Temporary URL
    EC-->>Client: 200 OK + Document List
```

## OpenAPI

API is documented using the OpenAPI 3.0 specification.

## Notes

- The OpenAPI specification serves as the authoritative source of truth for the API.
- Interactive API documentation is automatically generated from the OpenAPI definition.
- All changes are version-controlled in Git and automatically published through automated deployment processes.
- eCAPI v2 should be adopted as the preferred integration interface for all new developments. Existing eCAPI v1 consumers should plan a controlled migration to eCAPI v2 to benefit from improved search functionality, expanded metadata capabilities, and a more future-proof API architecture while maintaining compatibility with existing product information retrieval processes.


## Migration Recommendation: Migrating from eCAPI v1 to eCAPI v2

Organizations currently using eCAPI v1 are strongly encouraged to migrate to eCAPI v2 in order to benefit from enhanced search capabilities, additional metadata services, and a modernized API design. The migration effort is expected to be low, as the core functionality for retrieving electronic product information remains largely compatible between both versions.

## Benefits of Migrating to eCAPI v2
Improved product search capabilities through dedicated medicinal product search endpoints.
Access to additional metadata services, including company logo information.
Simplified version discovery endpoints.
Improved extensibility for future enhancements.
Continued support for existing product information retrieval scenarios.
Recommended Migration Approach
### 1. Review Current Integrations

Identify all existing eCAPI v1 endpoints currently used by your applications, particularly search-related functionality.

### 2. Update Search Endpoints

Replace legacy search endpoints:

```http
GET /v1/pil/search
```

with the new v2 endpoint:

```http
GET /v2/pil/medicinal-product/search
```

Applications should be tested to verify that expected search results are returned.

### 3. Update Version Discovery

Replace version-specific endpoints:

```http
/v1/version
/v1/api-versions
```

with:

```http
/version
/api-versions
```

to align with the new API structure.

### 4. Validate Core Retrieval Functions

Existing retrieval scenarios based on identifiers such as:

- PZN
- Business ID
- External ID

should be verified during testing, although these functions remain largely compatible between v1 and v2.

### 5. Adopt New Features

Where applicable, applications should be enhanced to leverage new metadata capabilities available in eCAPI v2, such as:

```http
GET /v2/company/logos
```

This functionality is not available in eCAPI v1.

## Migration Risk Assessment

| Area | Migration Impact |
|--------|------------------|
| Product Retrieval | Low |
| Identifier-Based Lookup | Low |
| Search Functionality | Medium |
| Metadata Services | Optional Enhancement |
| Authentication | No Significant Changes |