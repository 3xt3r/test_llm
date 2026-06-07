python3 sheduler.py --config config.yml
2026-06-07 16:51:23 | INFO    | GITLAB_TOKEN not set — will try anonymous clone first
2026-06-07 16:51:23 | INFO    | timeouts: scanner=3600s, distrib_scan=7200s, deptrack=3600s
2026-06-07 16:51:23 | INFO    | === product: express ===
2026-06-07 16:51:23 | INFO    | --- version: v4.22.2 ---
2026-06-07 16:51:23 | INFO    |   removing previous sources workspace: /home/kali/Desktop/jobs/express/sources
2026-06-07 16:51:23 | INFO    |     repo already cloned: express — fetching
2026-06-07 16:51:23 | INFO    |     running: git -c credential.helper= remote set-url origin https://github.com/expressjs/express.git
2026-06-07 16:51:23 | INFO    |     running: git -c credential.helper= fetch --prune --all
2026-06-07 16:51:24 | INFO    |     checkout express @ v4.22.2
2026-06-07 16:51:24 | INFO    |     running: git -c credential.helper= checkout v4.22.2
2026-06-07 16:51:24 | INFO    |     v4.22.2 is a tag — skipping reset to origin/
2026-06-07 16:51:24 | INFO    |     running: git -c credential.helper= submodule update --init --recursive
2026-06-07 16:51:24 | INFO    |     linking /home/kali/Desktop/jobs/express/sources/express -> /home/kali/Desktop/jobs/express/_repos/express
2026-06-07 16:51:24 | INFO    |   running scanner on /home/kali/Desktop/jobs/express/sources (DT project: express__v4.22.2, timeout=3600s)
2026-06-07 16:51:24 | INFO    |   job_dir: /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd
2026-06-07 16:51:24 | INFO    |     running: /home/kali/Desktop/venv/bin/python3 /home/kali/Desktop/oss_checks/scanner.py /home/kali/Desktop/jobs/express/sources --apply --deptrack --dt-project-name express__v4.22.2 --env-file /home/kali/Desktop/oss_checks/.env --job-dir /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd
16:51:25 [INFO] loaded .env: /home/kali/Desktop/oss_checks/.env
16:51:25 [INFO] [dt] auto-ensuring orig project 'express__v4.22.2-orig'...
16:51:25 [INFO] [dt] reusing existing project 'express__v4.22.2-orig' -> 77093aa6-2c10-4101-bed6-d7de8eb6052b
16:51:25 [INFO] [dt] server version: 4.14.2 — parentUUID support: yes
16:51:25 [INFO] [dt] auto-ensuring safe project 'express__v4.22.2 [safe]' (parent: 77093aa6-2c10-4101-bed6-d7de8eb6052b)...
16:51:25 [INFO] [dt] reusing existing project 'express__v4.22.2 [safe]' -> 95580e40-242b-47f3-9999-435433fecf2f
16:51:25 [INFO] original root (read-only): /home/kali/Desktop/jobs/express/sources
16:51:25 [INFO] working copy:              /home/kali/Desktop/jobs/express/jobs/sources/root_sources
16:51:25 [INFO] job directory:             /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd
16:51:25 [INFO] dependency-track: enabled url=http://localhost:8081 safe_project=95580e40-242b-47f3-9999-435433fecf2f orig_project=77093aa6-2c10-4101-bed6-d7de8eb6052b insecure=True
16:51:25 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs
16:51:25 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/sources
16:51:25 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd
16:51:25 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/sbom
16:51:25 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/reports
16:51:25 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/reports/asm
16:51:25 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/ecosystems
16:51:25 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/external_downloads
16:51:25 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/sbom/debug
16:51:25 [INFO] copied root sources to: /home/kali/Desktop/jobs/express/jobs/sources/root_sources
16:51:25 [INFO] RUN python3 /home/kali/Desktop/oss_checks/instruments/extract/extract.py /home/kali/Desktop/jobs/express/jobs/sources/root_sources  (cwd=/home/kali/Desktop/jobs/express/jobs/sources/root_sources)
16:51:25 [INFO] ecosystem report: /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/ecosystems/lock_summary.json
16:51:25 [INFO] lock suggestions: 0
16:51:25 [INFO] lock generation: ok=0, failed=0, skipped=0
16:51:25 [INFO] [cplus] oss_checks_dir: /home/kali/Desktop/oss_checks
16:51:25 [INFO] [cplus] cplus_scanner: /home/kali/Desktop/oss_checks/cpluschecks/scanner.py (exists=True)
16:51:25 [INFO] [cplus] cplus_known (abs): /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/sbom/cplus_sbom.json
16:51:25 [INFO] [cplus] scanner: /home/kali/Desktop/oss_checks/cpluschecks/scanner.py
16:51:25 [INFO] [cplus] scan_root: /home/kali/Desktop/jobs/express/jobs/sources/root_sources (exists=True)
16:51:25 [INFO] [cplus] output: /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/sbom/cplus_sbom.json
16:51:25 [INFO] [cplus] returncode: 0
16:51:25 [INFO] [cplus] stdout: [INFO] root=/home/kali/Desktop/jobs/express/jobs/sources/root_sources  checkers=94 workers=8
[INFO] candidate_files=0
[INFO] content cache ready in 0.00s
[INFO] submodule scan disabled
Scanning finished in 0.01s; total findings=0
Known SBOM written to /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/sbom/cplus_sbom.json
Unknown SBOM written to /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/sbom/cplus_sbom.unknown.json
16:51:25 [INFO] [cplus] output file exists: True
16:51:25 [INFO] [cplus] output file size: 307 bytes
16:51:25 [INFO] [cplus] found 0 C/C++ component(s)
[INFO] removed rust vendor dirs: 0
[INFO] renamed Cargo.lock.in files: 0
[INFO] hidden template pom.xml files: 0
16:51:25 [INFO] RUN trivy fs . --scanners license --format cyclonedx --output /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/sbom/origsbom.json --timeout 30m  (cwd=/home/kali/Desktop/jobs/express/jobs/sources/root_sources)
2026-06-07T16:51:25+03:00	INFO	[license] License scanning is enabled
2026-06-07T16:51:25+03:00	INFO	Number of language-specific files	num=0
[INFO] restored template pom.xml files: 0
16:51:25 [WARNING] [cplus] no cplus sbom files to merge — skipping
16:51:25 [INFO] [normalize] processing: origsbom.json
16:51:25 [INFO] [normalize] origsbom.json: components 0→0, vulnerabilities 0→0, filtered=0
16:51:25 [INFO] [normalize] saved: /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/sbom/debug/origsbom/origsbom_normalized.json
16:51:25 [INFO] [normalize] using normalized SBOM: /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/sbom/debug/origsbom/origsbom_normalized.json
[dt] uploaded: /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/sbom/debug/origsbom/origsbom_normalized.json (token=00f7ec8d-d7ea-4729-ba89-01c0ad77331f)
[dt] origsbom uploaded to orig project: 77093aa6-2c10-4101-bed6-d7de8eb6052b
[dt] ===== enrich origsbom =====
[dt] uploaded: /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/sbom/debug/origsbom/origsbom_normalized.json (token=660413df-a3b6-4f0f-9a9b-1e8ec784497c)
[dt] bom/token poll 1: processing=True
[dt] bom/token poll 2: processing=False
[dt] BOM processing complete
[dt] findings poll 1: count=0, stable=0
[dt] findings poll 2: count=0, stable=0
[dt] findings poll 3: count=0, stable=1
[dt] findings poll 4: count=0, stable=2
[dt] findings stabilized
[dt] downloaded: /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/sbom/.dt-tmp-enrich.json
[dt] enriched: components=0, vulnerabilities=0 (OSV filtered: 0)
[dt] starting DT cleanup: orig_vulns=0  candidate_components=0
[dt] ===== round: round1 =====
[dt] uploaded: /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/sbom/sbom-clean.json (token=c7a50164-27bc-44a2-848b-16479d06e5f4)
[dt] bom/token poll 1: processing=True
[dt] bom/token poll 2: processing=False
[dt] BOM processing complete
[dt] findings poll 1: count=0, stable=0
[dt] findings poll 2: count=0, stable=0
[dt] findings poll 3: count=0, stable=1
[dt] findings poll 4: count=0, stable=2
[dt] findings stabilized
[dt] downloaded: /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/sbom/.dt-tmp-round1.json
[dt] round=round1 components=0; vulnerabilities=0
[dt] remove_vulnerable: vulns=0  affects=0  matched_by_ref=0  matched_by_purl=0  matched_as_purl_ref=0  bad_purls=0  bad_name_ver=0
[dt] round1: vulns_in_candidates=0  components_remaining=0  removed=0
[dt] ===== round: round2 =====
[dt] uploaded: /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/sbom/sbom-clean.json (token=377a373a-bdf1-416b-b4ff-45e3029994e8)
[dt] bom/token poll 1: processing=True
[dt] bom/token poll 2: processing=False
[dt] BOM processing complete
[dt] findings poll 1: count=0, stable=0
[dt] findings poll 2: count=0, stable=0
[dt] findings poll 3: count=0, stable=1
[dt] findings poll 4: count=0, stable=2
[dt] findings stabilized
[dt] downloaded: /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/sbom/.dt-tmp-round2.json
[dt] round=round2 components=0; vulnerabilities=0
[dt] remove_vulnerable: vulns=0  affects=0  matched_by_ref=0  matched_by_purl=0  matched_as_purl_ref=0  bad_purls=0  bad_name_ver=0
[dt] round2: vulns_in_candidates=0  components_remaining=0  removed=0
[dt] clean after round2: 0 safe component(s), 0 vulnerabilities
[dt] fallback: no additional components found
[dt] SUMMARY: orig_vulns=0  candidates_sent=0  final_safe_components=0  missed_packages=0
[generic] C/C++ components found in enriched SBOM: 0
[dt] uploading final combined SBOM to safe project: 95580e40-242b-47f3-9999-435433fecf2f
[dt] uploaded: /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/sbom/sbom-clean.json (token=96346239-96f6-42e1-aa76-f93ac3382903)
[dt] no token received, skipping BOM processing wait
[dt] findings poll 1: count=0, stable=0
[dt] findings poll 2: count=0, stable=0
[dt] findings poll 3: count=0, stable=1
[dt] findings poll 4: count=0, stable=2
[dt] findings stabilized
[dt] final combined SBOM uploaded to safe project: 95580e40-242b-47f3-9999-435433fecf2f
[dt] ===== round: final =====
[dt] uploaded: /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/sbom/sbom-clean.json (token=975886b7-a4de-4617-b42d-5313c0b813c7)
[dt] bom/token poll 1: processing=True
[dt] bom/token poll 2: processing=False
[dt] BOM processing complete
[dt] findings poll 1: count=0, stable=0
[dt] findings poll 2: count=0, stable=0
[dt] findings poll 3: count=0, stable=1
[dt] findings poll 4: count=0, stable=2
[dt] findings stabilized
[dt] downloaded: /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/sbom/.dt-tmp-final.json
[dt] round=final components=0; vulnerabilities=0
[dt] remove_vulnerable: vulns=0  affects=0  matched_by_ref=0  matched_by_purl=0  matched_as_purl_ref=0  bad_purls=0  bad_name_ver=0
[dt] final round: vulns_found=0  components_after_cleanup=0
[dt] uploading cleaned combined SBOM to safe project: 95580e40-242b-47f3-9999-435433fecf2f
[dt] uploaded: /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/sbom/sbom-clean.json (token=680f34c0-88ea-4c94-aec0-70869a207094)
[dt] final cleaned SBOM uploaded to safe project: 95580e40-242b-47f3-9999-435433fecf2f
[OK] report.xlsx           : /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/reports/report.xlsx
[OK]   Vulnerabilities rows: 0
[OK]   SafeVersions rows   : 0
[OK] sbom-clean.json : /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/sbom/sbom-clean.json
[OK] missing versions txt          : /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/sbom/debug/missing_versions.txt
[OK] failed debug txt              : /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/sbom/debug/failed_safe_versions_debug.txt
16:56:11 [INFO] [vuln] cplus_sbom found: /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/sbom/cplus_sbom.json
16:56:11 [INFO] external_downloads: no hits found in /home/kali/Desktop/jobs/express/jobs/sources/root_sources
16:56:11 [INFO] registry_sources: nothing found in /home/kali/Desktop/jobs/express/jobs/sources/root_sources
16:56:11 [INFO] Found 0 unique (ecosystem, name, version) entries
[bin-scan] Found 0 native binary files
[bin-scan] Skipping XLSX output (empty)
[WARN] xlsx merge: no input files found; skipping
SBOM: /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/sbom/origsbom.json
Sources dir (already downloaded): /home/kali/Desktop/jobs/express/jobs/sources/transitive_libs
Include ecosystems: ['cargo', 'composer', 'conan', 'go', 'maven', 'npm', 'nuget', 'pypi']
Loaded SBOM with 0 components and 1 dependency entries
[info] CDX dependency graph nodes: 1, roots: 1
Found 0 unique (ecosystem, name, version) entries


[OK] Wrote 0 rows to /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/reports/licenses.xlsx
16:56:11 [INFO] pipeline summary:
16:56:11 [INFO] stage prepare_root_workspace: done
16:56:11 [INFO] stage prepare_root_workspace artifact: root_sources_dir -> /home/kali/Desktop/jobs/express/jobs/sources/root_sources
16:56:11 [INFO] stage ecosystem: done
16:56:11 [INFO] stage ecosystem artifact: report -> /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/ecosystems/lock_summary.json
16:56:11 [INFO] stage cplus_scan: done
16:56:11 [INFO] stage cplus_scan artifact: cplus_sbom -> /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/sbom/cplus_sbom.json
16:56:11 [INFO] stage trivy_sbom: done
16:56:11 [INFO] stage trivy_sbom artifact: sbom -> /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/sbom/origsbom.json
16:56:11 [INFO] stage vuln_management: done
16:56:11 [INFO] stage vuln_management artifact: missing_versions_txt -> /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/sbom/debug/missing_versions.txt
16:56:11 [INFO] stage vuln_management artifact: failed_debug_txt -> /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/sbom/debug/failed_safe_versions_debug.txt
16:56:11 [INFO] stage vuln_management artifact: report_xlsx -> /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/reports/report.xlsx
16:56:11 [INFO] stage vuln_management artifact: sbom_clean -> /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/sbom/sbom-clean.json
16:56:11 [INFO] stage asm_audit_root: skipped
16:56:11 [WARNING] stage asm_audit_root: no ASM matches for /home/kali/Desktop/jobs/express/jobs/sources/root_sources
16:56:11 [INFO] stage external_downloads_root: skipped
16:56:11 [WARNING] stage external_downloads_root: no external download calls found in root sources
16:56:11 [INFO] stage registry_sources_root: skipped
16:56:11 [WARNING] stage registry_sources_root: no registry configs found in root sources
16:56:11 [INFO] stage download_sources: skipped
16:56:11 [WARNING] stage download_sources: no packages found in origsbom.json
16:56:11 [INFO] stage toxic_repos: skipped
16:56:11 [WARNING] stage toxic_repos: no manual input and no sources_downloads.csv
16:56:11 [INFO] stage prepare_transitive_workspace: skipped
16:56:11 [WARNING] stage prepare_transitive_workspace: deps_dir does not exist
16:56:11 [INFO] stage binary_scan: done
16:56:11 [WARNING] stage binary_scan: binary scan found nothing to report
16:56:11 [INFO] stage license_collection: done
16:56:11 [INFO] stage license_collection artifact: report -> /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd/reports/licenses.xlsx
16:56:11 [INFO] stage asm_audit_transitive_libs: skipped
16:56:11 [WARNING] stage asm_audit_transitive_libs: scan_root does not exist: /home/kali/Desktop/jobs/express/jobs/sources/transitive_libs
16:56:11 [INFO] stage external_downloads_transitive: skipped
16:56:11 [WARNING] stage external_downloads_transitive: deps_dir does not exist — skipping transitive ext-download scan
16:56:11 [INFO] pipeline finished successfully
16:56:11 [INFO] artifacts directory: /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd
2026-06-07 16:56:11 | INFO    |   moving results: /home/kali/Desktop/jobs/express/jobs/38b8badf5ee740708ea1c2d6f001a7dd -> /home/kali/Desktop/results/2026-06-07/express__v4.22.2
2026-06-07 16:56:11 | INFO    |   cleaning sources workspace: /home/kali/Desktop/jobs/express/sources
2026-06-07 16:56:11 | INFO    |   [OK] express / v4.22.2 -> /home/kali/Desktop/results/2026-06-07/express__v4.22.2
2026-06-07 16:56:11 | INFO    | run log written: /home/kali/Desktop/results/2026-06-07/run.log
2026-06-07 16:56:11 | INFO    | all 1 scan(s) completed successfully
