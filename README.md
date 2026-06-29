Debug log: debug/debug.log

=== STEP 1: Generate SBOM with Syft ===
Syft source: --from docker
Command:
  syft scan /home/kali/Desktop/test.tar.gz test.tar.gz --from docker --scope all-layers -o cyclonedx-json=/home/kali/Desktop/results/2026-06-29/express__v4.22.2/sbom/test.cdx.json

Syft stdout:
<empty>

Syft stderr:
[0000] ERROR could not determine source: an error occurred attempting to resolve '/home/kali/Desktop/test.gz test_1.1.6.tar.gz': docker: could not parse reference: test.tar.gz garda-masking-ml-service_1.1.6.tar.gz

FATAL: Syft failed with exit code 1
FATAL: Syft failed with exit code 1
2026-06-29 13:36:54 | ERROR   | [image] [express__v4.22.2__masking_postrgres] syft+oval (branch=c10f2) failed rc=1

Syft stdout:
<empty>

Syft stderr:
[0001] ERROR could not determine source: an error occurred attempting to resolve 'gtest.tar.gz': docker: pull failed: Error response from daemon: pull access denied for test.tar.gz, repository does not exist or may require 'docker login'

FATAL: Syft failed with exit code 1
FATAL: Syft failed with exit code 1
