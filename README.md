6-06-30/OpenSearch__3.6.0/unpacked/extracted/d1_jacocoagent.jar_98342db592
[*] Распаковываю: /home/kali/Desktop/results/2026-06-30/OpenSearch__3.6.0/unpacked/extracted/d0_okhttp-4.12.0.jar_68e5626e8a/okhttp3/internal/publicsuffix/publicsuffixes.gz -> /home/kali/Desktop/results/2026-06-30/OpenSearch__3.6.0/unpacked/extracted/d1_publicsuffixes.gz_9be0cbb791
[*] Распаковываю: /home/kali/Desktop/results/2026-06-30/OpenSearch__3.6.0/unpacked/extracted/d0_opensearch-ml-algorithms-3.6.0.0.jar_f9abc2f976/analysis/bert-uncased.zip -> /home/kali/Desktop/results/2026-06-30/OpenSearch__3.6.0/unpacked/extracted/d1_bert-uncased.zip_e1491dbe99
[*] Распаковываю: /home/kali/Desktop/results/2026-06-30/OpenSearch__3.6.0/unpacked/extracted/d0_opensearch-ml-algorithms-3.6.0.0.jar_f9abc2f976/analysis/mbert-uncased.zip -> /home/kali/Desktop/results/2026-06-30/OpenSearch__3.6.0/unpacked/extracted/d1_mbert-uncased.zip_efa94c63ea
[*] Распаковываю: /home/kali/Desktop/results/2026-06-30/OpenSearch__3.6.0/unpacked/extracted/d0_okhttp-4.12.0.jar_e1383c43f2/okhttp3/internal/publicsuffix/publicsuffixes.gz -> /home/kali/Desktop/results/2026-06-30/OpenSearch__3.6.0/unpacked/extracted/d1_publicsuffixes.gz_1b87e3a80e
[*] Распаковываю: /home/kali/Desktop/results/2026-06-30/OpenSearch__3.6.0/unpacked/extracted/d1_org.jacoco.agent-0.8.14.jar_40809529a6/jacocoagent.jar -> /home/kali/Desktop/results/2026-06-30/OpenSearch__3.6.0/unpacked/extracted/d2_jacocoagent.jar_e369d3ddfc
[*] Распаковываю: /home/kali/Desktop/results/2026-06-30/OpenSearch__3.6.0/unpacked/extracted/d1_okhttp-4.12.0.jar_6c7055d065/okhttp3/internal/publicsuffix/publicsuffixes.gz -> /home/kali/Desktop/results/2026-06-30/OpenSearch__3.6.0/unpacked/extracted/d2_publicsuffixes.gz_0bdc7ef5ad
[*] Распаковываю: /home/kali/Desktop/results/2026-06-30/OpenSearch__3.6.0/unpacked/extracted/d1_opensearch-ml-algorithms-3.6.0.0.jar_939f9eadac/analysis/bert-uncased.zip -> /home/kali/Desktop/results/2026-06-30/OpenSearch__3.6.0/unpacked/extracted/d2_bert-uncased.zip_561aae161d
[*] Распаковываю: /home/kali/Desktop/results/2026-06-30/OpenSearch__3.6.0/unpacked/extracted/d1_opensearch-ml-algorithms-3.6.0.0.jar_939f9eadac/analysis/mbert-uncased.zip -> /home/kali/Desktop/results/2026-06-30/OpenSearch__3.6.0/unpacked/extracted/d2_mbert-uncased.zip_18751d9266
[*] Распаковываю: /home/kali/Desktop/results/2026-06-30/OpenSearch__3.6.0/unpacked/extracted/d1_okhttp-4.12.0.jar_911cdb0fa9/okhttp3/internal/publicsuffix/publicsuffixes.gz -> /home/kali/Desktop/results/2026-06-30/OpenSearch__3.6.0/unpacked/extracted/d2_publicsuffixes.gz_07a1e6fa7c
[*] Распаковано архивов: 1731
[*] Извлечено файлов: 669805
[*] Скопировано обычных файлов верхнего уровня: 2682
[!] Ошибок распаковки: 2
[*] Статистика распаковки: /home/kali/Desktop/results/2026-06-30/OpenSearch__3.6.0/debug/distrib/repack.stats.json
[*] Запускаю Trivy:
    trivy fs --format cyclonedx --output /home/kali/Desktop/results/2026-06-30/OpenSearch__3.6.0/sbom/repack.cdx.json /home/kali/Desktop/results/2026-06-30/OpenSearch__3.6.0/unpacked
