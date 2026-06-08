url -s http://localhost:8080/api/v1/metrics/vulnerability \
  -H "X-Api-Key: $odt_WeFtwiB1_NVGyddcyg2GQTyOPHeQit6qMBNFnwxJM" | jq '{
    nvd:      .nvd,
    github:   .github,
    osv:      .osv,
    internal: .internal
  }'
jq: parse error: Invalid numeric literal at line 1, column 10
