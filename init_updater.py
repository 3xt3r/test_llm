python3 sheduler.py --config config.yml
2026-06-07 20:08:46 | INFO    | GITLAB_TOKEN not set — will try anonymous clone first
2026-06-07 20:08:46 | INFO    | timeouts: scanner=3600s, distrib_scan=7200s, deptrack=3600s
2026-06-07 20:08:46 | INFO    | === product: express ===
2026-06-07 20:08:46 | INFO    | --- version: v4.22.2 ---
2026-06-07 20:08:46 | INFO    |     cloning: https://github.com/expressjs/express.git
2026-06-07 20:08:46 | INFO    |     running: git -c credential.helper= clone --no-checkout https://github.com/expressjs/express.git /home/kali/Desktop/jobs/express/_repos/express
2026-06-07 20:08:55 | INFO    |     checkout express @ v4.22.2
2026-06-07 20:08:55 | INFO    |     running: git -c credential.helper= checkout v4.22.2
2026-06-07 20:08:55 | INFO    |     v4.22.2 is a tag — skipping reset to origin/
2026-06-07 20:08:55 | INFO    |     running: git -c credential.helper= submodule update --init --recursive
2026-06-07 20:08:55 | INFO    |   running scanner on /home/kali/Desktop/jobs/express/_repos/express (DT project: express__v4.22.2, timeout=3600s)
2026-06-07 20:08:55 | INFO    |   job_dir: /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5
2026-06-07 20:08:55 | INFO    |     running: /home/kali/Desktop/venv/bin/python3 /home/kali/Desktop/oss_checks/scanner.py /home/kali/Desktop/jobs/express/_repos/express --apply --deptrack --dt-project-name express__v4.22.2 --env-file /home/kali/Desktop/oss_checks/.env --job-dir /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5
20:08:55 [INFO] loaded .env: /home/kali/Desktop/oss_checks/.env
20:08:55 [INFO] [dt] auto-ensuring orig project 'express__v4.22.2-orig'...
20:08:55 [INFO] [dt] reusing existing project 'express__v4.22.2-orig' -> 77093aa6-2c10-4101-bed6-d7de8eb6052b
20:08:55 [INFO] [dt] server version: 4.14.2 — parentUUID support: yes
20:08:55 [INFO] [dt] auto-ensuring safe project 'express__v4.22.2 [safe]' (parent: 77093aa6-2c10-4101-bed6-d7de8eb6052b)...
20:08:55 [INFO] [dt] reusing existing project 'express__v4.22.2 [safe]' -> 95580e40-242b-47f3-9999-435433fecf2f
20:08:55 [INFO] scan root: /home/kali/Desktop/jobs/express/_repos/express
20:08:55 [INFO] working copy:              /home/kali/Desktop/jobs/express/_repos/express
20:08:55 [INFO] job directory:             /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5
20:08:55 [INFO] dependency-track: enabled url=http://localhost:8081 safe_project=95580e40-242b-47f3-9999-435433fecf2f orig_project=77093aa6-2c10-4101-bed6-d7de8eb6052b insecure=True
20:08:55 [INFO] created directory: /home/kali/Desktop/jobs/express/_repos/jobs
20:08:55 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5
20:08:55 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/sbom
20:08:55 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/reports
20:08:55 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/reports/asm
20:08:55 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/ecosystems
20:08:55 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/external_downloads
20:08:55 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/sbom/debug
[cleanup] removing directory: /home/kali/Desktop/jobs/express/_repos/express/examples
[cleanup] removing directory: /home/kali/Desktop/jobs/express/_repos/express/test
20:08:55 [INFO] ecosystem report: /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/ecosystems/lock_summary.json
20:08:55 [INFO] lock suggestions: 1
20:08:55 [INFO] [lock] [1/1] start: package.json
20:08:55 [INFO] [lock]         cmd:  cd "/home/kali/Desktop/jobs/express/_repos/express" && npm install --package-lock-only
20:09:19 [INFO] [lock] [1/1] ok (rc=0, 23.6s): package.json
20:09:19 [INFO] lock generation: ok=1, failed=0, skipped=0
20:09:19 [INFO] [cplus] oss_checks_dir: /home/kali/Desktop/oss_checks
20:09:19 [INFO] [cplus] cplus_scanner: /home/kali/Desktop/oss_checks/cpluschecks/scanner.py (exists=True)
20:09:19 [INFO] [cplus] cplus_known (abs): /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/sbom/cplus_sbom.json
20:09:19 [INFO] [cplus] scanner: /home/kali/Desktop/oss_checks/cpluschecks/scanner.py
20:09:19 [INFO] [cplus] scan_root: /home/kali/Desktop/jobs/express/_repos/express (exists=True)
20:09:19 [INFO] [cplus] output: /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/sbom/cplus_sbom.json
20:09:19 [INFO] [cplus] returncode: 0
20:09:19 [INFO] [cplus] stdout: [INFO] root=/home/kali/Desktop/jobs/express/_repos/express  checkers=94 workers=8
[INFO] candidate_files=2
[INFO] content cache ready in 0.00s
[INFO] submodule scan disabled
Scanning finished in 0.07s; total findings=0
Known SBOM written to /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/sbom/cplus_sbom.json
Unknown SBOM written to /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/sbom/cplus_sbom.unknown.json
20:09:19 [INFO] [cplus] output file exists: True
20:09:19 [INFO] [cplus] output file size: 307 bytes
20:09:19 [INFO] [cplus] found 0 C/C++ component(s)
[INFO] removed rust vendor dirs: 0
[INFO] renamed Cargo.lock.in files: 0
[INFO] hidden template pom.xml files: 0
20:09:19 [INFO] RUN trivy fs . --scanners license --offline-scan --skip-db-update --format cyclonedx --output /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/sbom/origsbom.json --timeout 30m  (cwd=/home/kali/Desktop/jobs/express/_repos/express)
2026-06-07T20:09:19+03:00	INFO	[license] License scanning is enabled
2026-06-07T20:09:19+03:00	INFO	[npm] To collect the license information of packages, "npm install" needs to be performed beforehand	dir="node_modules"
2026-06-07T20:09:19+03:00	INFO	Suppressing dependencies for development and testing. To display them, try the '--include-dev-deps' flag.
2026-06-07T20:09:19+03:00	INFO	Number of language-specific files	num=1
[INFO] restored template pom.xml files: 0
20:09:19 [WARNING] [cplus] no cplus sbom files to merge — skipping
20:09:19 [INFO] [normalize] processing: origsbom.json
20:09:19 [INFO] [normalize] origsbom.json: components 68→68, vulnerabilities 0→0, filtered=0
20:09:19 [INFO] [normalize] saved: /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/sbom/debug/origsbom/origsbom_normalized.json
20:09:19 [INFO] [normalize] using normalized SBOM: /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/sbom/debug/origsbom/origsbom_normalized.json
[dt] uploaded: /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/sbom/debug/origsbom/origsbom_normalized.json (token=4e1d0f6c-c91a-4db0-bfef-514daf543e13)
[dt] origsbom uploaded to orig project: 77093aa6-2c10-4101-bed6-d7de8eb6052b
[dt] ===== enrich origsbom =====
[dt] uploaded: /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/sbom/debug/origsbom/origsbom_normalized.json (token=2bf9ba6c-bc00-4908-9e25-e43fe1c225d7)
[dt] bom/token poll 1: processing=True
[dt] bom/token poll 2: processing=False
[dt] BOM processing complete
[dt] findings poll 1: count=0, stable=0
[dt] findings stabilized (empty)
[dt] downloaded: /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/sbom/.dt-tmp-enrich.json
[dt] enriched: components=68, vulnerabilities=0 (OSV filtered: 0)
[dt] starting DT cleanup: orig_vulns=0  candidate_components=0
[dt] SBOM is empty (0 components, 0 vulnerabilities) — skipping DT cleanup rounds
[dt] uploading empty sbom-clean to safe project: 95580e40-242b-47f3-9999-435433fecf2f
[dt] uploaded: /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/sbom/sbom-clean.json (token=844dd11f-4d4a-445e-8de9-ee8f2c7f6e90)
[dt] empty sbom-clean uploaded to safe project: 95580e40-242b-47f3-9999-435433fecf2f
[OK] report.xlsx           : /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/reports/report.xlsx
[OK]   Vulnerabilities rows: 0
[OK]   SafeVersions rows   : 0
[OK] report.xlsx           : /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/reports/report.xlsx
[OK] sbom-clean.json : /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/sbom/sbom-clean.json
[OK] missing versions txt          : /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/sbom/debug/missing_versions.txt
[OK] failed debug txt              : /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/sbom/debug/failed_safe_versions_debug.txt
20:09:35 [INFO] [vuln] cplus_sbom found: /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/sbom/cplus_sbom.json
20:09:35 [INFO] external_downloads: 9 hit(s) found in /home/kali/Desktop/jobs/express/_repos/express
20:09:35 [INFO] external_downloads JSON report written: /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/external_downloads/external_downloads_root.json
20:09:35 [INFO] registry_sources: 1 source(s) found in /home/kali/Desktop/jobs/express/_repos/express
20:09:35 [INFO] registry_sources report written: /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/ecosystems/registry_sources_root.json
20:09:35 [INFO] Found 67 unique (ecosystem, name, version) entries
20:09:35 [INFO] Will download sources for 67 packages
20:09:35 [INFO] === npm :: accepts :: 1.3.8 (ref=pkg:npm/accepts@1.3.8) ===
20:09:35 [INFO] [npm] accepts@1.3.8 querying https://registry.npmjs.org/accepts
20:09:35 [INFO] downloading https://registry.npmjs.org/accepts/-/accepts-1.3.8.tgz
20:09:36 [INFO] [npm] accepts@1.3.8 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/accepts-1.3.8/accepts-1.3.8.tgz
20:09:36 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/accepts-1.3.8/accepts-1.3.8.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/accepts-1.3.8 as gztar
20:09:36 [INFO] === npm :: array-flatten :: 1.1.1 (ref=pkg:npm/array-flatten@1.1.1) ===
20:09:36 [INFO] [npm] array-flatten@1.1.1 querying https://registry.npmjs.org/array-flatten
20:09:37 [INFO] downloading https://registry.npmjs.org/array-flatten/-/array-flatten-1.1.1.tgz
20:09:37 [INFO] [npm] array-flatten@1.1.1 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/array-flatten-1.1.1/array-flatten-1.1.1.tgz
20:09:37 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/array-flatten-1.1.1/array-flatten-1.1.1.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/array-flatten-1.1.1 as gztar
20:09:37 [INFO] === npm :: body-parser :: 1.20.5 (ref=pkg:npm/body-parser@1.20.5) ===
20:09:37 [INFO] [npm] body-parser@1.20.5 querying https://registry.npmjs.org/body-parser
20:09:38 [INFO] downloading https://registry.npmjs.org/body-parser/-/body-parser-1.20.5.tgz
20:09:39 [INFO] [npm] body-parser@1.20.5 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/body-parser-1.20.5/body-parser-1.20.5.tgz
20:09:39 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/body-parser-1.20.5/body-parser-1.20.5.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/body-parser-1.20.5 as gztar
20:09:39 [INFO] === npm :: bytes :: 3.1.2 (ref=pkg:npm/bytes@3.1.2) ===
20:09:39 [INFO] [npm] bytes@3.1.2 querying https://registry.npmjs.org/bytes
20:09:40 [INFO] downloading https://registry.npmjs.org/bytes/-/bytes-3.1.2.tgz
20:09:40 [INFO] [npm] bytes@3.1.2 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/bytes-3.1.2/bytes-3.1.2.tgz
20:09:40 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/bytes-3.1.2/bytes-3.1.2.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/bytes-3.1.2 as gztar
20:09:40 [INFO] === npm :: call-bind-apply-helpers :: 1.0.2 (ref=pkg:npm/call-bind-apply-helpers@1.0.2) ===
20:09:40 [INFO] [npm] call-bind-apply-helpers@1.0.2 querying https://registry.npmjs.org/call-bind-apply-helpers
20:09:41 [INFO] downloading https://registry.npmjs.org/call-bind-apply-helpers/-/call-bind-apply-helpers-1.0.2.tgz
20:09:42 [INFO] [npm] call-bind-apply-helpers@1.0.2 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/call-bind-apply-helpers-1.0.2/call-bind-apply-helpers-1.0.2.tgz
20:09:42 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/call-bind-apply-helpers-1.0.2/call-bind-apply-helpers-1.0.2.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/call-bind-apply-helpers-1.0.2 as gztar
20:09:42 [INFO] === npm :: call-bound :: 1.0.4 (ref=pkg:npm/call-bound@1.0.4) ===
20:09:42 [INFO] [npm] call-bound@1.0.4 querying https://registry.npmjs.org/call-bound
20:09:43 [INFO] downloading https://registry.npmjs.org/call-bound/-/call-bound-1.0.4.tgz
20:09:43 [INFO] [npm] call-bound@1.0.4 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/call-bound-1.0.4/call-bound-1.0.4.tgz
20:09:43 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/call-bound-1.0.4/call-bound-1.0.4.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/call-bound-1.0.4 as gztar
20:09:43 [INFO] === npm :: content-disposition :: 0.5.4 (ref=pkg:npm/content-disposition@0.5.4) ===
20:09:43 [INFO] [npm] content-disposition@0.5.4 querying https://registry.npmjs.org/content-disposition
20:09:44 [INFO] downloading https://registry.npmjs.org/content-disposition/-/content-disposition-0.5.4.tgz
20:09:44 [INFO] [npm] content-disposition@0.5.4 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/content-disposition-0.5.4/content-disposition-0.5.4.tgz
20:09:44 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/content-disposition-0.5.4/content-disposition-0.5.4.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/content-disposition-0.5.4 as gztar
20:09:44 [INFO] === npm :: content-type :: 1.0.5 (ref=pkg:npm/content-type@1.0.5) ===
20:09:44 [INFO] [npm] content-type@1.0.5 querying https://registry.npmjs.org/content-type
20:09:46 [INFO] downloading https://registry.npmjs.org/content-type/-/content-type-1.0.5.tgz
20:09:46 [INFO] [npm] content-type@1.0.5 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/content-type-1.0.5/content-type-1.0.5.tgz
20:09:46 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/content-type-1.0.5/content-type-1.0.5.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/content-type-1.0.5 as gztar
20:09:46 [INFO] === npm :: cookie-signature :: 1.0.7 (ref=pkg:npm/cookie-signature@1.0.7) ===
20:09:46 [INFO] [npm] cookie-signature@1.0.7 querying https://registry.npmjs.org/cookie-signature
20:09:47 [INFO] downloading https://registry.npmjs.org/cookie-signature/-/cookie-signature-1.0.7.tgz
20:09:47 [INFO] [npm] cookie-signature@1.0.7 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/cookie-signature-1.0.7/cookie-signature-1.0.7.tgz
20:09:47 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/cookie-signature-1.0.7/cookie-signature-1.0.7.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/cookie-signature-1.0.7 as gztar
20:09:47 [INFO] === npm :: cookie :: 0.7.2 (ref=pkg:npm/cookie@0.7.2) ===
20:09:47 [INFO] [npm] cookie@0.7.2 querying https://registry.npmjs.org/cookie
20:09:48 [INFO] downloading https://registry.npmjs.org/cookie/-/cookie-0.7.2.tgz
20:09:48 [INFO] [npm] cookie@0.7.2 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/cookie-0.7.2/cookie-0.7.2.tgz
20:09:48 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/cookie-0.7.2/cookie-0.7.2.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/cookie-0.7.2 as gztar
20:09:48 [INFO] === npm :: debug :: 2.6.9 (ref=pkg:npm/debug@2.6.9) ===
20:09:48 [INFO] [npm] debug@2.6.9 querying https://registry.npmjs.org/debug
20:09:49 [INFO] downloading https://registry.npmjs.org/debug/-/debug-2.6.9.tgz
20:09:49 [INFO] [npm] debug@2.6.9 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/debug-2.6.9/debug-2.6.9.tgz
20:09:49 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/debug-2.6.9/debug-2.6.9.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/debug-2.6.9 as gztar
20:09:49 [INFO] === npm :: depd :: 2.0.0 (ref=pkg:npm/depd@2.0.0) ===
20:09:49 [INFO] [npm] depd@2.0.0 querying https://registry.npmjs.org/depd
20:09:51 [INFO] downloading https://registry.npmjs.org/depd/-/depd-2.0.0.tgz
20:09:51 [INFO] [npm] depd@2.0.0 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/depd-2.0.0/depd-2.0.0.tgz
20:09:51 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/depd-2.0.0/depd-2.0.0.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/depd-2.0.0 as gztar
20:09:51 [INFO] === npm :: destroy :: 1.2.0 (ref=pkg:npm/destroy@1.2.0) ===
20:09:51 [INFO] [npm] destroy@1.2.0 querying https://registry.npmjs.org/destroy
20:09:52 [INFO] downloading https://registry.npmjs.org/destroy/-/destroy-1.2.0.tgz
20:09:53 [INFO] [npm] destroy@1.2.0 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/destroy-1.2.0/destroy-1.2.0.tgz
20:09:53 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/destroy-1.2.0/destroy-1.2.0.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/destroy-1.2.0 as gztar
20:09:53 [INFO] === npm :: dunder-proto :: 1.0.1 (ref=pkg:npm/dunder-proto@1.0.1) ===
20:09:53 [INFO] [npm] dunder-proto@1.0.1 querying https://registry.npmjs.org/dunder-proto
20:09:54 [INFO] downloading https://registry.npmjs.org/dunder-proto/-/dunder-proto-1.0.1.tgz
20:09:54 [INFO] [npm] dunder-proto@1.0.1 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/dunder-proto-1.0.1/dunder-proto-1.0.1.tgz
20:09:54 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/dunder-proto-1.0.1/dunder-proto-1.0.1.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/dunder-proto-1.0.1 as gztar
20:09:54 [INFO] === npm :: ee-first :: 1.1.1 (ref=pkg:npm/ee-first@1.1.1) ===
20:09:54 [INFO] [npm] ee-first@1.1.1 querying https://registry.npmjs.org/ee-first
20:09:55 [INFO] downloading https://registry.npmjs.org/ee-first/-/ee-first-1.1.1.tgz
20:09:56 [INFO] [npm] ee-first@1.1.1 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/ee-first-1.1.1/ee-first-1.1.1.tgz
20:09:56 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/ee-first-1.1.1/ee-first-1.1.1.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/ee-first-1.1.1 as gztar
20:09:56 [INFO] === npm :: encodeurl :: 2.0.0 (ref=pkg:npm/encodeurl@2.0.0) ===
20:09:56 [INFO] [npm] encodeurl@2.0.0 querying https://registry.npmjs.org/encodeurl
20:09:57 [INFO] downloading https://registry.npmjs.org/encodeurl/-/encodeurl-2.0.0.tgz
20:09:57 [INFO] [npm] encodeurl@2.0.0 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/encodeurl-2.0.0/encodeurl-2.0.0.tgz
20:09:57 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/encodeurl-2.0.0/encodeurl-2.0.0.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/encodeurl-2.0.0 as gztar
20:09:57 [INFO] === npm :: es-define-property :: 1.0.1 (ref=pkg:npm/es-define-property@1.0.1) ===
20:09:57 [INFO] [npm] es-define-property@1.0.1 querying https://registry.npmjs.org/es-define-property
20:09:57 [INFO] downloading https://registry.npmjs.org/es-define-property/-/es-define-property-1.0.1.tgz
20:09:58 [INFO] [npm] es-define-property@1.0.1 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/es-define-property-1.0.1/es-define-property-1.0.1.tgz
20:09:58 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/es-define-property-1.0.1/es-define-property-1.0.1.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/es-define-property-1.0.1 as gztar
20:09:58 [INFO] === npm :: es-errors :: 1.3.0 (ref=pkg:npm/es-errors@1.3.0) ===
20:09:58 [INFO] [npm] es-errors@1.3.0 querying https://registry.npmjs.org/es-errors
20:09:59 [INFO] downloading https://registry.npmjs.org/es-errors/-/es-errors-1.3.0.tgz
20:09:59 [INFO] [npm] es-errors@1.3.0 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/es-errors-1.3.0/es-errors-1.3.0.tgz
20:09:59 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/es-errors-1.3.0/es-errors-1.3.0.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/es-errors-1.3.0 as gztar
20:09:59 [INFO] === npm :: es-object-atoms :: 1.1.2 (ref=pkg:npm/es-object-atoms@1.1.2) ===
20:09:59 [INFO] [npm] es-object-atoms@1.1.2 querying https://registry.npmjs.org/es-object-atoms
20:10:00 [INFO] downloading https://registry.npmjs.org/es-object-atoms/-/es-object-atoms-1.1.2.tgz
20:10:00 [INFO] [npm] es-object-atoms@1.1.2 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/es-object-atoms-1.1.2/es-object-atoms-1.1.2.tgz
20:10:00 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/es-object-atoms-1.1.2/es-object-atoms-1.1.2.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/es-object-atoms-1.1.2 as gztar
20:10:00 [INFO] === npm :: escape-html :: 1.0.3 (ref=pkg:npm/escape-html@1.0.3) ===
20:10:00 [INFO] [npm] escape-html@1.0.3 querying https://registry.npmjs.org/escape-html
20:10:01 [INFO] downloading https://registry.npmjs.org/escape-html/-/escape-html-1.0.3.tgz
20:10:01 [INFO] [npm] escape-html@1.0.3 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/escape-html-1.0.3/escape-html-1.0.3.tgz
20:10:01 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/escape-html-1.0.3/escape-html-1.0.3.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/escape-html-1.0.3 as gztar
20:10:01 [INFO] === npm :: etag :: 1.8.1 (ref=pkg:npm/etag@1.8.1) ===
20:10:01 [INFO] [npm] etag@1.8.1 querying https://registry.npmjs.org/etag
20:10:02 [INFO] downloading https://registry.npmjs.org/etag/-/etag-1.8.1.tgz
20:10:03 [INFO] [npm] etag@1.8.1 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/etag-1.8.1/etag-1.8.1.tgz
20:10:03 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/etag-1.8.1/etag-1.8.1.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/etag-1.8.1 as gztar
20:10:03 [INFO] === npm :: finalhandler :: 1.3.2 (ref=pkg:npm/finalhandler@1.3.2) ===
20:10:03 [INFO] [npm] finalhandler@1.3.2 querying https://registry.npmjs.org/finalhandler
20:10:04 [INFO] downloading https://registry.npmjs.org/finalhandler/-/finalhandler-1.3.2.tgz
20:10:04 [INFO] [npm] finalhandler@1.3.2 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/finalhandler-1.3.2/finalhandler-1.3.2.tgz
20:10:04 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/finalhandler-1.3.2/finalhandler-1.3.2.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/finalhandler-1.3.2 as gztar
20:10:04 [INFO] === npm :: forwarded :: 0.2.0 (ref=pkg:npm/forwarded@0.2.0) ===
20:10:04 [INFO] [npm] forwarded@0.2.0 querying https://registry.npmjs.org/forwarded
20:10:05 [INFO] downloading https://registry.npmjs.org/forwarded/-/forwarded-0.2.0.tgz
20:10:05 [INFO] [npm] forwarded@0.2.0 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/forwarded-0.2.0/forwarded-0.2.0.tgz
20:10:05 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/forwarded-0.2.0/forwarded-0.2.0.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/forwarded-0.2.0 as gztar
20:10:05 [INFO] === npm :: fresh :: 0.5.2 (ref=pkg:npm/fresh@0.5.2) ===
20:10:05 [INFO] [npm] fresh@0.5.2 querying https://registry.npmjs.org/fresh
20:10:07 [INFO] downloading https://registry.npmjs.org/fresh/-/fresh-0.5.2.tgz
20:10:07 [INFO] [npm] fresh@0.5.2 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/fresh-0.5.2/fresh-0.5.2.tgz
20:10:07 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/fresh-0.5.2/fresh-0.5.2.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/fresh-0.5.2 as gztar
20:10:07 [INFO] === npm :: function-bind :: 1.1.2 (ref=pkg:npm/function-bind@1.1.2) ===
20:10:07 [INFO] [npm] function-bind@1.1.2 querying https://registry.npmjs.org/function-bind
20:10:07 [INFO] downloading https://registry.npmjs.org/function-bind/-/function-bind-1.1.2.tgz
20:10:08 [INFO] [npm] function-bind@1.1.2 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/function-bind-1.1.2/function-bind-1.1.2.tgz
20:10:08 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/function-bind-1.1.2/function-bind-1.1.2.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/function-bind-1.1.2 as gztar
20:10:08 [INFO] === npm :: get-intrinsic :: 1.3.0 (ref=pkg:npm/get-intrinsic@1.3.0) ===
20:10:08 [INFO] [npm] get-intrinsic@1.3.0 querying https://registry.npmjs.org/get-intrinsic
20:10:08 [INFO] downloading https://registry.npmjs.org/get-intrinsic/-/get-intrinsic-1.3.0.tgz
20:10:09 [INFO] [npm] get-intrinsic@1.3.0 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/get-intrinsic-1.3.0/get-intrinsic-1.3.0.tgz
20:10:09 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/get-intrinsic-1.3.0/get-intrinsic-1.3.0.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/get-intrinsic-1.3.0 as gztar
20:10:09 [INFO] === npm :: get-proto :: 1.0.1 (ref=pkg:npm/get-proto@1.0.1) ===
20:10:09 [INFO] [npm] get-proto@1.0.1 querying https://registry.npmjs.org/get-proto
20:10:09 [INFO] downloading https://registry.npmjs.org/get-proto/-/get-proto-1.0.1.tgz
20:10:09 [INFO] [npm] get-proto@1.0.1 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/get-proto-1.0.1/get-proto-1.0.1.tgz
20:10:09 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/get-proto-1.0.1/get-proto-1.0.1.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/get-proto-1.0.1 as gztar
20:10:09 [INFO] === npm :: gopd :: 1.2.0 (ref=pkg:npm/gopd@1.2.0) ===
20:10:09 [INFO] [npm] gopd@1.2.0 querying https://registry.npmjs.org/gopd
20:10:10 [INFO] downloading https://registry.npmjs.org/gopd/-/gopd-1.2.0.tgz
20:10:11 [INFO] [npm] gopd@1.2.0 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/gopd-1.2.0/gopd-1.2.0.tgz
20:10:11 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/gopd-1.2.0/gopd-1.2.0.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/gopd-1.2.0 as gztar
20:10:11 [INFO] === npm :: has-symbols :: 1.1.0 (ref=pkg:npm/has-symbols@1.1.0) ===
20:10:11 [INFO] [npm] has-symbols@1.1.0 querying https://registry.npmjs.org/has-symbols
20:10:12 [INFO] downloading https://registry.npmjs.org/has-symbols/-/has-symbols-1.1.0.tgz
20:10:12 [INFO] [npm] has-symbols@1.1.0 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/has-symbols-1.1.0/has-symbols-1.1.0.tgz
20:10:12 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/has-symbols-1.1.0/has-symbols-1.1.0.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/has-symbols-1.1.0 as gztar
20:10:12 [INFO] === npm :: hasown :: 2.0.4 (ref=pkg:npm/hasown@2.0.4) ===
20:10:12 [INFO] [npm] hasown@2.0.4 querying https://registry.npmjs.org/hasown
20:10:14 [INFO] downloading https://registry.npmjs.org/hasown/-/hasown-2.0.4.tgz
20:10:14 [INFO] [npm] hasown@2.0.4 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/hasown-2.0.4/hasown-2.0.4.tgz
20:10:14 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/hasown-2.0.4/hasown-2.0.4.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/hasown-2.0.4 as gztar
20:10:14 [INFO] === npm :: http-errors :: 2.0.1 (ref=pkg:npm/http-errors@2.0.1) ===
20:10:14 [INFO] [npm] http-errors@2.0.1 querying https://registry.npmjs.org/http-errors
20:10:15 [INFO] downloading https://registry.npmjs.org/http-errors/-/http-errors-2.0.1.tgz
20:10:15 [INFO] [npm] http-errors@2.0.1 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/http-errors-2.0.1/http-errors-2.0.1.tgz
20:10:15 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/http-errors-2.0.1/http-errors-2.0.1.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/http-errors-2.0.1 as gztar
20:10:15 [INFO] === npm :: iconv-lite :: 0.4.24 (ref=pkg:npm/iconv-lite@0.4.24) ===
20:10:15 [INFO] [npm] iconv-lite@0.4.24 querying https://registry.npmjs.org/iconv-lite
20:10:16 [INFO] downloading https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.24.tgz
20:10:17 [INFO] [npm] iconv-lite@0.4.24 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/iconv-lite-0.4.24/iconv-lite-0.4.24.tgz
20:10:17 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/iconv-lite-0.4.24/iconv-lite-0.4.24.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/iconv-lite-0.4.24 as gztar
20:10:17 [INFO] === npm :: inherits :: 2.0.4 (ref=pkg:npm/inherits@2.0.4) ===
20:10:17 [INFO] [npm] inherits@2.0.4 querying https://registry.npmjs.org/inherits
20:10:17 [INFO] downloading https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz
20:10:18 [INFO] [npm] inherits@2.0.4 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/inherits-2.0.4/inherits-2.0.4.tgz
20:10:18 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/inherits-2.0.4/inherits-2.0.4.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/inherits-2.0.4 as gztar
20:10:18 [INFO] === npm :: ipaddr.js :: 1.9.1 (ref=pkg:npm/ipaddr.js@1.9.1) ===
20:10:18 [INFO] [npm] ipaddr.js@1.9.1 querying https://registry.npmjs.org/ipaddr.js
20:10:18 [INFO] downloading https://registry.npmjs.org/ipaddr.js/-/ipaddr.js-1.9.1.tgz
20:10:19 [INFO] [npm] ipaddr.js@1.9.1 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/ipaddr.js-1.9.1/ipaddr.js-1.9.1.tgz
20:10:19 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/ipaddr.js-1.9.1/ipaddr.js-1.9.1.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/ipaddr.js-1.9.1 as gztar
20:10:19 [INFO] === npm :: math-intrinsics :: 1.1.0 (ref=pkg:npm/math-intrinsics@1.1.0) ===
20:10:19 [INFO] [npm] math-intrinsics@1.1.0 querying https://registry.npmjs.org/math-intrinsics
20:10:20 [INFO] downloading https://registry.npmjs.org/math-intrinsics/-/math-intrinsics-1.1.0.tgz
20:10:20 [INFO] [npm] math-intrinsics@1.1.0 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/math-intrinsics-1.1.0/math-intrinsics-1.1.0.tgz
20:10:20 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/math-intrinsics-1.1.0/math-intrinsics-1.1.0.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/math-intrinsics-1.1.0 as gztar
20:10:20 [INFO] === npm :: media-typer :: 0.3.0 (ref=pkg:npm/media-typer@0.3.0) ===
20:10:20 [INFO] [npm] media-typer@0.3.0 querying https://registry.npmjs.org/media-typer
20:10:21 [INFO] downloading https://registry.npmjs.org/media-typer/-/media-typer-0.3.0.tgz
20:10:21 [INFO] [npm] media-typer@0.3.0 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/media-typer-0.3.0/media-typer-0.3.0.tgz
20:10:21 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/media-typer-0.3.0/media-typer-0.3.0.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/media-typer-0.3.0 as gztar
20:10:21 [INFO] === npm :: merge-descriptors :: 1.0.3 (ref=pkg:npm/merge-descriptors@1.0.3) ===
20:10:21 [INFO] [npm] merge-descriptors@1.0.3 querying https://registry.npmjs.org/merge-descriptors
20:10:22 [INFO] downloading https://registry.npmjs.org/merge-descriptors/-/merge-descriptors-1.0.3.tgz
20:10:23 [INFO] [npm] merge-descriptors@1.0.3 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/merge-descriptors-1.0.3/merge-descriptors-1.0.3.tgz
20:10:23 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/merge-descriptors-1.0.3/merge-descriptors-1.0.3.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/merge-descriptors-1.0.3 as gztar
20:10:23 [INFO] === npm :: methods :: 1.1.2 (ref=pkg:npm/methods@1.1.2) ===
20:10:23 [INFO] [npm] methods@1.1.2 querying https://registry.npmjs.org/methods
20:10:24 [INFO] downloading https://registry.npmjs.org/methods/-/methods-1.1.2.tgz
20:10:24 [INFO] [npm] methods@1.1.2 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/methods-1.1.2/methods-1.1.2.tgz
20:10:24 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/methods-1.1.2/methods-1.1.2.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/methods-1.1.2 as gztar
20:10:24 [INFO] === npm :: mime-db :: 1.52.0 (ref=pkg:npm/mime-db@1.52.0) ===
20:10:24 [INFO] [npm] mime-db@1.52.0 querying https://registry.npmjs.org/mime-db
20:10:25 [INFO] downloading https://registry.npmjs.org/mime-db/-/mime-db-1.52.0.tgz
20:10:25 [INFO] [npm] mime-db@1.52.0 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/mime-db-1.52.0/mime-db-1.52.0.tgz
20:10:25 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/mime-db-1.52.0/mime-db-1.52.0.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/mime-db-1.52.0 as gztar
20:10:25 [INFO] === npm :: mime-types :: 2.1.35 (ref=pkg:npm/mime-types@2.1.35) ===
20:10:25 [INFO] [npm] mime-types@2.1.35 querying https://registry.npmjs.org/mime-types
20:10:26 [INFO] downloading https://registry.npmjs.org/mime-types/-/mime-types-2.1.35.tgz
20:10:26 [INFO] [npm] mime-types@2.1.35 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/mime-types-2.1.35/mime-types-2.1.35.tgz
20:10:26 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/mime-types-2.1.35/mime-types-2.1.35.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/mime-types-2.1.35 as gztar
20:10:26 [INFO] === npm :: mime :: 1.6.0 (ref=pkg:npm/mime@1.6.0) ===
20:10:26 [INFO] [npm] mime@1.6.0 querying https://registry.npmjs.org/mime
20:10:26 [INFO] downloading https://registry.npmjs.org/mime/-/mime-1.6.0.tgz
20:10:27 [INFO] [npm] mime@1.6.0 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/mime-1.6.0/mime-1.6.0.tgz
20:10:27 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/mime-1.6.0/mime-1.6.0.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/mime-1.6.0 as gztar
20:10:27 [INFO] === npm :: ms :: 2.0.0 (ref=pkg:npm/ms@2.0.0) ===
20:10:27 [INFO] [npm] ms@2.0.0 querying https://registry.npmjs.org/ms
20:10:28 [INFO] downloading https://registry.npmjs.org/ms/-/ms-2.0.0.tgz
20:10:28 [INFO] [npm] ms@2.0.0 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/ms-2.0.0/ms-2.0.0.tgz
20:10:28 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/ms-2.0.0/ms-2.0.0.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/ms-2.0.0 as gztar
20:10:28 [INFO] === npm :: ms :: 2.1.3 (ref=pkg:npm/ms@2.1.3) ===
20:10:28 [INFO] [npm] ms@2.1.3 querying https://registry.npmjs.org/ms
20:10:29 [INFO] downloading https://registry.npmjs.org/ms/-/ms-2.1.3.tgz
20:10:29 [INFO] [npm] ms@2.1.3 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/ms-2.1.3/ms-2.1.3.tgz
20:10:29 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/ms-2.1.3/ms-2.1.3.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/ms-2.1.3 as gztar
20:10:29 [INFO] === npm :: negotiator :: 0.6.3 (ref=pkg:npm/negotiator@0.6.3) ===
20:10:29 [INFO] [npm] negotiator@0.6.3 querying https://registry.npmjs.org/negotiator
20:10:30 [INFO] downloading https://registry.npmjs.org/negotiator/-/negotiator-0.6.3.tgz
20:10:30 [INFO] [npm] negotiator@0.6.3 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/negotiator-0.6.3/negotiator-0.6.3.tgz
20:10:30 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/negotiator-0.6.3/negotiator-0.6.3.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/negotiator-0.6.3 as gztar
20:10:30 [INFO] === npm :: object-inspect :: 1.13.4 (ref=pkg:npm/object-inspect@1.13.4) ===
20:10:30 [INFO] [npm] object-inspect@1.13.4 querying https://registry.npmjs.org/object-inspect
20:10:31 [INFO] downloading https://registry.npmjs.org/object-inspect/-/object-inspect-1.13.4.tgz
20:10:31 [INFO] [npm] object-inspect@1.13.4 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/object-inspect-1.13.4/object-inspect-1.13.4.tgz
20:10:31 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/object-inspect-1.13.4/object-inspect-1.13.4.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/object-inspect-1.13.4 as gztar
20:10:31 [INFO] === npm :: on-finished :: 2.4.1 (ref=pkg:npm/on-finished@2.4.1) ===
20:10:31 [INFO] [npm] on-finished@2.4.1 querying https://registry.npmjs.org/on-finished
20:10:32 [INFO] downloading https://registry.npmjs.org/on-finished/-/on-finished-2.4.1.tgz
20:10:33 [INFO] [npm] on-finished@2.4.1 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/on-finished-2.4.1/on-finished-2.4.1.tgz
20:10:33 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/on-finished-2.4.1/on-finished-2.4.1.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/on-finished-2.4.1 as gztar
20:10:33 [INFO] === npm :: parseurl :: 1.3.3 (ref=pkg:npm/parseurl@1.3.3) ===
20:10:33 [INFO] [npm] parseurl@1.3.3 querying https://registry.npmjs.org/parseurl
20:10:34 [INFO] downloading https://registry.npmjs.org/parseurl/-/parseurl-1.3.3.tgz
20:10:34 [INFO] [npm] parseurl@1.3.3 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/parseurl-1.3.3/parseurl-1.3.3.tgz
20:10:34 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/parseurl-1.3.3/parseurl-1.3.3.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/parseurl-1.3.3 as gztar
20:10:34 [INFO] === npm :: path-to-regexp :: 0.1.13 (ref=pkg:npm/path-to-regexp@0.1.13) ===
20:10:34 [INFO] [npm] path-to-regexp@0.1.13 querying https://registry.npmjs.org/path-to-regexp
20:10:35 [INFO] downloading https://registry.npmjs.org/path-to-regexp/-/path-to-regexp-0.1.13.tgz
20:10:35 [INFO] [npm] path-to-regexp@0.1.13 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/path-to-regexp-0.1.13/path-to-regexp-0.1.13.tgz
20:10:35 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/path-to-regexp-0.1.13/path-to-regexp-0.1.13.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/path-to-regexp-0.1.13 as gztar
20:10:35 [INFO] === npm :: proxy-addr :: 2.0.7 (ref=pkg:npm/proxy-addr@2.0.7) ===
20:10:35 [INFO] [npm] proxy-addr@2.0.7 querying https://registry.npmjs.org/proxy-addr
20:10:37 [INFO] downloading https://registry.npmjs.org/proxy-addr/-/proxy-addr-2.0.7.tgz
20:10:37 [INFO] [npm] proxy-addr@2.0.7 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/proxy-addr-2.0.7/proxy-addr-2.0.7.tgz
20:10:37 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/proxy-addr-2.0.7/proxy-addr-2.0.7.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/proxy-addr-2.0.7 as gztar
20:10:37 [INFO] === npm :: qs :: 6.15.2 (ref=pkg:npm/qs@6.15.2) ===
20:10:37 [INFO] [npm] qs@6.15.2 querying https://registry.npmjs.org/qs
20:10:38 [INFO] downloading https://registry.npmjs.org/qs/-/qs-6.15.2.tgz
20:10:39 [INFO] [npm] qs@6.15.2 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/qs-6.15.2/qs-6.15.2.tgz
20:10:39 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/qs-6.15.2/qs-6.15.2.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/qs-6.15.2 as gztar
20:10:39 [INFO] === npm :: range-parser :: 1.2.1 (ref=pkg:npm/range-parser@1.2.1) ===
20:10:39 [INFO] [npm] range-parser@1.2.1 querying https://registry.npmjs.org/range-parser
20:10:40 [INFO] downloading https://registry.npmjs.org/range-parser/-/range-parser-1.2.1.tgz
20:10:40 [INFO] [npm] range-parser@1.2.1 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/range-parser-1.2.1/range-parser-1.2.1.tgz
20:10:40 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/range-parser-1.2.1/range-parser-1.2.1.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/range-parser-1.2.1 as gztar
20:10:40 [INFO] === npm :: raw-body :: 2.5.3 (ref=pkg:npm/raw-body@2.5.3) ===
20:10:40 [INFO] [npm] raw-body@2.5.3 querying https://registry.npmjs.org/raw-body
20:10:41 [INFO] downloading https://registry.npmjs.org/raw-body/-/raw-body-2.5.3.tgz
20:10:42 [INFO] [npm] raw-body@2.5.3 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/raw-body-2.5.3/raw-body-2.5.3.tgz
20:10:42 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/raw-body-2.5.3/raw-body-2.5.3.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/raw-body-2.5.3 as gztar
20:10:42 [INFO] === npm :: safe-buffer :: 5.2.1 (ref=pkg:npm/safe-buffer@5.2.1) ===
20:10:42 [INFO] [npm] safe-buffer@5.2.1 querying https://registry.npmjs.org/safe-buffer
20:10:43 [INFO] downloading https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.2.1.tgz
20:10:43 [INFO] [npm] safe-buffer@5.2.1 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/safe-buffer-5.2.1/safe-buffer-5.2.1.tgz
20:10:43 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/safe-buffer-5.2.1/safe-buffer-5.2.1.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/safe-buffer-5.2.1 as gztar
20:10:43 [INFO] === npm :: safer-buffer :: 2.1.2 (ref=pkg:npm/safer-buffer@2.1.2) ===
20:10:43 [INFO] [npm] safer-buffer@2.1.2 querying https://registry.npmjs.org/safer-buffer
20:10:44 [INFO] downloading https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz
20:10:45 [INFO] [npm] safer-buffer@2.1.2 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/safer-buffer-2.1.2/safer-buffer-2.1.2.tgz
20:10:45 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/safer-buffer-2.1.2/safer-buffer-2.1.2.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/safer-buffer-2.1.2 as gztar
20:10:45 [INFO] === npm :: send :: 0.19.2 (ref=pkg:npm/send@0.19.2) ===
20:10:45 [INFO] [npm] send@0.19.2 querying https://registry.npmjs.org/send
20:10:45 [INFO] downloading https://registry.npmjs.org/send/-/send-0.19.2.tgz
20:10:46 [INFO] [npm] send@0.19.2 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/send-0.19.2/send-0.19.2.tgz
20:10:46 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/send-0.19.2/send-0.19.2.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/send-0.19.2 as gztar
20:10:46 [INFO] === npm :: serve-static :: 1.16.3 (ref=pkg:npm/serve-static@1.16.3) ===
20:10:46 [INFO] [npm] serve-static@1.16.3 querying https://registry.npmjs.org/serve-static
20:10:47 [INFO] downloading https://registry.npmjs.org/serve-static/-/serve-static-1.16.3.tgz
20:10:47 [INFO] [npm] serve-static@1.16.3 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/serve-static-1.16.3/serve-static-1.16.3.tgz
20:10:47 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/serve-static-1.16.3/serve-static-1.16.3.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/serve-static-1.16.3 as gztar
20:10:47 [INFO] === npm :: setprototypeof :: 1.2.0 (ref=pkg:npm/setprototypeof@1.2.0) ===
20:10:47 [INFO] [npm] setprototypeof@1.2.0 querying https://registry.npmjs.org/setprototypeof
20:10:48 [INFO] downloading https://registry.npmjs.org/setprototypeof/-/setprototypeof-1.2.0.tgz
20:10:48 [INFO] [npm] setprototypeof@1.2.0 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/setprototypeof-1.2.0/setprototypeof-1.2.0.tgz
20:10:48 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/setprototypeof-1.2.0/setprototypeof-1.2.0.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/setprototypeof-1.2.0 as gztar
20:10:48 [INFO] === npm :: side-channel-list :: 1.0.1 (ref=pkg:npm/side-channel-list@1.0.1) ===
20:10:48 [INFO] [npm] side-channel-list@1.0.1 querying https://registry.npmjs.org/side-channel-list
20:10:49 [INFO] downloading https://registry.npmjs.org/side-channel-list/-/side-channel-list-1.0.1.tgz
20:10:49 [INFO] [npm] side-channel-list@1.0.1 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/side-channel-list-1.0.1/side-channel-list-1.0.1.tgz
20:10:49 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/side-channel-list-1.0.1/side-channel-list-1.0.1.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/side-channel-list-1.0.1 as gztar
20:10:49 [INFO] === npm :: side-channel-map :: 1.0.1 (ref=pkg:npm/side-channel-map@1.0.1) ===
20:10:49 [INFO] [npm] side-channel-map@1.0.1 querying https://registry.npmjs.org/side-channel-map
20:10:50 [INFO] downloading https://registry.npmjs.org/side-channel-map/-/side-channel-map-1.0.1.tgz
20:10:51 [INFO] [npm] side-channel-map@1.0.1 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/side-channel-map-1.0.1/side-channel-map-1.0.1.tgz
20:10:51 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/side-channel-map-1.0.1/side-channel-map-1.0.1.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/side-channel-map-1.0.1 as gztar
20:10:51 [INFO] === npm :: side-channel-weakmap :: 1.0.2 (ref=pkg:npm/side-channel-weakmap@1.0.2) ===
20:10:51 [INFO] [npm] side-channel-weakmap@1.0.2 querying https://registry.npmjs.org/side-channel-weakmap
20:10:52 [INFO] downloading https://registry.npmjs.org/side-channel-weakmap/-/side-channel-weakmap-1.0.2.tgz
20:10:52 [INFO] [npm] side-channel-weakmap@1.0.2 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/side-channel-weakmap-1.0.2/side-channel-weakmap-1.0.2.tgz
20:10:52 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/side-channel-weakmap-1.0.2/side-channel-weakmap-1.0.2.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/side-channel-weakmap-1.0.2 as gztar
20:10:52 [INFO] === npm :: side-channel :: 1.1.0 (ref=pkg:npm/side-channel@1.1.0) ===
20:10:52 [INFO] [npm] side-channel@1.1.0 querying https://registry.npmjs.org/side-channel
20:10:53 [INFO] downloading https://registry.npmjs.org/side-channel/-/side-channel-1.1.0.tgz
20:10:53 [INFO] [npm] side-channel@1.1.0 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/side-channel-1.1.0/side-channel-1.1.0.tgz
20:10:53 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/side-channel-1.1.0/side-channel-1.1.0.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/side-channel-1.1.0 as gztar
20:10:53 [INFO] === npm :: statuses :: 2.0.2 (ref=pkg:npm/statuses@2.0.2) ===
20:10:53 [INFO] [npm] statuses@2.0.2 querying https://registry.npmjs.org/statuses
20:10:55 [INFO] downloading https://registry.npmjs.org/statuses/-/statuses-2.0.2.tgz
20:10:55 [INFO] [npm] statuses@2.0.2 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/statuses-2.0.2/statuses-2.0.2.tgz
20:10:55 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/statuses-2.0.2/statuses-2.0.2.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/statuses-2.0.2 as gztar
20:10:55 [INFO] === npm :: toidentifier :: 1.0.1 (ref=pkg:npm/toidentifier@1.0.1) ===
20:10:55 [INFO] [npm] toidentifier@1.0.1 querying https://registry.npmjs.org/toidentifier
20:10:56 [INFO] downloading https://registry.npmjs.org/toidentifier/-/toidentifier-1.0.1.tgz
20:10:56 [INFO] [npm] toidentifier@1.0.1 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/toidentifier-1.0.1/toidentifier-1.0.1.tgz
20:10:56 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/toidentifier-1.0.1/toidentifier-1.0.1.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/toidentifier-1.0.1 as gztar
20:10:56 [INFO] === npm :: type-is :: 1.6.18 (ref=pkg:npm/type-is@1.6.18) ===
20:10:56 [INFO] [npm] type-is@1.6.18 querying https://registry.npmjs.org/type-is
20:10:57 [INFO] downloading https://registry.npmjs.org/type-is/-/type-is-1.6.18.tgz
20:10:57 [INFO] [npm] type-is@1.6.18 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/type-is-1.6.18/type-is-1.6.18.tgz
20:10:57 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/type-is-1.6.18/type-is-1.6.18.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/type-is-1.6.18 as gztar
20:10:57 [INFO] === npm :: unpipe :: 1.0.0 (ref=pkg:npm/unpipe@1.0.0) ===
20:10:57 [INFO] [npm] unpipe@1.0.0 querying https://registry.npmjs.org/unpipe
20:10:59 [INFO] downloading https://registry.npmjs.org/unpipe/-/unpipe-1.0.0.tgz
20:10:59 [INFO] [npm] unpipe@1.0.0 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/unpipe-1.0.0/unpipe-1.0.0.tgz
20:10:59 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/unpipe-1.0.0/unpipe-1.0.0.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/unpipe-1.0.0 as gztar
20:10:59 [INFO] === npm :: utils-merge :: 1.0.1 (ref=pkg:npm/utils-merge@1.0.1) ===
20:10:59 [INFO] [npm] utils-merge@1.0.1 querying https://registry.npmjs.org/utils-merge
20:11:01 [INFO] downloading https://registry.npmjs.org/utils-merge/-/utils-merge-1.0.1.tgz
20:11:01 [INFO] [npm] utils-merge@1.0.1 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/utils-merge-1.0.1/utils-merge-1.0.1.tgz
20:11:01 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/utils-merge-1.0.1/utils-merge-1.0.1.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/utils-merge-1.0.1 as gztar
20:11:01 [INFO] === npm :: vary :: 1.1.2 (ref=pkg:npm/vary@1.1.2) ===
20:11:01 [INFO] [npm] vary@1.1.2 querying https://registry.npmjs.org/vary
20:11:02 [INFO] downloading https://registry.npmjs.org/vary/-/vary-1.1.2.tgz
20:11:03 [INFO] [npm] vary@1.1.2 downloaded to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/vary-1.1.2/vary-1.1.2.tgz
20:11:03 [INFO] unpacking /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/vary-1.1.2/vary-1.1.2.tgz to /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/vary-1.1.2 as gztar
20:11:03 [INFO] Logged 67 processed packages to: /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/sources_downloads.csv
20:11:03 [INFO] All downloads finished without recorded failures (or dry-run mode).
20:11:06 [INFO] RUN python3 /home/kali/Desktop/oss_checks/instruments/extract/extract.py /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs  (cwd=/home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs)
[cleanup] removing directory: /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/es-errors-1.3.0/package/test
[cleanup] removing directory: /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/object-inspect-1.13.4/package/example
[cleanup] removing directory: /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/object-inspect-1.13.4/package/test
[cleanup] removing directory: /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/math-intrinsics-1.1.0/package/test
[cleanup] removing directory: /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/side-channel-list-1.0.1/package/test
[cleanup] removing directory: /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/get-proto-1.0.1/package/test
[cleanup] removing directory: /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/call-bound-1.0.4/package/test
[cleanup] removing directory: /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/side-channel-weakmap-1.0.2/package/test
[cleanup] removing directory: /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/function-bind-1.1.2/package/test
[cleanup] removing directory: /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/es-object-atoms-1.1.2/package/test
[cleanup] removing directory: /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/side-channel-map-1.0.1/package/test
[cleanup] removing directory: /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/qs-6.15.2/package/test
[cleanup] removing directory: /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/dunder-proto-1.0.1/package/test
[cleanup] removing directory: /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/get-intrinsic-1.3.0/package/test
[cleanup] removing directory: /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/call-bind-apply-helpers-1.0.2/package/test
[cleanup] removing directory: /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/side-channel-1.1.0/package/test
[cleanup] removing directory: /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/has-symbols-1.1.0/package/test
[cleanup] removing directory: /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/setprototypeof-1.2.0/package/test
[cleanup] removing directory: /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/es-define-property-1.0.1/package/test
[cleanup] removing directory: /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/npm/gopd-1.2.0/package/test
[bin-scan] Found 0 native binary files
[bin-scan] Skipping XLSX output (empty)
[WARN] xlsx merge: no input files found; skipping
SBOM: /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/sbom/origsbom.json
Sources dir (already downloaded): /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs
Include ecosystems: ['cargo', 'composer', 'conan', 'go', 'maven', 'npm', 'nuget', 'pypi']
Loaded SBOM with 68 components and 69 dependency entries
[info] CDX dependency graph nodes: 69, roots: 1
Found 67 unique (ecosystem, name, version) entries
[100%] (67/67) npm vary 1.1.2 ...0.1 .....0.2 .....

