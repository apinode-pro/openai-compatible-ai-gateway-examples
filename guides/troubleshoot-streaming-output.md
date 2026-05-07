# Troubleshoot Streaming Output With API NODE

Streaming issues are usually client-side parsing or endpoint-mode mismatches.

## First test non-streaming

```bash
curl "https://apinode.pro/responses" \
  -H "Authorization: Bearer $APINODE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-5.5","input":"Say hello"}'
```

If non-streaming fails, fix authentication, base URL, model, or payload first.

## Then test streaming

```bash
curl -N "https://apinode.pro/responses" \
  -H "Authorization: Bearer $APINODE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-5.5","input":"Say hello","stream":true}'
```

## Common causes

- The tool expects Chat Completions stream events but is calling the Responses API.
- A proxy buffers server-sent events.
- CI logs hide or truncate streaming output.
- The client waits for a final text field instead of consuming stream events.
- The request times out before the stream finishes.

## Practical workaround

For smoke tests and CI, use non-streaming requests. Add streaming only after the basic request path is stable.
