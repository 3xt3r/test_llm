sudo docker logs dependency-track-apiserver-1 -f 2>&1 | grep -iE "osv|github|nvd|mirror|epss|error"

Это займёт 30–90 минут при наличии NVD API-ключа.
3. Проверить что все базы загружены
bash# Общий счётчик
curl -s "http://localhost:8081/api/v1/vulnerability?pageSize=1" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM" \
  -I | grep -i "x-total-count"

# Проверить что OSV появился
curl -s "http://localhost:8081/api/v1/vulnerability?pageSize=3" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM" | \
  jq '[.[] | .source] | unique'
Должны увидеть ["NVD","OSV","GITHUB"].
4. Повторить анализ numpy
bashcurl -X POST "http://localhost:8081/api/v1/finding/project/16397239-aff6-4559-a954-a47b592b33df/analyze" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM"

# Подождать 30 секунд и проверить findings
curl -s "http://localhost:8081/api/v1/finding/project/16397239-aff6-4559-a954-a47b592b33df" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM" | \
  jq '[.[] | {vuln: .vulnerability.vulnId, severity: .vulnerability.severity, source: .vulnerability.source}]'
5. Если всё работает — загрузить реальные BOM-файлы ваших проектов
bashcurl -X PUT http://localhost:8081/api/v1/bom \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM" \
  -F "autoCreate=true" \
  -F "projectName=ИМЯ_ПРОЕКТА" \
  -F "projectVersion=1.0.0" \
  -F "bom=@/путь/до/bom.xml"
Скажите на каком шаге застряли или что именно хотите настроить дальше — интеграцию с CI/CD, нотификации, политики или что-то ещё.
