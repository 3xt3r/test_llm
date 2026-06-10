cd ~/Desktop

sudo docker rm -f dependency-track-frontend-1 dependency-track-apiserver-1 dependency-track-postgres-1 2>/dev/null || true

sudo docker volume ls -q | grep -i dependency | xargs -r sudo docker volume rm

sudo docker rmi -f dependencytrack/frontend:latest dependencytrack/apiserver:latest postgres:17-alpine 2>/dev/null || true

sudo docker system prune -a --volumes -f

rm -rf dependency-track-local
mkdir dependency-track-local
cd dependency-track-local

curl -LO https://dependencytrack.org/docker-compose.yml

sudo docker compose up -d

sudo docker compose ps
