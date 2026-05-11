# Provider Abstraction for Custom OpenAI-Compatible Endpoints

Use this checklist when an app currently assumes one OpenAI client but users ask
for local, enterprise, Azure, LiteLLM, LM Studio, or gateway-backed endpoints.

## Minimal Fix

Create one provider configuration object and pass it to every model call:

```text
provider:
  kind: openai-compatible
  base_url: https://gateway.example.com/v1
  api_key_env: OPENAI_API_KEY
  model: gpt-5.5
  extra_headers: {}
```

The application should not build URLs or credentials in scattered UI, workflow,
and job code paths.

## Required Contracts

- Chat, transcription, embeddings, and similar-review features each declare the
  capabilities they need.
- Unsupported provider/model combinations fail before sending user data.
- `base_url`, `model`, key env var, and optional headers are visible in a
  redacted diagnostics view.
- Default OpenAI behavior remains unchanged for existing users.
- Local and enterprise providers can be configured without code changes.

## Regression Tests

Add tests that assert:

- A non-default `base_url` is preserved in every request builder.
- A local endpoint can be configured without requiring a cloud API key name.
- Optional headers are forwarded only to the configured endpoint.
- Error messages include the failing capability, not the secret value.
- A hard-coded `api.openai.com` URL does not appear in non-default provider
  requests.

## Maintainer-Ready PR Shape

For a small first PR, avoid rewriting every provider at once. Start with:

1. A provider config type.
2. One request builder that consumes the config.
3. One UI or environment config path.
4. A redacted docs example.
5. Regression coverage for custom `base_url` and model name handling.

