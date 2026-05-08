# Troubleshoot Custom OpenAI Endpoint Configuration

Custom OpenAI-compatible endpoint bugs usually come from one of three fields not being passed through correctly:

```json
{
  "baseURL": "https://apinode.pro",
  "apiKey": "<your_api_key>",
  "model": "gpt-5.5"
}
```

Use this checklist when a tool says the endpoint is missing, the API key is missing, or the model is not found.

## 1. Confirm the Base URL Is Only the Base URL

Use:

```text
https://apinode.pro
```

Do not use a full request path as the base URL unless the tool explicitly asks for a full endpoint:

```text
https://apinode.pro/responses
```

Most clients append the request path themselves.

## 2. Confirm the API Key Reaches the Runtime

Many apps store provider settings in UI state, but the underlying runtime reads a different environment variable or config key.

Check both layers:

```text
UI/provider config: apiKey or token is set
Runtime config: the launched process receives the same key
```

For local smoke tests:

```bash
test -n "$APINODE_API_KEY" && echo "APINODE_API_KEY is set"
```

Do not print the key itself.

## 3. Confirm the Actual Model ID

Use `gpt-5.5` as the model ID:

```text
Display name: API NODE GPT-5.5
Model ID:     gpt-5.5
```

Do not send the display name as the model ID unless the tool documents that behavior.

## 4. Check Endpoint Mode

API NODE examples use the Responses API:

```text
Base URL: https://apinode.pro
Path:     /responses
Model:    gpt-5.5
```

If the tool only supports Chat Completions, verify the expected payload shape before reusing a Responses API example.

## 5. Minimal Direct Test

Run a direct request outside the app:

```bash
curl "https://apinode.pro/responses" \
  -H "Authorization: Bearer $APINODE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-5.5","input":"Say hello"}'
```

If this works but the app fails, the issue is probably in how the app maps provider settings into the underlying client or process.

## Common Symptoms

| Symptom | Likely Cause |
|---|---|
| Endpoint missing | Base URL field is not propagated to the runtime client. |
| Missing API key or token | UI config has the key, but the spawned process reads a different env/config key. |
| 404 | Full endpoint path was used as a base URL, or the client appended the wrong path. |
| Model not found | Display label was sent instead of the model ID. |
| Streaming fails | Client and endpoint disagree on stream event format. |

## Safe Issue Report Template

When reporting a bug to a tool maintainer, include only redacted fields:

```text
Tool:
Base URL: https://apinode.pro
Model: gpt-5.5
Endpoint mode: Responses API
Error: <redacted error>
API key: redacted, confirmed present in runtime
```

Never include API keys, account IDs, billing data, or private logs.
