Посмотрим в логи — там будет видно что именно происходит при анализе:
bashdocker compose logs dtrack-apiserver --tail=50 | grep -iE "numpy|pypi|osv|nvd|mirror|error|warn"
И проверим есть ли вообще CVE для PyPI в базе:
bashcurl -s "http://localhost:8081/api/v1/vulnerability?pageSize=5&source=OSV" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM" | jq '[.[] | {vulnId: .vulnId, source: .source}]'
И проверим как сохранился компонент — правильно ли подхватился purl:
bashcurl -s "http://localhost:8081/api/v1/component/project/16397239-aff6-4559-a954-a47b592b33df" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM" | jq '[.[] | {name: .name, version: .version, purl: .purl}]'
Покажите вывод всех трёх — сразу станет понятно где обрыв.
