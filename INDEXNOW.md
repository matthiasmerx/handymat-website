# IndexNow

Deze site gebruikt het IndexNow-protocol om Bing en Yandex direct te laten weten wanneer een pagina is toegevoegd of gewijzigd, in plaats van te wachten tot hun crawler vanzelf langskomt. Google ondersteunt dit protocol niet en wordt dus niet via deze weg bereikt; voor Google blijft de sitemap en normale crawling de aangewezen route.

## Hoe het werkt

De sleutel `c858108357903ccfb47fdcbe0ed2ba8a` staat als losstaand tekstbestand in de root van de site, bereikbaar op `https://handymat.nl/c858108357903ccfb47fdcbe0ed2ba8a.txt`. Bing en Yandex gebruiken dat bestand om te verifiëren dat de submit daadwerkelijk van de eigenaar van handymat.nl komt. Het script `scripts/indexnow.sh` stuurt vervolgens een POST-request naar `https://api.indexnow.org/indexnow` met de sitenaam, de sleutel, de locatie van het sleutelbestand en de lijst van gewijzigde URL's.

## Het script opnieuw draaien

Na een wijziging aan een bestaande pagina of het toevoegen van een nieuwe pagina kan het script direct vanuit de root van de site gedraaid worden.

Voor een enkele gewijzigde pagina, bijvoorbeeld na het toevoegen van een nieuw portfolio-item:

```bash
scripts/indexnow.sh portfolio.html
```

Voor meerdere gewijzigde pagina's tegelijk:

```bash
scripts/indexnow.sh portfolio.html sitemap.xml
```

Zonder argumenten stuurt het script de volledige lijst van alle bekende pagina's opnieuw op:

```bash
scripts/indexnow.sh
```

Dit laatste is vooral bedoeld voor de eerste volledige submit of voor een incidentele algehele herbevestiging; voor dagelijks gebruik volstaat het om alleen de daadwerkelijk gewijzigde pagina('s) mee te geven.

## Nieuwe pagina toevoegen

Wanneer er een geheel nieuwe pagina bijkomt (dus niet alleen een wijziging aan een bestaande pagina), moet die pagina ook worden toegevoegd aan de `ALL_PAGES`-lijst bovenin `scripts/indexnow.sh`, zodat een toekomstige volledige submit die pagina meeneemt. Vergeet ook niet de pagina toe te voegen aan `sitemap.xml`.

## Verwacht resultaat

Een geslaagde submit geeft een HTTP-status 200 (of 202) terug van de IndexNow API. Het script toont deze statuscode en de eventuele response-body in de terminal, en sluit af met een foutmelding en een niet-nul exitcode als de submit is mislukt.
