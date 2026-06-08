services:
  apiserver:
    image: dependencytrack/apiserver:4.14.2
    depends_on:
      postgres:
        condition: service_healthy
    environment:
      # Database
      ALPINE_DATABASE_MODE: "external"
      ALPINE_DATABASE_URL: "jdbc:postgresql://postgres:5432/dtrack"
      ALPINE_DATABASE_DRIVER: "org.postgresql.Driver"
      ALPINE_DATABASE_USERNAME: "dtrack"
      ALPINE_DATABASE_PASSWORD: "dtrack"
      ALPINE_DATABASE_POOL_ENABLED: "true"
      ALPINE_DATABASE_POOL_MAX_SIZE: "20"
      ALPINE_DATABASE_POOL_MIN_IDLE: "10"
      ALPINE_DATABASE_POOL_IDLE_TIMEOUT: "300000"
      ALPINE_DATABASE_POOL_MAX_LIFETIME: "600000"

      # OSV — перечисляем нужные экосистемы
      GOOGLE_OSV_ENABLED: "PyPI;npm;Maven;crates.io;NuGet;RubyGems;Go;Hex;Pub;Packagist"

      # GitHub Advisory Database — вставьте свой PAT
      GITHUB_ADVISORIES_ENABLED: "true"
      GITHUB_ADVISORIES_ACCESS_TOKEN: "ghp_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

      # NVD API — вставьте свой ключ с nvd.nist.gov
      NVD_API_ENABLED: "true"
      NVD_API_KEY: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"

      # EPSS (вероятность эксплуатации)
      EPSS_ENABLED: "true"

      # CORS
      ALPINE_CORS_ENABLED: "true"
      ALPINE_CORS_ALLOW_ORIGIN: "*"
      ALPINE_CORS_ALLOW_METHODS: "GET, POST, PUT, DELETE, OPTIONS"
      ALPINE_CORS_ALLOW_HEADERS: "Origin, Content-Type, Authorization, X-Requested-With, Content-Length, Accept, X-Api-Key, X-Total-Count, *"
      ALPINE_CORS_EXPOSE_HEADERS: "Origin, Content-Type, Authorization, X-Requested-With, Content-Length, Accept, X-Api-Key, X-Total-Count"
      ALPINE_CORS_ALLOW_CREDENTIALS: "true"
      ALPINE_CORS_MAX_AGE: "3600"

      # Таймауты HTTP (секунды)
      ALPINE_HTTP_TIMEOUT_CONNECTION: "30"
      ALPINE_HTTP_TIMEOUT_SOCKET: "60"
      ALPINE_HTTP_TIMEOUT_POOL: "60"

      # Логирование
      LOGGING_LEVEL: "INFO"

      # JVM — под 4 ГБ лимит контейнера
      EXTRA_JAVA_OPTIONS: "-XX:ActiveProcessorCount=4 -XX:+UseContainerSupport"

    deploy:
      resources:
        limits:
          memory: 4g
        reservations:
          memory: 2g
      restart_policy:
        condition: on-failure
        delay: 10s
        max_attempts: 3

    ports:
      - "8081:8080"

    volumes:
      - dtrack-data:/data

    healthcheck:
      test: ["CMD-SHELL", "curl -f -s --max-time 3 --noproxy '*' -o /dev/null http://127.0.0.1:8080/health"]
      interval: 30s
      start_period: 120s
      timeout: 5s
      retries: 5

    restart: unless-stopped

  frontend:
    image: dependencytrack/frontend:4.14.2
    depends_on:
      apiserver:
        condition: service_healthy
    environment:
      API_BASE_URL: "http://localhost:8081"
    ports:
      - "8080:8080"
    healthcheck:
      test: ["CMD-SHELL", "curl -f -s --max-time 3 -o /dev/null http://127.0.0.1:8080"]
      interval: 30s
      start_period: 30s
      timeout: 3s
      retries: 3
    restart: unless-stopped

  postgres:
    image: postgres:17-alpine
    environment:
      POSTGRES_DB: "dtrack"
      POSTGRES_USER: "dtrack"
      POSTGRES_PASSWORD: "dtrack"
      PGDATA: "/var/lib/postgresql/data/pgdata"
      # Оптимизация под DT
      POSTGRES_INITDB_ARGS: "--encoding=UTF8 --lc-collate=C --lc-ctype=C"
    command: >
      postgres
      -c max_connections=50
      -c shared_buffers=256MB
      -c effective_cache_size=512MB
      -c work_mem=16MB
      -c maintenance_work_mem=64MB
      -c checkpoint_completion_target=0.9
      -c wal_buffers=16MB
      -c default_statistics_target=100
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U dtrack -d dtrack"]
      interval: 5s
      timeout: 3s
      retries: 5
      start_period: 10s
    volumes:
      - postgres-data:/var/lib/postgresql/data
    restart: unless-stopped

volumes:
  dtrack-data:
    driver: local
  postgres-data:
    driver: local
