Тоже пустой ответ. Попробуем без фильтра — посмотрим все настройки:
bashcurl -s "http://localhost:8081/api/v1/configProperty" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM" | jq .
Если и это пустое — скорее всего проблема с правами API-ключа. Проверьте какие права у ключа:
bash# Посмотреть все команды (teams) и их права
curl -s "http://localhost:8081/api/v1/team" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM" | jq '[.[] | {name: .name, permissions: [.permissions[].name]}]'
Для управления конфигурацией ключу нужно право SYSTEM_CONFIGURATION. Если его нет — зайдите в UI:
Administration → Access Management → Teams → [ваша команда] → Permissions
И добавьте SYSTEM_CONFIGURATION, после чего повторите запрос про аналайзеры.