2026-06-30T13:14:04+03:00	INFO	"--format cyclonedx" disables security scanning. Specify "--scanners vuln" explicitly if you want to include vulnerabilities in the "cyclonedx" report.
2026-06-30T13:14:05+03:00	WARN	[pom] Dependency version cannot be determined. Child dependencies will not be found.	details="https://trivy.dev/docs/v0.68/guide/coverage/language/java#empty-dependency-version"

📣 Notices:
  - Version 0.72.0 of Trivy is now available, current version is 0.68.2

To suppress version checks, run Trivy scans with the --skip-version-check flag

2026-06-30T13:19:04+03:00	WARN	Provide a higher timeout value, see https://trivy.dev/docs/v0.68/guide/references/troubleshooting#timeout
2026-06-30T13:19:04+03:00	FATAL	Fatal error	run error: fs scan error: scan error: scan failed: failed analysis: analyze error: analyzer timed out: extracted/d1_compiler-0.9.3.jar_47ba0d8e7b/META-INF/maven/com.github.spullara.mustache.java/compiler/pom.xml parse error: failed to parse extracted/d1_compiler-0.9.3.jar_47ba0d8e7b/META-INF/maven/com.github.spullara.mustache.java/compiler/pom.xml: failed to parse extracted/d1_compiler-0.9.3.jar_47ba0d8e7b/META-INF/maven/com.github.spullara.mustache.java/compiler/pom.xml: analyze error (/home/kali/Desktop/results/2026-06-30/OpenSearch__3.6.0/unpacked/extracted/d1_compiler-0.9.3.jar_47ba0d8e7b/META-INF/maven/com.github.spullara.mustache.java/compiler/pom.xml): pom resolve error: parent error: 2 errors occurred:
	* stat /home/kali/Desktop/results/2026-06-30/OpenSearch__3.6.0/unpacked/extracted/d1_compiler-0.9.3.jar_47ba0d8e7b/META-INF/maven/com.github.spullara.mustache.java/pom.xml: no such file or directory
	* fetch repository error: Get "http://maven.twttr.com/com/github/spullara/mustache/java/mustache.java/0.9.3/mustache.java-0.9.3.pom": context deadline exceeded


error: trivy exited with code 1

[binary-repack] sbom_repack_deps.py exited with code 1

[binary-repack] Done.
  binary SBOM : /home/kali/Desktop/results/2026-06-30/OpenSearch__3.6.0/sbom/binary.json
  repack SBOM : /home/kali/Desktop/results/2026-06-30/OpenSearch__3.6.0/sbom/repack.cdx.json
  debug files : /home/kali/Desktop/results/2026-06-30/OpenSearch__3.6.0/debug/distrib/
[scan-full] binary-repack step finished with code 1 — checking produced files
[scan-full] warning: binary SBOM was not produced: /home/kali/Desktop/results/2026-06-30/OpenSearch__3.6.0/sbom/binary.json
[scan-full] warning: repack SBOM was not produced: /home/kali/Desktop/results/2026-06-30/OpenSearch__3.6.0/sbom/repack.cdx.json

[scan-full] No SBOM files produced — nothing to merge
2026-06-30 13:19:07 | ERROR   | [distrib] [OpenSearch__3.6.0__opensearch] scan failed rc=1
2026-06-30 13:19:07 | INFO    | [distrib] all distrib threads finished
2026-06-30 13:19:07 | INFO    | run log written: /home/kali/Desktop/results/2026-06-30/run.log
2026-06-30 13:19:07 | INFO    | all 1 scan(s) completed successfully
(venv) kali@kali-VirtualBox:~/Desktop/oss_checks$ cd /home/kali/Desktop/results/2026-06-30/OpenSearch__3.6.0/sbom/
(venv) kali@kali-VirtualBox:~/Desktop/results/2026-06-30/OpenSearch__3.6.0/sbom$ ls
debug  origsbom.json  sbom-clean.json
(venv) kali@kali-VirtualBox:~/Desktop/results/2026-06-30/OpenSearch__3.6.0/sbom$ 
