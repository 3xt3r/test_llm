python3 sheduler.py --config config.yml
2026-06-07 19:57:33 | INFO    | GITLAB_TOKEN not set — will try anonymous clone first
2026-06-07 19:57:33 | INFO    | timeouts: scanner=3600s, distrib_scan=7200s, deptrack=3600s
2026-06-07 19:57:33 | INFO    | === product: express ===
2026-06-07 19:57:33 | INFO    | --- version: v4.22.2 ---
2026-06-07 19:57:33 | INFO    |     cloning: https://github.com/expressjs/express.git
2026-06-07 19:57:33 | INFO    |     running: git -c credential.helper= clone --no-checkout https://github.com/expressjs/express.git /home/kali/Desktop/jobs/express/_repos/express
2026-06-07 19:57:39 | INFO    |     checkout express @ v4.22.2
2026-06-07 19:57:39 | INFO    |     running: git -c credential.helper= checkout v4.22.2
2026-06-07 19:57:39 | INFO    |     v4.22.2 is a tag — skipping reset to origin/
2026-06-07 19:57:39 | INFO    |     running: git -c credential.helper= submodule update --init --recursive
2026-06-07 19:57:39 | INFO    |   running scanner on /home/kali/Desktop/jobs/express/_repos/express (DT project: express__v4.22.2, timeout=3600s)
2026-06-07 19:57:39 | INFO    |   job_dir: /home/kali/Desktop/jobs/express/jobs/ecea79e04c3e43a3bdede819f2d3bb71
2026-06-07 19:57:39 | INFO    |     running: /home/kali/Desktop/venv/bin/python3 /home/kali/Desktop/oss_checks/scanner.py /home/kali/Desktop/jobs/express/_repos/express --apply --deptrack --dt-project-name express__v4.22.2 --env-file /home/kali/Desktop/oss_checks/.env --job-dir /home/kali/Desktop/jobs/express/jobs/ecea79e04c3e43a3bdede819f2d3bb71
19:57:39 [INFO] loaded .env: /home/kali/Desktop/oss_checks/.env
19:57:39 [INFO] [dt] auto-ensuring orig project 'express__v4.22.2-orig'...
19:57:39 [INFO] [dt] reusing existing project 'express__v4.22.2-orig' -> 77093aa6-2c10-4101-bed6-d7de8eb6052b
19:57:39 [INFO] [dt] server version: 4.14.2 — parentUUID support: yes
19:57:39 [INFO] [dt] auto-ensuring safe project 'express__v4.22.2 [safe]' (parent: 77093aa6-2c10-4101-bed6-d7de8eb6052b)...
19:57:39 [INFO] [dt] reusing existing project 'express__v4.22.2 [safe]' -> 95580e40-242b-47f3-9999-435433fecf2f
19:57:39 [INFO] scan root: /home/kali/Desktop/jobs/express/_repos/express
19:57:39 [INFO] working copy:              /home/kali/Desktop/jobs/express/_repos/express
19:57:39 [INFO] job directory:             /home/kali/Desktop/jobs/express/jobs/ecea79e04c3e43a3bdede819f2d3bb71
19:57:39 [INFO] dependency-track: enabled url=http://localhost:8081 safe_project=95580e40-242b-47f3-9999-435433fecf2f orig_project=77093aa6-2c10-4101-bed6-d7de8eb6052b insecure=True
19:57:39 [INFO] created directory: /home/kali/Desktop/jobs/express/_repos/jobs
19:57:39 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/ecea79e04c3e43a3bdede819f2d3bb71
19:57:39 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/ecea79e04c3e43a3bdede819f2d3bb71/sbom
19:57:39 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/ecea79e04c3e43a3bdede819f2d3bb71/reports
19:57:39 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/ecea79e04c3e43a3bdede819f2d3bb71/reports/asm
19:57:39 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/ecea79e04c3e43a3bdede819f2d3bb71/ecosystems
19:57:39 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/ecea79e04c3e43a3bdede819f2d3bb71/external_downloads
19:57:39 [INFO] created directory: /home/kali/Desktop/jobs/express/jobs/ecea79e04c3e43a3bdede819f2d3bb71/sbom/debug
[cleanup] removing directory: /home/kali/Desktop/jobs/express/_repos/express/examples
[cleanup] removing directory: /home/kali/Desktop/jobs/express/_repos/express/test
19:57:39 [INFO] ecosystem report: /home/kali/Desktop/jobs/express/jobs/ecea79e04c3e43a3bdede819f2d3bb71/ecosystems/lock_summary.json
19:57:39 [INFO] lock suggestions: 1
19:57:39 [INFO] [lock] [1/1] start: package.json
19:57:39 [INFO] [lock]         cmd:  cd "/home/kali/Desktop/jobs/express/_repos/express" && npm install --package-lock-only
19:57:44 [INFO] [lock] [1/1] ok (rc=0, 4.9s): package.json
19:57:44 [INFO] lock generation: ok=1, failed=0, skipped=0
19:57:44 [INFO] [cplus] oss_checks_dir: /home/kali/Desktop/oss_checks
19:57:44 [INFO] [cplus] cplus_scanner: /home/kali/Desktop/oss_checks/cpluschecks/scanner.py (exists=True)
19:57:44 [INFO] [cplus] cplus_known (abs): /home/kali/Desktop/jobs/express/jobs/ecea79e04c3e43a3bdede819f2d3bb71/sbom/cplus_sbom.json
19:57:44 [INFO] [cplus] scanner: /home/kali/Desktop/oss_checks/cpluschecks/scanner.py
19:57:44 [INFO] [cplus] scan_root: /home/kali/Desktop/jobs/express/_repos/express (exists=True)
19:57:44 [INFO] [cplus] output: /home/kali/Desktop/jobs/express/jobs/ecea79e04c3e43a3bdede819f2d3bb71/sbom/cplus_sbom.json
19:57:45 [INFO] [cplus] returncode: 0
19:57:45 [INFO] [cplus] stdout: [INFO] root=/home/kali/Desktop/jobs/express/_repos/express  checkers=94 workers=8
[INFO] candidate_files=2
[INFO] content cache ready in 0.00s
[INFO] submodule scan disabled
Scanning finished in 0.07s; total findings=0
Known SBOM written to /home/kali/Desktop/jobs/express/jobs/ecea79e04c3e43a3bdede819f2d3bb71/sbom/cplus_sbom.json
Unknown SBOM written to /home/kali/Desktop/jobs/express/jobs/ecea79e04c3e43a3bdede819f2d3bb71/sbom/cplus_sbom.unknown.json
19:57:45 [INFO] [cplus] output file exists: True
19:57:45 [INFO] [cplus] output file size: 307 bytes
19:57:45 [INFO] [cplus] found 0 C/C++ component(s)
[INFO] removed rust vendor dirs: 0
[INFO] renamed Cargo.lock.in files: 0
[INFO] hidden template pom.xml files: 0
19:57:45 [INFO] RUN trivy fs . --scanners vuln,license --follow-symlinks --format cyclonedx --output /home/kali/Desktop/jobs/express/jobs/ecea79e04c3e43a3bdede819f2d3bb71/sbom/origsbom.json --timeout 30m  (cwd=/home/kali/Desktop/jobs/express/_repos/express)
Scan local filesystem

