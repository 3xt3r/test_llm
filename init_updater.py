sudo docker exec dependency-track-apiserver-1 \
  cat /tmp/Dependency-Track-0_0_0_0-8080/webapp/WEB-INF/classes/application.properties | \
  grep -iE "osv|github|nvd|epss|google"
