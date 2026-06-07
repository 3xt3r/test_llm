python3 sheduler.py --config config.yml
2026-06-07 19:44:09 | INFO    | GITLAB_TOKEN not set — will try anonymous clone first
2026-06-07 19:44:09 | INFO    | timeouts: scanner=3600s, distrib_scan=7200s, deptrack=3600s
2026-06-07 19:44:09 | INFO    | === product: express ===
2026-06-07 19:44:09 | INFO    | --- version: v4.22.2 ---
2026-06-07 19:44:09 | INFO    |     repo already cloned: express — fetching
2026-06-07 19:44:09 | INFO    |     running: git -c credential.helper= remote set-url origin https://github.com/expressjs/express.git
2026-06-07 19:44:09 | INFO    |     running: git -c credential.helper= fetch --prune --all
2026-06-07 19:44:10 | INFO    |     checkout express @ v4.22.2
2026-06-07 19:44:10 | INFO    |     running: git -c credential.helper= checkout v4.22.2
2026-06-07 19:44:10 | INFO    |     v4.22.2 is a tag — skipping reset to origin/
2026-06-07 19:44:10 | INFO    |     running: git -c credential.helper= submodule update --init --recursive
2026-06-07 19:44:10 | INFO    |     linking /home/kali/Desktop/jobs/express/sources/express -> /home/kali/Desktop/jobs/express/_repos/express
2026-06-07 19:44:10 | INFO    |   running scanner on /home/kali/Desktop/jobs/express/sources (DT project: express__v4.22.2, timeout=3600s)
2026-06-07 19:44:10 | INFO    |   job_dir: /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1
2026-06-07 19:44:10 | INFO    |     running: /home/kali/Desktop/venv/bin/python3 /home/kali/Desktop/oss_checks/scanner.py /home/kali/Desktop/jobs/express/sources --apply --deptrack --dt-project-name express__v4.22.2 --env-file /home/kali/Desktop/oss_checks/.env --job-dir /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1
19:44:10 [INFO] loaded .env: /home/kali/Desktop/oss_checks/.env
19:44:10 [INFO] [dt] auto-ensuring orig project 'express__v4.22.2-orig'...
19:44:10 [INFO] [dt] reusing existing project 'express__v4.22.2-orig' -> 77093aa6-2c10-4101-bed6-d7de8eb6052b
19:44:10 [INFO] [dt] server version: 4.14.2 — parentUUID support: yes
19:44:10 [INFO] [dt] auto-ensuring safe project 'express__v4.22.2 [safe]' (parent: 77093aa6-2c10-4101-bed6-d7de8eb6052b)...
19:44:10 [INFO] [dt] reusing existing project 'express__v4.22.2 [safe]' -> 95580e40-242b-47f3-9999-435433fecf2f
19:44:10 [INFO] original root (read-only): /home/kali/Desktop/jobs/express/sources
19:44:10 [INFO] working copy:              /home/kali/Desktop/jobs/express/jobs/sources/root_sources
19:44:10 [INFO] job directory:             /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1
19:44:10 [INFO] dependency-track: enabled url=http://localhost:8081 safe_project=95580e40-242b-47f3-9999-435433fecf2f orig_project=77093aa6-2c10-4101-bed6-d7de8eb6052b insecure=True
19:44:10 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs
19:44:10 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/sources
19:44:10 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1
19:44:10 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/sbom
19:44:10 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/reports
19:44:10 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/reports/asm
19:44:10 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/ecosystems
19:44:10 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/external_downloads
19:44:10 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/sbom/debug
19:44:10 [INFO] copied root sources to: /home/kali/Desktop/jobs/express/jobs/sources/root_sources
19:44:10 [INFO] RUN python3 /home/kali/Desktop/oss_checks/instruments/extract/extract.py /home/kali/Desktop/jobs/express/jobs/sources/root_sources  (cwd=/home/kali/Desktop/jobs/express/jobs/sources/root_sources)
19:44:11 [INFO] ecosystem report: /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/ecosystems/lock_summary.json
19:44:11 [INFO] lock suggestions: 1
19:44:11 [INFO] [lock] [1/1] start: express/package.json
19:44:11 [INFO] [lock]         cmd:  cd "/home/kali/Desktop/jobs/express/jobs/sources/root_sources/express" && npm install --package-lock-only
19:44:15 [INFO] [lock] [1/1] ok (rc=0, 4.8s): express/package.json
19:44:15 [INFO] lock generation: ok=1, failed=0, skipped=0
19:44:15 [INFO] [cplus] oss_checks_dir: /home/kali/Desktop/oss_checks
19:44:15 [INFO] [cplus] cplus_scanner: /home/kali/Desktop/oss_checks/cpluschecks/scanner.py (exists=True)
19:44:15 [INFO] [cplus] cplus_known (abs): /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/sbom/cplus_sbom.json
19:44:15 [INFO] [cplus] scanner: /home/kali/Desktop/oss_checks/cpluschecks/scanner.py
19:44:15 [INFO] [cplus] scan_root: /home/kali/Desktop/jobs/express/jobs/sources/root_sources (exists=True)
19:44:15 [INFO] [cplus] output: /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/sbom/cplus_sbom.json
19:44:16 [INFO] [cplus] returncode: 0
19:44:16 [INFO] [cplus] stdout: [INFO] root=/home/kali/Desktop/jobs/express/jobs/sources/root_sources  checkers=94 workers=8
[INFO] candidate_files=0
[INFO] content cache ready in 0.00s
[INFO] submodule scan disabled
Scanning finished in 0.01s; total findings=0
Known SBOM written to /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/sbom/cplus_sbom.json
Unknown SBOM written to /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/sbom/cplus_sbom.unknown.json
19:44:16 [INFO] [cplus] output file exists: True
19:44:16 [INFO] [cplus] output file size: 307 bytes
19:44:16 [INFO] [cplus] found 0 C/C++ component(s)
[INFO] removed rust vendor dirs: 0
[INFO] renamed Cargo.lock.in files: 0
[INFO] hidden template pom.xml files: 0
19:44:16 [INFO] RUN trivy fs . --scanners license --format cyclonedx --output /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/sbom/origsbom.json --timeout 30m  (cwd=/home/kali/Desktop/jobs/express/jobs/sources/root_sources)
2026-06-07T19:44:16+03:00	INFO	[license] License scanning is enabled
2026-06-07T19:44:16+03:00	INFO	Number of language-specific files	num=0
[INFO] restored template pom.xml files: 0
19:44:16 [WARNING] [cplus] no cplus sbom files to merge — skipping
19:44:16 [INFO] [normalize] processing: origsbom.json
19:44:16 [INFO] [normalize] origsbom.json: components 0→0, vulnerabilities 0→0, filtered=0
19:44:16 [INFO] [normalize] saved: /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/sbom/debug/origsbom/origsbom_normalized.json
19:44:16 [INFO] [normalize] using normalized SBOM: /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/sbom/debug/origsbom/origsbom_normalized.json
[dt] uploaded: /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/sbom/debug/origsbom/origsbom_normalized.json (token=5e230419-3e51-4cd5-95ad-930ea1e51d9b)
[dt] origsbom uploaded to orig project: 77093aa6-2c10-4101-bed6-d7de8eb6052b
[dt] ===== enrich origsbom =====
[dt] uploaded: /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/sbom/debug/origsbom/origsbom_normalized.json (token=1dff3b17-47ff-4770-bbe8-b43664b706c6)
[dt] bom/token poll 1: processing=True
[dt] bom/token poll 2: processing=False
[dt] BOM processing complete
[dt] findings poll 1: count=0, stable=0
[dt] findings poll 2: count=0, stable=0
[dt] findings poll 3: count=0, stable=1
[dt] findings poll 4: count=0, stable=2
[dt] findings stabilized
[dt] downloaded: /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/sbom/.dt-tmp-enrich.json
[dt] enriched: components=0, vulnerabilities=0 (OSV filtered: 0)
[dt] starting DT cleanup: orig_vulns=0  candidate_components=0
[dt] SBOM is empty (0 components, 0 vulnerabilities) — skipping DT cleanup rounds
[dt] uploading empty sbom-clean to safe project: 95580e40-242b-47f3-9999-435433fecf2f
[dt] uploaded: /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/sbom/sbom-clean.json (token=13805981-6956-4a3e-a713-484d46f6cc63)
[dt] empty sbom-clean uploaded to safe project: 95580e40-242b-47f3-9999-435433fecf2f
[OK] report.xlsx           : /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/reports/report.xlsx
[OK]   Vulnerabilities rows: 0
[OK]   SafeVersions rows   : 0
[OK] report.xlsx           : /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/reports/report.xlsx
[OK] sbom-clean.json : /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/sbom/sbom-clean.json
[OK] missing versions txt          : /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/sbom/debug/missing_versions.txt
[OK] failed debug txt              : /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/sbom/debug/failed_safe_versions_debug.txt
19:45:16 [INFO] [vuln] cplus_sbom found: /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/sbom/cplus_sbom.json
19:45:16 [INFO] external_downloads: no hits found in /home/kali/Desktop/jobs/express/jobs/sources/root_sources
19:45:16 [INFO] registry_sources: nothing found in /home/kali/Desktop/jobs/express/jobs/sources/root_sources
19:45:16 [INFO] Found 0 unique (ecosystem, name, version) entries
[bin-scan] Found 0 native binary files
[bin-scan] Skipping XLSX output (empty)
[WARN] xlsx merge: no input files found; skipping
SBOM: /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/sbom/origsbom.json
Sources dir (already downloaded): /home/kali/Desktop/jobs/express/jobs/sources/transitive_libs
Include ecosystems: ['cargo', 'composer', 'conan', 'go', 'maven', 'npm', 'nuget', 'pypi']
Loaded SBOM with 0 components and 1 dependency entries
[info] CDX dependency graph nodes: 1, roots: 1
Found 0 unique (ecosystem, name, version) entries


