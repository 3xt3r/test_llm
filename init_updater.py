curl -s "http://localhost:8081/api/v1/configProperty" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM" | jq .
[
  {
    "groupName": "access-management",
    "propertyName": "acl.enabled",
    "propertyValue": "false",
    "propertyType": "BOOLEAN",
    "description": "Flag to enable/disable access control to projects in the portfolio"
  },
  {
    "groupName": "artifact",
    "propertyName": "bom.validation.mode",
    "propertyValue": "ENABLED",
    "propertyType": "STRING",
    "description": "Flag to control the BOM validation mode"
  },
  {
    "groupName": "artifact",
    "propertyName": "bom.validation.tags.exclusive",
    "propertyValue": "[]",
    "propertyType": "STRING",
    "description": "JSON array of tags for which BOM validation shall NOT be performed"
  },
  {
    "groupName": "artifact",
    "propertyName": "bom.validation.tags.inclusive",
    "propertyValue": "[]",
    "propertyType": "STRING",
    "description": "JSON array of tags for which BOM validation shall be performed"
  },
  {
    "groupName": "artifact",
    "propertyName": "cyclonedx.enabled",
    "propertyValue": "true",
    "propertyType": "BOOLEAN",
    "description": "Flag to enable/disable the systems ability to accept CycloneDX uploads"
  },
  {
    "groupName": "email",
    "propertyName": "smtp.enabled",
    "propertyValue": "false",
    "propertyType": "BOOLEAN",
    "description": "Flag to enable/disable SMTP"
  },
  {
    "groupName": "email",
    "propertyName": "smtp.from.address",
    "propertyType": "STRING",
    "description": "The from email address to use to send output SMTP mail"
  },
  {
    "groupName": "email",
    "propertyName": "smtp.password",
    "propertyValue": "HiddenDecryptedPropertyPlaceholder",
    "propertyType": "ENCRYPTEDSTRING",
    "description": "The optional password for the username used for authentication"
  },
  {
    "groupName": "email",
    "propertyName": "smtp.server.hostname",
    "propertyType": "STRING",
    "description": "The hostname or IP address of the SMTP mail server"
  },
  {
    "groupName": "email",
    "propertyName": "smtp.server.port",
    "propertyType": "INTEGER",
    "description": "The port the SMTP server listens on"
  },
  {
    "groupName": "email",
    "propertyName": "smtp.ssltls",
    "propertyValue": "false",
    "propertyType": "BOOLEAN",
    "description": "Flag to enable/disable the use of SSL/TLS when connecting to the SMTP server"
  },
  {
    "groupName": "email",
    "propertyName": "smtp.trustcert",
    "propertyValue": "false",
    "propertyType": "BOOLEAN",
    "description": "Flag to enable/disable the trust of the certificate presented by the SMTP server"
  },
  {
    "groupName": "email",
    "propertyName": "smtp.username",
    "propertyType": "STRING",
    "description": "The optional username to authenticate with when sending outbound SMTP mail"
  },
  {
    "groupName": "email",
    "propertyName": "subject.prefix",
    "propertyValue": "[Dependency-Track]",
    "propertyType": "STRING",
    "description": "The Prefix Subject email to use"
  },
  {
    "groupName": "general",
    "propertyName": "badge.enabled",
    "propertyValue": "false",
    "propertyType": "BOOLEAN",
    "description": "Flag to enable/disable unauthenticated access to SVG badge from metrics"
  },
  {
    "groupName": "general",
    "propertyName": "base.url",
    "propertyType": "URL",
    "description": "URL used to construct links back to Dependency-Track from external systems"
  },
  {
    "groupName": "general",
    "propertyName": "default.locale",
    "propertyType": "STRING",
    "description": "Determine the default Language to use"
  },
  {
    "groupName": "general",
    "propertyName": "welcome.message.enabled",
    "propertyValue": "false",
    "propertyType": "BOOLEAN",
    "description": "Bool that says whether to show the welcome message or not"
  },
  {
    "groupName": "general",
    "propertyName": "welcome.message.html",
    "propertyValue": "%3Chtml%3E%3Ch1%3EYour%20Welcome%20Message%3C%2Fh1%3E%3C%2Fhtml%3E",
    "propertyType": "STRING",
    "description": "Custom HTML Code that is displayed before login"
  },
  {
    "groupName": "integrations",
    "propertyName": "defectdojo.apiKey",
    "propertyType": "STRING",
    "description": "API Key for DefectDojo"
  },
  {
    "groupName": "integrations",
    "propertyName": "defectdojo.enabled",
    "propertyValue": "false",
    "propertyType": "BOOLEAN",
    "description": "Flag to enable/disable DefectDojo integration"
  },
  {
    "groupName": "integrations",
    "propertyName": "defectdojo.reimport.enabled",
    "propertyValue": "false",
    "propertyType": "BOOLEAN",
    "description": "Flag to enable/disable DefectDojo reimport-scan API endpoint"
  },
  {
    "groupName": "integrations",
    "propertyName": "defectdojo.sync.cadence",
    "propertyValue": "60",
    "propertyType": "INTEGER",
    "description": "The cadence (in minutes) to upload to DefectDojo"
  },
  {
    "groupName": "integrations",
    "propertyName": "defectdojo.url",
    "propertyType": "URL",
    "description": "Base URL to DefectDojo"
  },
  {
    "groupName": "integrations",
    "propertyName": "fortify.ssc.enabled",
    "propertyValue": "false",
    "propertyType": "BOOLEAN",
    "description": "Flag to enable/disable Fortify SSC integration"
  },
  {
    "groupName": "integrations",
    "propertyName": "fortify.ssc.sync.cadence",
    "propertyValue": "60",
    "propertyType": "INTEGER",
    "description": "The cadence (in minutes) to upload to Fortify SSC"
  },
  {
    "groupName": "integrations",
    "propertyName": "fortify.ssc.token",
    "propertyValue": "HiddenDecryptedPropertyPlaceholder",
    "propertyType": "ENCRYPTEDSTRING",
    "description": "The token to use to authenticate to Fortify SSC"
  },
  {
    "groupName": "integrations",
    "propertyName": "fortify.ssc.url",
    "propertyType": "URL",
    "description": "Base URL to Fortify SSC"
  },
  {
    "groupName": "integrations",
    "propertyName": "jira.password",
    "propertyValue": "HiddenDecryptedPropertyPlaceholder",
    "propertyType": "ENCRYPTEDSTRING",
    "description": "The password for the username or bearer token used for authentication"
  },
  {
    "groupName": "integrations",
    "propertyName": "jira.url",
    "propertyType": "URL",
    "description": "The base URL of the JIRA instance"
  },
  {
    "groupName": "integrations",
    "propertyName": "jira.username",
    "propertyType": "STRING",
    "description": "The optional username to authenticate with when creating an Jira issue"
  },
  {
    "groupName": "integrations",
    "propertyName": "kenna.api.url",
    "propertyValue": "https://api.kennasecurity.com",
    "propertyType": "STRING",
    "description": "Kenna Security API URL"
  },
  {
    "groupName": "integrations",
    "propertyName": "kenna.connector.id",
    "propertyType": "STRING",
    "description": "The Kenna Security connector identifier to upload to"
  },
  {
    "groupName": "integrations",
    "propertyName": "kenna.enabled",
    "propertyValue": "false",
    "propertyType": "BOOLEAN",
    "description": "Flag to enable/disable Kenna Security integration"
  },
  {
    "groupName": "integrations",
    "propertyName": "kenna.sync.cadence",
    "propertyValue": "60",
    "propertyType": "INTEGER",
    "description": "The cadence (in minutes) to upload to Kenna Security"
  },
  {
    "groupName": "integrations",
    "propertyName": "kenna.token",
    "propertyValue": "HiddenDecryptedPropertyPlaceholder",
    "propertyType": "ENCRYPTEDSTRING",
    "description": "The token to use when authenticating to Kenna Security"
  },
  {
    "groupName": "internal-components",
    "propertyName": "groups.regex",
    "propertyType": "STRING",
    "description": "Regex that matches groups of internal components"
  },
  {
    "groupName": "internal-components",
    "propertyName": "match-mode",
    "propertyValue": "OR",
    "propertyType": "STRING",
    "description": "Determines how internal component regexes are combined: OR (default) or AND"
  },
  {
    "groupName": "internal-components",
    "propertyName": "names.regex",
    "propertyType": "STRING",
    "description": "Regex that matches names of internal components"
  },
  {
    "groupName": "notification",
    "propertyName": "template.baseDir",
    "propertyValue": "/data/",
    "propertyType": "STRING",
    "description": "The base directory to use when searching for notification templates"
  },
  {
    "groupName": "notification",
    "propertyName": "template.default.override.enabled",
    "propertyValue": "false",
    "propertyType": "BOOLEAN",
    "description": "Flag to enable/disable override of default notification templates"
  },
  {
    "groupName": "scanner",
    "propertyName": "analysis.cache.validity.period",
    "propertyValue": "43200000",
    "propertyType": "NUMBER",
    "description": "Validity period for individual component vulnerability and metadats analysis cache"
  },
  {
    "groupName": "scanner",
    "propertyName": "internal.enabled",
    "propertyValue": "true",
    "propertyType": "BOOLEAN",
    "description": "Flag to enable/disable the internal analyzer"
  },
  {
    "groupName": "scanner",
    "propertyName": "internal.fuzzy.enabled",
    "propertyValue": "false",
    "propertyType": "BOOLEAN",
    "description": "Flag to enable/disable non-exact fuzzy matching using the internal analyzer"
  },
  {
    "groupName": "scanner",
    "propertyName": "internal.fuzzy.exclude.internal",
    "propertyValue": "true",
    "propertyType": "BOOLEAN",
    "description": "Flag to enable/disable fuzzy matching on components that are marked internal."
  },
  {
    "groupName": "scanner",
    "propertyName": "internal.fuzzy.exclude.purl",
    "propertyValue": "true",
    "propertyType": "BOOLEAN",
    "description": "Flag to enable/disable fuzzy matching on components that have a Package URL (PURL) defined"
  },
  {
    "groupName": "scanner",
    "propertyName": "npmaudit.enabled",
    "propertyValue": "true",
    "propertyType": "BOOLEAN",
    "description": "Flag to enable/disable NPM Audit"
  },
  {
    "groupName": "scanner",
    "propertyName": "ossindex.alias.sync.enabled",
    "propertyValue": "true",
    "propertyType": "BOOLEAN",
    "description": "Flag to enable/disable alias synchronization for OSS Index"
  },
  {
    "groupName": "scanner",
    "propertyName": "ossindex.api.token",
    "propertyValue": "HiddenDecryptedPropertyPlaceholder",
    "propertyType": "ENCRYPTEDSTRING",
    "description": "The API token used for OSS Index authentication"
  },
  {
    "groupName": "scanner",
    "propertyName": "ossindex.api.username",
    "propertyType": "STRING",
    "description": "The API username used for OSS Index authentication"
  },
  {
    "groupName": "scanner",
    "propertyName": "ossindex.base.url",
    "propertyValue": "https://ossindex.sonatype.org",
    "propertyType": "URL",
    "description": "Base URL for OSS Index API"
  },
  {
    "groupName": "scanner",
    "propertyName": "ossindex.enabled",
    "propertyValue": "true",
    "propertyType": "BOOLEAN",
    "description": "Flag to enable/disable Sonatype OSS Index"
  },
  {
    "groupName": "scanner",
    "propertyName": "snyk.alias.sync.enabled",
    "propertyValue": "false",
    "propertyType": "BOOLEAN",
    "description": "Flag to enable/disable alias synchronization for Snyk"
  },
  {
    "groupName": "scanner",
    "propertyName": "snyk.api.token",
    "propertyValue": "HiddenDecryptedPropertyPlaceholder",
    "propertyType": "ENCRYPTEDSTRING",
    "description": "The API token used for Snyk API authentication"
  },
  {
    "groupName": "scanner",
    "propertyName": "snyk.api.version",
    "propertyValue": "2023-06-22",
    "propertyType": "STRING",
    "description": "Snyk API version"
  },
  {
    "groupName": "scanner",
    "propertyName": "snyk.base.url",
    "propertyValue": "https://api.snyk.io",
    "propertyType": "URL",
    "description": "Base Url pointing to the hostname and path for Snyk analysis"
  },
  {
    "groupName": "scanner",
    "propertyName": "snyk.cvss.source",
    "propertyValue": "NVD",
    "propertyType": "STRING",
    "description": "Type of source to be prioritized for cvss calculation"
  },
  {
    "groupName": "scanner",
    "propertyName": "snyk.enabled",
    "propertyValue": "false",
    "propertyType": "BOOLEAN",
    "description": "Flag to enable/disable Snyk Vulnerability Analysis"
  },
  {
    "groupName": "scanner",
    "propertyName": "snyk.org.id",
    "propertyType": "STRING",
    "description": "The Organization ID used for Snyk API access"
  },
  {
    "groupName": "scanner",
    "propertyName": "trivy.api.token",
    "propertyValue": "HiddenDecryptedPropertyPlaceholder",
    "propertyType": "ENCRYPTEDSTRING",
    "description": "The API token used for Trivy API authentication"
  },
  {
    "groupName": "scanner",
    "propertyName": "trivy.base.url",
    "propertyType": "URL",
    "description": "Base Url pointing to the hostname and path for Trivy analysis"
  },
  {
    "groupName": "scanner",
    "propertyName": "trivy.enabled",
    "propertyValue": "false",
    "propertyType": "BOOLEAN",
    "description": "Flag to enable/disable Trivy Vulnerability Analysis"
  },
  {
    "groupName": "scanner",
    "propertyName": "trivy.ignore.unfixed",
    "propertyValue": "false",
    "propertyType": "BOOLEAN",
    "description": "Flag to ignore unfixed vulnerabilities"
  },
  {
    "groupName": "scanner",
    "propertyName": "trivy.scanner.scanLibrary",
    "propertyValue": "true",
    "propertyType": "BOOLEAN",
    "description": "Flag to enable library scanning"
  },
  {
    "groupName": "scanner",
    "propertyName": "trivy.scanner.scanOs",
    "propertyValue": "true",
    "propertyType": "BOOLEAN",
    "description": "Flag to enable os scanning"
  },
  {
    "groupName": "scanner",
    "propertyName": "vulndb.api.oath1.consumerSecret",
    "propertyValue": "HiddenDecryptedPropertyPlaceholder",
    "propertyType": "ENCRYPTEDSTRING",
    "description": "The OAuth 1.0a consumer secret"
  },
  {
    "groupName": "scanner",
    "propertyName": "vulndb.api.oauth1.consumerKey",
    "propertyType": "STRING",
    "description": "The OAuth 1.0a consumer key"
  },
  {
    "groupName": "scanner",
    "propertyName": "vulndb.enabled",
    "propertyValue": "true",
    "propertyType": "BOOLEAN",
    "description": "Flag to enable/disable VulnDB"
  },
  {
    "groupName": "search-indexes",
    "propertyName": "consistency.check.cadence",
    "propertyValue": "4320",
    "propertyType": "INTEGER",
    "description": "Lucene indexes consistency check cadence (in minutes)"
  },
  {
    "groupName": "search-indexes",
    "propertyName": "consistency.check.delta.threshold",
    "propertyValue": "20",
    "propertyType": "INTEGER",
    "description": "Threshold used to trigger an index rebuild when comparing database table and corresponding lucene index (in percentage). It must be an integer between 1 and 100"
  },
  {
    "groupName": "search-indexes",
    "propertyName": "consistency.check.enabled",
    "propertyValue": "true",
    "propertyType": "BOOLEAN",
    "description": "Flag to enable lucene indexes periodic consistency check"
  },
  {
    "groupName": "task-scheduler",
    "propertyName": "component.analysis.cache.clear.cadence",
    "propertyValue": "24",
    "propertyType": "INTEGER",
    "description": "Cleanup cadence (in hours) for component vulnerability analysis cache"
  },
  {
    "groupName": "task-scheduler",
    "propertyName": "ghsa.mirror.cadence",
    "propertyValue": "24",
    "propertyType": "INTEGER",
    "description": "Mirror cadence (in hours) for Github Security Advisories"
  },
  {
    "groupName": "task-scheduler",
    "propertyName": "internal.components.identification.cadence",
    "propertyValue": "6",
    "propertyType": "INTEGER",
    "description": "Internal component identification cadence (in hours)"
  },
  {
    "groupName": "task-scheduler",
    "propertyName": "ldap.sync.cadence",
    "propertyValue": "6",
    "propertyType": "INTEGER",
    "description": "Sync cadence (in hours) for LDAP"
  },
  {
    "groupName": "task-scheduler",
    "propertyName": "nist.mirror.cadence",
    "propertyValue": "24",
    "propertyType": "INTEGER",
    "description": "Mirror cadence (in hours) for NVD database"
  },
  {
    "groupName": "task-scheduler",
    "propertyName": "osv.mirror.cadence",
    "propertyValue": "24",
    "propertyType": "INTEGER",
    "description": "Mirror cadence (in hours) for OSV database"
  },
  {
    "groupName": "task-scheduler",
    "propertyName": "portfolio.metrics.update.cadence",
    "propertyValue": "1",
    "propertyType": "INTEGER",
    "description": "Update cadence (in hours) for portfolio metrics"
  },
  {
    "groupName": "task-scheduler",
    "propertyName": "portfolio.vulnerability.analysis.cadence",
    "propertyValue": "24",
    "propertyType": "INTEGER",
    "description": "Launch cadence (in hours) for portfolio vulnerability analysis"
  },
  {
    "groupName": "task-scheduler",
    "propertyName": "repository.metadata.fetch.cadence",
    "propertyValue": "24",
    "propertyType": "INTEGER",
    "description": "Metadada fetch cadence (in hours) for package repositories"
  },
  {
    "groupName": "task-scheduler",
    "propertyName": "vulndb.mirror.cadence",
    "propertyValue": "24",
    "propertyType": "INTEGER",
    "description": "Mirror cadence (in hours) for VulnDB database"
  },
  {
    "groupName": "task-scheduler",
    "propertyName": "vulnerability.metrics.update.cadence",
    "propertyValue": "1",
    "propertyType": "INTEGER",
    "description": "Update cadence (in hours) for vulnerability metrics"
  },
  {
    "groupName": "telemetry",
    "propertyName": "last.submission.data",
    "propertyValue": "{\"system_id\":\"e81132d9-8039-40ea-bcb4-e084d87a86ca\",\"dt_version\":\"4.14.2\",\"db_type\":\"PostgreSQL\",\"db_version\":\"17.10\"}",
    "propertyType": "STRING",
    "description": "Data of the last telemetry submission"
  },
  {
    "groupName": "telemetry",
    "propertyName": "last.submission.epoch.seconds",
    "propertyValue": "1780929252",
    "propertyType": "INTEGER",
    "description": "Timestamp of the last telemetry submission in epoch seconds"
  },
  {
    "groupName": "telemetry",
    "propertyName": "submission.enabled",
    "propertyValue": "true",
    "propertyType": "BOOLEAN",
    "description": "Whether submission of telemetry data is enabled"
  },
  {
    "groupName": "vuln-source",
    "propertyName": "epss.enabled",
    "propertyValue": "true",
    "propertyType": "BOOLEAN",
    "description": "Flag to enable/disable Exploit Prediction Scoring System"
  },
  {
    "groupName": "vuln-source",
    "propertyName": "epss.feeds.url",
    "propertyValue": "https://epss.cyentia.com",
    "propertyType": "URL",
    "description": "A base URL pointing to the hostname and path of the EPSS feeds"
  },
  {
    "groupName": "vuln-source",
    "propertyName": "github.advisories.access.token",
    "propertyType": "STRING",
    "description": "The access token used for GitHub API authentication"
  },
  {
    "groupName": "vuln-source",
    "propertyName": "github.advisories.alias.sync.enabled",
    "propertyValue": "true",
    "propertyType": "BOOLEAN",
    "description": "Flag to enable/disable alias synchronization for GitHub Advisories"
  },
  {
    "groupName": "vuln-source",
    "propertyName": "github.advisories.api.url",
    "propertyValue": "https://api.github.com/graphql",
    "propertyType": "STRING",
    "description": "URL of the GitHub GraphQL API"
  },
  {
    "groupName": "vuln-source",
    "propertyName": "github.advisories.enabled",
    "propertyValue": "false",
    "propertyType": "BOOLEAN",
    "description": "Flag to enable/disable GitHub Advisories"
  },
  {
    "groupName": "vuln-source",
    "propertyName": "github.advisories.last.modified.epoch.seconds",
    "propertyType": "INTEGER",
    "description": "Epoch timestamp in seconds of the latest observed GHSA modification time"
  },
  {
    "groupName": "vuln-source",
    "propertyName": "google.osv.alias.sync.enabled",
    "propertyValue": "false",
    "propertyType": "BOOLEAN",
    "description": "Flag to enable/disable alias synchronization for OSV"
  },
  {
    "groupName": "vuln-source",
    "propertyName": "google.osv.base.url",
    "propertyValue": "https://osv-vulnerabilities.storage.googleapis.com/",
    "propertyType": "URL",
    "description": "A base URL pointing to the hostname and path for OSV mirroring"
  },
  {
    "groupName": "vuln-source",
    "propertyName": "google.osv.enabled",
    "propertyValue": "Maven;RubyGems;openEuler;CRAN;PyPI;TuxCare;Mageia;UVI;Wolfi;Azure Linux;Packagist;SUSE;[EMPTY];openSUSE;MinimOS;AlmaLinux;Pub;CleanStart;Ubuntu;Bitnami;Root;Red Hat;Alpine;npm;crates.io;NuGet;Android;Rocky Linux;Linux;BellSoft Hardened Containers;Alpaquita;VSCode;Chainguard;opam;SwiftURL",
    "propertyType": "STRING",
    "description": "List of enabled ecosystems to mirror OSV"
  },
  {
    "groupName": "vuln-source",
    "propertyName": "nvd.api.download.feeds",
    "propertyValue": "false",
    "propertyType": "BOOLEAN",
    "description": "Whether to download feed files even though mirroring via REST API is enabled"
  },
  {
    "groupName": "vuln-source",
    "propertyName": "nvd.api.enabled",
    "propertyValue": "false",
    "propertyType": "BOOLEAN",
    "description": "Whether to enable NVD mirroring via REST API"
  },
  {
    "groupName": "vuln-source",
    "propertyName": "nvd.api.key",
    "propertyValue": "HiddenDecryptedPropertyPlaceholder",
    "propertyType": "ENCRYPTEDSTRING",
    "description": "API key for the NVD REST API"
  },
  {
    "groupName": "vuln-source",
    "propertyName": "nvd.api.last.modified.epoch.seconds",
    "propertyValue": "0",
    "propertyType": "INTEGER",
    "description": "Epoch timestamp in seconds of the latest observed CVE modification time"
  },
  {
    "groupName": "vuln-source",
    "propertyName": "nvd.api.url",
    "propertyValue": "https://services.nvd.nist.gov/rest/json/cves/2.0",
    "propertyType": "URL",
    "description": "REST API URL for the NVD's CVE API 2.0"
  },
  {
    "groupName": "vuln-source",
    "propertyName": "nvd.enabled",
    "propertyValue": "true",
    "propertyType": "BOOLEAN",
    "description": "Flag to enable/disable National Vulnerability Database"
  },
  {
    "groupName": "vuln-source",
    "propertyName": "nvd.feeds.url",
    "propertyValue": "https://nvd.nist.gov/feeds",
    "propertyType": "URL",
    "description": "A base URL pointing to the hostname and path of the NVD feeds"
  }
]
(venv) kali@kali-RedmiBook-16:~/Desktop/oss_checks$ curl -s "http://localhost:8081/api/v1/team" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM" | jq '[.[] | {name: .name, permissions: [.permissions[].name]}]'
[
  {
    "name": "Administrators",
    "permissions": [
      "ACCESS_MANAGEMENT",
      "BOM_UPLOAD",
      "POLICY_MANAGEMENT",
      "POLICY_VIOLATION_ANALYSIS",
      "PORTFOLIO_MANAGEMENT",
      "PROJECT_CREATION_UPLOAD",
      "SYSTEM_CONFIGURATION",
      "TAG_MANAGEMENT",
      "VIEW_BADGES",
      "VIEW_POLICY_VIOLATION",
      "VIEW_PORTFOLIO",
      "VIEW_VULNERABILITY",
      "VULNERABILITY_ANALYSIS",
      "VULNERABILITY_MANAGEMENT"
    ]
  },
  {
    "name": "Automation",
    "permissions": [
      "BOM_UPLOAD",
      "VIEW_PORTFOLIO"
    ]
  },
  {
    "name": "Badge Viewers",
    "permissions": [
      "VIEW_BADGES"
    ]
  },
  {
    "name": "Portfolio Managers",
    "permissions": [
      "PORTFOLIO_MANAGEMENT",
      "VIEW_PORTFOLIO"
    ]
  }
]
