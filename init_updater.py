он не подтянул cve23:36Claude responded: Это частая проблема.Это частая проблема. Несколько причин почему CVE не появляются:
1. Подождать — анализ асинхронный
bash# Проверить что обработка завершена
curl -s "http://localhost:8081/api/v1/bom/token/ВАШ_ТОКЕН" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM"
Должно вернуть {"processing":false}. Если true — ещё ждите.
2. Проверить включены ли аналайзеры
bashcurl -s "http://localhost:8081/api/v1/analyzer" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM"
Покажите вывод — посмотрим какие включены.
3. Принудительно запустить анализ компонента
Найти UUID проекта:
bashcurl -s "http://localhost:8081/api/v1/project?name=test-numpy" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM" | jq '.[0].uuid'
Затем запустить анализ вручную:
bashcurl -X POST "http://localhost:8081/api/v1/finding/project/ВАШ_UUID_ПРОЕКТА/analyze" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM"
Покажите вывод команды с аналайзерами — сразу станет понятно в чём дело.
