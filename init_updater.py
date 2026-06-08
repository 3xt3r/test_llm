Анализ запустился (токен получен), но /api/v1/analyzer вернул пустой ответ — эндпоинт не существует в версии 4.14.2.
Подождите 30 секунд и проверьте нашлись ли findings:
bashcurl -s "http://localhost:8081/api/v1/finding/project/16397239-aff6-4559-a954-a47b592b33df" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM" | jq length
Если 0 — проверим аналайзеры через правильный эндпоинт для 4.14:
bashcurl -s "http://localhost:8081/api/v1/configProperty/aggregate" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM" | jq '[.[] | select(.groupName == "analyzer")]'
Это покажет какие аналайзеры включены и правильно ли они сконфигурированы.
