Справедливое замечание. Проблема в том, что я давал советы основываясь на документации, но не знал точных названий переменных окружения для вашей версии 4.14.2 — они отличаются от того что описано в общей документации.
Давайте сделаем правильно один раз. Найдём точные названия прямо из исходников:
bashsudo docker exec dependency-track-apiserver-1 \
  find / -name "application.properties" 2>/dev/null | head -5
И:
bashsudo docker exec dependency-track-apiserver-1 \
  env | sort | grep -iE "osv|github|nvd|epss|google|mirror"
Это покажет какие переменные контейнер реально понимает и как они называются в 4.14.2. После этого дам финальный рабочий docker-compose.yml без угадываний.
