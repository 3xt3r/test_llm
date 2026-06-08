(venv) kali@kali-RedmiBook-16:~/Desktop/oss_checks$ sudo docker ps -a
CONTAINER ID   IMAGE                       COMMAND                  CREATED      STATUS                PORTS                                         NAMES
0c38c628e4c4   dependencytrack/frontend    "/docker-entrypoint.…"   2 days ago   Up 2 days             0.0.0.0:8080->8080/tcp, [::]:8080->8080/tcp   dependency-track-frontend-1
17210ea7a937   dependencytrack/apiserver   "/usr/bin/tini -- /b…"   2 days ago   Up 2 days (healthy)   0.0.0.0:8081->8080/tcp, [::]:8081->8080/tcp   dependency-track-apiserver-1
2fef75560716   postgres:17-alpine          "docker-entrypoint.s…"   2 days ago   Up 2 days (healthy)   5432/tcp                                      dependency-track-postgres-1
(venv) kali@kali-RedmiBook-16:~/Desktop/oss_checks$ sudo docker ps --format "{{.Names}}"
dependency-track-frontend-1
dependency-track-apiserver-1
dependency-track-postgres-1
(venv) kali@kali-RedmiBook-16:~/Desktop/oss_checks$ sudo docker logs dependency-track-apiserver-1 --tail=100 2>&1
2026-06-08 07:31:30,113 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 50310be0-df0c-4816-ad1b-a31444fa5574
2026-06-08 07:31:30,114 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 88aa31ba-08e7-4ab6-aaaf-9ddfe4edbf06
2026-06-08 07:31:30,569 INFO [ProjectMetricsUpdateTask] Executing metrics update for project d61a12d6-7010-4af1-b3fd-5fb60185b11c
2026-06-08 07:31:30,569 INFO [ProjectMetricsUpdateTask] Executing metrics update for project d138ed93-3543-4db6-a699-1c7b7f26ef73
2026-06-08 07:31:30,569 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 6e7fa2b5-fde8-41b8-a7e4-078f6232bbf5
2026-06-08 07:31:30,569 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 16397239-aff6-4559-a954-a47b592b33df
2026-06-08 07:31:30,570 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 01d591ed-8eb6-4f3d-bd70-e09c7622dfcb
2026-06-08 07:31:30,570 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 7a6c5d37-f594-4c47-ba28-8f191bb6ed7f
2026-06-08 07:31:31,133 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 95580e40-242b-47f3-9999-435433fecf2f
2026-06-08 07:31:31,133 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 77093aa6-2c10-4101-bed6-d7de8eb6052b
2026-06-08 07:31:31,591 INFO [PortfolioMetricsUpdateTask] Completed portfolio metrics update in 00:04:273
2026-06-08 13:45:20,490 INFO [InternalAnalysisTask] Starting internal analysis task [eventToken=30f5fc19-d922-4b8d-be57-e0f96dde2935]
2026-06-08 13:45:20,490 INFO [InternalAnalysisTask] Analyzing 1 component(s) [eventToken=30f5fc19-d922-4b8d-be57-e0f96dde2935]
2026-06-08 13:45:20,498 INFO [InternalAnalysisTask] Internal analysis complete [eventToken=30f5fc19-d922-4b8d-be57-e0f96dde2935]
2026-06-08 13:45:20,500 WARN [OssIndexAnalysisTask] An API token has not been specified for use with OSS Index; Skipping [eventToken=30f5fc19-d922-4b8d-be57-e0f96dde2935]
2026-06-08 13:45:20,502 INFO [RepositoryMetaAnalyzerTask] Performing component repository metadata analysis against 1 components
2026-06-08 13:45:20,502 INFO [PolicyEngine] Evaluating 1 component(s) against applicable policies [eventToken=30f5fc19-d922-4b8d-be57-e0f96dde2935, projectName=commons-lang__rel/commons-lang-3.17.0-orig, projectUuid=16397239-aff6-4559-a954-a47b592b33df, projectVersion=null]
2026-06-08 13:45:20,558 INFO [PolicyEngine] Policy analysis complete [eventToken=30f5fc19-d922-4b8d-be57-e0f96dde2935, projectName=commons-lang__rel/commons-lang-3.17.0-orig, projectUuid=16397239-aff6-4559-a954-a47b592b33df, projectVersion=null]
2026-06-08 13:45:20,559 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 16397239-aff6-4559-a954-a47b592b33df
2026-06-08 13:45:53,813 INFO [RepositoryMetaAnalyzerTask] Completed component repository metadata analysis against 1 components
2026-06-08 14:33:21,112 INFO [VulnerabilityMetricsUpdateTask] Executing metrics update on vulnerability database
2026-06-08 14:33:21,112 INFO [PortfolioMetricsUpdateTask] Executing portfolio metrics update
2026-06-08 14:33:21,115 INFO [ProjectMetricsUpdateTask] Executing metrics update for project dcf7943a-8288-4f93-8785-6bd123eee3b2
2026-06-08 14:33:21,115 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 4880d666-81f8-4f86-aeb4-519e71e964e0
2026-06-08 14:33:21,115 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 422d9460-81cb-4f38-9125-b63069972700
2026-06-08 14:33:21,115 INFO [ProjectMetricsUpdateTask] Executing metrics update for project c1123885-35ac-4cc5-b587-6ede7fd9dd64
2026-06-08 14:33:21,115 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 68d35c44-cca1-48da-990e-6627a35a1543
2026-06-08 14:33:21,116 INFO [ProjectMetricsUpdateTask] Executing metrics update for project c797a87b-deb1-4035-880d-092737ca9968
2026-06-08 14:33:21,601 INFO [VulnerabilityMetricsUpdateTask] Completed metrics update on vulnerability database in 00:00:489
2026-06-08 14:33:22,714 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 600e818f-b85d-4692-af57-7247c103b0a3
2026-06-08 14:33:22,714 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 125fdde8-8d2d-4ca2-ac1a-a10a26e1158e
2026-06-08 14:33:22,714 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 001b27cc-5aba-424a-9f1b-861f675bfdd2
2026-06-08 14:33:22,715 INFO [ProjectMetricsUpdateTask] Executing metrics update for project c7c06608-9308-435c-b7f4-d42e71d05c78
2026-06-08 14:33:22,714 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 429f00de-2ed3-45d0-82df-5efa048c00c1
2026-06-08 14:33:22,715 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 7943bed9-16b6-4f50-b50e-131d47eb39cb
2026-06-08 14:33:23,913 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 8c68b6d3-7edb-49ae-99b6-b43395fe7b8f
2026-06-08 14:33:23,913 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 43d01794-f879-4021-b2cc-7be212262542
2026-06-08 14:33:23,913 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 9cf548e6-9b56-4d7a-a820-20130ee85d8a
2026-06-08 14:33:23,913 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 97c918ae-7c87-4fed-88fb-1fbd65e14dd0
2026-06-08 14:33:23,913 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 88aa31ba-08e7-4ab6-aaaf-9ddfe4edbf06
2026-06-08 14:33:23,913 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 50310be0-df0c-4816-ad1b-a31444fa5574
2026-06-08 14:33:24,419 INFO [ProjectMetricsUpdateTask] Executing metrics update for project d61a12d6-7010-4af1-b3fd-5fb60185b11c
2026-06-08 14:33:24,419 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 16397239-aff6-4559-a954-a47b592b33df
2026-06-08 14:33:24,419 INFO [ProjectMetricsUpdateTask] Executing metrics update for project d138ed93-3543-4db6-a699-1c7b7f26ef73
2026-06-08 14:33:24,419 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 6e7fa2b5-fde8-41b8-a7e4-078f6232bbf5
2026-06-08 14:33:24,419 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 7a6c5d37-f594-4c47-ba28-8f191bb6ed7f
2026-06-08 14:33:24,419 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 01d591ed-8eb6-4f3d-bd70-e09c7622dfcb
2026-06-08 14:33:24,956 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 95580e40-242b-47f3-9999-435433fecf2f
2026-06-08 14:33:24,956 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 77093aa6-2c10-4101-bed6-d7de8eb6052b
2026-06-08 14:33:25,429 INFO [PortfolioMetricsUpdateTask] Completed portfolio metrics update in 00:04:317
2026-06-08 20:29:15,809 INFO [PortfolioMetricsUpdateTask] Executing portfolio metrics update
2026-06-08 20:29:15,809 INFO [VulnerabilityMetricsUpdateTask] Executing metrics update on vulnerability database
2026-06-08 20:29:15,812 INFO [ProjectMetricsUpdateTask] Executing metrics update for project c1123885-35ac-4cc5-b587-6ede7fd9dd64
2026-06-08 20:29:15,812 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 422d9460-81cb-4f38-9125-b63069972700
2026-06-08 20:29:15,812 INFO [ProjectMetricsUpdateTask] Executing metrics update for project dcf7943a-8288-4f93-8785-6bd123eee3b2
2026-06-08 20:29:15,812 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 68d35c44-cca1-48da-990e-6627a35a1543
2026-06-08 20:29:15,812 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 4880d666-81f8-4f86-aeb4-519e71e964e0
2026-06-08 20:29:15,813 INFO [ProjectMetricsUpdateTask] Executing metrics update for project c797a87b-deb1-4035-880d-092737ca9968
2026-06-08 20:29:16,107 INFO [VulnerabilityMetricsUpdateTask] Completed metrics update on vulnerability database in 00:00:298
2026-06-08 20:29:17,206 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 600e818f-b85d-4692-af57-7247c103b0a3
2026-06-08 20:29:17,207 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 125fdde8-8d2d-4ca2-ac1a-a10a26e1158e
2026-06-08 20:29:17,207 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 429f00de-2ed3-45d0-82df-5efa048c00c1
2026-06-08 20:29:17,207 INFO [ProjectMetricsUpdateTask] Executing metrics update for project c7c06608-9308-435c-b7f4-d42e71d05c78
2026-06-08 20:29:17,207 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 001b27cc-5aba-424a-9f1b-861f675bfdd2
2026-06-08 20:29:17,207 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 7943bed9-16b6-4f50-b50e-131d47eb39cb
2026-06-08 20:29:18,172 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 97c918ae-7c87-4fed-88fb-1fbd65e14dd0
2026-06-08 20:29:18,172 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 9cf548e6-9b56-4d7a-a820-20130ee85d8a
2026-06-08 20:29:18,172 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 8c68b6d3-7edb-49ae-99b6-b43395fe7b8f
2026-06-08 20:29:18,172 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 43d01794-f879-4021-b2cc-7be212262542
2026-06-08 20:29:18,172 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 88aa31ba-08e7-4ab6-aaaf-9ddfe4edbf06
2026-06-08 20:29:18,173 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 50310be0-df0c-4816-ad1b-a31444fa5574
2026-06-08 20:29:18,577 INFO [ProjectMetricsUpdateTask] Executing metrics update for project d61a12d6-7010-4af1-b3fd-5fb60185b11c
2026-06-08 20:29:18,577 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 6e7fa2b5-fde8-41b8-a7e4-078f6232bbf5
2026-06-08 20:29:18,577 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 16397239-aff6-4559-a954-a47b592b33df
2026-06-08 20:29:18,578 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 7a6c5d37-f594-4c47-ba28-8f191bb6ed7f
2026-06-08 20:29:18,578 INFO [ProjectMetricsUpdateTask] Executing metrics update for project d138ed93-3543-4db6-a699-1c7b7f26ef73
2026-06-08 20:29:18,578 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 01d591ed-8eb6-4f3d-bd70-e09c7622dfcb
2026-06-08 20:29:19,036 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 95580e40-242b-47f3-9999-435433fecf2f
2026-06-08 20:29:19,036 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 77093aa6-2c10-4101-bed6-d7de8eb6052b
2026-06-08 20:29:19,496 INFO [PortfolioMetricsUpdateTask] Completed portfolio metrics update in 00:03:687
2026-06-08 20:34:25,212 INFO [InternalAnalysisTask] Starting internal analysis task [eventToken=c490d6ee-5c52-4215-8fc9-4a531cb363e3]
2026-06-08 20:34:25,212 INFO [InternalAnalysisTask] Analyzing 1 component(s) [eventToken=c490d6ee-5c52-4215-8fc9-4a531cb363e3]
2026-06-08 20:34:25,217 INFO [InternalAnalysisTask] Internal analysis complete [eventToken=c490d6ee-5c52-4215-8fc9-4a531cb363e3]
2026-06-08 20:34:25,219 WARN [OssIndexAnalysisTask] An API token has not been specified for use with OSS Index; Skipping [eventToken=c490d6ee-5c52-4215-8fc9-4a531cb363e3]
2026-06-08 20:34:25,223 INFO [PolicyEngine] Evaluating 1 component(s) against applicable policies [eventToken=c490d6ee-5c52-4215-8fc9-4a531cb363e3, projectName=express__v4.22.2-orig, projectUuid=77093aa6-2c10-4101-bed6-d7de8eb6052b, projectVersion=null]
2026-06-08 20:34:25,223 INFO [RepositoryMetaAnalyzerTask] Performing component repository metadata analysis against 1 components
2026-06-08 20:34:25,229 INFO [RepositoryMetaAnalyzerTask] Completed component repository metadata analysis against 1 components
2026-06-08 20:34:25,254 INFO [PolicyEngine] Policy analysis complete [eventToken=c490d6ee-5c52-4215-8fc9-4a531cb363e3, projectName=express__v4.22.2-orig, projectUuid=77093aa6-2c10-4101-bed6-d7de8eb6052b, projectVersion=null]
2026-06-08 20:34:25,255 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 77093aa6-2c10-4101-bed6-d7de8eb6052b
2026-06-08 20:35:05,078 INFO [UserResource] Successful user login / username: admin / IP Address: 172.18.0.1 / User Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:147.0) Gecko/20100101 Firefox/147.0 [requestId=20f43acd-7939-4c45-890b-bec30809c40e, requestMethod=POST, requestUri=/v1/user/login]
2026-06-08 20:37:27,224 INFO [FindingResource] Analysis of project 16397239-aff6-4559-a954-a47b592b33df requested by odt_WeFtwiB1******************************** [principal=odt_WeFtwiB1********************************, requestUri=/v1/finding/project/{uuid}/analyze, requestId=dfc66888-a47d-4e5c-9953-dfa5ccf900e2, requestMethod=POST]
2026-06-08 20:37:27,251 INFO [InternalAnalysisTask] Starting internal analysis task [eventToken=b2551e5c-52a3-4089-9956-841685c33193, projectName=commons-lang__rel/commons-lang-3.17.0-orig, vulnAnalysisLevel=ON_DEMAND, projectUuid=16397239-aff6-4559-a954-a47b592b33df, projectVersion=null]
2026-06-08 20:37:27,251 INFO [InternalAnalysisTask] Analyzing 1 component(s) [eventToken=b2551e5c-52a3-4089-9956-841685c33193, projectName=commons-lang__rel/commons-lang-3.17.0-orig, vulnAnalysisLevel=ON_DEMAND, projectUuid=16397239-aff6-4559-a954-a47b592b33df, projectVersion=null]
2026-06-08 20:37:27,256 INFO [InternalAnalysisTask] Internal analysis complete [eventToken=b2551e5c-52a3-4089-9956-841685c33193, projectName=commons-lang__rel/commons-lang-3.17.0-orig, vulnAnalysisLevel=ON_DEMAND, projectUuid=16397239-aff6-4559-a954-a47b592b33df, projectVersion=null]
2026-06-08 20:37:27,257 WARN [OssIndexAnalysisTask] An API token has not been specified for use with OSS Index; Skipping [eventToken=b2551e5c-52a3-4089-9956-841685c33193, projectName=commons-lang__rel/commons-lang-3.17.0-orig, vulnAnalysisLevel=ON_DEMAND, projectUuid=16397239-aff6-4559-a954-a47b592b33df, projectVersion=null]
2026-06-08 20:37:27,270 INFO [PolicyEngine] Evaluating 1 component(s) against applicable policies [eventToken=b2551e5c-52a3-4089-9956-841685c33193, projectName=commons-lang__rel/commons-lang-3.17.0-orig, projectUuid=16397239-aff6-4559-a954-a47b592b33df, projectVersion=null]
2026-06-08 20:37:27,271 INFO [RepositoryMetaAnalyzerTask] Performing component repository metadata analysis against 1 components
2026-06-08 20:37:27,275 INFO [RepositoryMetaAnalyzerTask] Completed component repository metadata analysis against 1 components
2026-06-08 20:37:27,339 INFO [PolicyEngine] Policy analysis complete [eventToken=b2551e5c-52a3-4089-9956-841685c33193, projectName=commons-lang__rel/commons-lang-3.17.0-orig, projectUuid=16397239-aff6-4559-a954-a47b592b33df, projectVersion=null]
2026-06-08 20:37:27,339 INFO [ProjectMetricsUpdateTask] Executing metrics update for project 16397239-aff6-4559-a954-a47b592b33df
