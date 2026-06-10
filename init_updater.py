sudo docker compose up -d
sudo docker compose logs -f
cd ~/Desktop/dependency-track-local
sudo docker compose up -d
sudo docker compose logs -f apiserver | grep -Ei "osv|github|ghsa|internal|analyz|vulnerab|purl|cpe|error|warn|401|403"
