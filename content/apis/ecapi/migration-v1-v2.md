---
title: "Migration from eCAPI v1 to v2"
weight: 30
type: docs
---

# Migration from eCAPI v1 to v2

## Key Changes

| Area | eCAPI v1 | eCAPI v2 |
|----------|----------|----------|
| Search | `/v1/pil/search` | `/v2/pil/medicinal-product/search` |
| Company Logos | Not available | Available |
| Version Information | `/v1/version` | `/version` |
| ePIL Retrieval | Available | Compatible |

## Summary

eCAPI v2 extends the functionality of eCAPI v1 by adding new search mechanisms for medicinal products, additional metadata endpoints (e.g., company logos), and simplified version endpoints.

The endpoints for retrieving ePIL documents remain largely compatible, allowing a migration from v1 to v2 with minimal adjustment effort.