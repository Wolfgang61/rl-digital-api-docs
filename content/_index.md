---
title: "RL Digital API Documentation"
linkTitle: "Home"
---

# RL Digital API Documentation

Evaluierung von Hugo + Docsy im Rahmen von DIGIT-2604 zur Neustrukturierung der internen und externen API-Dokumentation.

## Bewertete Funktionen

- OpenAPI-basierte API-Dokumentation
- Technische und fachliche Dokumentation aus einer Quelle
- Mermaid-Diagramme
- Versionierung und Release Notes
- Volltextsuche
- Automatisierte Bereitstellung
- Git-basierte Zusammenarbeit

## APIs

### eAAPI

👉 [Zur eAAPI](/rl-digital-api-docs/apis/eaapi/)

### eCAPI

👉 [Zur eCAPI](/rl-digital-api-docs/apis/ecapi/)

### PAPI

👉 [Zur PAPI](/rl-digital-api-docs/apis/papi)



## API- und Dokumentationsarchitektur

```mermaid
flowchart TB
    subgraph Partners[Externe Partner]
      PH[Pharma/Dienstleister]
      KV[Krankenversicherer]
    end

    subgraph RL[RL Digital]
      EA[eAAPI v1]
      EC1[eCAPI v1]
      EC2[eCAPI v2]
      PA[PAPI v1]
      BE[Backend Services]
      DS[(Document Store)]
    end

    subgraph Portal[Internes Portal]
      UI[Portal Frontend]
    end

    PH -->|Einlieferung| EA
    KV -->|Abruf| EC1
    KV -->|Suche/Abruf| EC2
    UI -->|Portal-Funktionen| PA
    EA --> BE
    EC1 --> BE
    EC2 --> BE
    PA --> BE
    BE --> DS
```

## Architektur

```mermaid
flowchart LR

subgraph Sources
    OA[OpenAPI Specs]
    MD[Markdown Dokumentation]
    MM[Mermaid Diagramme]
end

subgraph Build
    HU[Hugo]
    DO[Docsy]
end

subgraph Deployment
    GH[GitHub Actions]
    WS[Dokumentationsportal]
end

OA --> HU
MD --> HU
MM --> HU

HU --> DO
DO --> GH
GH --> WS
```

## PoC-Ergebnis

| Kriterium | Status |
|-----------|---------|
| Hugo Evaluation | ✅ |
| Docsy Evaluation | ✅ |
| OpenAPI Integration | ✅ |
| Mermaid Integration | ✅ |
| Versionskonzept | ✅ |
| Suchfunktion | ✅ |
| Hosting | ✅ |
| CI/CD | ✅ |

## Nächste Schritte

1. Versionierung fertigstellen
2. OpenAPI-Automatisierung integrieren
3. GitHub Actions vervollständigen
4. Hosting-Konzept dokumentieren
5. Architekturentscheidung für DIGIT-2604 vorbereiten