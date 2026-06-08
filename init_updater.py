Access-Control-Allow-Headers: Origin, Content-Type, Authorization, X-Requested-With, Content-Length, Accept, Origin, X-Api-Key, X-Total-Count, *
Access-Control-Expose-Headers: Origin, Content-Type, Authorization, X-Requested-With, Content-Length, Accept, Origin, X-Api-Key, X-Total-Count
(venv) kali@kali-RedmiBook-16:~/Desktop/oss_checks$ curl -X POST "http://localhost:8081/api/v1/finding/project/16397239-aff6-4559-a954-a47b592b33df/analyze" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM"
{"token":"b2551e5c-52a3-4089-9956-841685c33193"}(vencurl -s "http://localhost:8081/api/v1/analyzer" \url -s "http://localhost:8081/api/v1/analyzer" \
  -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM"
(venv) kali@kali-RedmiBook-16:~/Desktop/oss_checks$ curl -s "http://localhost:8081/api/v1/analyzer"   -H "X-Api-Key: odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM"
(venv) kali@kali-RedmiBook-16:~/Desktop/oss_checks$ 

