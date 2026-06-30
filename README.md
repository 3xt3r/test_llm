loads_transitive.json
11:37:22 [INFO] pipeline finished successfully
11:37:22 [INFO] artifacts directory: /home/kali/Desktop/jobs/OpenSearch/jobs/a767bfeacc0546949f47dee90ad3bcb6
2026-06-30 11:37:22 | INFO    |   moving results: /home/kali/Desktop/jobs/OpenSearch/jobs/a767bfeacc0546949f47dee90ad3bcb6 -> /home/kali/Desktop/results/2026-06-30/OpenSearch__3.7.0
2026-06-30 11:37:23 | INFO    | [distrib] started thread for OpenSearch / 3.7.0 / opensearch
2026-06-30 11:37:23 | INFO    |   [OK] OpenSearch / 3.7.0 -> /home/kali/Desktop/results/2026-06-30/OpenSearch__3.7.0
2026-06-30 11:37:23 | WARNING | [distrib] [OpenSearch__3.7.0__opensearch] scan_dir not found: /home/kali/Desktop/opensearch-3.6.0-linux-x64.tar.gz — skipping
2026-06-30 11:37:23 | INFO    | [distrib] waiting for 1 distrib thread(s) to finish...
2026-06-30 11:37:23 | INFO    | [distrib] all distrib threads finished
2026-06-30 11:37:23 | INFO    | run log written: /home/kali/Desktop/results/2026-06-30/run.log
2026-06-30 11:37:23 | INFO    | all 1 scan(s) completed successfully
(venv) kali@kali-VirtualBox:~/Desktop/oss_checks$ cd ..
(venv) kali@kali-VirtualBox:~/Desktop$ ls /home/kali/Desktop/opensearch-3.6.0-linux-x64.tar.gz
/home/kali/Desktop/opensearch-3.6.0-linux-x64.tar.gz
(venv) kali@kali-VirtualBox:~/Desktop$ 

scanner_py: /home/kali/Desktop/oss_checks/scanner.py
work_dir: /home/kali/Desktop/jobs
results_dir: /home/kali/Desktop/results
env_file: /home/kali/Desktop/oss_checks/env

products:
  - name: OpenSearch
    versions:
      - version: "3.7.0"
        repos:
          - url: https://github.com/opensearch-project/OpenSearch
            branch: 3.7.0
            dir: OpenSearch
        distribs:
          - name: opensearch
            scan_dir: /home/kali/Desktop/opensearch-3.6.0-linux-x64.tar.gz
  # Пример с distribs + images для одного продукта
  # - name: myproduct
  #   versions:
  #     - version: "1.2.3"
  #       repos:
  #         - url: https://github.com/org/myproduct.git
  #           branch: v1.2.3
  #           dir: myproduct
  #       distribs:
  #         - name: alt-linux
  #           scan_dir: /data/packages/myproduct-1.2.3/
  #           cve_branch: c10f2
  #       images:
  #         - name: myproduct-app         # имя для отчёта
  #           image: myproduct:1.2.3      # docker image ref (уже загружен в daemon)
  #           cve_branch: c10f2
  #         - name: myproduct-app-archive # путь к .tar / .tar.gz / .tgz от docker save
  #           image: /data/images/myproduct-1.2.3.tar.gz
  #           cve_branch: c10f2
