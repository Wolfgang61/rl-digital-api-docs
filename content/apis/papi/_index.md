---
title: "PAPI"
weight: 30
---

Funktionen des Portals. Die fachlichen Inhalte sind Platzhalter und müssen gegen die freigegebene Produktdokumentation geprüft werden.

## Dokumentation

- Dokumentation wurde noch nicht erstellt
  

```mermaid
flowchart LR
    UI[Portal Frontend] -->|POST publication-jobs| PAPI[Portal API]
    PAPI --> AUTH[Autorisierung]
    AUTH --> JOB[Job Service]
    JOB --> DB[(Job-Datenbank)]
    JOB --> BUS[Event Bus]
    BUS --> PUB[Publication Worker]
    PUB --> DOC[(Dokumentenspeicher)]
    PUB --> STATUS[Status Update]
    STATUS --> DB
```