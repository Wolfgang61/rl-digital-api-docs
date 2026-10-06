# PoC-Abnahme DIGIT-2604

| Kriterium | Nachweis in dieser Vorlage | Status |
|---|---|---|
| Hugo und Docsy bauen die Site | `npm run build` | prüfbar |
| Syntax-Highlighting | YAML-, JSON- und Bash-Codeblöcke | prüfbar |
| OpenAPI-Integration | Shortcode und versionierte Dateien unter `static/openapi` | prüfbar |
| Semantische Ergänzungen | `content/de/docs/concepts` | prüfbar |
| Mermaid-Diagramme | Architektur- und Sequenzdiagramm | prüfbar |
| Navigation und Suche | Docsy-Navigation und Offline-Suche | prüfbar |
| Versionierung | API- und Release-Notes-Struktur | prüfbar |
| noindex/nofollow | Head-Hook und `robots.txt` | prüfbar |
| CI | `.github/workflows/ci.yml` | prüfbar |
| GitHub Pages | `.github/workflows/pages.yml` | prüfbar |
| Zugriffsschutz/Zielhosting | Bewertungsseite vorhanden | bewertet, nicht umgesetzt |

## Abnahmebefehle

```bash
npm ci
python3 -m pip install -r scripts/requirements.txt
npm run check
npm run dev
```
