# Troubleshoot an OpenAI-Compatible Endpoint Routed to the Wrong Provider

Use this when a custom OpenAI-compatible endpoint is configured, but the app behaves like it is calling a different provider protocol such as Anthropic Messages.

## Symptom

Common signs:

- The endpoint works with curl.
- The app sends a request to the custom base URL.
- The request body looks like Anthropic Messages instead of OpenAI Chat Completions or Responses API.
- The app has a generic "custom provider" setting, but no explicit OpenAI-compatible protocol option.

## Correct Mental Model

An endpoint URL is not enough. The app also needs to know the request protocol.

```text
Provider protocol + base URL + path + model
```

For OpenAI-compatible Chat Completions:

```text
protocol = openai-chat-completions
path     = /chat/completions
```

For OpenAI-compatible Responses API:

```text
protocol = openai-responses
path     = /responses
```

## Minimal Diagnosis

Send a direct request first:

```bash
curl "$APINODE_BASE_URL/responses" \
  -H "Authorization: Bearer $APINODE_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"model\":\"$APINODE_MODEL\",\"input\":\"Reply with OK\"}"
```

If this works but the app fails, inspect the app request log:

- Path used.
- JSON body shape.
- Auth header.
- Model value.
- Adapter or provider class selected by the app.

## Fix Pattern

Apps usually need a separate option such as:

```text
Provider protocol: OpenAI-compatible
Base URL: https://apinode.pro
Model: gpt-5.5
```

Then the app should route to the OpenAI-compatible adapter, not a provider-specific adapter.

## Implementation Checklist for App Maintainers

- Store provider protocol separately from provider display name.
- Keep `base_url` as the origin or API root, not a full operation path.
- Join paths in one place.
- Do not infer protocol from model name alone.
- Add one smoke test that asserts the OpenAI-compatible adapter emits the expected path and body shape.

## Related Guides

- [Endpoint readiness checklist](endpoint-readiness-checklist.md)
- [Troubleshoot custom OpenAI endpoint configuration](troubleshoot-custom-openai-endpoint.md)
- [Troubleshoot Responses API vs Chat Completions](troubleshoot-responses-api-vs-chat-completions.md)
