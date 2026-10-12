---
title: "Migration von eCAPI v1 nach v2"
weight: 30
---

# Migration von eCAPI v1 nach v2

## Wichtigste Änderungen

| Bereich | eCAPI v1 | eCAPI v2 |
|----------|----------|----------|
| Suche | `/v1/pil/search` | `/v2/pil/medicinal-product/search` |
| Company Logos | nicht vorhanden | verfügbar |
| Versionsinformationen | `/v1/version` | `/version` |
| ePIL Abruf | vorhanden | kompatibel |

## Zusammenfassung

eCAPI v2 erweitert die Funktionalität von eCAPI v1 um neue Suchmechanismen für Medicinal Products, zusätzliche Metadaten-Endpunkte (z. B. Company Logos) sowie vereinfachte Versionsendpunkte.

Die Endpunkte zum Abruf von ePIL-Dokumenten bleiben weitgehend kompatibel, wodurch eine Migration von v1 zu v2 mit geringem Anpassungsaufwand möglich ist.