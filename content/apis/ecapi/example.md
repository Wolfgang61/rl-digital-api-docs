---
title: "Example: Using eCAPI v2"
linkTitle: "Usage Example"
weight: 15
description: "Complete curl walkthrough for searching and retrieving an ePIL with eCAPI v2."
---

## Overview

This example demonstrates a complete read workflow with eCAPI v2:

1. Request an OAuth2 access token.
2. Search for a medicinal product by PZN.
3. Retrieve the electronic product information (ePIL) for the PZN.
4. Reuse the response `ETag` for conditional requests.

The [eCAPI v2 reference](v2/) is generated from the [OpenAPI specification](openapi/ecapi-v2.json).

## Prerequisites

You need:

- an OAuth2 client enabled for eCAPI,
- `curl` and `jq`,
- a valid PZN.

Set the environment-specific values before running the requests:

```bash
export BASE_URL="https://qa-digital.systems-tooling.de"
export CLIENT_ID="<client_id>"
export CLIENT_SECRET="<client_secret>"
export PZN="00094113"
```

Never store client secrets in source code, repositories, or logs.

## Step 1: Request an access token

The token endpoint accepts the OAuth2-standard
`application/x-www-form-urlencoded` format. JSON requests are also supported
by the API.

```bash
TOKEN_RESPONSE=$(curl --fail-with-body -sS -X POST "$BASE_URL/ecapi/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  --data-urlencode "grant_type=client_credentials" \
  --data-urlencode "client_id=$CLIENT_ID" \
  --data-urlencode "client_secret=$CLIENT_SECRET")

TOKEN=$(echo "$TOKEN_RESPONSE" | jq -er '.access_token')
export TOKEN
```

A successful response has HTTP status `200` and contains a bearer token:

```json
{
  "token_type": "Bearer",
  "expires_in": 3600,
  "access_token": "<access_token>"
}
```

## Step 2: Search for a medicinal product

Use the `q` query parameter to search by PZN, GTIN, or medicinal product name.
The eCAPI v2 search response is a FHIR `Bundle`.

```bash
SEARCH_RESPONSE=$(curl --fail-with-body -sS \
  "$BASE_URL/ecapi/v2/medicinal-product/search?q=$PZN&limit=5" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Accept: application/fhir+json")

echo "$SEARCH_RESPONSE" | jq .
```

Example response (`200 OK`):

```json
{
  "resourceType": "Bundle",
  "type": "searchset",
  "total": 1,
  "entry": [
    {
      "resource": {
        "resourceType": "MedicinalProductDefinition",
        "id": "mpd-12345",
        "name": [
          {
            "productName": "Example Medicinal Product"
          }
        ]
      }
    }
  ]
}
```

The response is illustrative. The returned resources and identifiers depend on
the selected environment and the search value.

## Step 3: Retrieve the ePIL by PZN

Request the published ePIL using the same PZN. The server returns FHIR JSON
when `application/fhir+json` is requested.

```bash
curl --fail-with-body -sS \
  "$BASE_URL/ecapi/v2/pil/pzn/$PZN" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Accept: application/fhir+json" \
  | jq .
```

Example response (`200 OK`):

```json
{
  "resourceType": "Bundle",
  "type": "searchset",
  "total": 1,
  "entry": [
    {
      "resource": {
        "resourceType": "Composition",
        "id": "comp-12345",
        "status": "final"
      }
    }
  ]
}
```

The endpoint can also return FHIR XML when the client requests
`application/fhir+xml`.

## Step 4: Cache an ePIL with `ETag`

Store the response headers and body when retrieving an ePIL:

```bash
curl --fail-with-body -sS \
  -D pil.headers \
  -o pil.json \
  "$BASE_URL/ecapi/v2/pil/pzn/$PZN" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Accept: application/fhir+json"

ETAG=$(awk 'tolower($1) == "etag:" { sub(/\r$/, "", $2); print $2 }' pil.headers)
```

For a later request, send the stored value in `If-None-Match`:

```bash
curl -sS -D - -o /dev/null \
  "$BASE_URL/ecapi/v2/pil/pzn/$PZN" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Accept: application/fhir+json" \
  -H "If-None-Match: $ETAG"
```

If the representation has not changed, the server returns `304 Not Modified`
with an empty body. Use the cached `pil.json` in that case. A changed
representation returns `200 OK` with the current FHIR bundle.

## Error handling

| Situation | Expected response |
| --- | --- |
| Token issued | `200 OK` with `access_token` |
| Product found | `200 OK` with a FHIR `Bundle` |
| ePIL found | `200 OK` with FHIR JSON or XML |
| Cached representation is current | `304 Not Modified` with an empty body |
| Invalid credentials | `401` with an OAuth2 error response |
| Product or ePIL not found | `404` with a FHIR `OperationOutcome` |
| Rate limit exceeded | `429` with `Retry-After`; wait before retrying |

The rate limit applies per client across all eCAPI endpoints. Clients should
honour `Retry-After` and avoid tight retry loops.

For all endpoint parameters, response codes, and schemas, use the
[eCAPI v2 OpenAPI reference](v2/).
