(venv) kali@kali-RedmiBook-16:~/Desktop/oss_checks$ curl -s "http://localhost:8081/api/v1/finding/project/16397239-aff6-4559-a954-a47b592b33df" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM" | jq length
0
(venv) kali@kali-RedmiBook-16:~/Desktop/oss_checks$ curl -s "http://localhost:8081/api/v1/configProperty/aggregate" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM" | jq '[.[] | select(.groupName == "analyzer")]'
(venv) kali@kali-RedmiBook-16:~/Desktop/oss_checks$ 
