[*] Запускаю Trivy:
    trivy fs --format cyclonedx --output /home/kali/Desktop/results/2026-06-27/express__v4.22.2/sbom/repack.cdx.json /home/kali/Desktop/results/2026-06-27/express__v4.22.2/unpacked
2026-06-27T00:11:39+03:00	INFO	"--format cyclonedx" disables security scanning. Specify "--scanners vuln" explicitly if you want to include vulnerabilities in the "cyclonedx" report.
2026-06-27T00:11:41+03:00	INFO	[npm] To collect the license information of packages, "npm install" needs to be performed beforehand	dir="extracted/d1_promise-all-reject-late-1.0.1.tgz_d8370e0f30/package/node_modules"
2026-06-27T00:11:41+03:00	INFO	[npm] To collect the license information of packages, "npm install" needs to be performed beforehand	dir="extracted/d2_promise-all-reject-late-1.0.1.tgz_9281e7edb3/package/node_modules"
2026-06-27T00:11:41+03:00	INFO	Suppressing dependencies for development and testing. To display them, try the '--include-dev-deps' flag.
2026-06-27T00:11:41+03:00	INFO	Number of language-specific files	num=2

📣 Notices:
  - Version 0.71.2 of Trivy is now available, current version is 0.68.2

To suppress version checks, run Trivy scans with the --skip-version-check flag

[+] Готово: /home/kali/Desktop/results/2026-06-27/express__v4.22.2/sbom/repack.cdx.json
[+] Trivy CycloneDX SBOM собран по распакованному каталогу: /home/kali/Desktop/results/2026-06-27/express__v4.22.2/unpacked

[binary-repack] Done.
  binary SBOM : /home/kali/Desktop/results/2026-06-27/express__v4.22.2/sbom/binary.json
  repack SBOM : /home/kali/Desktop/results/2026-06-27/express__v4.22.2/sbom/repack.cdx.json
  debug files : /home/kali/Desktop/results/2026-06-27/express__v4.22.2/debug/distrib/
/home/kali/Desktop/venv/lib/python3.12/site-packages/urllib3/connectionpool.py:1110: InsecureRequestWarning: Unverified HTTPS request is being made to host '192.168.225.95'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
  warnings.warn(
[dt] uploaded binary.json → project 219e4e29-fc76-4bfe-bce3-97678bacb99d (token=aa89eb71-c85f-4d85-9f1a-9445360ccca4)
/home/kali/Desktop/venv/lib/python3.12/site-packages/urllib3/connectionpool.py:1110: InsecureRequestWarning: Unverified HTTPS request is being made to host '192.168.225.95'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
  warnings.warn(
[dt] uploaded repack.cdx.json → project 134bf438-f8a0-4ef9-903e-95a4691d601d (token=d1d1f1fc-8442-4dac-b162-169db7554011)

============================================================
[scan-full] Merging 2 SBOM(s) → /home/kali/Desktop/results/2026-06-27/express__v4.22.2/sbom/merged.json
  binary.json
  repack.cdx.json
============================================================

[scan-full] Done.
  merged SBOM  : /home/kali/Desktop/results/2026-06-27/express__v4.22.2/sbom/merged.json  (0 components)
  binary.json
  repack.cdx.json
  debug files  : /home/kali/Desktop/results/2026-06-27/express__v4.22.2/debug/distrib/
2026-06-27 00:11:43 | ERROR   | [distrib] [express__v4.22.2__NDR_alt] scan failed rc=1
2026-06-27 00:11:43 | INFO    | [distrib] all distrib threads finished
2026-06-27 00:11:44 | INFO    | run log written: /home/kali/Desktop/results/2026-06-27/run.log
2026-06-27 00:11:44 | ERROR   | 1/1 scan(s) failed
