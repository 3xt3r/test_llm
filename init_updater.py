curl -s "http://localhost:8081/api/v1/vulnerability?pageSize=1&source=NVD" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM" \
  -I | grep -i "x-total-count"

curl -s "http://localhost:8081/api/v1/vulnerability?pageSize=1&source=GITHUB" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM" \
  -I | grep -i "x-total-count"

curl -s "http://localhost:8081/api/v1/vulnerability?pageSize=1&source=OSV" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM" \
  -I | grep -i "x-total-count"
