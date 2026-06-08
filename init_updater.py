Всё автоматически — ничего качать вручную не нужно. Docker сам скачает образы, Dependency-Track сам скачает базы уязвимостей.
Вот пошаговая инструкция:

Шаг 1 — Убедись, что Docker установлен
bashdocker --version
docker compose version
Если не установлен — скачай Docker Desktop.

Шаг 2 — Создай папку и файл
bashmkdir dependency-track && cd dependency-track
Создай файл docker-compose.yml:
bashcat > docker-compose.yml << 'EOF'
volumes:
  postgres-data: {}
  apiserver-data: {}

services:

  postgres:
    image: postgres:17-alpine
    environment:
      POSTGRES_DB: dtrack
      POSTGRES_USER: dtrack
      POSTGRES_PASSWORD: dtrack_local
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U dtrack -d dtrack"]
      interval: 5s
      timeout: 3s
      retries: 5
    volumes:
      - postgres-data:/var/lib/postgresql/data
    restart: unless-stopped

  apiserver:
    image: dependencytrack/apiserver:latest
    depends_on:
      postgres:
        condition: service_healthy
    environment:
      ALPINE_DATABASE_MODE: external
      ALPINE_DATABASE_URL: jdbc:postgresql://postgres:5432/dtrack
      ALPINE_DATABASE_DRIVER: org.postgresql.Driver
      ALPINE_DATABASE_USERNAME: dtrack
      ALPINE_DATABASE_PASSWORD: dtrack_local
      ALPINE_DATABASE_POOL_ENABLED: "true"
      ALPINE_NVD_API_ENABLED: "true"
      ALPINE_VULNERABILITY_ALIAS_SYNCHRONIZATION_ENABLED: "true"
      ALPINE_WORKER_THREADS: "4"
    ports:
      - "8081:8080"
    volumes:
      - apiserver-data:/data
    restart: unless-stopped

  frontend:
    image: dependencytrack/frontend:latest
    depends_on:
      - apiserver
    environment:
      API_BASE_URL: http://localhost:8081
    ports:
      - "8080:8080"
    restart: unless-stopped
EOF

Шаг 3 — Запусти
bashdocker compose up -d
Docker скачает три образа (~1 GB суммарно) и запустит контейнеры.

Шаг 4 — Жди готовности API-сервера
bashdocker compose logs -f apiserver | grep -i "dependency-track is ready"
Подождёт и выведет строку Dependency-Track is ready — это занимает 1–3 минуты. После этого нажми Ctrl+C.

Шаг 5 — Открой UI и смени пароль
Открой в браузере: http://localhost:8080

Логин: admin
Пароль: admin

Сразу попросит сменить пароль — смени.

Шаг 6 — Включи источники уязвимостей
6.1. NVD API key (бесплатно, но необязательно)
Без ключа работает, но медленнее. Если хочешь ключ:

Перейди на https://nvd.nist.gov/developers/request-an-api-key
Введи email → получишь ключ письмом
В UI: Administration → Vulnerability Sources → NVD → вставь ключ → Save

6.2. OSV ← главное для PURL/пакетов
Administration → Vulnerability Sources → OSV
→ Enable ✓
→ Выбери свои экосистемы (Maven, npm, PyPI, Go, NuGet — что используешь)
→ Save
6.3. GitHub Advisories ← для open source пакетов

Создай токен на https://github.com/settings/tokens → Generate new token (classic) → scope: read:packages
В UI: Administration → Vulnerability Sources → GitHub Advisories → вставь токен → Enable → Save


Шаг 7 — Дождись зеркалирования баз
bashdocker compose logs -f apiserver | grep -iE "mirror|nvd|osv|github"
NVD качается 20–40 минут (150k+ CVE). OSV и GitHub — быстрее. Прогресс видно в логах.
Или смотри прямо в UI: Administration → Tasks — там список задач и статус каждой.

Шаг 8 — Проверь, что всё работает

Projects → Create Project → дай название
Components → Add Component → например, Name: lodash, Version: 4.17.11, PURL: pkg:npm/lodash@4.17.11
Через минуту компонент должен показать найденные CVE


После этого всё готово к работе. Скажи, какой у тебя стек — помогу настроить генерацию SBOM и загрузку в Dependency-Track.
