# Troubleshoot Runtime Config Not Applied

Use this when an app saves a custom OpenAI-compatible base URL in settings, but runtime traffic still goes to `api.openai.com`.

## Symptom

The user can prove the endpoint works:

- Direct `curl` succeeds.
- Another client using the same key and base URL succeeds.
- The app UI shows the custom provider settings as saved.

But runtime requests still go to:

```text
https://api.openai.com/...
```

## Likely Cause

The saved settings and runtime client are using different provider records, state stores, or code paths.

Common examples:

- Settings dialog writes a custom provider object, but task execution reads the default OpenAI provider.
- Chat uses custom settings, but title generation, planning, templates, or background jobs create a separate OpenAI client.
- The UI stores `baseURL`, but runtime expects `baseUrl`.
- A restart is needed because the server loaded provider config only at boot.
- The app has both "OpenAI" and "OpenAI Compatible" providers and silently falls back to "OpenAI".

## Debug Log To Add

Log this right before the request is sent. Redact secrets.

```text
provider_id:
provider_protocol:
base_url_host_and_path:
request_path:
model:
api_key_source:
runtime_component:
```

Do not log API keys, bearer headers, full account URLs with secrets, or request bodies that may contain private user data.

## Minimal Reproduction

```bash
export OPENAI_API_KEY="redacted"
export OPENAI_BASE_URL="https://example.com/v1"
export OPENAI_MODEL="model-id"

curl "$OPENAI_BASE_URL/chat/completions" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"model\":\"$OPENAI_MODEL\",\"messages\":[{\"role\":\"user\",\"content\":\"Reply OK\"}]}"
```

If this succeeds but the app still calls `api.openai.com`, the fix is probably in config propagation, not provider compatibility.

## Maintainer Fix Pattern

- Store provider protocol, base URL, model, and key reference together.
- Pass the selected provider id into every runtime path that creates an LLM client.
- Add a regression test proving the runtime request URL uses the saved custom base URL.
- Add one test for secondary paths such as background summaries, title generation, embeddings, and templates.

