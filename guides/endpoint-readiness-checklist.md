# OpenAI-Compatible Endpoint Readiness Checklist

Use this checklist before wiring a custom OpenAI-compatible endpoint into an app, coding agent, or CI job.

Default API NODE values:

```text
Base URL: https://apinode.pro
Model:    gpt-5.5
API:      OpenAI Responses API
```

## 1. Verify the Endpoint Directly

Start outside the app. A direct request removes UI, SDK, and config-loading variables.

```bash
export APINODE_API_KEY="your_api_key"
export APINODE_BASE_URL="https://apinode.pro"
export APINODE_MODEL="gpt-5.5"

curl "$APINODE_BASE_URL/responses" \
  -H "Authorization: Bearer $APINODE_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"model\":\"$APINODE_MODEL\",\"input\":\"Reply with READY\"}"
```

Expected result:

- HTTP 200.
- Non-empty text output.
- No API key, model, or path error.

## 2. Confirm the API Family

Responses API and Chat Completions use different paths and response shapes.

```text
Responses API:        /responses
Chat Completions API: /v1/chat/completions or /chat/completions
```

Do not pass a Chat Completions payload to `/responses`, and do not pass a Responses payload to `/chat/completions`.

## 3. Check Base URL Joining

Many bugs come from double paths.

Good:

```text
base_url = https://apinode.pro
request  = /responses
```

Risky:

```text
base_url = https://apinode.pro/responses
request  = /responses
```

That can produce:

```text
https://apinode.pro/responses/responses
```

## 4. Check Auth Propagation

Confirm the same API key reaches the exact client used by the feature you are testing.

This matters when an app has separate clients for:

- Chat.
- Reasoning models.
- Embeddings.
- Image generation.
- Template generation.
- Background jobs.

If one path works and another returns `Incorrect API key`, the failing path may be ignoring the custom endpoint config.

## 5. Check Model Names

Use the model identifier expected by the endpoint, not the display name shown in a UI.

For API NODE:

```text
gpt-5.5
```

If the app rewrites model names, test with a raw request first and then compare the app logs.

## 6. Add One App Integration at a Time

After the direct request works:

1. Add the base URL.
2. Add the API key through the app's normal secret mechanism.
3. Add the model.
4. Run one non-streaming request.
5. Add streaming only after the basic request works.

That sequence keeps failures easy to isolate.

## Related Guides

- [Troubleshoot 401 invalid API key](troubleshoot-401-invalid-api-key.md)
- [Troubleshoot 404 base URL issues](troubleshoot-404-base-url.md)
- [Troubleshoot Responses API vs Chat Completions](troubleshoot-responses-api-vs-chat-completions.md)
