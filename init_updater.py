python3 sheduler.py --config config.yml
2026-06-07 19:53:07 | INFO    | GITLAB_TOKEN not set — will try anonymous clone first
2026-06-07 19:53:07 | INFO    | timeouts: scanner=3600s, distrib_scan=7200s, deptrack=3600s
2026-06-07 19:53:07 | INFO    | === product: express ===
2026-06-07 19:53:07 | INFO    | --- version: v4.22.2 ---
2026-06-07 19:53:07 | INFO    |     cloning: https://github.com/expressjs/express.git
2026-06-07 19:53:07 | INFO    |     running: git -c credential.helper= clone --no-checkout https://github.com/expressjs/express.git /home/kali/Desktop/jobs/express/_repos/express
2026-06-07 19:53:15 | INFO    |     checkout express @ v4.22.2
2026-06-07 19:53:15 | INFO    |     running: git -c credential.helper= checkout v4.22.2
2026-06-07 19:53:15 | INFO    |     v4.22.2 is a tag — skipping reset to origin/
2026-06-07 19:53:15 | INFO    |     running: git -c credential.helper= submodule update --init --recursive
2026-06-07 19:53:15 | INFO    |     linking /home/kali/Desktop/jobs/express/sources/express -> /home/kali/Desktop/jobs/express/_repos/express
2026-06-07 19:53:15 | INFO    |   running scanner on /home/kali/Desktop/jobs/express/sources (DT project: express__v4.22.2, timeout=3600s)
2026-06-07 19:53:15 | INFO    |   job_dir: /home/kali/Desktop/jobs/express/jobs/ad299a0eefc14088820e4c890dcaeaeb
2026-06-07 19:53:15 | INFO    |     running: /home/kali/Desktop/venv/bin/python3 /home/kali/Desktop/oss_checks/scanner.py /home/kali/Desktop/jobs/express/sources --apply --deptrack --dt-project-name express__v4.22.2 --env-file /home/kali/Desktop/oss_checks/.env --job-dir /home/kali/Desktop/jobs/express/jobs/ad299a0eefc14088820e4c890dcaeaeb
19:53:16 [INFO] loaded .env: /home/kali/Desktop/oss_checks/.env
19:53:16 [INFO] [dt] auto-ensuring orig project 'express__v4.22.2-orig'...
19:53:16 [INFO] [dt] reusing existing project 'express__v4.22.2-orig' -> 77093aa6-2c10-4101-bed6-d7de8eb6052b
19:53:16 [INFO] [dt] server version: 4.14.2 — parentUUID support: yes
19:53:16 [INFO] [dt] auto-ensuring safe project 'express__v4.22.2 [safe]' (parent: 77093aa6-2c10-4101-bed6-d7de8eb6052b)...
19:53:16 [INFO] [dt] reusing existing project 'express__v4.22.2 [safe]' -> 95580e40-242b-47f3-9999-435433fecf2f
19:53:16 [INFO] original root (read-only): /home/kali/Desktop/jobs/express/sources
19:53:16 [INFO] working copy:              /home/kali/Desktop/jobs/express/jobs/sources/root_sources
19:53:16 [INFO] job directory:             /home/kali/Desktop/jobs/express/jobs/ad299a0eefc14088820e4c890dcaeaeb
19:53:16 [INFO] dependency-track: enabled url=http://localhost:8081 safe_project=95580e40-242b-47f3-9999-435433fecf2f orig_project=77093aa6-2c10-4101-bed6-d7de8eb6052b insecure=True
19:53:16 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs
19:53:16 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/sources
19:53:16 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/ad299a0eefc14088820e4c890dcaeaeb
19:53:16 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/ad299a0eefc14088820e4c890dcaeaeb/sbom
19:53:16 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/ad299a0eefc14088820e4c890dcaeaeb/reports
19:53:16 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/ad299a0eefc14088820e4c890dcaeaeb/reports/asm
19:53:16 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/ad299a0eefc14088820e4c890dcaeaeb/ecosystems
19:53:16 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/ad299a0eefc14088820e4c890dcaeaeb/external_downloads
19:53:16 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/ad299a0eefc14088820e4c890dcaeaeb/sbom/debug
19:53:16 [INFO] copied root sources to: /home/kali/Desktop/jobs/express/jobs/sources/root_sources
19:53:16 [INFO] RUN python3 /home/kali/Desktop/oss_checks/instruments/extract/extract.py /home/kali/Desktop/jobs/express/jobs/sources/root_sources  (cwd=/home/kali/Desktop/jobs/express/jobs/sources/root_sources)
19:53:16 [INFO] ecosystem report: /home/kali/Desktop/jobs/express/jobs/ad299a0eefc14088820e4c890dcaeaeb/ecosystems/lock_summary.json
19:53:16 [INFO] lock suggestions: 1
19:53:16 [INFO] [lock] [1/1] start: express/package.json
19:53:16 [INFO] [lock]         cmd:  cd "/home/kali/Desktop/jobs/express/jobs/sources/root_sources/express" && npm install --package-lock-only
19:53:41 [INFO] [lock] [1/1] ok (rc=0, 25.3s): express/package.json
19:53:41 [INFO] lock generation: ok=1, failed=0, skipped=0
19:53:41 [INFO] [cplus] oss_checks_dir: /home/kali/Desktop/oss_checks
19:53:41 [INFO] [cplus] cplus_scanner: /home/kali/Desktop/oss_checks/cpluschecks/scanner.py (exists=True)
19:53:41 [INFO] [cplus] cplus_known (abs): /home/kali/Desktop/jobs/express/jobs/ad299a0eefc14088820e4c890dcaeaeb/sbom/cplus_sbom.json
19:53:41 [INFO] [cplus] scanner: /home/kali/Desktop/oss_checks/cpluschecks/scanner.py
19:53:41 [INFO] [cplus] scan_root: /home/kali/Desktop/jobs/express/jobs/sources/root_sources (exists=True)
19:53:41 [INFO] [cplus] output: /home/kali/Desktop/jobs/express/jobs/ad299a0eefc14088820e4c890dcaeaeb/sbom/cplus_sbom.json
19:53:41 [INFO] [cplus] returncode: 0
19:53:41 [INFO] [cplus] stdout: [INFO] root=/home/kali/Desktop/jobs/express/jobs/sources/root_sources  checkers=94 workers=8
[INFO] candidate_files=0
[INFO] content cache ready in 0.00s
[INFO] submodule scan disabled
Scanning finished in 0.01s; total findings=0
Known SBOM written to /home/kali/Desktop/jobs/express/jobs/ad299a0eefc14088820e4c890dcaeaeb/sbom/cplus_sbom.json
Unknown SBOM written to /home/kali/Desktop/jobs/express/jobs/ad299a0eefc14088820e4c890dcaeaeb/sbom/cplus_sbom.unknown.json
19:53:41 [INFO] [cplus] output file exists: True
19:53:41 [INFO] [cplus] output file size: 307 bytes
19:53:41 [INFO] [cplus] found 0 C/C++ component(s)
[INFO] removed rust vendor dirs: 0
[INFO] renamed Cargo.lock.in files: 0
[INFO] hidden template pom.xml files: 0
19:53:41 [INFO] RUN trivy fs . --scanners license --format cyclonedx --output /home/kali/Desktop/jobs/express/jobs/ad299a0eefc14088820e4c890dcaeaeb/sbom/origsbom.json --timeout 30m  (cwd=/home/kali/Desktop/jobs/express/jobs/sources/root_sources)
2026-06-07T19:53:41+03:00	INFO	[license] License scanning is enabled
2026-06-07T19:53:41+03:00	INFO	Number of language-specific files	num=0
[INFO] restored template pom.xml files: 0
19:53:42 [WARNING] [cplus] no cplus sbom files to merge — skipping
19:53:42 [INFO] [normalize] processing: origsbom.json
19:53:42 [INFO] [normalize] origsbom.json: components 0→0, vulnerabilities 0→0, filtered=0
19:53:42 [INFO] [normalize] saved: /home/kali/Desktop/jobs/express/jobs/ad299a0eefc14088820e4c890dcaeaeb/sbom/debug/origsbom/origsbom_normalized.json
19:53:42 [INFO] [normalize] using normalized SBOM: /home/kali/Desktop/jobs/express/jobs/ad299a0eefc14088820e4c890dcaeaeb/sbom/debug/origsbom/origsbom_normalized.json
[dt] uploaded: /home/kali/Desktop/jobs/express/jobs/ad299a0eefc14088820e4c890dcaeaeb/sbom/debug/origsbom/origsbom_normalized.json (token=d0a70564-3b7c-4c12-ba14-e51a8749fba5)
[dt] origsbom uploaded to orig project: 77093aa6-2c10-4101-bed6-d7de8eb6052b
[dt] ===== enrich origsbom =====
[dt] uploaded: /home/kali/Desktop/jobs/express/jobs/ad299a0eefc14088820e4c890dcaeaeb/sbom/debug/origsbom/origsbom_normalized.json (token=4afb6494-7cb4-4832-a6f2-0420b13fd8f6)
[dt] bom/token poll 1: processing=True
[dt] bom/token poll 2: processing=False
[dt] BOM processing complete
[dt] findings poll 1: count=0, stable=0
[dt] findings poll 2: count=0, stable=0
[dt] findings poll 3: count=0, stable=1
