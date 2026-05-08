# OpenAI-Compatible Embeddings Endpoint Checklist

Many RAG systems and retrievers can call a remote embeddings service through an OpenAI-compatible endpoint.

This guide focuses on the endpoint contract, not a specific provider.

## Request Shape

Typical path:

```text
/openai/v1/embeddings
```

or:

```text
/v1/embeddings
```

Typical request body:

```json
{
  "model": "embedding-model-name",
  "input": ["hello", "world"]
}
```

Typical response shape:

```json
{
  "data": [
    { "embedding": [0.1, 0.2], "index": 0 },
    { "embedding": [0.3, 0.4], "index": 1 }
  ],
  "model": "embedding-model-name"
}
```

## Smoke Test

```bash
export EMBEDDINGS_BASE_URL="https://example.com/openai/v1"
export EMBEDDINGS_API_KEY="..."
export EMBEDDINGS_MODEL="embedding-model-name"

curl "$EMBEDDINGS_BASE_URL/embeddings" \
  -H "Authorization: Bearer $EMBEDDINGS_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"model\":\"$EMBEDDINGS_MODEL\",\"input\":[\"hello\",\"world\"]}"
```

## Client Checklist

- Keep the endpoint URL configurable.
- Keep the model name configurable.
- Preserve input order by `index`.
- Treat empty embeddings as an error.
- Surface HTTP errors with redacted headers.
- Do not log API keys or raw private documents.
- Include network round-trip time in retriever metrics.
- Keep a local/mock embeddings client for CI.

## App Maintainer Tests

Useful tests:

- Batch input preserves order.
- Single string and list inputs are both handled if your app supports both.
- Connection errors produce actionable messages.
- Provider errors redact auth headers.
- Empty `data` arrays fail clearly.

## Related Guides

- [Endpoint readiness checklist](endpoint-readiness-checklist.md)
- [Base URL path joining rules](base-url-path-joining-rules.md)
- [OpenAI-compatible environment variable patterns](openai-compatible-env-vars.md)
