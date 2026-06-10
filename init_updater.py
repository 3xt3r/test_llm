t java.net.http/jdk.internal.net.http.MultiExchange.lambda$responseAsyncImpl$2(Unknown Source)
apiserver-1  | 	at java.net.http/jdk.internal.net.http.MultiExchange.responseAsyncImpl(Unknown Source)
apiserver-1  | 	at java.net.http/jdk.internal.net.http.MultiExchange.lambda$responseAsync0$0(Unknown Source)
apiserver-1  | 	at java.net.http/jdk.internal.net.http.HttpClientImpl$DelegatingExecutor.execute(Unknown Source)
apiserver-1  | 	at java.net.http/jdk.internal.net.http.MultiExchange.responseAsync(Unknown Source)
apiserver-1  | 	at java.net.http/jdk.internal.net.http.HttpClientImpl.sendAsync(Unknown Source)
apiserver-1  | 2026-06-10 11:11:55,835 INFO [VulnDataSourcesResource] Triggered vulnerability data source mirror for github [principal=admin, requestUri=/vuln-data-sources/{name}/mirror-runs, requestId=4ca67f65-3a43-4a75-9479-65c83f6856cb, requestMethod=POST]
apiserver-1  | 2026-06-10 11:11:56,022 INFO [MirrorVulnDataSourceActivity] Starting mirror [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 11:11:56,032 INFO [GitHubVulnDataSource] Downloading and processing GitHub advisories updated since null (interleaved by page) [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 11:11:57,056 ERROR [GitHubSecurityAdvisoryClient] {
apiserver-1  |   "documentation_url": "https://docs.github.com/rest",
apiserver-1  |   "status": "401"
apiserver-1  | } [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 11:11:57,056 INFO [GitHubVulnDataSource] Fetched 0 advisories across 0 page(s) [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 11:11:57,306 WARN [ActivityTaskWorker] Activity failed; Next retry due at 2026-06-10T11:12:06.986266184Z (attempt 2/6) [activityName=mirror-vuln-data-source, workflowRunId=019eb13b-53b5-7e33-8c5b-4a5291209825, activityTaskAttempt=1]
apiserver-1  | io.github.jeremylong.openvulnerability.client.ghsa.GitHubSecurityAdvisoryException: GitHub GraphQL Returned Status Code: 401
apiserver-1  | 	at io.github.jeremylong.openvulnerability.client.ghsa.GitHubSecurityAdvisoryClient.next(GitHubSecurityAdvisoryClient.java:388)
apiserver-1  | 	at org.dependencytrack.vulndatasource.github.GitHubVulnDataSource.hasNext(GitHubVulnDataSource.java:85)
apiserver-1  | 2026-06-10 11:12:09,346 INFO [MirrorVulnDataSourceActivity] Starting mirror [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 11:12:09,352 INFO [GitHubVulnDataSource] Downloading and processing GitHub advisories updated since null (interleaved by page) [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 11:12:11,026 ERROR [GitHubSecurityAdvisoryClient] {
apiserver-1  |   "documentation_url": "https://docs.github.com/rest",
apiserver-1  |   "status": "401"
apiserver-1  | } [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 11:12:11,026 INFO [GitHubVulnDataSource] Fetched 0 advisories across 0 page(s) [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 11:12:11,127 WARN [ActivityTaskWorker] Activity failed; Next retry due at 2026-06-10T11:12:21.264527714Z (attempt 3/6) [activityName=mirror-vuln-data-source, workflowRunId=019eb13b-53b5-7e33-8c5b-4a5291209825, activityTaskAttempt=2]
apiserver-1  | io.github.jeremylong.openvulnerability.client.ghsa.GitHubSecurityAdvisoryException: GitHub GraphQL Returned Status Code: 401
apiserver-1  | 	at io.github.jeremylong.openvulnerability.client.ghsa.GitHubSecurityAdvisoryClient.next(GitHubSecurityAdvisoryClient.java:388)
apiserver-1  | 	at org.dependencytrack.vulndatasource.github.GitHubVulnDataSource.hasNext(GitHubVulnDataSource.java:85)
apiserver-1  | 2026-06-10 11:12:21,697 INFO [MirrorVulnDataSourceActivity] Starting mirror [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 11:12:21,703 INFO [GitHubVulnDataSource] Downloading and processing GitHub advisories updated since null (interleaved by page) [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 11:12:22,895 ERROR [GitHubSecurityAdvisoryClient] {
apiserver-1  |   "documentation_url": "https://docs.github.com/rest",
apiserver-1  |   "status": "401"
apiserver-1  | } [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 11:12:22,895 INFO [GitHubVulnDataSource] Fetched 0 advisories across 0 page(s) [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 11:12:23,218 WARN [ActivityTaskWorker] Activity failed; Next retry due at 2026-06-10T11:12:39.653302563Z (attempt 4/6) [activityName=mirror-vuln-data-source, workflowRunId=019eb13b-53b5-7e33-8c5b-4a5291209825, activityTaskAttempt=3]
apiserver-1  | io.github.jeremylong.openvulnerability.client.ghsa.GitHubSecurityAdvisoryException: GitHub GraphQL Returned Status Code: 401
apiserver-1  | 	at io.github.jeremylong.openvulnerability.client.ghsa.GitHubSecurityAdvisoryClient.next(GitHubSecurityAdvisoryClient.java:388)
apiserver-1  | 	at org.dependencytrack.vulndatasource.github.GitHubVulnDataSource.hasNext(GitHubVulnDataSource.java:85)
apiserver-1  | 2026-06-10 11:12:26,662 INFO [MirrorVulnDataSourceActivity] Processed 2200 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:12:40,404 INFO [MirrorVulnDataSourceActivity] Starting mirror [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 11:12:40,409 INFO [GitHubVulnDataSource] Downloading and processing GitHub advisories updated since null (interleaved by page) [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 11:12:41,531 ERROR [GitHubSecurityAdvisoryClient] {
apiserver-1  |   "documentation_url": "https://docs.github.com/rest",
apiserver-1  |   "status": "401"
apiserver-1  | } [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 11:12:41,532 INFO [GitHubVulnDataSource] Fetched 0 advisories across 0 page(s) [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 11:12:41,940 WARN [ActivityTaskWorker] Activity failed; Next retry due at 2026-06-10T11:13:12.473553365Z (attempt 5/6) [activityName=mirror-vuln-data-source, workflowRunId=019eb13b-53b5-7e33-8c5b-4a5291209825, activityTaskAttempt=4]
apiserver-1  | io.github.jeremylong.openvulnerability.client.ghsa.GitHubSecurityAdvisoryException: GitHub GraphQL Returned Status Code: 401
apiserver-1  | 	at io.github.jeremylong.openvulnerability.client.ghsa.GitHubSecurityAdvisoryClient.next(GitHubSecurityAdvisoryClient.java:388)
apiserver-1  | 	at org.dependencytrack.vulndatasource.github.GitHubVulnDataSource.hasNext(GitHubVulnDataSource.java:85)
apiserver-1  | 2026-06-10 11:12:56,699 INFO [MirrorVulnDataSourceActivity] Processed 4375 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:13:13,450 INFO [MirrorVulnDataSourceActivity] Starting mirror [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 11:13:13,457 INFO [GitHubVulnDataSource] Downloading and processing GitHub advisories updated since null (interleaved by page) [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 11:13:14,950 ERROR [GitHubSecurityAdvisoryClient] {
apiserver-1  |   "documentation_url": "https://docs.github.com/rest",
apiserver-1  |   "status": "401"
apiserver-1  | } [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 11:13:14,951 INFO [GitHubVulnDataSource] Fetched 0 advisories across 0 page(s) [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 11:13:15,356 WARN [ActivityTaskWorker] Activity failed; Next retry due at 2026-06-10T11:13:51.017128996Z (attempt 6/6) [activityName=mirror-vuln-data-source, workflowRunId=019eb13b-53b5-7e33-8c5b-4a5291209825, activityTaskAttempt=5]
apiserver-1  | io.github.jeremylong.openvulnerability.client.ghsa.GitHubSecurityAdvisoryException: GitHub GraphQL Returned Status Code: 401
apiserver-1  | 	at io.github.jeremylong.openvulnerability.client.ghsa.GitHubSecurityAdvisoryClient.next(GitHubSecurityAdvisoryClient.java:388)
apiserver-1  | 	at org.dependencytrack.vulndatasource.github.GitHubVulnDataSource.hasNext(GitHubVulnDataSource.java:85)
apiserver-1  | 2026-06-10 11:13:26,797 INFO [MirrorVulnDataSourceActivity] Processed 6825 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:13:52,706 INFO [MirrorVulnDataSourceActivity] Starting mirror [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 11:13:52,716 INFO [GitHubVulnDataSource] Downloading and processing GitHub advisories updated since null (interleaved by page) [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 11:13:54,344 ERROR [GitHubSecurityAdvisoryClient] {
apiserver-1  |   "documentation_url": "https://docs.github.com/rest",
apiserver-1  |   "status": "401"
apiserver-1  | } [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 11:13:54,344 INFO [GitHubVulnDataSource] Fetched 0 advisories across 0 page(s) [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 11:13:54,403 WARN [ActivityTaskWorker] Activity failed terminally after 6 attempt(s) [activityName=mirror-vuln-data-source, workflowRunId=019eb13b-53b5-7e33-8c5b-4a5291209825, activityTaskAttempt=6]
apiserver-1  | io.github.jeremylong.openvulnerability.client.ghsa.GitHubSecurityAdvisoryException: GitHub GraphQL Returned Status Code: 401
apiserver-1  | 	at io.github.jeremylong.openvulnerability.client.ghsa.GitHubSecurityAdvisoryClient.next(GitHubSecurityAdvisoryClient.java:388)
apiserver-1  | 	at org.dependencytrack.vulndatasource.github.GitHubVulnDataSource.hasNext(GitHubVulnDataSource.java:85)
apiserver-1  | 2026-06-10 11:13:57,853 INFO [MirrorVulnDataSourceActivity] Processed 9250 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:14:28,642 INFO [MirrorVulnDataSourceActivity] Processed 10250 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:14:58,698 INFO [MirrorVulnDataSourceActivity] Processed 11100 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:15:29,834 INFO [MirrorVulnDataSourceActivity] Processed 12225 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:15:59,960 INFO [MirrorVulnDataSourceActivity] Processed 13150 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:16:30,119 INFO [MirrorVulnDataSourceActivity] Processed 14300 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:17:01,822 INFO [MirrorVulnDataSourceActivity] Processed 16400 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:17:31,823 INFO [MirrorVulnDataSourceActivity] Processed 17350 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:18:02,204 INFO [MirrorVulnDataSourceActivity] Processed 18300 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:18:32,217 INFO [MirrorVulnDataSourceActivity] Processed 19150 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:19:02,289 INFO [MirrorVulnDataSourceActivity] Processed 20350 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:19:32,291 INFO [MirrorVulnDataSourceActivity] Processed 21975 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:20:03,570 INFO [MirrorVulnDataSourceActivity] Processed 22875 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:20:34,359 INFO [MirrorVulnDataSourceActivity] Processed 23675 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:21:04,970 INFO [MirrorVulnDataSourceActivity] Processed 24575 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:21:35,317 INFO [MirrorVulnDataSourceActivity] Processed 25750 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:22:07,733 INFO [MirrorVulnDataSourceActivity] Processed 27500 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:22:37,793 INFO [MirrorVulnDataSourceActivity] Processed 28750 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:23:09,325 INFO [MirrorVulnDataSourceActivity] Processed 29900 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:23:39,415 INFO [MirrorVulnDataSourceActivity] Processed 30875 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:24:09,568 INFO [MirrorVulnDataSourceActivity] Processed 32350 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:24:40,682 INFO [MirrorVulnDataSourceActivity] Processed 33475 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:25:10,921 INFO [MirrorVulnDataSourceActivity] Processed 34675 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:25:41,148 INFO [MirrorVulnDataSourceActivity] Processed 35775 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:26:11,380 INFO [MirrorVulnDataSourceActivity] Processed 37625 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:26:41,561 INFO [MirrorVulnDataSourceActivity] Processed 39950 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:27:11,617 INFO [MirrorVulnDataSourceActivity] Processed 41775 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:27:41,686 INFO [MirrorVulnDataSourceActivity] Processed 44000 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:28:12,224 INFO [MirrorVulnDataSourceActivity] Processed 46750 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:28:42,356 INFO [MirrorVulnDataSourceActivity] Processed 49750 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:29:12,603 INFO [MirrorVulnDataSourceActivity] Processed 51950 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:29:42,757 INFO [MirrorVulnDataSourceActivity] Processed 54675 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:30:12,884 INFO [MirrorVulnDataSourceActivity] Processed 57650 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:30:43,119 INFO [MirrorVulnDataSourceActivity] Processed 59875 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:31:13,530 INFO [MirrorVulnDataSourceActivity] Processed 62425 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:31:43,809 INFO [MirrorVulnDataSourceActivity] Processed 64500 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:32:13,984 INFO [MirrorVulnDataSourceActivity] Processed 66650 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:32:44,114 INFO [MirrorVulnDataSourceActivity] Processed 70050 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:33:14,340 INFO [MirrorVulnDataSourceActivity] Processed 73225 vulnerabilities so far [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 11:33:36,438 INFO [MirrorVulnDataSourceActivity] Completed mirror; processed 77401 vulnerabilities in PT21M39.989564636S [vulnDataSourceName=nvd]
apiserver-1  | 2026-06-10 16:09:55,156 INFO [VulnerabilityMetricsUpdateTask] Refreshing vulnerability metrics
apiserver-1  | 2026-06-10 16:09:56,710 INFO [VulnerabilityMetricsUpdateTask] Refreshed vulnerability metrics in PT1.553555432S
apiserver-1  | 2026-06-10 16:10:03,084 INFO [VulnDataSourcesResource] Triggered vulnerability data source mirror for github [principal=admin, requestUri=/vuln-data-sources/{name}/mirror-runs, requestId=1f426c6d-8c3b-4871-b10e-257b75fef31c, requestMethod=POST]
apiserver-1  | 2026-06-10 16:10:03,217 INFO [MirrorVulnDataSourceActivity] Starting mirror [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 16:10:03,226 INFO [GitHubVulnDataSource] Downloading and processing GitHub advisories updated since null (interleaved by page) [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 16:10:04,989 ERROR [GitHubSecurityAdvisoryClient] {
apiserver-1  |   "documentation_url": "https://docs.github.com/rest",
apiserver-1  |   "status": "401"
apiserver-1  | } [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 16:10:04,990 INFO [GitHubVulnDataSource] Fetched 0 advisories across 0 page(s) [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 16:10:05,301 WARN [ActivityTaskWorker] Activity failed; Next retry due at 2026-06-10T16:10:11.637889986Z (attempt 2/6) [activityName=mirror-vuln-data-source, workflowRunId=019eb24c-43bc-7bf1-b22b-03558a738eec, activityTaskAttempt=1]
apiserver-1  | io.github.jeremylong.openvulnerability.client.ghsa.GitHubSecurityAdvisoryException: GitHub GraphQL Returned Status Code: 401
apiserver-1  | 	at io.github.jeremylong.openvulnerability.client.ghsa.GitHubSecurityAdvisoryClient.next(GitHubSecurityAdvisoryClient.java:388)
apiserver-1  | 	at org.dependencytrack.vulndatasource.github.GitHubVulnDataSource.hasNext(GitHubVulnDataSource.java:85)
apiserver-1  | 2026-06-10 16:10:11,719 INFO [MirrorVulnDataSourceActivity] Starting mirror [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 16:10:11,724 INFO [GitHubVulnDataSource] Downloading and processing GitHub advisories updated since null (interleaved by page) [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 16:10:12,817 ERROR [GitHubSecurityAdvisoryClient] {
apiserver-1  |   "documentation_url": "https://docs.github.com/rest",
apiserver-1  |   "status": "401"
apiserver-1  | } [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 16:10:12,817 INFO [GitHubVulnDataSource] Fetched 0 advisories across 0 page(s) [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 16:10:12,875 WARN [ActivityTaskWorker] Activity failed; Next retry due at 2026-06-10T16:10:21.268706955Z (attempt 3/6) [activityName=mirror-vuln-data-source, workflowRunId=019eb24c-43bc-7bf1-b22b-03558a738eec, activityTaskAttempt=2]
apiserver-1  | io.github.jeremylong.openvulnerability.client.ghsa.GitHubSecurityAdvisoryException: GitHub GraphQL Returned Status Code: 401
apiserver-1  | 	at io.github.jeremylong.openvulnerability.client.ghsa.GitHubSecurityAdvisoryClient.next(GitHubSecurityAdvisoryClient.java:388)
apiserver-1  | 	at org.dependencytrack.vulndatasource.github.GitHubVulnDataSource.hasNext(GitHubVulnDataSource.java:85)
apiserver-1  | 2026-06-10 16:10:21,297 INFO [MirrorVulnDataSourceActivity] Starting mirror [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 16:10:21,306 INFO [GitHubVulnDataSource] Downloading and processing GitHub advisories updated since null (interleaved by page) [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 16:10:22,653 ERROR [GitHubSecurityAdvisoryClient] {
apiserver-1  |   "documentation_url": "https://docs.github.com/rest",
apiserver-1  |   "status": "401"
apiserver-1  | } [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 16:10:22,653 INFO [GitHubVulnDataSource] Fetched 0 advisories across 0 page(s) [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 16:10:23,018 WARN [ActivityTaskWorker] Activity failed; Next retry due at 2026-06-10T16:10:41.011113132Z (attempt 4/6) [activityName=mirror-vuln-data-source, workflowRunId=019eb24c-43bc-7bf1-b22b-03558a738eec, activityTaskAttempt=3]
apiserver-1  | io.github.jeremylong.openvulnerability.client.ghsa.GitHubSecurityAdvisoryException: GitHub GraphQL Returned Status Code: 401
apiserver-1  | 	at io.github.jeremylong.openvulnerability.client.ghsa.GitHubSecurityAdvisoryClient.next(GitHubSecurityAdvisoryClient.java:388)
apiserver-1  | 	at org.dependencytrack.vulndatasource.github.GitHubVulnDataSource.hasNext(GitHubVulnDataSource.java:85)
apiserver-1  | 2026-06-10 16:10:43,053 INFO [MirrorVulnDataSourceActivity] Starting mirror [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 16:10:43,062 INFO [GitHubVulnDataSource] Downloading and processing GitHub advisories updated since null (interleaved by page) [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 16:10:44,668 ERROR [GitHubSecurityAdvisoryClient] {
apiserver-1  |   "documentation_url": "https://docs.github.com/rest",
apiserver-1  |   "status": "401"
apiserver-1  | } [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 16:10:44,668 INFO [GitHubVulnDataSource] Fetched 0 advisories across 0 page(s) [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 16:10:44,915 WARN [ActivityTaskWorker] Activity failed; Next retry due at 2026-06-10T16:11:09.990862191Z (attempt 5/6) [activityName=mirror-vuln-data-source, workflowRunId=019eb24c-43bc-7bf1-b22b-03558a738eec, activityTaskAttempt=4]
apiserver-1  | io.github.jeremylong.openvulnerability.client.ghsa.GitHubSecurityAdvisoryException: GitHub GraphQL Returned Status Code: 401
apiserver-1  | 	at io.github.jeremylong.openvulnerability.client.ghsa.GitHubSecurityAdvisoryClient.next(GitHubSecurityAdvisoryClient.java:388)
apiserver-1  | 	at org.dependencytrack.vulndatasource.github.GitHubVulnDataSource.hasNext(GitHubVulnDataSource.java:85)
apiserver-1  | 2026-06-10 16:11:10,429 INFO [MirrorVulnDataSourceActivity] Starting mirror [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 16:11:10,437 INFO [GitHubVulnDataSource] Downloading and processing GitHub advisories updated since null (interleaved by page) [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 16:11:11,292 ERROR [GitHubSecurityAdvisoryClient] {
apiserver-1  |   "documentation_url": "https://docs.github.com/rest",
apiserver-1  |   "status": "401"
apiserver-1  | } [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 16:11:11,292 INFO [GitHubVulnDataSource] Fetched 0 advisories across 0 page(s) [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 16:11:11,451 WARN [ActivityTaskWorker] Activity failed; Next retry due at 2026-06-10T16:11:57.957001598Z (attempt 6/6) [activityName=mirror-vuln-data-source, workflowRunId=019eb24c-43bc-7bf1-b22b-03558a738eec, activityTaskAttempt=5]
apiserver-1  | io.github.jeremylong.openvulnerability.client.ghsa.GitHubSecurityAdvisoryException: GitHub GraphQL Returned Status Code: 401
apiserver-1  | 	at io.github.jeremylong.openvulnerability.client.ghsa.GitHubSecurityAdvisoryClient.next(GitHubSecurityAdvisoryClient.java:388)
apiserver-1  | 	at org.dependencytrack.vulndatasource.github.GitHubVulnDataSource.hasNext(GitHubVulnDataSource.java:85)
apiserver-1  | 2026-06-10 16:11:58,901 INFO [MirrorVulnDataSourceActivity] Starting mirror [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 16:11:58,910 INFO [GitHubVulnDataSource] Downloading and processing GitHub advisories updated since null (interleaved by page) [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 16:12:00,606 ERROR [GitHubSecurityAdvisoryClient] {
apiserver-1  |   "documentation_url": "https://docs.github.com/rest",
apiserver-1  |   "status": "401"
apiserver-1  | } [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 16:12:00,607 INFO [GitHubVulnDataSource] Fetched 0 advisories across 0 page(s) [vulnDataSourceName=github]
apiserver-1  | 2026-06-10 16:12:00,709 WARN [ActivityTaskWorker] Activity failed terminally after 6 attempt(s) [activityName=mirror-vuln-data-source, workflowRunId=019eb24c-43bc-7bf1-b22b-03558a738eec, activityTaskAttempt=6]
apiserver-1  | io.github.jeremylong.openvulnerability.client.ghsa.GitHubSecurityAdvisoryException: GitHub GraphQL Returned Status Code: 401
apiserver-1  | 	at io.github.jeremylong.openvulnerability.client.ghsa.GitHubSecurityAdvisoryClient.next(GitHubSecurityAdvisoryClient.java:388)
apiserver-1  | 	at org.dependencytrack.vulndatasource.github.GitHubVulnDataSource.hasNext(GitHubVulnDataSource.java:85)
apiserver-1  | 2026-06-10 16:15:40,943 WARN [ImportBomActivity] More than one existing component matches the identity org.dependencytrack.model.ComponentIdentity@868306a9; Proceeding with first match, others will be deleted [bomSerialNumber=7bdefb0c-410f-4843-84c6-3d91ee3c5a67, bomFormat=CycloneDX, bomUploadToken=019eb251-69d4-7e25-8b1b-0b26f66cd1f3, projectName=test, bomSpecVersion=1.5, projectUuid=e2419e3e-b535-41c4-83eb-4e8c1752a034, projectVersion=1, bomVersion=1]
apiserver-1  | 2026-06-10 16:15:41,008 WARN [ImportBomActivity] The dependency graph has 0 entries, but the project (metadata.component node of the BOM) is not one of them; Graph will be incomplete because it is not possible to determine its root [bomSerialNumber=7bdefb0c-410f-4843-84c6-3d91ee3c5a67, bomFormat=CycloneDX, bomUploadToken=019eb251-69d4-7e25-8b1b-0b26f66cd1f3, projectName=test, bomSpecVersion=1.5, projectUuid=e2419e3e-b535-41c4-83eb-4e8c1752a034, projectVersion=1, bomVersion=1]
apiserver-1  | 2026-06-10 16:15:41,043 INFO [ImportBomActivity] BOM processed successfully in 00:00:00.403 [bomUploadToken=019eb251-69d4-7e25-8b1b-0b26f66cd1f3, projectName=test, projectUuid=e2419e3e-b535-41c4-83eb-4e8c1752a034, projectVersion=1]
apiserver-1  | 2026-06-10 16:15:41,183 INFO [AnalyzeProjectWorkflow] Starting project analysis [workflowName=analyze-project, workflowInstanceId=analyze-project:bom-upload:019eb251-69d4-7e25-8b1b-0b26f66cd1f3, workflowRunId=019eb251-6bfa-7f9b-9567-691ac1221be5, projectUuid=e2419e3e-b535-41c4-83eb-4e8c1752a034]
apiserver-1  | 2026-06-10 16:15:41,281 INFO [VulnAnalysisWorkflow] Starting vulnerability analysis [workflowName=vuln-analysis, workflowInstanceId=null, workflowRunId=019eb251-6c84-7aba-b385-622a3b192abf, projectUuid=e2419e3e-b535-41c4-83eb-4e8c1752a034]
apiserver-1  | 2026-06-10 16:15:43,673 INFO [VulnAnalysisWorkflow] Vulnerability analysis completed [workflowName=vuln-analysis, workflowInstanceId=null, workflowRunId=019eb251-6c84-7aba-b385-622a3b192abf, projectUuid=e2419e3e-b535-41c4-83eb-4e8c1752a034]
apiserver-1  | 2026-06-10 16:15:44,273 INFO [AnalyzeProjectWorkflow] Project analysis completed [workflowName=analyze-project, workflowInstanceId=analyze-project:bom-upload:019eb251-69d4-7e25-8b1b-0b26f66cd1f3, workflowRunId=019eb251-6bfa-7f9b-9567-691ac1221be5, projectUuid=e2419e3e-b535-41c4-83eb-4e8c1752a034]

