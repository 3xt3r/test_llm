2026-06-27 12:05:59 | INFO    | [distrib] [express__v4.22.2__NDR_alt] starting scan: /home/kali/Desktop/NDR (timeout=7200s)
[scan-full] found 1 archive(s) to unpack in /home/kali/Desktop/NDR
[scan-full] skip (already unpacked): .rpm → _unpacked/
[env] loaded: /home/kali/Desktop/oss_checks/env

[scan-full] Scanning: /home/kali/Desktop/NDR
[scan-full] Detected: rpm, archives

============================================================
[scan-full] Step: rpm  (/home/kali/Desktop/NDR)
============================================================
written report: /home/kali/Desktop/results/2026-06-27/express__v4.22.2/debug/report.txt
written updated sbom: /home/kali/Desktop/results/2026-06-27/express__v4.22.2/sbom/alt.json
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
syft_alt_cve_report.py version: 2026-05-21-c10f2-only-final
Script path: /home/kali/Desktop/oss_checks/distrib/sbom_alt_cve_working.py
Script sha256/16: f2d57c8fcb1fb1ad
Python: /home/kali/Desktop/venv/bin/python
CWD: /home/kali/Desktop/results/2026-06-27/express__v4.22.2
Target OVAL branch: c10f2
Mode: first generate SBOM with Syft, then scan SBOM against ALT OVAL c10f2 only
Mode: every RPM detected by Syft is treated as ALT RPM
Mode: output contains c10f2 vulnerabilities only
Debug log: debug/debug.log

=== STEP 1: Generate SBOM with Syft ===
Syft source: --from docker
Command:
  sudo syft scan /home/kali/Desktop/results/2026-06-27/express__v4.22.2/sbom/alt.json --from docker --scope all-layers -o cyclonedx-json=sbom/docker.cdx.json
[sudo] password for kali: 

Syft stdout:
<empty>

Syft stderr:
[0000] ERROR could not determine source: an error occurred attempting to resolve '/home/kali/Desktop/results/2026-06-27/express__v4.22.2/sbom/alt.json': docker: docker not available: failed to connect to Docker daemon. Ensure Docker is running and accessible

FATAL: Syft failed with exit code 1
FATAL: Syft failed with exit code 1
error: CVE scanner exited with code 1
[scan-full] rpm step failed (code 1)

============================================================
[scan-full] Step: binary-repack  (/home/kali/Desktop/NDR)
============================================================

[binary-repack] Step 1/2 — sbom_binary.py → /home/kali/Desktop/results/2026-06-27/express__v4.22.2/sbom/binary.json

[*] Источник пакетов: /home/kali/Desktop/NDR
[*] Выходной файл: /home/kali/Desktop/results/2026-06-27/express__v4.22.2/sbom/binary.json
Traceback (most recent call last):
  File "/home/kali/Desktop/oss_checks/distrib/sbom_binary.py", line 634, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "/home/kali/Desktop/oss_checks/distrib/sbom_binary.py", line 618, in main
    rc = build_binary_sbom(pkg_dir, output_file, unpack_dir, errors_file)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/kali/Desktop/oss_checks/distrib/sbom_binary.py", line 355, in build_binary_sbom
    prepare_unpack_dir(unpack_dir)
    ^^^^^^^^^^^^^^^^^^
NameError: name 'prepare_unpack_dir' is not defined

[binary-repack] sbom_binary.py exited with code 1 — continuing to repack step

[binary-repack] Step 2/2 — sbom_repack_deps.py → /home/kali/Desktop/results/2026-06-27/express__v4.22.2/sbom/repack.cdx.json

Traceback (most recent call last):
  File "/home/kali/Desktop/oss_checks/distrib/sbom_repack_deps.py", line 362, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "/home/kali/Desktop/oss_checks/distrib/sbom_repack_deps.py", line 347, in main
    stats = repack_recursively(input_path, unpack_dir, max_depth=args.max_depth)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/kali/Desktop/oss_checks/distrib/sbom_repack_deps.py", line 213, in repack_recursively
    if not looks_like_archive(path):
           ^^^^^^^^^^^^^^^^^^
NameError: name 'looks_like_archive' is not defined

[binary-repack] sbom_repack_deps.py exited with code 1

[binary-repack] Done.
  binary SBOM : /home/kali/Desktop/results/2026-06-27/express__v4.22.2/sbom/binary.json
  repack SBOM : /home/kali/Desktop/results/2026-06-27/express__v4.22.2/sbom/repack.cdx.json
  debug files : /home/kali/Desktop/results/2026-06-27/express__v4.22.2/debug/distrib/
[scan-full] binary-repack step finished with code 1 — checking produced files
[scan-full] warning: binary SBOM was not produced: /home/kali/Desktop/results/2026-06-27/express__v4.22.2/sbom/binary.json
[scan-full] warning: repack SBOM was not produced: /home/kali/Desktop/results/2026-06-27/express__v4.22.2/sbom/repack.cdx.json

[scan-full] No SBOM files produced — nothing to merge
2026-06-27 12:09:43 | ERROR   | [distrib] [express__v4.22.2__NDR_alt] scan failed rc=1
2026-06-27 12:09:43 | INFO    | [distrib] all distrib threads finished
2026-06-27 12:09:43 | INFO    | run log written: /home/kali/Desktop/results/2026-06-27/run.log
2026-06-27 12:09:43 | INFO    | all 1 scan(s) completed successfully
