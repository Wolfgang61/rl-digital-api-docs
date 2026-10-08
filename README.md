# RL Digital API Documentation

Vollständige Hugo-und-Docsy-Vorlage für DIGIT-2604. Sie kombiniert technische OpenAPI-Referenzen mit handgepflegter semantischer Dokumentation, Mermaid-Diagrammen, Versionierung, Suche, Qualitätsprüfungen und GitHub-Pages-Deployment.

## Voraussetzungen

- Git
- Go 1.22 oder neuer
- Node.js 22.12 oder neuer
- Hugo Extended 0.147.5

Docsy wird als versioniertes Hugo Module eingebunden. Ein lokaler Theme-Checkout
oder ein Git-Submodul ist nicht erforderlich.

## Schnellstart unter WSL

```bash
git clone https://github.com/Wolfgang61/rl-digital-api-docs.git
cd rl-digital-api-docs
hugo mod verify
npm ci
npm run dev
```

Danach die lokale Hugo-Adresse öffnen, standardmäßig `http://localhost:1313/rl-digital-api-docs/`.

`hugo mod verify` lädt die in `go.mod` festgeschriebene Docsy-Version in den
globalen Hugo-Modul-Cache und prüft sie gegen `go.sum`. `npm ci` installiert
anschließend exakt die in `package-lock.json` festgeschriebenen Frontend-
Abhängigkeiten.

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

`npm run check` validiert die OpenAPI-Dateien und Markdown-Inhalte und führt
einen Produktionsbuild aus. `npm run build` erstellt die veröffentlichbare Site
unter `public/`.

## GitHub Pages

In GitHub unter `Settings > Pages > Build and deployment` die Quelle `GitHub Actions` wählen. Der Workflow `.github/workflows/ci.yml` prüft, baut und veröffentlicht die Seite. Für ein anderes Repository den `baseURL`-Wert in `hugo.toml` oder im Workflow anpassen.

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