[OK] Wrote 0 rows to /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/reports/licenses.xlsx
19:45:16 [INFO] pipeline summary:
19:45:16 [INFO] stage prepare_root_workspace: done
19:45:16 [INFO] stage prepare_root_workspace artifact: root_sources_dir -> /home/kali/Desktop/jobs/express/jobs/sources/root_sources
19:45:16 [INFO] stage ecosystem: done
19:45:16 [INFO] stage ecosystem artifact: report -> /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/ecosystems/lock_summary.json
19:45:16 [INFO] stage cplus_scan: done
19:45:16 [INFO] stage cplus_scan artifact: cplus_sbom -> /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/sbom/cplus_sbom.json
19:45:16 [INFO] stage trivy_sbom: done
19:45:16 [INFO] stage trivy_sbom artifact: sbom -> /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/sbom/origsbom.json
19:45:16 [INFO] stage vuln_management: done
19:45:16 [INFO] stage vuln_management artifact: missing_versions_txt -> /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/sbom/debug/missing_versions.txt
19:45:16 [INFO] stage vuln_management artifact: failed_debug_txt -> /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/sbom/debug/failed_safe_versions_debug.txt
19:45:16 [INFO] stage vuln_management artifact: report_xlsx -> /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/reports/report.xlsx
19:45:16 [INFO] stage vuln_management artifact: sbom_clean -> /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/sbom/sbom-clean.json
19:45:16 [INFO] stage asm_audit_root: skipped
19:45:16 [WARNING] stage asm_audit_root: no ASM matches for /home/kali/Desktop/jobs/express/jobs/sources/root_sources
19:45:16 [INFO] stage external_downloads_root: skipped
19:45:16 [WARNING] stage external_downloads_root: no external download calls found in root sources
19:45:16 [INFO] stage registry_sources_root: skipped
19:45:16 [WARNING] stage registry_sources_root: no registry configs found in root sources
19:45:16 [INFO] stage download_sources: skipped
19:45:16 [WARNING] stage download_sources: no packages found in origsbom.json
19:45:16 [INFO] stage toxic_repos: skipped
19:45:16 [WARNING] stage toxic_repos: no manual input and no sources_downloads.csv
19:45:16 [INFO] stage prepare_transitive_workspace: skipped
19:45:16 [WARNING] stage prepare_transitive_workspace: deps_dir does not exist
19:45:16 [INFO] stage binary_scan: done
19:45:16 [WARNING] stage binary_scan: binary scan found nothing to report
19:45:16 [INFO] stage license_collection: done
19:45:16 [INFO] stage license_collection artifact: report -> /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1/reports/licenses.xlsx
19:45:16 [INFO] stage asm_audit_transitive_libs: skipped
19:45:16 [WARNING] stage asm_audit_transitive_libs: scan_root does not exist: /home/kali/Desktop/jobs/express/jobs/sources/transitive_libs
19:45:16 [INFO] stage external_downloads_transitive: skipped
19:45:16 [WARNING] stage external_downloads_transitive: deps_dir does not exist — skipping transitive ext-download scan
19:45:16 [INFO] pipeline finished successfully
19:45:16 [INFO] artifacts directory: /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1
2026-06-07 19:45:16 | INFO    |   moving results: /home/kali/Desktop/jobs/express/jobs/bf09416b1c2a40ae87c9b3d6f2488ae1 -> /home/kali/Desktop/results/2026-06-07/express__v4.22.2
2026-06-07 19:45:16 | INFO    |   cleaning sources workspace: /home/kali/Desktop/jobs/express/sources
2026-06-07 19:45:16 | INFO    |   [OK] express / v4.22.2 -> /home/kali/Desktop/results/2026-06-07/express__v4.22.2
2026-06-07 19:45:16 | INFO    | === product: flask ===
2026-06-07 19:45:16 | INFO    | --- version: 3.1.3 ---
2026-06-07 19:45:16 | INFO    |     cloning: https://github.com/pallets/flask.git
2026-06-07 19:45:16 | INFO    |     running: git -c credential.helper= clone --no-checkout https://github.com/pallets/flask.git /home/kali/Desktop/jobs/flask/_repos/flask
2026-06-07 19:45:26 | INFO    |     checkout flask @ 3.1.3
2026-06-07 19:45:26 | INFO    |     running: git -c credential.helper= checkout 3.1.3
2026-06-07 19:45:26 | INFO    |     3.1.3 is a tag — skipping reset to origin/
2026-06-07 19:45:26 | INFO    |     running: git -c credential.helper= submodule update --init --recursive
2026-06-07 19:45:26 | INFO    |     linking /home/kali/Desktop/jobs/flask/sources/flask -> /home/kali/Desktop/jobs/flask/_repos/flask
2026-06-07 19:45:26 | INFO    |   running scanner on /home/kali/Desktop/jobs/flask/sources (DT project: flask__3.1.3, timeout=3600s)
2026-06-07 19:45:26 | INFO    |   job_dir: /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5
2026-06-07 19:45:26 | INFO    |     running: /home/kali/Desktop/venv/bin/python3 /home/kali/Desktop/oss_checks/scanner.py /home/kali/Desktop/jobs/flask/sources --apply --deptrack --dt-project-name flask__3.1.3 --env-file /home/kali/Desktop/oss_checks/.env --job-dir /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5
19:45:26 [INFO] loaded .env: /home/kali/Desktop/oss_checks/.env
19:45:26 [INFO] [dt] auto-ensuring orig project 'flask__3.1.3-orig'...
19:45:26 [INFO] [dt] reusing existing project 'flask__3.1.3-orig' -> 01d591ed-8eb6-4f3d-bd70-e09c7622dfcb
19:45:26 [INFO] [dt] server version: 4.14.2 — parentUUID support: yes
19:45:26 [INFO] [dt] auto-ensuring safe project 'flask__3.1.3 [safe]' (parent: 01d591ed-8eb6-4f3d-bd70-e09c7622dfcb)...
19:45:26 [INFO] [dt] reusing existing project 'flask__3.1.3 [safe]' -> 7a6c5d37-f594-4c47-ba28-8f191bb6ed7f
19:45:26 [INFO] original root (read-only): /home/kali/Desktop/jobs/flask/sources
19:45:26 [INFO] working copy:              /home/kali/Desktop/jobs/flask/jobs/sources/root_sources
19:45:26 [INFO] job directory:             /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5
19:45:26 [INFO] dependency-track: enabled url=http://localhost:8081 safe_project=7a6c5d37-f594-4c47-ba28-8f191bb6ed7f orig_project=01d591ed-8eb6-4f3d-bd70-e09c7622dfcb insecure=True
19:45:26 [INFO] created directory: /home/kali/Desktop/jobs/flask/jobs
19:45:26 [INFO] created directory: /home/kali/Desktop/jobs/flask/jobs/sources
19:45:26 [INFO] created directory: /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5
19:45:26 [INFO] created directory: /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/sbom
19:45:26 [INFO] created directory: /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/reports
19:45:26 [INFO] created directory: /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/reports/asm
19:45:26 [INFO] created directory: /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/ecosystems
19:45:26 [INFO] created directory: /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/external_downloads
19:45:26 [INFO] created directory: /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/sbom/debug
19:45:26 [INFO] copied root sources to: /home/kali/Desktop/jobs/flask/jobs/sources/root_sources
19:45:26 [INFO] RUN python3 /home/kali/Desktop/oss_checks/instruments/extract/extract.py /home/kali/Desktop/jobs/flask/jobs/sources/root_sources  (cwd=/home/kali/Desktop/jobs/flask/jobs/sources/root_sources)
19:45:26 [INFO] ecosystem report: /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/ecosystems/lock_summary.json
19:45:26 [INFO] lock suggestions: 1
19:45:26 [INFO] [lock] [1/1] start: flask/pyproject.toml
19:45:26 [INFO] [lock]         cmd:  cd "/home/kali/Desktop/jobs/flask/jobs/sources/root_sources/flask" && uv lock
19:45:26 [INFO] [lock] [1/1] failed (rc=127, 0.0s): flask/pyproject.toml
19:45:26 [WARNING] [lock]         stderr: /bin/sh: 1: uv: not found
19:45:26 [INFO] lock generation: ok=0, failed=1, skipped=0
19:45:26 [INFO] [cplus] oss_checks_dir: /home/kali/Desktop/oss_checks
19:45:26 [INFO] [cplus] cplus_scanner: /home/kali/Desktop/oss_checks/cpluschecks/scanner.py (exists=True)
19:45:26 [INFO] [cplus] cplus_known (abs): /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/sbom/cplus_sbom.json
19:45:26 [INFO] [cplus] scanner: /home/kali/Desktop/oss_checks/cpluschecks/scanner.py
19:45:26 [INFO] [cplus] scan_root: /home/kali/Desktop/jobs/flask/jobs/sources/root_sources (exists=True)
19:45:26 [INFO] [cplus] output: /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/sbom/cplus_sbom.json
19:45:27 [INFO] [cplus] returncode: 0
19:45:27 [INFO] [cplus] stdout: [INFO] root=/home/kali/Desktop/jobs/flask/jobs/sources/root_sources  checkers=94 workers=8
[INFO] candidate_files=0
[INFO] content cache ready in 0.00s
[INFO] submodule scan disabled
Scanning finished in 0.01s; total findings=0
Known SBOM written to /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/sbom/cplus_sbom.json
Unknown SBOM written to /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/sbom/cplus_sbom.unknown.json
19:45:27 [INFO] [cplus] output file exists: True
19:45:27 [INFO] [cplus] output file size: 307 bytes
19:45:27 [INFO] [cplus] found 0 C/C++ component(s)
[INFO] removed rust vendor dirs: 0
[INFO] renamed Cargo.lock.in files: 0
[INFO] hidden template pom.xml files: 0
19:45:27 [INFO] RUN trivy fs . --scanners license --format cyclonedx --output /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/sbom/origsbom.json --timeout 30m  (cwd=/home/kali/Desktop/jobs/flask/jobs/sources/root_sources)
2026-06-07T19:45:27+03:00	INFO	[license] License scanning is enabled
2026-06-07T19:45:27+03:00	INFO	Number of language-specific files	num=0
[INFO] restored template pom.xml files: 0
19:45:27 [WARNING] [cplus] no cplus sbom files to merge — skipping
19:45:27 [INFO] [normalize] processing: origsbom.json
19:45:27 [INFO] [normalize] origsbom.json: components 0→0, vulnerabilities 0→0, filtered=0
19:45:27 [INFO] [normalize] saved: /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/sbom/debug/origsbom/origsbom_normalized.json
19:45:27 [INFO] [normalize] using normalized SBOM: /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/sbom/debug/origsbom/origsbom_normalized.json
[dt] uploaded: /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/sbom/debug/origsbom/origsbom_normalized.json (token=956f2e7b-a143-4f1f-909b-794fd1cbe380)
[dt] origsbom uploaded to orig project: 01d591ed-8eb6-4f3d-bd70-e09c7622dfcb
[dt] ===== enrich origsbom =====
[dt] uploaded: /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/sbom/debug/origsbom/origsbom_normalized.json (token=411ad65a-c53e-45e1-9cfd-dbd9fcd3aaa8)
[dt] bom/token poll 1: processing=True
[dt] bom/token poll 2: processing=False
[dt] BOM processing complete
[dt] findings poll 1: count=0, stable=0
[dt] findings poll 2: count=0, stable=0
[dt] findings poll 3: count=0, stable=1
[dt] findings poll 4: count=0, stable=2
[dt] findings stabilized
[dt] downloaded: /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/sbom/.dt-tmp-enrich.json
[dt] enriched: components=0, vulnerabilities=0 (OSV filtered: 0)
[dt] starting DT cleanup: orig_vulns=0  candidate_components=0
[dt] SBOM is empty (0 components, 0 vulnerabilities) — skipping DT cleanup rounds
[dt] uploading empty sbom-clean to safe project: 7a6c5d37-f594-4c47-ba28-8f191bb6ed7f
[dt] uploaded: /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/sbom/sbom-clean.json (token=b9b41989-5868-4280-bc30-bb6a241630fe)
[dt] empty sbom-clean uploaded to safe project: 7a6c5d37-f594-4c47-ba28-8f191bb6ed7f
[OK] report.xlsx           : /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/reports/report.xlsx
[OK]   Vulnerabilities rows: 0
[OK]   SafeVersions rows   : 0
[OK] report.xlsx           : /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/reports/report.xlsx
[OK] sbom-clean.json : /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/sbom/sbom-clean.json
[OK] missing versions txt          : /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/sbom/debug/missing_versions.txt
[OK] failed debug txt              : /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/sbom/debug/failed_safe_versions_debug.txt
19:46:27 [INFO] [vuln] cplus_sbom found: /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/sbom/cplus_sbom.json
19:46:27 [INFO] external_downloads: no hits found in /home/kali/Desktop/jobs/flask/jobs/sources/root_sources
19:46:27 [INFO] registry_sources: nothing found in /home/kali/Desktop/jobs/flask/jobs/sources/root_sources
19:46:27 [INFO] Found 0 unique (ecosystem, name, version) entries
[bin-scan] Found 0 native binary files
[bin-scan] Skipping XLSX output (empty)
[WARN] xlsx merge: no input files found; skipping
SBOM: /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/sbom/origsbom.json
Sources dir (already downloaded): /home/kali/Desktop/jobs/flask/jobs/sources/transitive_libs
Include ecosystems: ['cargo', 'composer', 'conan', 'go', 'maven', 'npm', 'nuget', 'pypi']
Loaded SBOM with 0 components and 1 dependency entries
[info] CDX dependency graph nodes: 1, roots: 1
Found 0 unique (ecosystem, name, version) entries


