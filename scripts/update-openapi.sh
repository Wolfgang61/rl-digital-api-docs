#!/bin/bash

set -e

echo "Lade eAAPI v1..."
curl -s https://qa-digital.systems-tooling.de/docs/eaapi.json \
  -o static/openapi/eaapi-v1.json

echo "Lade eCAPI v1..."
curl -s https://qa-digital.systems-tooling.de/docs/ecapi/v1/ecapi.json \
  -o static/openapi/ecapi-v1.json

echo "Lade eCAPI v2..."
curl -s https://qa-digital.systems-tooling.de/docs/ecapi/v2/ecapi.json \
  -o static/openapi/ecapi-v2.json

echo "Fertig."
