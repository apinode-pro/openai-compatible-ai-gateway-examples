# Separate Chat and Embeddings Endpoints

Many apps support an OpenAI-compatible chat endpoint but forget to route embeddings through the same custom provider path. The result is confusing: chat works, while indexing, memory, or retrieval fails against `api.openai.com`.

## The Pattern

Treat chat and embeddings as separate provider surfaces.

```text
LLM provider:
  base_url
  api_key
  chat_model
  protocol

Embeddings provider:
  base_url
  api_key
  embedding_model
  dimensions
```

The UI can offer to copy the LLM endpoint into the embeddings endpoint, but the stored settings should remain separate.

## Why Separate Settings Help

Different endpoints may have different:

- Paths.
- Models.
- Dimensions.
- API key requirements.
- Timeouts.
- Batch limits.

For example, a local OpenAI-compatible chat server may use:

```text
http://host.docker.internal:1234/v1/chat/completions
```

The embeddings endpoint should be:

```text
http://host.docker.internal:1234/v1/embeddings
```

not:

```text
https://api.openai.com/v1/embeddings
```

## Minimal Embeddings Smoke Test

```bash
export EMBEDDINGS_BASE_URL="http://host.docker.internal:1234/v1"
export EMBEDDINGS_API_KEY="not-needed"
export EMBEDDINGS_MODEL="text-embedding-model"

curl "$EMBEDDINGS_BASE_URL/embeddings" \
  -H "Authorization: Bearer $EMBEDDINGS_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"model\":\"$EMBEDDINGS_MODEL\",\"input\":[\"hello\",\"world\"]}"
```

## App Maintainer Checklist

- Add a persisted embeddings provider enum value for OpenAI-compatible endpoints.
- Register embeddings settings in the same settings system as LLM settings.
- Allow blank or placeholder API keys for local endpoints when safe.
- Verify requests go to the configured embeddings base URL.
- Parse `data[*].embedding` in input order.
- Report vector dimension clearly.
- Redact keys and document text in logs.

## Regression Tests

Add tests for:

- Chat custom endpoint works.
- Embeddings custom endpoint works.
- Chat endpoint config does not silently override embeddings config.
- Embeddings request never falls back to `api.openai.com` when a custom base URL is configured.

## Related Guides

- [OpenAI-compatible embeddings endpoint checklist](openai-compatible-embeddings-endpoint.md)
- [Base URL path joining rules](base-url-path-joining-rules.md)
- [Endpoint readiness checklist](endpoint-readiness-checklist.md)
