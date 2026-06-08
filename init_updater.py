(venv) kali@kali-RedmiBook-16:~/Desktop/oss_checks$ curl -s "http://localhost:8081/api/v1/vulnerability?pageSize=1&source=NVD" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM" \
  -I | grep -i "x-total-count"

curl -s "http://localhost:8081/api/v1/vulnerability?pageSize=1&source=GITHUB" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM" \
  -I | grep -i "x-total-count"

curl -s "http://localhost:8081/api/v1/vulnerability?pageSize=1&source=OSV" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM" \
  -I | grep -i "x-total-count"
X-Total-Count: 355986
Access-Control-Allow-Headers: Origin, Content-Type, Authorization, X-Requested-With, Content-Length, Accept, Origin, X-Api-Key, X-Total-Count, *
Access-Control-Expose-Headers: Origin, Content-Type, Authorization, X-Requested-With, Content-Length, Accept, Origin, X-Api-Key, X-Total-Count
X-Total-Count: 355986
Access-Control-Allow-Headers: Origin, Content-Type, Authorization, X-Requested-With, Content-Length, Accept, Origin, X-Api-Key, X-Total-Count, *
Access-Control-Expose-Headers: Origin, Content-Type, Authorization, X-Requested-With, Content-Length, Accept, Origin, X-Api-Key, X-Total-Count
X-Total-Count: 355986
Access-Control-Allow-Headers: Origin, Content-Type, Authorization, X-Requested-With, Content-Length, Accept, Origin, X-Api-Key, X-Total-Count, *
Access-Control-Expose-Headers: Origin, Content-Type, Authorization, X-Requested-With, Content-Length, Accept, Origin, X-Api-Key, X-Total-Count
