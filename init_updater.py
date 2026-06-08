$ sudo docker compose logs dtrack-apiserver --tail=50 | grep -iE "numpy|pypi|osv|nvd|mirror|error|warn"
[sudo] password for kali: 
no configuration file provided: not found
(venv) kali@kali-RedmiBook-16:~/Desktop/oss_checks$ curl -s "http://localhost:8081/api/v1/vulnerability?pageSize=5&source=OSV" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM" | jq '[.[] | {vulnId: .vulnId, source: .source}]'
[
  {
    "vulnId": "CVE-2026-0544",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21428",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21436",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21437",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0546",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0547",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0565",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0566",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0567",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0568",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21429",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0569",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0570",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21430",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21431",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21432",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21433",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21440",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21444",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0571",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21445",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21446",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21447",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21448",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21449",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21450",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21451",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21452",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21483",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21484",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21644",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21645",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21646",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21647",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21648",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21649",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21650",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21651",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21652",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0574",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0575",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0576",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0577",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0578",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0579",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0580",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0581",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0582",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0583",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0584",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0585",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0586",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0587",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0588",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0589",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0590",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0591",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0592",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0597",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21633",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21634",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21635",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0605",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0621",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0625",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0606",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0607",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21439",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21507",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21673",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21674",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21675",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0604",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21485",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21486",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21487",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21676",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21677",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21744",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21745",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21746",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21747",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21748",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21749",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21750",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21411",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21488",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21489",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21493",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0640",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0641",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21490",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21491",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21494",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-21492",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0628",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0642",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0643",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0649",
    "source": "NVD"
  },
  {
    "vulnId": "CVE-2026-0650",
    "source": "NVD"
  }
]
(venv) kali@kali-RedmiBook-16:~/Desktop/oss_checks$ curl -s "http://localhost:8081/api/v1/component/project/16397239-aff6-4559-a954-a47b592b33df" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM" | jq '[.[] | {name: .name, version: .version, purl: .purl}]'
[
  {
    "name": "numpy",
    "version": "1.19.0",
    "purl": "pkg:pypi/numpy@1.19.0"
  }
]
(venv) kali@kali-RedmiBook-16:~/Desktop/oss_checks$ 