[OK] Wrote 0 rows to /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/reports/licenses.xlsx
19:46:27 [INFO] pipeline summary:
19:46:27 [INFO] stage prepare_root_workspace: done
19:46:27 [INFO] stage prepare_root_workspace artifact: root_sources_dir -> /home/kali/Desktop/jobs/flask/jobs/sources/root_sources
19:46:27 [INFO] stage ecosystem: done
19:46:27 [INFO] stage ecosystem artifact: report -> /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/ecosystems/lock_summary.json
19:46:27 [WARNING] stage ecosystem: lock generation had failures: ok=0, failed=1, skipped=0
19:46:27 [INFO] stage cplus_scan: done
19:46:27 [INFO] stage cplus_scan artifact: cplus_sbom -> /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/sbom/cplus_sbom.json
19:46:27 [INFO] stage trivy_sbom: done
19:46:27 [INFO] stage trivy_sbom artifact: sbom -> /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/sbom/origsbom.json
19:46:27 [INFO] stage vuln_management: done
19:46:27 [INFO] stage vuln_management artifact: missing_versions_txt -> /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/sbom/debug/missing_versions.txt
19:46:27 [INFO] stage vuln_management artifact: failed_debug_txt -> /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/sbom/debug/failed_safe_versions_debug.txt
19:46:27 [INFO] stage vuln_management artifact: report_xlsx -> /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/reports/report.xlsx
19:46:27 [INFO] stage vuln_management artifact: sbom_clean -> /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/sbom/sbom-clean.json
19:46:27 [INFO] stage asm_audit_root: skipped
19:46:27 [WARNING] stage asm_audit_root: no ASM matches for /home/kali/Desktop/jobs/flask/jobs/sources/root_sources
19:46:27 [INFO] stage external_downloads_root: skipped
19:46:27 [WARNING] stage external_downloads_root: no external download calls found in root sources
19:46:27 [INFO] stage registry_sources_root: skipped
19:46:27 [WARNING] stage registry_sources_root: no registry configs found in root sources
19:46:27 [INFO] stage download_sources: skipped
19:46:27 [WARNING] stage download_sources: no packages found in origsbom.json
19:46:27 [INFO] stage toxic_repos: skipped
19:46:27 [WARNING] stage toxic_repos: no manual input and no sources_downloads.csv
19:46:27 [INFO] stage prepare_transitive_workspace: skipped
19:46:27 [WARNING] stage prepare_transitive_workspace: deps_dir does not exist
19:46:27 [INFO] stage binary_scan: done
19:46:27 [WARNING] stage binary_scan: binary scan found nothing to report
19:46:27 [INFO] stage license_collection: done
19:46:27 [INFO] stage license_collection artifact: report -> /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5/reports/licenses.xlsx
19:46:27 [INFO] stage asm_audit_transitive_libs: skipped
19:46:27 [WARNING] stage asm_audit_transitive_libs: scan_root does not exist: /home/kali/Desktop/jobs/flask/jobs/sources/transitive_libs
19:46:27 [INFO] stage external_downloads_transitive: skipped
19:46:27 [WARNING] stage external_downloads_transitive: deps_dir does not exist — skipping transitive ext-download scan
19:46:27 [INFO] pipeline finished successfully
19:46:27 [INFO] artifacts directory: /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5
2026-06-07 19:46:27 | INFO    |   moving results: /home/kali/Desktop/jobs/flask/jobs/152b6de973204f0daf1b20db4e05b3e5 -> /home/kali/Desktop/results/2026-06-07/flask__3.1.3
2026-06-07 19:46:27 | INFO    |   cleaning sources workspace: /home/kali/Desktop/jobs/flask/sources
2026-06-07 19:46:27 | INFO    |   [OK] flask / 3.1.3 -> /home/kali/Desktop/results/2026-06-07/flask__3.1.3
2026-06-07 19:46:27 | INFO    | === product: ripgrep ===
2026-06-07 19:46:27 | INFO    | --- version: 15.1.0 ---
2026-06-07 19:46:27 | INFO    |     cloning: https://github.com/BurntSushi/ripgrep.git
2026-06-07 19:46:27 | INFO    |     running: git -c credential.helper= clone --no-checkout https://github.com/BurntSushi/ripgrep.git /home/kali/Desktop/jobs/ripgrep/_repos/ripgrep
2026-06-07 19:46:32 | INFO    |     checkout ripgrep @ 15.1.0
2026-06-07 19:46:32 | INFO    |     running: git -c credential.helper= checkout 15.1.0
2026-06-07 19:46:32 | INFO    |     15.1.0 is a tag — skipping reset to origin/
2026-06-07 19:46:32 | INFO    |     running: git -c credential.helper= submodule update --init --recursive
2026-06-07 19:46:32 | INFO    |     linking /home/kali/Desktop/jobs/ripgrep/sources/ripgrep -> /home/kali/Desktop/jobs/ripgrep/_repos/ripgrep
2026-06-07 19:46:32 | INFO    |   running scanner on /home/kali/Desktop/jobs/ripgrep/sources (DT project: ripgrep__15.1.0, timeout=3600s)
2026-06-07 19:46:32 | INFO    |   job_dir: /home/kali/Desktop/jobs/ripgrep/jobs/af9621cb442143a6924f9ba14fdd6781
2026-06-07 19:46:32 | INFO    |     running: /home/kali/Desktop/venv/bin/python3 /home/kali/Desktop/oss_checks/scanner.py /home/kali/Desktop/jobs/ripgrep/sources --apply --deptrack --dt-project-name ripgrep__15.1.0 --env-file /home/kali/Desktop/oss_checks/.env --job-dir /home/kali/Desktop/jobs/ripgrep/jobs/af9621cb442143a6924f9ba14fdd6781
19:46:33 [INFO] loaded .env: /home/kali/Desktop/oss_checks/.env
19:46:33 [INFO] [dt] auto-ensuring orig project 'ripgrep__15.1.0-orig'...
19:46:33 [INFO] [dt] reusing existing project 'ripgrep__15.1.0-orig' -> 6e7fa2b5-fde8-41b8-a7e4-078f6232bbf5
19:46:33 [INFO] [dt] server version: 4.14.2 — parentUUID support: yes
19:46:33 [INFO] [dt] auto-ensuring safe project 'ripgrep__15.1.0 [safe]' (parent: 6e7fa2b5-fde8-41b8-a7e4-078f6232bbf5)...
19:46:33 [INFO] [dt] reusing existing project 'ripgrep__15.1.0 [safe]' -> d138ed93-3543-4db6-a699-1c7b7f26ef73
19:46:33 [INFO] original root (read-only): /home/kali/Desktop/jobs/ripgrep/sources
19:46:33 [INFO] working copy:              /home/kali/Desktop/jobs/ripgrep/jobs/sources/root_sources
19:46:33 [INFO] job directory:             /home/kali/Desktop/jobs/ripgrep/jobs/af9621cb442143a6924f9ba14fdd6781
19:46:33 [INFO] dependency-track: enabled url=http://localhost:8081 safe_project=d138ed93-3543-4db6-a699-1c7b7f26ef73 orig_project=6e7fa2b5-fde8-41b8-a7e4-078f6232bbf5 insecure=True
19:46:33 [INFO] created directory: /home/kali/Desktop/jobs/ripgrep/jobs
19:46:33 [INFO] created directory: /home/kali/Desktop/jobs/ripgrep/jobs/sources
19:46:33 [INFO] created directory: /home/kali/Desktop/jobs/ripgrep/jobs/af9621cb442143a6924f9ba14fdd6781
19:46:33 [INFO] created directory: /home/kali/Desktop/jobs/ripgrep/jobs/af9621cb442143a6924f9ba14fdd6781/sbom
19:46:33 [INFO] created directory: /home/kali/Desktop/jobs/ripgrep/jobs/af9621cb442143a6924f9ba14fdd6781/reports
19:46:33 [INFO] created directory: /home/kali/Desktop/jobs/ripgrep/jobs/af9621cb442143a6924f9ba14fdd6781/reports/asm
19:46:33 [INFO] created directory: /home/kali/Desktop/jobs/ripgrep/jobs/af9621cb442143a6924f9ba14fdd6781/ecosystems
19:46:33 [INFO] created directory: /home/kali/Desktop/jobs/ripgrep/jobs/af9621cb442143a6924f9ba14fdd6781/external_downloads
19:46:33 [INFO] created directory: /home/kali/Desktop/jobs/ripgrep/jobs/af9621cb442143a6924f9ba14fdd6781/sbom/debug
19:46:33 [INFO] copied root sources to: /home/kali/Desktop/jobs/ripgrep/jobs/sources/root_sources
19:46:33 [INFO] RUN python3 /home/kali/Desktop/oss_checks/instruments/extract/extract.py /home/kali/Desktop/jobs/ripgrep/jobs/sources/root_sources  (cwd=/home/kali/Desktop/jobs/ripgrep/jobs/sources/root_sources)
19:46:33 [INFO] ecosystem report: /home/kali/Desktop/jobs/ripgrep/jobs/af9621cb442143a6924f9ba14fdd6781/ecosystems/lock_summary.json
19:46:33 [INFO] lock suggestions: 11
19:46:33 [INFO] [lock] [1/11] start: ripgrep/Cargo.toml
19:46:33 [INFO] [lock]         cmd:  cd "/home/kali/Desktop/jobs/ripgrep/jobs/sources/root_sources/ripgrep" && cargo generate-lockfile
19:46:33 [INFO] [lock] [1/11] failed (rc=101, 0.1s): ripgrep/Cargo.toml
19:46:33 [WARNING] [lock]         stderr: error: failed to parse manifest at `/home/kali/Desktop/jobs/ripgrep/_repos/ripgrep/Cargo.toml`

Caused by:
  feature `edition2024` is required

  The package requires the Cargo feature called `edition2024`, but that feature is not stabilized in this version of Cargo (1.75.0).
  Consider adding `cargo-features = ["edition2024"]` to the top of Cargo.toml (above the [package] table) to tell Cargo you are opting in to use this unstable feature.
  See https://doc.rust-lang.org/nightly/cargo/reference/unstable.html#edition-2024 for more information about the status of this feature.
19:46:33 [INFO] [lock] [2/11] start: ripgrep/crates/grep/Cargo.toml
19:46:33 [INFO] [lock]         cmd:  cd "/home/kali/Desktop/jobs/ripgrep/jobs/sources/root_sources/ripgrep/crates/grep" && cargo generate-lockfile
19:46:33 [INFO] [lock] [2/11] failed (rc=101, 0.1s): ripgrep/crates/grep/Cargo.toml
19:46:33 [WARNING] [lock]         stderr: error: failed to parse manifest at `/home/kali/Desktop/jobs/ripgrep/_repos/ripgrep/crates/grep/Cargo.toml`

Caused by:
