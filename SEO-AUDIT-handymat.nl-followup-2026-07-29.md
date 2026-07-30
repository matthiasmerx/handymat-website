# SEO Audit — handymat.nl (vervolgmeting)

Datum: 2026-07-29 · Herhaalde audit via dezelfde 10 subagents als de eerste meting (2026-07-12, zie [SEO-AUDIT-handymat.nl.md](SEO-AUDIT-handymat.nl.md)), na de fixes die sindsdien zijn doorgevoerd. Elke agent kreeg de vorige bevindingen als context en heeft alles opnieuw live geverifieerd, niet blind overgenomen.

## SEO Health Score: 64/100 (was 58/100, +6)

| Categorie | Gewicht | Score toen | Score nu | Bijdrage nu |
|---|---|---|---|---|
| Technical SEO | 22% | 66/100 | **78/100** | 17.2 |
| Content Quality | 23% | 57/100 | **60/100** | 13.8 |
| On-Page SEO | 20% | 52/100 | 54/100 | 10.8 |
| Schema / Structured Data | 10% | 70/100 | **82/100** | 8.2 |
| Performance (CWV) | 10% | 60/100 | **70/100** | 7.0 |
| AI Search Readiness (GEO) | 10% | 54/100 | 56/100 | 5.6 |
| Images | 5% | 35/100 | 32/100 | 1.6 |

Aanvullende, niet in de hoofdscore meegewogen metingen:
- **Local SEO score: 45/100** (was 41/100, oorspronkelijk 27/100)
- **SXO Gap Score: 43/100** (was 42/100)

