cat > init-trivy-locks.gradle <<'EOF'
allprojects {
    dependencyLocking {
        lockAllConfigurations()
    }

    tasks.register("resolveTrivyLockDeps") {
        doLast {
            configurations.findAll { conf ->
                conf.canBeResolved &&
                !conf.name.toLowerCase().contains("test") &&
                !conf.name.toLowerCase().contains("integ") &&
                !conf.name.toLowerCase().contains("qa") &&
                !conf.name.toLowerCase().contains("fixture")
            }.each { conf ->
                try {
                    println("Resolving ${project.path}:${conf.name}")
                    conf.resolve()
                } catch (Exception e) {
                    println("SKIP ${project.path}:${conf.name} -> ${e.class.simpleName}: ${e.message}")
                }
            }
        }
    }
}
EOF

Этот вариант пытается резолвить production-похожие конфигурации и пропускает тестовые/QA/fixtures, чтобы Trivy не получил слишком много dev-зависимостей.

4. Сгенерируй gradle.lockfile
./gradlew resolveTrivyLockDeps \
  --init-script init-trivy-locks.gradle \
  --write-locks \
  --no-daemon \
  -Dorg.gradle.java.home=/usr/lib/jvm/java-21-openjdk-amd64
