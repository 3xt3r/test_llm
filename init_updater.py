sudo docker exec dependency-track-apiserver-1 \
  find / -name "application.properties" 2>/dev/null | head -5
[sudo] password for kali: 
/tmp/Dependency-Track-0_0_0_0-8080/webapp/WEB-INF/classes/application.properties
(venv) kali@kali-RedmiBook-16:~/Desktop/oss_checks$ sudo docker exec dependency-track-apiserver-1 \
  env | sort | grep -iE "osv|github|nvd|epss|google|mirror"
EPSS_ENABLED=true
GITHUB_ADVISORIES_ACCESS_TOKEN=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
GITHUB_ADVISORIES_ENABLED=true
GOOGLE_OSV_ENABLED=PyPI;npm;Maven;crates.io;NuGet;RubyGems;Go;Hex;Pub;Packagist
NVD_API_ENABLED=true
NVD_API_KEY=31DACAE2-4941-F111-836A-129478FCB64D
(venv) kali@kali-RedmiBook-16:~/Desktop/oss_checks$ 
