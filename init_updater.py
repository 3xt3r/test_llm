$ python3 sheduler.py --config config.yml
2026-06-07 19:28:32 | INFO    | GITLAB_TOKEN not set — will try anonymous clone first
2026-06-07 19:28:32 | INFO    | timeouts: scanner=3600s, distrib_scan=7200s, deptrack=3600s
2026-06-07 19:28:32 | INFO    | === product: express ===
2026-06-07 19:28:32 | INFO    | --- version: v4.22.2 ---
2026-06-07 19:28:32 | INFO    |     cloning: https://github.com/expressjs/express.git
2026-06-07 19:28:32 | INFO    |     running: git -c credential.helper= clone --no-checkout https://github.com/expressjs/express.git /home/kali/Desktop/jobs/express/_repos/express
2026-06-07 19:28:40 | INFO    |     checkout express @ v4.22.2
2026-06-07 19:28:40 | INFO    |     running: git -c credential.helper= checkout v4.22.2
2026-06-07 19:28:40 | INFO    |     v4.22.2 is a tag — skipping reset to origin/
2026-06-07 19:28:40 | INFO    |     running: git -c credential.helper= submodule update --init --recursive
2026-06-07 19:28:40 | INFO    |     linking /home/kali/Desktop/jobs/express/sources/express -> /home/kali/Desktop/jobs/express/_repos/express
2026-06-07 19:28:40 | INFO    |   running scanner on /home/kali/Desktop/jobs/express/sources (DT project: express__v4.22.2, timeout=3600s)
2026-06-07 19:28:40 | INFO    |   job_dir: /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3
2026-06-07 19:28:40 | INFO    |     running: /home/kali/Desktop/venv/bin/python3 /home/kali/Desktop/oss_checks/scanner.py /home/kali/Desktop/jobs/express/sources --apply --deptrack --dt-project-name express__v4.22.2 --env-file /home/kali/Desktop/oss_checks/.env --job-dir /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3
19:28:40 [INFO] loaded .env: /home/kali/Desktop/oss_checks/.env
19:28:40 [INFO] [dt] auto-ensuring orig project 'express__v4.22.2-orig'...
19:28:40 [INFO] [dt] reusing existing project 'express__v4.22.2-orig' -> 77093aa6-2c10-4101-bed6-d7de8eb6052b
19:28:40 [INFO] [dt] server version: 4.14.2 — parentUUID support: yes
19:28:40 [INFO] [dt] auto-ensuring safe project 'express__v4.22.2 [safe]' (parent: 77093aa6-2c10-4101-bed6-d7de8eb6052b)...
19:28:40 [INFO] [dt] reusing existing project 'express__v4.22.2 [safe]' -> 95580e40-242b-47f3-9999-435433fecf2f
19:28:40 [INFO] original root (read-only): /home/kali/Desktop/jobs/express/sources
19:28:40 [INFO] working copy:              /home/kali/Desktop/jobs/express/jobs/sources/root_sources
19:28:40 [INFO] job directory:             /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3
19:28:40 [INFO] dependency-track: enabled url=http://localhost:8081 safe_project=95580e40-242b-47f3-9999-435433fecf2f orig_project=77093aa6-2c10-4101-bed6-d7de8eb6052b insecure=True
19:28:40 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs
19:28:40 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/sources
19:28:40 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3
19:28:40 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/sbom
19:28:40 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/reports
19:28:40 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/reports/asm
19:28:40 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/ecosystems
19:28:40 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/external_downloads
19:28:40 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/sbom/debug
19:28:40 [INFO] copied root sources to: /home/kali/Desktop/jobs/express/jobs/sources/root_sources
19:28:40 [INFO] RUN python3 /home/kali/Desktop/oss_checks/instruments/extract/extract.py /home/kali/Desktop/jobs/express/jobs/sources/root_sources  (cwd=/home/kali/Desktop/jobs/express/jobs/sources/root_sources)
19:28:41 [INFO] ecosystem report: /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/ecosystems/lock_summary.json
19:28:41 [INFO] lock suggestions: 1
19:28:41 [INFO] [lock] [1/1] start: express/package.json
19:28:41 [INFO] [lock]         cmd:  cd "/home/kali/Desktop/jobs/express/jobs/sources/root_sources/express" && npm install --package-lock-only
19:29:05 [INFO] [lock] [1/1] ok (rc=0, 24.1s): express/package.json
19:29:05 [INFO] lock generation: ok=1, failed=0, skipped=0
19:29:05 [INFO] [cplus] oss_checks_dir: /home/kali/Desktop/oss_checks
19:29:05 [INFO] [cplus] cplus_scanner: /home/kali/Desktop/oss_checks/cpluschecks/scanner.py (exists=True)
19:29:05 [INFO] [cplus] cplus_known (abs): /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/sbom/cplus_sbom.json
19:29:05 [INFO] [cplus] scanner: /home/kali/Desktop/oss_checks/cpluschecks/scanner.py
19:29:05 [INFO] [cplus] scan_root: /home/kali/Desktop/jobs/express/jobs/sources/root_sources (exists=True)
19:29:05 [INFO] [cplus] output: /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/sbom/cplus_sbom.json
19:29:05 [INFO] [cplus] returncode: 0
19:29:05 [INFO] [cplus] stdout: [INFO] root=/home/kali/Desktop/jobs/express/jobs/sources/root_sources  checkers=94 workers=8
[INFO] candidate_files=0
[INFO] content cache ready in 0.00s
[INFO] submodule scan disabled
Scanning finished in 0.01s; total findings=0
Known SBOM written to /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/sbom/cplus_sbom.json
Unknown SBOM written to /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/sbom/cplus_sbom.unknown.json
19:29:05 [INFO] [cplus] output file exists: True
19:29:05 [INFO] [cplus] output file size: 307 bytes
19:29:05 [INFO] [cplus] found 0 C/C++ component(s)
[INFO] removed rust vendor dirs: 0
[INFO] renamed Cargo.lock.in files: 0
[INFO] hidden template pom.xml files: 0
19:29:05 [INFO] RUN trivy fs . --scanners license --format cyclonedx --output /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/sbom/origsbom.json --timeout 30m  (cwd=/home/kali/Desktop/jobs/express/jobs/sources/root_sources)
2026-06-07T19:29:05+03:00	INFO	[license] License scanning is enabled
2026-06-07T19:29:05+03:00	INFO	Number of language-specific files	num=0
[INFO] restored template pom.xml files: 0
19:29:05 [WARNING] [cplus] no cplus sbom files to merge — skipping
19:29:05 [INFO] [normalize] processing: origsbom.json
19:29:05 [INFO] [normalize] origsbom.json: components 0→0, vulnerabilities 0→0, filtered=0
19:29:05 [INFO] [normalize] saved: /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/sbom/debug/origsbom/origsbom_normalized.json
19:29:05 [INFO] [normalize] using normalized SBOM: /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/sbom/debug/origsbom/origsbom_normalized.json
[dt] uploaded: /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/sbom/debug/origsbom/origsbom_normalized.json (token=203757bf-826c-4290-8cb1-fa4956c45e48)
[dt] origsbom uploaded to orig project: 77093aa6-2c10-4101-bed6-d7de8eb6052b
[dt] ===== enrich origsbom =====
[dt] uploaded: /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/sbom/debug/origsbom/origsbom_normalized.json (token=12bf3ec8-a6a3-4289-9842-69f68e7ffc85)
[dt] bom/token poll 1: processing=True
[dt] bom/token poll 2: processing=False
[dt] BOM processing complete
[dt] findings poll 1: count=0, stable=0
[dt] findings poll 2: count=0, stable=0
[dt] findings poll 3: count=0, stable=1
[dt] findings poll 4: count=0, stable=2
[dt] findings stabilized
[dt] downloaded: /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/sbom/.dt-tmp-enrich.json
[dt] enriched: components=0, vulnerabilities=0 (OSV filtered: 0)
[dt] starting DT cleanup: orig_vulns=0  candidate_components=0
[dt] SBOM is empty (0 components, 0 vulnerabilities) — skipping DT cleanup rounds
[dt] uploading empty sbom-clean to safe project: 95580e40-242b-47f3-9999-435433fecf2f
[dt] uploaded: /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/sbom/sbom-clean.json (token=04bc9359-8cd7-4cdb-8ffa-a60b31f654e9)
[dt] empty sbom-clean uploaded to safe project: 95580e40-242b-47f3-9999-435433fecf2f
[OK] report.xlsx           : /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/reports/report.xlsx
[OK]   Vulnerabilities rows: 0
[OK]   SafeVersions rows   : 0
[OK] report.xlsx           : /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/reports/report.xlsx
[OK] sbom-clean.json : /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/sbom/sbom-clean.json
[OK] missing versions txt          : /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/sbom/debug/missing_versions.txt
[OK] failed debug txt              : /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/sbom/debug/failed_safe_versions_debug.txt
19:30:05 [INFO] [vuln] cplus_sbom found: /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/sbom/cplus_sbom.json
19:30:05 [INFO] external_downloads: no hits found in /home/kali/Desktop/jobs/express/jobs/sources/root_sources
19:30:05 [INFO] registry_sources: nothing found in /home/kali/Desktop/jobs/express/jobs/sources/root_sources
19:30:05 [INFO] Found 0 unique (ecosystem, name, version) entries
[bin-scan] Found 0 native binary files
[bin-scan] Skipping XLSX output (empty)
[WARN] xlsx merge: no input files found; skipping
SBOM: /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/sbom/origsbom.json
Sources dir (already downloaded): /home/kali/Desktop/jobs/express/jobs/sources/transitive_libs
Include ecosystems: ['cargo', 'composer', 'conan', 'go', 'maven', 'npm', 'nuget', 'pypi']
Loaded SBOM with 0 components and 1 dependency entries
[info] CDX dependency graph nodes: 1, roots: 1
Found 0 unique (ecosystem, name, version) entries


