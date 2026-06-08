curl -s http://localhost:8080/api/v1/metrics/vulnerability \
  -H "X-Api-Key: $ADMIN_KEY" | jq '{
    nvd:      .nvd,
    github:   .github,
    osv:      .osv,
    internal: .internal
  }'