De vooruitgang zit vrijwel volledig in technische en schema-fixes die vandaag zijn doorgevoerd. Contentdiepte (de drie dunne dienstenpagina's) en het canonical/duplicate-URL-probleem zijn niet aangeraakt en blijven de grootste hefbomen voor de volgende stap.

---

## Wat er sinds vanochtend is gefixt (door alle relevante agents onafhankelijk geverifieerd)

1. **Mobiele header-centrering**: bevestigd perfect symmetrisch op alle 12 pagina's, op 375px/390px/430px (visual-agent, exacte metingen).
2. **CLS op de homepage**: 0.139 → **0.042**, ruim onder de 0.1-drempel. Logo heeft nu overal `width="600" height="306"` (technical- en performance-agent, onafhankelijk bevestigd).
3. **privacy.html live en overal consistent gelinkt**: alle 12 pagina's linken nu naar `/privacy` (was `#` of een 404 op portfolio.html). Bevestigd door 4 agents onafhankelijk (technical, content, local, sxo).
4. **Verweesde schema-microdata op portfolio.html verwijderd**: bevestigd door schema-, technical-, local- en content-agent — nul overblijvende `itemscope`/`itemtype`/`itemprop`-fragmenten.
5. **Security headers en CSP live**: X-Frame-Options, X-Content-Type-Options, Referrer-Policy en een CSP staan bevestigd in de live response headers. De CSP breekt niets — expliciet getest tegen de portfolio-modal en de BTW-toggle op tarieven.html (technical-agent).
6. **KvK-nummer (42120954)** staat nu op alle drie juridische pagina's, placeholder `[invullen]` is nergens meer te vinden. Dit hief een concrete blokkade op voor Werkspot- en KvK Ondernemersplein-vermeldingen (backlinks-agent, local-agent, content-agent).
7. **Schema-score gestegen naar 82/100** dankzij bovenstaande opschoning.

Terzijde, gecorrigeerd door de content- en schema-agent: de eerder gerapporteerde "encoding bug" in `priceRange` (zou als kapotte tekens renderen) is definitief een fout van de fetch-tooling in deze sessie gebleken, geen echt sitebug. Dit hoeft niet meer terug te komen.

---

## Wat nog openstaat (bevestigd ongewijzigd, geen verrassing)

- **Geen reviews, nergens** — nog steeds de meest consistente bevinding across alle agents. Blijft de hoogste-impact actie.
- **Dubbele URL's zonder canonical tag** — nu op alle **12** pagina's (privacy.html erft hetzelfde probleem). Nog steeds de grootste technische makke.
- **Drie dunne dienstenpagina's** (it-diensten.html 80 woorden, verhuurders-vastgoed.html 102, wandpanelen.html 118) — geen woord content bijgekomen sinds 12 juli. Verhuurders-vastgoed.html blijft de zwakste pagina (SXO-persona-score 48/100).
- **Adres alleen zichtbaar op de juridische pagina's** (bijeffect van de KvK-fix) — op de hoofdpagina's staat het nog steeds alleen onzichtbaar in de schema.
- **Geen geo-coördinaten, openingHoursSpecification, Service- of BreadcrumbList-schema.**
- **Geen llms.txt, geen IndexNow, geen vraag-gestileerde koppen of FAQ-schema.**
- **Mobiele navigatie breekt nog naar twee regels** bij 375px.
- **Geen zichtbare bel/WhatsApp-CTA above the fold** op index.html; op contact.html afhankelijk van schermgrootte (op een iPhone SE-formaat scherm nog steeds deels onder de vouw).
- **Sitemap `lastmod`-datums nog steeds 2026-07-10** ondanks meerdere sindsdien gedeployde wijzigingen.

## Nieuwe bevinding — escalatie, geen verrassing maar wel actie waard

**portfolio.html is zwaarder geworden, niet lichter: 9,2 MB (was 7,89 MB).** Onafhankelijk bevestigd door zowel de technical- als de performance-agent. De vijf nieuwe portfolio-projecten van vandaag zijn toegevoegd zonder beeldoptimalisatie — dezelfde twee grote boosdoeners van de vorige meting (`terras-heemstede-na.png` 2,65 MB, `plinten-heemstede.jpg` 2,16 MB) staan er nog steeds onaangeroerd bij, plus een dozijn nieuwe foto's van 300-475 KB die ook geen width/height of WebP-conversie hebben gekregen. De LCP van portfolio.html is daardoor nu 2,59s — net over de 2,5s-grens naar "Needs Improvement". Advies: maak beeldoptimalisatie een vaste stap bij het toevoegen van elk nieuw portfolio-item, niet een losse opruimactie achteraf.

Kleinere technische nuance: van de 50 `<img>`-tags sitewide hebben er nu 12 (de logo-instanties) width/height — de overige 38 (portfolio-foto's, dienstenfoto's, bus-foto, contactfoto) nog niet. Dat is voorlopig geen actief zichtbare bug (de CSS-grid reserveert toevallig al ruimte), maar wel een fragiele situatie zonder eigen vangnet.

---

## Bijgewerkt geprioriteerd actieplan

**Kritiek**
1. Canonical tags toevoegen op alle 12 pagina's (kies één URL-vorm, bijv. de extensieloze variant die de navigatie al gebruikt).
2. Beeldoptimalisatie van de portfolio-foto's, te beginnen met de twee bekende zware bestanden, en dit als vaste stap opnemen bij toekomstige toevoegingen.
3. Reviews verzamelen bij de inmiddels 10+ getoonde klanten.

**Hoog**
4. Zichtbaar adres (of op zijn minst stad/regio) toevoegen aan de hoofdpagina's, niet alleen de juridische pagina's.
5. `geo`-coördinaten en `openingHoursSpecification` toevoegen aan de schema.
6. Nu de KvK-blokkade weg is: Werkspot.nl en/of Homedeal.nl claimen, plus Google Business Profile en Bing Places.
7. verhuurders-vastgoed.html inhoudelijk uitbreiden (onderhoudsplan, reactietijd, per-unit-prijsindicatie, case study).

**Middel**
8. Overige 38 afbeeldingen van width/height voorzien (of CSS aspect-ratio).
9. Mobiele navigatie op één regel laten passen bij 375px.
10. Sitemap `lastmod`-datums bijwerken — al lokaal gecorrigeerd door de audit-agent (zie hieronder), nog niet gecommit.
11. it-diensten.html en wandpanelen.html inhoudelijk verdiepen.

**Laag**
12. llms.txt aanmaken.
13. IndexNow implementeren.

---

## Let op: één bestand staat al klaar, nog niet gecommit

De sitemap-agent heeft `sitemap.xml` lokaal al bijgewerkt (realistische `lastmod`-datums per pagina op basis van git-geschiedenis, en de nutteloze `priority`-tags verwijderd). Dit is nog niet gecommit — wil je dat ik dat meeneemt in de volgende deploy?

---

Vorige meting: [SEO-AUDIT-handymat.nl.md](SEO-AUDIT-handymat.nl.md) (2026-07-12, score 58/100).