[OK] Wrote 0 rows to /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/reports/licenses.xlsx
19:30:05 [INFO] pipeline summary:
19:30:05 [INFO] stage prepare_root_workspace: done
19:30:05 [INFO] stage prepare_root_workspace artifact: root_sources_dir -> /home/kali/Desktop/jobs/express/jobs/sources/root_sources
19:30:05 [INFO] stage ecosystem: done
19:30:05 [INFO] stage ecosystem artifact: report -> /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/ecosystems/lock_summary.json
19:30:05 [INFO] stage cplus_scan: done
19:30:05 [INFO] stage cplus_scan artifact: cplus_sbom -> /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/sbom/cplus_sbom.json
19:30:05 [INFO] stage trivy_sbom: done
19:30:05 [INFO] stage trivy_sbom artifact: sbom -> /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/sbom/origsbom.json
19:30:05 [INFO] stage vuln_management: done
19:30:05 [INFO] stage vuln_management artifact: missing_versions_txt -> /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/sbom/debug/missing_versions.txt
19:30:05 [INFO] stage vuln_management artifact: failed_debug_txt -> /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/sbom/debug/failed_safe_versions_debug.txt
19:30:05 [INFO] stage vuln_management artifact: report_xlsx -> /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/reports/report.xlsx
19:30:05 [INFO] stage vuln_management artifact: sbom_clean -> /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/sbom/sbom-clean.json
19:30:05 [INFO] stage asm_audit_root: skipped
19:30:05 [WARNING] stage asm_audit_root: no ASM matches for /home/kali/Desktop/jobs/express/jobs/sources/root_sources
19:30:05 [INFO] stage external_downloads_root: skipped
19:30:05 [WARNING] stage external_downloads_root: no external download calls found in root sources
19:30:05 [INFO] stage registry_sources_root: skipped
19:30:05 [WARNING] stage registry_sources_root: no registry configs found in root sources
19:30:05 [INFO] stage download_sources: skipped
19:30:05 [WARNING] stage download_sources: no packages found in origsbom.json
19:30:05 [INFO] stage toxic_repos: skipped
19:30:05 [WARNING] stage toxic_repos: no manual input and no sources_downloads.csv
19:30:05 [INFO] stage prepare_transitive_workspace: skipped
19:30:05 [WARNING] stage prepare_transitive_workspace: deps_dir does not exist
19:30:05 [INFO] stage binary_scan: done
19:30:05 [WARNING] stage binary_scan: binary scan found nothing to report
19:30:05 [INFO] stage license_collection: done
19:30:05 [INFO] stage license_collection artifact: report -> /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3/reports/licenses.xlsx
19:30:05 [INFO] stage asm_audit_transitive_libs: skipped
19:30:05 [WARNING] stage asm_audit_transitive_libs: scan_root does not exist: /home/kali/Desktop/jobs/express/jobs/sources/transitive_libs
19:30:05 [INFO] stage external_downloads_transitive: skipped
19:30:05 [WARNING] stage external_downloads_transitive: deps_dir does not exist — skipping transitive ext-download scan
19:30:05 [INFO] pipeline finished successfully
19:30:05 [INFO] artifacts directory: /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3
2026-06-07 19:30:05 | INFO    |   moving results: /home/kali/Desktop/jobs/express/jobs/6897e991a6824b848bfc90995d4907c3 -> /home/kali/Desktop/results/2026-06-07/express__v4.22.2
2026-06-07 19:30:05 | INFO    |   cleaning sources workspace: /home/kali/Desktop/jobs/express/sources
2026-06-07 19:30:05 | INFO    |   [OK] express / v4.22.2 -> /home/kali/Desktop/results/2026-06-07/express__v4.22.2
2026-06-07 19:30:05 | INFO    | run log written: /home/kali/Desktop/results/2026-06-07/run.log
2026-06-07 19:30:05 | INFO    | all 1 scan(s) completed successfully
