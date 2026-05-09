# OpenAI-Compatible Embeddings Troubleshooting Index

Embedding failures are often caused by a different set of assumptions than chat failures. A chat request can work while embeddings still fail because the app uses a separate endpoint, model, request body, or vector dimension.

Use this index when an app reports embedding errors with an OpenAI-compatible provider.

## Fast Triage

Check these items first:

- The app supports a separate embeddings base URL, or it clearly reuses the chat base URL for `/embeddings`.
- The configured embedding model exists on the target provider.
- The vector store dimension matches the embedding model output dimension.
- The app does not hardcode `text-embedding-3-small` when a custom model is configured.
- The app does not send provider-specific fields such as `encoding_format: null` if the endpoint rejects them.
- The endpoint returns the OpenAI embeddings shape: `data[0].embedding` as an array of numbers.

## Useful Guides

- [OpenAI-compatible embeddings endpoint checklist](openai-compatible-embeddings-endpoint.md)
- [Separate chat and embeddings endpoints](separate-chat-and-embeddings-endpoints.md)
- [Troubleshoot embeddings encoding_format null errors](troubleshoot-embeddings-encoding-format-null.md)
- [Base URL path joining rules](base-url-path-joining-rules.md)

## Minimal Smoke Test

```bash
export APINODE_API_KEY="your_api_key"
export APINODE_BASE_URL="https://apinode.pro"
export APINODE_EMBEDDING_MODEL="text-embedding-3-small"

curl "$APINODE_BASE_URL/embeddings" \
  -H "Authorization: Bearer $APINODE_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"model\":\"$APINODE_EMBEDDING_MODEL\",\"input\":\"embedding smoke test\"}"
```

If this works but the app fails, the bug is probably in the app's config plumbing, model override, request body, or vector-store dimension handling.

## Maintainer Checklist

For app maintainers, the most useful provider-neutral fixes are:

- Accept `OPENAI_BASE_URL` or an app-specific equivalent.
- Accept a separate `EMBEDDINGS_BASE_URL` when chat and embeddings are routed differently.
- Accept a separate `EMBEDDINGS_MODEL`.
- Log the resolved provider, base URL host, model name, and vector dimension at startup without logging secrets.
- Fail fast when the configured vector dimension does not match the stored index dimension.

