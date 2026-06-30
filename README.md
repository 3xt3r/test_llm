export JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
export PATH="$JAVA_HOME/bin:$PATH"

Проверь:

echo $JAVA_HOME
which java
which javac
java -version
javac -version

Должно быть примерно так:

/usr/lib/jvm/java-21-openjdk-amd64
/usr/lib/jvm/java-21-openjdk-amd64/bin/java
/usr/lib/jvm/java-21-openjdk-amd64/bin/javac

Потом запусти Gradle без daemon:

./gradlew dependencies --no-daemon

Если опять та же ошибка, запусти с явным указанием Java home:

./gradlew dependencies --no-daemon -Dorg.gradle.java.home=/usr/lib/jvm/java-21-openjdk-amd64

Лучше сразу смотреть зависимости конкретного модуля:

./gradlew :server:dependencies --configuration runtimeClasspath --no-daemon -Dorg.gradle.java.home=/usr/lib/jvm/java-21-openjdk-amd64

Если всё равно падает, почисти кеш Gradle toolchains:

rm -rf ~/.gradle/caches/jdks
rm -rf ~/.gradle/daemon

и снова:

./gradlew :server:dependencies --configuration runtimeClasspath --no-daemon -Dorg.gradle.java.home=/usr/lib/jvm/java-21-openjdk-amd64

Ещё момент: у тебя Java такая:

openjdk version "21.0.11-ea"

ea означает early access. Для OpenSearch лучше использовать обычный стабильный JDK 21, например Temurin/Adoptium 21 или нормальный openjdk-21-jdk, не ea. Но сначала попробуй команды выше — возможно, достаточно остановить Gradle daemon и явно выставить JAVA_HOME.
