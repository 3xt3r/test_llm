python3 sheduler.py --config config.yml
2026-06-08 10:15:21 | INFO    | GITLAB_TOKEN not set — will try anonymous clone first
2026-06-08 10:15:21 | INFO    | timeouts: scanner=3600s, distrib_scan=7200s, deptrack=3600s
2026-06-08 10:15:21 | INFO    | === product: gin ===
2026-06-08 10:15:21 | INFO    | --- version: v1.8.2 ---
2026-06-08 10:15:21 | INFO    |     repo already cloned: gin — fetching
2026-06-08 10:15:21 | INFO    |     running: git -c credential.helper= remote set-url origin https://github.com/gin-gonic/gin.git
2026-06-08 10:15:21 | INFO    |     running: git -c credential.helper= fetch --prune --all
2026-06-08 10:15:22 | INFO    |     checkout gin @ v1.8.2
2026-06-08 10:15:22 | INFO    |     running: git -c credential.helper= checkout v1.8.2
2026-06-08 10:15:22 | ERROR   |     [FAIL] git checkout v1.8.2: error: Your local changes to the following files would be overwritten by checkout:
	go.mod
	go.sum
Please commit your changes or stash them before you switch branches.
Aborting
2026-06-08 10:15:22 | ERROR   |     skipping gin because checkout v1.8.2 failed: error: Your local changes to the following files would be overwritten by checkout:
	go.mod
	go.sum
Please commit your changes or stash them before you switch branches.
Aborting
2026-06-08 10:15:22 | ERROR   |   [FAIL] gin / v1.8.2: all repositories failed; scanner was not run
2026-06-08 10:15:22 | INFO    | run log written: /home/kali/Desktop/results/2026-06-08/run.log
2026-06-08 10:15:22 | ERROR   | 1/1 scan(s) failed
