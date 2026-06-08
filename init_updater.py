Попробуем найти где описаны настройки OSV:
bashsudo docker exec dependency-track-apiserver-1 \
  grep -r "osv\|OSV\|google.osv" /tmp/Dependency-Track-0_0_0_0-8080/ 2>/dev/null | \
  grep -v ".class" | head -20
И посмотрим полный application.properties:
bashsudo docker exec dependency-track-apiserver-1 \
  cat /tmp/Dependency-Track-0_0_0_0-8080/webapp/WEB-INF/classes/application.properties
