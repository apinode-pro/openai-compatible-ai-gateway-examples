# Troubleshoot `encoding_format: null` on OpenAI-Compatible Embeddings

Some strict OpenAI-compatible embeddings endpoints reject this request field:

```json
{
  "encoding_format": null
}
```

They expect either:

```json
"encoding_format": "float"
```

or no `encoding_format` field at all.

## Symptom

The endpoint returns an error similar to:

```text
Expected 'float' | 'base64', received null
```

## Why It Happens

Some SDKs or gateway wrappers include optional parameters with a `null` value instead of omitting them. Strict providers validate the JSON body and reject `null`.

## Fix

For embeddings that should return float vectors, send:

```json
{
  "model": "embedding-model",
  "input": ["hello", "world"],
  "encoding_format": "float"
}
```

If your provider does not require the field, omitting it is also safer than sending `null`.

## Client Checklist

- Do not serialize optional fields with `null` values.
- Set `encoding_format` to `"float"` when the downstream endpoint validates it.
- Add a test that asserts the request body does not contain `encoding_format: null`.
- Keep provider-specific overrides close to request construction.

## Smoke Test

```bash
curl "$EMBEDDINGS_BASE_URL/embeddings" \
  -H "Authorization: Bearer $EMBEDDINGS_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"model\":\"$EMBEDDINGS_MODEL\",\"input\":[\"hello\"],\"encoding_format\":\"float\"}"
```

## Related Guides

- [OpenAI-compatible embeddings endpoint checklist](openai-compatible-embeddings-endpoint.md)
- [Separate chat and embeddings endpoints](separate-chat-and-embeddings-endpoints.md)
