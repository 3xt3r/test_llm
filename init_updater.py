Теперь всё ясно. В application.properties нет ни одного упоминания OSV, GitHub, NVD API — эти настройки хранятся только в базе данных, а не читаются из переменных окружения. Переменные окружения которые мы добавляли — DT 4.14.2 их просто игнорирует.
Нужно настраивать через API напрямую в БД. Выполните все команды разом:
bashAPI="http://localhost:8081/api/v1/configProperty"
KEY="odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM"

# OSV — включить нужные экосистемы
curl -s -X PUT "$API" -H "X-Api-Key: $KEY" -H "Content-Type: application/json" \
  -d '{"groupName":"vuln-source","propertyName":"google.osv.enabled","propertyValue":"PyPI;npm;Maven;crates.io;NuGet;RubyGems;Go;Hex;Pub;Packagist","propertyType":"STRING"}'

# GitHub — включить
curl -s -X PUT "$API" -H "X-Api-Key: $KEY" -H "Content-Type: application/json" \
  -d '{"groupName":"vuln-source","propertyName":"github.advisories.enabled","propertyValue":"true","propertyType":"BOOLEAN"}'

# GitHub — токен
curl -s -X PUT "$API" -H "X-Api-Key: $KEY" -H "Content-Type: application/json" \
  -d '{"groupName":"vuln-source","propertyName":"github.advisories.access.token","propertyValue":"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","propertyType":"STRING"}'

# NVD API — включить
curl -s -X PUT "$API" -H "X-Api-Key: $KEY" -H "Content-Type: application/json" \
  -d '{"groupName":"vuln-source","propertyName":"nvd.api.enabled","propertyValue":"true","propertyType":"BOOLEAN"}'

# NVD API — ключ
curl -s -X PUT "$API" -H "X-Api-Key: $KEY" -H "Content-Type: application/json" \
  -d '{"groupName":"vuln-source","propertyName":"nvd.api.key","propertyValue":"31DACAE2-4941-F111-836A-129478FCB64D","propertyType":"ENCRYPTEDSTRING"}'
Затем запустить зеркалирование вручную изнутри контейнера:
bash# OSV
sudo docker exec dependency-track-apiserver-1 \
  curl -s -X POST http://localhost:8080/api/v1/task/mirror/osv \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM"

# GitHub
sudo docker exec dependency-track-apiserver-1 \
  curl -s -X POST http://localhost:8080/api/v1/task/mirror/github \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM"
И сразу смотреть логи:
bashsudo docker logs dependency-track-apiserver-1 -f 2>&1 | grep -iE "osv|github|mirror|error"
На этот раз должно появиться OsvDownloadTask с реальной загрузкой по экосистемам.
