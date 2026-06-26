(venv) kali@kali-VirtualBox:~/Desktop/oss_checks$ python  scheduler.py --config config.yml
2026-06-26 23:34:30 | INFO    | timeouts: scanner=3600s, distrib_scan=7200s, deptrack=3600s
2026-06-26 23:34:30 | INFO    | === product: express ===
2026-06-26 23:34:30 | INFO    | --- version: v4.22.2 ---
2026-06-26 23:34:30 | INFO    |     cloning: https://github.com/expressjs/express.git
2026-06-26 23:34:30 | INFO    |     running: git -c credential.helper= clone --no-checkout https://github.com/expressjs/express.git /home/kali/Desktop/jobs/express/_repos/express
2026-06-26 23:34:35 | INFO    |     checkout express @ v4.22.2
2026-06-26 23:34:35 | INFO    |     running: git -c credential.helper= -c http.extraHeader=Authorization: Basic *** checkout -- .
2026-06-26 23:34:35 | ERROR   |     [FAIL] git checkout -- . (reset local changes): error: pathspec '.' did not match any file(s) known to git
2026-06-26 23:34:35 | INFO    |     running: git -c credential.helper= -c http.extraHeader=Authorization: Basic *** clean -fd
2026-06-26 23:34:35 | INFO    |     running: git -c credential.helper= -c http.extraHeader=Authorization: Basic *** checkout v4.22.2
2026-06-26 23:34:35 | INFO    |     v4.22.2 is a tag — skipping reset to origin/
2026-06-26 23:34:35 | INFO    |     running: git -c credential.helper= -c http.extraHeader=Authorization: Basic *** submodule update --init --recursive
2026-06-26 23:34:36 | INFO    |   running scanner on /home/kali/Desktop/jobs/express/_repos/express (DT project: express__v4.22.2, timeout=3600s)
2026-06-26 23:34:36 | INFO    |   job_dir: /home/kali/Desktop/jobs/express/jobs/8edf075309004ebeb5e7d6cb5b044a47
2026-06-26 23:34:36 | INFO    |     running: /home/kali/Desktop/venv/bin/python /home/kali/Desktop/oss_checks/scanner.py /home/kali/Desktop/jobs/express/_repos/express --apply --deptrack --dt-project-name express__v4.22.2 --env-file /home/kali/Desktop/oss_checks/env --job-dir /home/kali/Desktop/jobs/express/jobs/8edf075309004ebeb5e7d6cb5b044a47 --only-cve
Traceback (most recent call last):
  File "/home/kali/Desktop/oss_checks/scanner.py", line 13, in <module>
    from ecosystem_management import (
ImportError: cannot import name 'EcosystemScanOptions' from 'ecosystem_management' (/home/kali/Desktop/oss_checks/ecosystem_management/__init__.py)
2026-06-26 23:34:36 | ERROR   |     [FAIL] scanner.py: exited with code 1
2026-06-26 23:34:36 | INFO    |   moving results: /home/kali/Desktop/jobs/express/jobs/8edf075309004ebeb5e7d6cb5b044a47 -> /home/kali/Desktop/results/2026-06-26/express__v4.22.2
2026-06-26 23:34:36 | INFO    | [distrib] started thread for express / v4.22.2 / express_test
2026-06-26 23:34:36 | ERROR   |   [FAIL] express / v4.22.2: exited with code 1
2026-06-26 23:34:36 | INFO    | [distrib] waiting for 1 distrib thread(s) to finish...
2026-06-26 23:34:36 | INFO    | [distrib] [express__v4.22.2__express_test] orig project not found yet (attempt 1/5) — retrying in 10s
2026-06-26 23:34:54 | INFO    | [distrib] [express__v4.22.2__express_test] orig project not found yet (attempt 2/5) — retrying in 10s
2026-06-26 23:35:05 | INFO    | [distrib] [express__v4.22.2__express_test] orig project not found yet (attempt 3/5) — retrying in 10s
2026-06-26 23:35:15 | INFO    | [distrib] [express__v4.22.2__express_test] orig project not found yet (attempt 4/5) — retrying in 10s
2026-06-26 23:35:25 | INFO    | [distrib] [express__v4.22.2__express_test] orig project not found yet (attempt 5/5) — retrying in 10s
2026-06-26 23:35:35 | WARNING | [distrib] [express__v4.22.2__express_test] orig project 'express__v4.22.2-orig' not found — projects will have no parent
2026-06-26 23:35:35 | INFO    | [dt] reusing existing project 'express__v4.22.2__express_test__packages':v4.22.2 -> d7189b1e-ab22-417f-87bc-27f24aa51474
2026-06-26 23:35:35 | INFO    | [distrib] [express__v4.22.2__express_test] project 'express__v4.22.2__express_test__packages' -> d7189b1e-ab22-417f-87bc-27f24aa51474
2026-06-26 23:35:36 | INFO    | [dt] reusing existing project 'express__v4.22.2__express_test__binary':v4.22.2 -> 8832367a-dfb2-4f9a-a744-0455d733454a
2026-06-26 23:35:36 | INFO    | [distrib] [express__v4.22.2__express_test] project 'express__v4.22.2__express_test__binary' -> 8832367a-dfb2-4f9a-a744-0455d733454a
2026-06-26 23:35:36 | INFO    | [dt] reusing existing project 'express__v4.22.2__express_test__repack':v4.22.2 -> dab2f61f-866d-41de-be24-cc17cbb0ee14
2026-06-26 23:35:36 | INFO    | [distrib] [express__v4.22.2__express_test] project 'express__v4.22.2__express_test__repack' -> dab2f61f-866d-41de-be24-cc17cbb0ee14
2026-06-26 23:35:36 | INFO    | [distrib] [express__v4.22.2__express_test] starting scan: /home/kali/Desktop/NDR (timeout=7200s)
[scan-full] found 1 archive(s) to unpack in /home/kali/Desktop/NDR
[scan-full] skip (already unpacked): GardaNDR-4.4.0.2.x86_64.rpm → GardaNDR-4.4.0.2.x86_64_unpacked/
[env] loaded: /home/kali/Desktop/oss_checks/env

[scan-full] Scanning: /home/kali/Desktop/NDR
[scan-full] Detected: rpm, archives
[dt] Dependency Track configured: https://192.168.225.95

============================================================
[scan-full] Step: rpm  (/home/kali/Desktop/NDR)
============================================================
written report: /home/kali/Desktop/results/2026-06-26/express__v4.22.2/debug/report.txt
written updated sbom: /home/kali/Desktop/results/2026-06-26/express__v4.22.2/sbom/alt.json
Reorder applied: yes
{
  "scan_rpm_total": 180,
  "scan_matched_by_syft_location_suffix": 180,
  "scan_unmatched": 0,
  "scan_buildhost_empty": 0,
  "scan_rpm_query_errors": 0,
  "compare_rpm_total": 2547,
  "compare_matched_by_sha256": 80,
  "compare_unmatched": 2467,
  "compare_buildhost_empty": 0,
  "compare_rpm_query_errors": 0,
  "removed_cert_properties": 0,
  "default_props_added": 720,
  "filtered_components_for_final_compare": 27,
  "final_compare_rpm_files_found": 2547,
  "final_version_mismatches": 26,
  "final_missing_on_disk": 1,
  "final_provided_by_added": 26,
  "rpm_components_total": 180,
  "identified_distribution_refs_added": 106,
  "identified_distribution_refs_missing_path": 0,
  "unidentified_vcs_placeholders_set": 74
}
running CVE scanner for generated SBOM...
usage: sbom_alt_cve_working.py [-h] [--from-archive] [--no-sudo-syft] [--skip-syft] [--sbom SBOM] [-o O] [--no-cache] [--tmpdir DIR] image
sbom_alt_cve_working.py: error: unrecognized arguments: --c10f2
error: CVE scanner exited with code 2
[scan-full] rpm step failed (code 2)

============================================================
[scan-full] Step: binary-repack  (/home/kali/Desktop/NDR)
============================================================

[binary-repack] Step 1/2 — sbom_binary.py → /home/kali/Desktop/results/2026-06-26/express__v4.22.2/sbom/binary.json


[!] Ошибка распаковки: Command '['cpio', '-idm']' returned non-zero exit status 2.

[binary-repack] sbom_binary.py exited with code 1
[scan-full] binary-repack step failed (code 1)

[scan-full] No SBOM files produced — nothing to merge
2026-06-26 23:36:47 | ERROR   | [distrib] [express__v4.22.2__express_test] scan failed rc=1
2026-06-26 23:36:47 | INFO    | [distrib] all distrib threads finished
2026-06-26 23:36:47 | INFO    | run log written: /home/kali/Desktop/results/2026-06-26/run.log
2026-06-26 23:36:47 | ERROR   | 1/1 scan(s) failed
