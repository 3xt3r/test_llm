Картина ясная. Проблем несколько:
1. OSV не загружен — в базе только NVD записи, OSV записей нет совсем. Все 355k — это NVD.
2. NVD не привязывает CVE к PyPI пакетам — NVD не знает о pkg:pypi/numpy, он оперирует CPE (cpe:2.3:a:numpy:numpy). Без CPE в BOM внутренний аналайзер не матчит.
Решение: запустить OSV зеркалирование вручную
bashcurl -X POST "http://localhost:8081/api/v1/task/mirror/osv" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM"
Затем следить за логами (найдите имя контейнера):
bashdocker ps --format "{{.Names}}"
bashdocker logs ИМЯ_КОНТЕЙНЕРА -f 2>&1 | grep -iE "osv|pypi|mirror"
После того как OSV загрузится — проверить что PyPI записи появились:
bashcurl -s "http://localhost:8081/api/v1/vulnerability?pageSize=5" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM" | jq '[.[] | select(.source == "OSV") | {vulnId: .vulnId, source: .source}] | .[0:5]'
Если OSV появился — повторить анализ проекта и findings должны появиться. OSV как раз матчит по pkg:pypi/... напрямую.You said: а github?а github?23:48Claude responded: Из конфига видно:Из конфига видно:
json"github.advisories.enabled": "false"
"github.advisories.access.token": null  ← токен не задан
Нужно сначала создать GitHub PAT, потом включить.
Шаг 1: создать токен на GitHub
Идёте на https://github.com/settings/tokens → Generate new token (classic) → выбираете только read:packages → копируете токен.
Шаг 2: добавить токен и включить
bash# Добавить токен
curl -X POST "http://localhost:8081/api/v1/configProperty" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM" \
  -H "Content-Type: application/json" \
  -d '{"groupName":"vuln-source","propertyName":"github.advisories.access.token","propertyValue":"ВАШ_ТОКЕН","propertyType":"STRING"}'

# Включить GitHub Advisories
curl -X POST "http://localhost:8081/api/v1/configProperty" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM" \
  -H "Content-Type: application/json" \
  -d '{"groupName":"vuln-source","propertyName":"github.advisories.enabled","propertyValue":"true","propertyType":"BOOLEAN"}'
Шаг 3: запустить зеркалирование
bashcurl -X POST "http://localhost:8081/api/v1/task/mirror/github" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM"
GitHub Advisory Database хорошо покрывает PyPI — для numpy там есть записи с прямой привязкой к pkg:pypi/numpy. Так что после загрузки findings по numpy должны появиться даже без OSV.


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
