1. OSV и GitHub mirror вообще не запускались — в логах нет ни одной строки OsvMirrorTask или GithubAdvisoryMirrorTask. Значит задачи не триггернулись.
2. OSS Index пропускается — An API token has not been specified for use with OSS Index; Skipping
3. InternalAnalysisTask отрабатывает мгновенно (6мс) — это значит что в локальной базе нет записей привязанных к pkg:pypi/numpy, и матчинга не происходит.
Запустим OSV и GitHub mirror принудительно прямо в контейнере:
bash# OSV
sudo docker exec dependency-track-apiserver-1 \
  curl -s -X POST http://localhost:8080/api/v1/task/mirror/osv \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM"

# GitHub
sudo docker exec dependency-track-apiserver-1 \
  curl -s -X POST http://localhost:8080/api/v1/task/mirror/github \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM"
Обратите внимание — здесь порт 8080 (изнутри контейнера), а не 8081.
Затем сразу следим за логами:
bashsudo docker logs dependency-track-apiserver-1 -f 2>&1 | grep -iE "osv|github|mirror|error"
Должны появиться строки вида:
INFO [OsvMirrorTask] Mirroring OSV vulnerabilities for ecosystem: PyPI
INFO [GithubAdvisoryMirrorTask] Synchronizing GitHub Advisories
Покажите что появится в логах после запуска.
