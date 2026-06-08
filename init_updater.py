NVD работает через старые feeds, а не через REST API. Нужно включить:
bashcurl -X POST "http://localhost:8081/api/v1/configProperty" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM" \
  -H "Content-Type: application/json" \
  -d '{"groupName":"vuln-source","propertyName":"nvd.api.enabled","propertyValue":"true","propertyType":"BOOLEAN"}'
2. GitHub Advisories отключён
json"github.advisories.enabled": "false"
Включить:
bashcurl -X POST "http://localhost:8081/api/v1/configProperty" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM" \
  -H "Content-Type: application/json" \
  -d '{"groupName":"vuln-source","propertyName":"github.advisories.enabled","propertyValue":"true","propertyType":"BOOLEAN"}'
После этого запустить зеркалирование NVD вручную:
bashcurl -X POST "http://localhost:8081/api/v1/task/mirror/nvd" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM"
И повторить анализ проекта:
bashcurl -X POST "http://localhost:8081/api/v1/finding/project/16397239-aff6-4559-a954-a47b592b33df/analyze" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM"
OSV у вас включён и настроен хорошо — PyPI есть в списке экосистем, так что numpy должен находиться через него. Подождите 1–2 минуты после анализа и проверьте findings снова.