[OK] Wrote 67 rows to /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/reports/licenses.xlsx
20:11:25 [INFO] external_downloads: 5 hit(s) found in /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs
20:11:25 [INFO] external_downloads JSON report written: /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/external_downloads/external_downloads_transitive.json
20:11:25 [INFO] pipeline summary:
20:11:25 [INFO] stage ecosystem: done
20:11:25 [INFO] stage ecosystem artifact: report -> /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/ecosystems/lock_summary.json
20:11:25 [INFO] stage cplus_scan: done
20:11:25 [INFO] stage cplus_scan artifact: cplus_sbom -> /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/sbom/cplus_sbom.json
20:11:25 [INFO] stage trivy_sbom: done
20:11:25 [INFO] stage trivy_sbom artifact: sbom -> /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/sbom/origsbom.json
20:11:25 [INFO] stage vuln_management: done
20:11:25 [INFO] stage vuln_management artifact: missing_versions_txt -> /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/sbom/debug/missing_versions.txt
20:11:25 [INFO] stage vuln_management artifact: failed_debug_txt -> /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/sbom/debug/failed_safe_versions_debug.txt
20:11:25 [INFO] stage vuln_management artifact: report_xlsx -> /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/reports/report.xlsx
20:11:25 [INFO] stage vuln_management artifact: sbom_clean -> /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/sbom/sbom-clean.json
20:11:25 [INFO] stage asm_audit_root: skipped
20:11:25 [WARNING] stage asm_audit_root: no ASM matches for /home/kali/Desktop/jobs/express/_repos/express
20:11:25 [INFO] stage external_downloads_root: done
20:11:25 [INFO] stage external_downloads_root artifact: report -> /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/external_downloads/external_downloads_root.json
20:11:25 [INFO] stage registry_sources_root: done
20:11:25 [INFO] stage registry_sources_root artifact: report -> /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/ecosystems/registry_sources_root.json
20:11:25 [INFO] stage download_sources: done
20:11:25 [INFO] stage download_sources artifact: sources_downloads_csv -> /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs/sources_downloads.csv
20:11:25 [INFO] stage toxic_repos: done
20:11:25 [INFO] stage toxic_repos artifact: report -> /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/reports/toxic_repos_report.csv
20:11:25 [INFO] stage prepare_transitive_workspace: done
20:11:25 [INFO] stage prepare_transitive_workspace artifact: deps_dir -> /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs
20:11:25 [INFO] stage binary_scan: done
20:11:25 [WARNING] stage binary_scan: binary scan found nothing to report
20:11:25 [INFO] stage license_collection: done
20:11:25 [INFO] stage license_collection artifact: report -> /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/reports/licenses.xlsx
20:11:25 [INFO] stage asm_audit_transitive_libs: skipped
20:11:25 [WARNING] stage asm_audit_transitive_libs: no ASM matches for /home/kali/Desktop/jobs/express/_repos/jobs/transitive_libs
20:11:25 [INFO] stage external_downloads_transitive: done
20:11:25 [INFO] stage external_downloads_transitive artifact: report -> /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5/external_downloads/external_downloads_transitive.json
20:11:25 [INFO] pipeline finished successfully
20:11:25 [INFO] artifacts directory: /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5
2026-06-07 20:11:25 | INFO    |   moving results: /home/kali/Desktop/jobs/express/jobs/f7b068c694d1432982e32eda3a6d39e5 -> /home/kali/Desktop/results/2026-06-07/express__v4.22.2
2026-06-07 20:11:25 | INFO    |   [OK] express / v4.22.2 -> /home/kali/Desktop/results/2026-06-07/express__v4.22.2
2026-06-07 20:11:25 | INFO    | === product: express ===
2026-06-07 20:11:25 | INFO    | --- version: v4.18.1 ---
2026-06-07 20:11:25 | INFO    |     repo already cloned: express — fetching
2026-06-07 20:11:25 | INFO    |     running: git -c credential.helper= remote set-url origin https://github.com/expressjs/express.git
2026-06-07 20:11:25 | INFO    |     running: git -c credential.helper= fetch --prune --all
2026-06-07 20:11:27 | INFO    |     checkout express @ v4.18.1
2026-06-07 20:11:27 | INFO    |     running: git -c credential.helper= checkout v4.18.1
2026-06-07 20:11:27 | ERROR   |     [FAIL] git checkout v4.18.1: error: pathspec 'v4.18.1' did not match any file(s) known to git
2026-06-07 20:11:27 | ERROR   |     skipping express because checkout v4.18.1 failed: error: pathspec 'v4.18.1' did not match any file(s) known to git
2026-06-07 20:11:27 | ERROR   |   [FAIL] express / v4.18.1: all repositories failed; scanner was not run
2026-06-07 20:11:27 | INFO    | run log written: /home/kali/Desktop/results/2026-06-07/run.log
2026-06-07 20:11:27 | ERROR   | 1/2 scan(s) failed