Usage:
  trivy filesystem [flags] PATH

Aliases:
  filesystem, fs

Examples:
  # Scan a local project including language-specific files
  $ trivy fs /path/to/your_project

  # Scan a single file
  $ trivy fs ./trivy-ci-test/Pipfile.lock

Cache Flags
      --cache-backend string   [EXPERIMENTAL] cache backend (e.g. redis://localhost:6379) (default "memory")
      --cache-ttl duration     cache TTL when using redis as cache backend
      --redis-ca string        redis ca file location, if using redis as cache backend
      --redis-cert string      redis certificate file location, if using redis as cache backend
      --redis-key string       redis key file location, if using redis as cache backend
      --redis-tls              enable redis TLS with public certificates, if using redis as cache backend

DB Flags
      --db-repository strings        OCI repository(ies) to retrieve trivy-db in order of priority (default [mirror.gcr.io/aquasec/trivy-db:2,ghcr.io/aquasecurity/trivy-db:2])
      --download-db-only             download/update vulnerability database but don't run a scan
      --download-java-db-only        download/update Java index database but don't run a scan
      --java-db-repository strings   OCI repository(ies) to retrieve trivy-java-db in order of priority (default [mirror.gcr.io/aquasec/trivy-java-db:1,ghcr.io/aquasecurity/trivy-java-db:1])
      --no-progress                  suppress progress bar
      --skip-db-update               skip updating vulnerability database
      --skip-java-db-update          skip updating Java index database

License Flags
      --ignored-licenses strings         specify a list of license to ignore
      --license-confidence-level float   specify license classifier's confidence level (default 0.9)
      --license-full                     eagerly look for licenses in source code headers and license files

Misconfiguration Flags
      --ansible-extra-vars strings        set additional variables as key=value or @file (YAML/JSON)
      --ansible-inventory strings         specify inventory host path or comma separated host list
      --ansible-playbook strings          specify playbook file path(s) to scan
      --cf-params strings                 specify paths to override the CloudFormation parameters files
      --checks-bundle-repository string   OCI registry URL to retrieve checks bundle from (default "mirror.gcr.io/aquasec/trivy-checks:2")
      --config-file-schemas strings       specify paths to JSON configuration file schemas to determine that a file matches some configuration and pass the schema to Rego checks for type checking
      --helm-api-versions strings         Available API versions used for Capabilities.APIVersions. This flag is the same as the api-versions flag of the helm template command. (can specify multiple or separate values with commas: policy/v1/PodDisruptionBudget,apps/v1/Deployment)
      --helm-kube-version string          Kubernetes version used for Capabilities.KubeVersion. This flag is the same as the kube-version flag of the helm template command.
      --helm-set strings                  specify Helm values on the command line (can specify multiple or separate values with commas: key1=val1,key2=val2)
      --helm-set-file strings             specify Helm values from respective files specified via the command line (can specify multiple or separate values with commas: key1=path1,key2=path2)
      --helm-set-string strings           specify Helm string values on the command line (can specify multiple or separate values with commas: key1=val1,key2=val2)
      --helm-values strings               specify paths to override the Helm values.yaml files
      --include-non-failures              include successes, available with '--scanners misconfig'
      --misconfig-scanners strings        comma-separated list of misconfig scanners to use for misconfiguration scanning (default [azure-arm,cloudformation,dockerfile,helm,kubernetes,terraform,terraformplan-json,terraformplan-snapshot,ansible])
      --raw-config-scanners strings       specify the types of scanners that will also scan raw configurations. For example, scanners will scan a non-adapted configuration into a shared state (allowed values: terraform)
      --render-cause strings              specify configuration types for which the rendered causes will be shown in the table report (allowed values: terraform,ansible)
      --tf-exclude-downloaded-modules     exclude misconfigurations for downloaded terraform modules
      --tf-vars strings                   specify paths to override the Terraform tfvars files

Module Flags
      --enable-modules strings   [EXPERIMENTAL] module names to enable
      --module-dir string        specify directory to the wasm modules that will be loaded (default "/home/kali/.trivy/modules")

Package Flags
      --include-dev-deps            include development dependencies in the report (supported: npm, yarn, gradle)
      --pkg-relationships strings   list of package relationships
                                    Allowed values:
                                      - unknown
                                      - root
                                      - workspace
                                      - direct
                                      - indirect
                                     (default [unknown,root,workspace,direct,indirect])
      --pkg-types strings           list of package types (allowed values: os,library) (default [os,library])

Client/Server Flags
      --custom-headers strings   custom headers in client mode
      --server string            server address in client mode
      --token string             for authentication in client/server mode
      --token-header string      specify a header name for token in client/server mode (default "Trivy-Token")

Registry Flags
      --password strings        password. Comma-separated passwords allowed. TRIVY_PASSWORD should be used for security reasons.
      --password-stdin          password from stdin. Comma-separated passwords are not supported.
      --registry-token string   registry token
      --username strings        username. Comma-separated usernames allowed.

Rego Flags
      --check-namespaces strings    Rego namespaces
      --config-check strings        specify the paths to the Rego check files or to the directories containing them, applying config files
      --config-data strings         specify paths from which data for the Rego checks will be recursively loaded
      --include-deprecated-checks   include deprecated checks
      --rego-error-limit int        maximum number of compile errors allowed during Rego policy evaluation (default 10)
      --skip-check-update           skip fetching rego check updates
      --trace-rego                  enable more verbose trace output for custom queries

Report Flags
      --compliance string          compliance report to generate
      --dependency-tree            [EXPERIMENTAL] show dependency origin tree of vulnerable packages
      --exit-code int              specify exit code when any security issues are found
  -f, --format string              format
                                   Allowed values:
                                     - table
                                     - json
                                     - template
                                     - sarif
                                     - cyclonedx
                                     - spdx
                                     - spdx-json
                                     - github
                                     - cosign-vuln
                                    (default "table")
      --ignore-policy string       specify the Rego file path to evaluate each vulnerability
      --ignorefile string          specify .trivyignore file (default ".trivyignore")
      --list-all-pkgs              output all packages in the JSON report regardless of vulnerability (default true)
  -o, --output string              output file name
      --output-plugin-arg string   [EXPERIMENTAL] output plugin arguments
      --report string              specify a compliance report format for the output (allowed values: all,summary) (default "all")
  -s, --severity strings           severities of security issues to be displayed
                                   Allowed values:
                                     - UNKNOWN
                                     - LOW
                                     - MEDIUM
                                     - HIGH
                                     - CRITICAL
                                    (default [UNKNOWN,LOW,MEDIUM,HIGH,CRITICAL])
      --show-suppressed            [EXPERIMENTAL] show suppressed vulnerabilities
      --table-mode strings         [EXPERIMENTAL] tables that will be displayed in 'table' format (allowed values: summary,detailed) (default [summary,detailed])
  -t, --template string            output template

Scan Flags
      --detection-priority string   specify the detection priority:
                                      - "precise": Prioritizes precise by minimizing false positives.
                                      - "comprehensive": Aims to detect more security findings at the cost of potential false positives.
                                     (allowed values: precise,comprehensive) (default "precise")
      --disable-telemetry           disable sending anonymous usage data to Aqua
      --distro string               [EXPERIMENTAL] specify a distribution, <family>/<version>
      --file-patterns strings       specify config file patterns
      --offline-scan                do not issue API requests to identify dependencies
      --parallel int                number of goroutines enabled for parallel scanning, set 0 to auto-detect parallelism (default 5)
      --rekor-url string            [EXPERIMENTAL] address of rekor STL server (default "https://rekor.sigstore.dev")
      --sbom-sources strings        [EXPERIMENTAL] try to retrieve SBOM from the specified sources (allowed values: oci,rekor)
      --scanners strings            comma-separated list of what security issues to detect (allowed values: vuln,misconfig,secret,license) (default [vuln,secret])
      --skip-dirs strings           specify the directories or glob patterns to skip
      --skip-files strings          specify the files or glob patterns to skip
      --skip-version-check          suppress notices about version updates and Trivy announcements

Secret Flags
      --secret-config string   specify a path to config file for secret scanning (default "trivy-secret.yaml")

Vulnerability Flags
      --ignore-status strings          comma-separated list of vulnerability status to ignore
                                       Allowed values:
                                         - unknown
                                         - not_affected
                                         - affected
                                         - fixed
                                         - under_investigation
                                         - will_not_fix
                                         - fix_deferred
                                         - end_of_life
      --ignore-unfixed                 display only fixed vulnerabilities
      --skip-vex-repo-update           [EXPERIMENTAL] Skip VEX Repository update
      --vex strings                    [EXPERIMENTAL] VEX sources ("repo", "oci" or file path)
      --vuln-severity-source strings   order of data sources for selecting vulnerability severity level
                                       Allowed values:
                                         - nvd
                                         - redhat
                                         - redhat-oval
                                         - debian
                                         - ubuntu
                                         - alpine
                                         - amazon
                                         - oracle-oval
                                         - suse-cvrf
                                         - photon
                                         - arch-linux
                                         - alma
                                         - rocky
                                         - cbl-mariner
                                         - azure
                                         - ruby-advisory-db
                                         - php-security-advisories
                                         - nodejs-security-wg
                                         - ghsa
                                         - glad
                                         - aqua
                                         - osv
                                         - k8s
                                         - wolfi
                                         - chainguard
                                         - bitnami
                                         - govulndb
                                         - julia
                                         - echo
                                         - minimos
                                         - rootio
                                         - auto
                                        (default [auto])

Global Flags:
      --cacert string             Path to PEM-encoded CA certificate file
      --cache-dir string          cache directory (default "/home/kali/.cache/trivy")
  -c, --config string             config path (default "trivy.yaml")
  -d, --debug                     debug mode
      --generate-default-config   write the default config to trivy-default.yaml
      --insecure                  allow insecure server connections
  -q, --quiet                     suppress progress bar and log output
      --timeout duration          timeout (default 5m0s)
  -v, --version                   show version

2026-06-07T19:57:45+03:00	FATAL	Fatal error	unknown flag: --follow-symlinks
19:57:45 [ERROR] rc=1: trivy fs . --scanners vuln,license --follow-symlinks --format cyclonedx --output /home/kali/Desktop/jobs/express/jobs/ecea79e04c3e43a3bdede819f2d3bb71/sbom/origsbom.json --timeout 30m
[INFO] restored template pom.xml files: 0
2026-06-07 19:57:45 | ERROR   |     [FAIL] scanner.py: exited with code 1
2026-06-07 19:57:45 | INFO    |   moving results: /home/kali/Desktop/jobs/express/jobs/ecea79e04c3e43a3bdede819f2d3bb71 -> /home/kali/Desktop/results/2026-06-07/express__v4.22.2
2026-06-07 19:57:45 | ERROR   |   [FAIL] express / v4.22.2: exited with code 1
2026-06-07 19:57:45 | INFO    | run log written: /home/kali/Desktop/results/2026-06-07/run.log
2026-06-07 19:57:45 | ERROR   | 1/1 scan(s) failed
