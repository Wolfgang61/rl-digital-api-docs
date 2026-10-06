# RL Digital API Documentation

Vollständige Hugo-und-Docsy-Vorlage für DIGIT-2604. Sie kombiniert technische OpenAPI-Referenzen mit handgepflegter semantischer Dokumentation, Mermaid-Diagrammen, Versionierung, Suche, Qualitätsprüfungen und GitHub-Pages-Deployment.

## Voraussetzungen

- Git
- Go 1.23 oder neuer
- Node.js 22 oder neuer
- Hugo Extended 0.146 oder neuer

## Schnellstart unter WSL

```bash
unzip rl-digital-api-docs.zip
cd rl-digital-api-docs
npm ci
npm run dev
```

Danach die lokale Hugo-Adresse öffnen, standardmäßig `http://localhost:1313/rl-digital-api-docs/`.

## OpenAPI-Spezifikationen aktualisieren

```bash
npm run fetch:openapi
npm run validate:openapi
```

Die Quell-URLs und Zieldateien stehen in `config/openapi-sources.json`. Die mitgelieferten Spezifikationen sind bewusst kleine Platzhalter, damit der Build sofort funktioniert. Sie enthalten keine Produktivdaten.

## Qualitätsprüfung und Build

```bash
npm run check
npm run build
```

## GitHub Pages

In GitHub unter `Settings > Pages > Build and deployment` die Quelle `GitHub Actions` wählen. Der Workflow `.github/workflows/pages.yml` baut und veröffentlicht die Seite. Für ein anderes Repository den `baseURL`-Wert in `hugo.toml` oder im Workflow anpassen.

## Zielhosting und Zugriffsschutz

GitHub Pages ist in dieser Vorlage nur als PoC-Ziel enthalten. `noindex, nofollow` und `robots.txt` sind kein Zugriffsschutz. Für interne oder vertrauliche Dokumentation muss das spätere Hosting echte Authentifizierung und Autorisierung bereitstellen, beispielsweise über einen vorgeschalteten Unternehmenszugang.

## Struktur

- `content/de/docs/apis`: eAAPI, eCAPI und PAPI
- `content/de/docs/concepts`: fachliche Semantik
- `content/de/docs/architecture`: Architektur und Mermaid
- `content/de/docs/releases`: Versionierung und Release Notes
- `static/openapi`: OpenAPI-Dateien für die Referenzansicht
- `scripts`: Abruf, Konvertierung und Validierung
- `docs/acceptance`: PoC-Abnahme und Hostingbewertung
- `.github/workflows`: CI und GitHub Pages
