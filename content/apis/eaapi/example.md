---
title: "Example: Successful ePIL Submission"
linkTitle: "Example Workflow"
weight: 15
description: "Complete curl walkthrough of a successful ePIL submission via eAAPI v1."
---

## Overview

This walkthrough demonstrates a fully successful ePIL submission via eAAPI v1:

- Requesting an access token
- Uploading an ePIL
- Checking the processing status
- Evaluating the result

The complete endpoint and schema documentation is available in [OpenAPI Documentationrerequisites

| Value | Description |
| --- | --- |
| `BASE_URL` | Environment base URL, e.g. `https://qa-digital.systems-tooling.de` |
| `CLIENT_ID` / `CLIENT_SECRET` | OAuth2 client credentials of the submitting tenant |
| ePIL file | FHIR Bundle according to the [ePIL FHIR Implementation Guide](https://fhir.pharmaprotect.de/digital/epil-fL="https://qa-digital.systems-tooling.de"
export CLIENT_ID="<client_id>"
export CLIENT_SECRET="<client_secret>"
```

{{% alert title="Note" color="warning" %}}
Client secrets must be stored in a secure secret management solution and must never be committed to repositories, tickets, or logs.
{{% /alert %}}

## Step 1: Request an Access Token

```bash
curl -X POST "$BASE_URL/eaapi/token" \
  -H "Content-Type: application/json" \
  -d "{
        \"grant_type\": \"client_credentials\",
        \"client_id\": \"$CLIENT_ID\",
        \"client_secret\": \"$CLIENT_SECRET\"
      }"
```

Response (`200 OK`):

```json
{
  "token_type": "Bearer",
  "expires_in": 3600,
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9..."
}
```

Store the token for subsequent requests:

```bash
export TOKEN="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9..."
```

## Step 2: Upload an ePIL

The upload is performed as `multipart/form-data` using the `file` field.

```bash
curl -X POST "$BASE_URL/eaapi/v1/pil/create" \
  -H "Authorization: Bearer $TOKEN" \
  -F "file=@epil-bundle.json"
```

Response (`202 Accepted`):

```json
{
  "_id": {
    "id": "9fba01ee-171e-cca1-040f-ab17b4167a19"
  },
  "status": "processing",
  "intent": "order",
  "focus": {
    "reference": "DocumentReference/9fba01ee-171e-cca1-040f-ab17b4167a19"
  },
  "resourceType": "Task"
}
```

`_id.id` is the `requestId` and is required for the status query:

```bash
export REQUEST_ID="9fba01ee-171e-cca1-040f-ab17b4167a19"
```

## Step 3: Check the Processing Status

Processing is asynchronous. Query the status repeatedly until `status` is no longer `processing`.

```bash
curl "$BASE_URL/eaapi/v1/pil/upload-status/$REQUEST_ID" \
  -H "Authorization: Bearer $TOKEN"
```

Response (`200 OK`) after successful processing:

```json
{
  "_id": {
    "id": "9fba01ee-171e-cca1-040f-ab17b4167a19"
  },
  "status": "success",
  "intent": "order",
  "focus": {
    "reference": "DocumentReference/9fba01ee-171e-cca1-040f-ab17b4167a19"
  },
  "output": [
    {
      "type": {
        "text": "businessId"
      },
      "valueCoding": {
        "system": "http://pharmaprotect.de/digital/epil",
        "code": "8a3f6502-db6e-5afb-b701-54395df701d9"
      }
    },
    {
      "type": {
        "text": "medicinalProductId"
      },
      "valueCoding": {
        "system": "http://pharmaprotect.de/digital/epil/medicinal-product-definition",
        "code": "f29661b7-672d-588b-874d-bf1b228d6127"
      }
    }
  ],
  "resourceType": "Task"
}
```

{{% alert title="Important" color="warning" %}}
Processing errors are also returned with HTTP `200`. Success must be determined exclusively from `status == "success"` and not from the HTTP status code.
{{% /alert %}}

## Step 4: Evaluate the Result

| Field | Meaning |
| --- | --- |
| `status` | `success` confirms a successful submission |
| `output[].type.text == "businessId"` | Business identifier of the ePIL; required for actions such as blocking |
| `output[].type.text == "medicinalProductId"` | IDs of the created or linked medicinal products |

Extract the `businessId`:

```bash
curl -s "$BASE_URL/eaapi/v1/pil/upload-status/$REQUEST_ID" \
  -H "Authorization: Bearer $TOKEN" \
  | jq -r '.output[] | select(.type.text == "businessId") | .valueCoding.code'
```

## Complete Example Script

```bash
#!/usr/bin/env bash
set -euo pipefail

TOKEN=$(curl -s -X POST "$BASE_URL/eaapi/token" \
  -H "Content-Type: application/json" \
  -d "{\"grant_type\":\"client_credentials\",\"client_id\":\"$CLIENT_ID\",\"client_secret\":\"$CLIENT_SECRET\"}" \
  | jq -r '.access_token')

REQUEST_ID=$(curl -s -X POST "$BASE_URL/eaapi/v1/pil/create" \
  -H "Authorization: Bearer $TOKEN" \
  -F "file=@epil-bundle.json" \
  | jq -r '._id.id')

STATUS="processing"

while [ "$STATUS" = "processing" ]; do
  sleep 5

  RESPONSE=$(curl -s "$BASE_URL/eaapi/v1/pil/upload-status/$REQUEST_ID" \
    -H "Authorization: Bearer $TOKEN")

  STATUS=$(echo "$RESPONSE" | jq -r '.status')
done

if [ "$STATUS" != "success" ]; then
  echo "Submission failed: $(echo "$RESPONSE" | jq -r '.statusReason.concept.text // "unknown"')" >&2
  exit 1
fi

echo "$RESPONSE" | jq -r '.output[] | select(.type.text == "businessId") | .valueCoding.code'
```

## Workflow Overview

```mermaid
sequenceDiagram
    autonumber
    participant C as Client
    participant EA as eAAPI

    C->>EA: POST /eaapi/token
    EA-->>C: 200 access_token

    C->>EA: POST /eaapi/v1/pil/create (multipart file)
    EA-->>C: 202 Task status=processing + requestId

    loop until status != processing
        C->>EA: GET /eaapi/v1/pil/upload-status/{requestId}
        EA-->>C: 200 Task status
    end

    EA-->>C: 200 Task status=success + businessId
```

## Alternative: Synchronous Upload

For enabled clients, `POST /eaapi/v1/pil/create-sync` returns the same result directly with HTTP `200`, eliminating the need for polling.

As with the asynchronous workflow, clients must evaluate:

```text
status == "success"
```

```bash
curl -X POST "$BASE_URL/eaapi/v1/pil/create-sync" \
  -H "Authorization: Bearer $TOKEN" \
  -F "file=@epil-bundle.json"
```

## Error Handling

| Situation | Detection |
| --- | --- |
| Invalid client credentials | HTTP `401` with `error: invalid_client` |
| Client not authorized | HTTP `403` |
| Empty or invalid file | HTTP `400` with `OperationOutcome` |
| Business processing error | HTTP `200` with `status = failed` or `exception`; details available in `statusReason.concept.text` |

The complete list of response codes and schemas is available in the [OpenAPI Documentation](/apis/)