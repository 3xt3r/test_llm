urs ago   Up 35 hours (healthy)                     5432/tcp                                      dependency-track-postgres-1
(venv) kali@kali-RedmiBook-16:~/Desktop$ sudo docker system prune
WARNING! This will remove:
  - all stopped containers
  - all networks not used by at least one container
  - all dangling images
  - unused build cache

Are you sure you want to continue? [y/N] y
Total reclaimed space: 0B
(venv) kali@kali-RedmiBook-16:~/Desktop$ sudo docker system prune -a --volumes
WARNING! This will remove:
  - all stopped containers
  - all networks not used by at least one container
  - all anonymous volumes not used by at least one container
  - all images without at least one container associated to them
  - all build cache

Are you sure you want to continue? [y/N] y
Total reclaimed space: 0B
(venv) kali@kali-RedmiBook-16:~/Desktop$ sudo docker image prune -a
WARNING! This will remove all images without at least one container associated to them.
Are you sure you want to continue? [y/N] y
Total reclaimed space: 0B
(venv) kali@kali-RedmiBook-16:~/Desktop$ sudo docker image prune -a --volumes
unknown flag: --volumes

Usage:  docker image prune [OPTIONS]

Run 'docker image prune --help' for more information
(venv) kali@kali-RedmiBook-16:~/Desktop$ sudo docker ps -a
CONTAINER ID   IMAGE                              COMMAND                  CREATED        STATUS                            PORTS                                         NAMES
76b2b5608681   dependencytrack/frontend:latest    "/docker-entrypoint.…"   35 hours ago   Up 35 hours                       0.0.0.0:8080->8080/tcp, [::]:8080->8080/tcp   dependency-track-frontend-1
b3abd5eeabe8   dependencytrack/apiserver:latest   "/usr/bin/tini -- /b…"   35 hours ago   Restarting (255) 49 seconds ago                                                 dependency-track-apiserver-1
03ebfe6fa958   postgres:17-alpine                 "docker-entrypoint.s…"   35 hours ago   Up 35 hours (healthy)             5432/tcp                                      dependency-track-postgres-1
(venv) kali@kali-RedmiBook-16:~/Desktop$ 

