#!/usr/bin/env bash
# Meldt gewijzigde URL's van handymat.nl bij Bing/Yandex via het IndexNow-protocol.
# Google ondersteunt IndexNow niet; dit is uitsluitend voor Bing en Yandex.
#
# Gebruik:
#   scripts/indexnow.sh                          -> submit alle bekende pagina's
#   scripts/indexnow.sh pad1.html pad2.html ...   -> submit alleen de opgegeven pagina's (relatief aan de root)
#
# Zie INDEXNOW.md voor uitleg.

set -euo pipefail

HOST="handymat.nl"
KEY="c858108357903ccfb47fdcbe0ed2ba8a"
KEY_LOCATION="https://${HOST}/${KEY}.txt"
ENDPOINT="https://api.indexnow.org/indexnow"

# Alle huidige pagina's uit sitemap.xml (extensieloos, consistent met canonicals).
# Noindex-pagina's (privacy, algemene voorwaarden, EN-varianten daarvan) staan
# hier bewust niet in, net als in de sitemap.
ALL_PAGES=(
  ""
  "over-mij"
  "diensten"
  "verhuurders-vastgoed"
  "it-diensten"
  "wandpanelen"
  "portfolio"
  "tarieven"
  "en/"
  "en/about"
  "en/services"
  "en/portfolio"
  "en/rates"
  "en/property-management"
)

if [ "$#" -gt 0 ]; then
  PAGES=("$@")
else
  PAGES=("${ALL_PAGES[@]}")
fi

URL_LIST_JSON=""
for page in "${PAGES[@]}"; do
  url="https://${HOST}/${page}"
  if [ -n "$URL_LIST_JSON" ]; then
    URL_LIST_JSON+=","
  fi
  URL_LIST_JSON+="\"${url}\""
done

PAYLOAD=$(cat <<EOF
{
  "host": "${HOST}",
  "key": "${KEY}",
  "keyLocation": "${KEY_LOCATION}",
  "urlList": [${URL_LIST_JSON}]
}
EOF
)

echo "Versturen naar ${ENDPOINT} voor ${#PAGES[@]} URL('s)..."

RESPONSE=$(curl -s -w "\n%{http_code}" -X POST "${ENDPOINT}" \
  -H "Content-Type: application/json; charset=utf-8" \
  -d "${PAYLOAD}")

HTTP_CODE=$(echo "${RESPONSE}" | tail -n1)
BODY=$(echo "${RESPONSE}" | sed '$d')

echo "HTTP-status: ${HTTP_CODE}"
if [ -n "${BODY}" ]; then
  echo "Response body: ${BODY}"
fi

if [ "${HTTP_CODE}" != "200" ] && [ "${HTTP_CODE}" != "202" ]; then
  echo "IndexNow-submit is mislukt." >&2
  exit 1
fi

echo "IndexNow-submit gelukt."
