# Codex Provider Block Reference

Use this when configuring Codex with an OpenAI-compatible gateway.

## Responses API

```toml
model_provider = "OpenAI"
model = "gpt-5.5"
model_reasoning_effort = "xhigh"

[model_providers.OpenAI]
name = "OpenAI"
base_url = "https://apinode.pro"
wire_api = "responses"
requires_openai_auth = true
```

Store the API key outside the config file.

## Chat Completions API

Use Chat Completions only when the target client or model path requires it:

```toml
model_provider = "OpenAI"
model = "gpt-5.5"

[model_providers.OpenAI]
name = "OpenAI"
base_url = "https://apinode.pro/v1"
wire_api = "chat"
requires_openai_auth = true
```

## Checks

- `wire_api` matches the request shape the client will send.
- `base_url` does not double-include `/v1`.
- API keys are stored in environment variables or an approved secret store.
- The model ID is a real gateway model ID.

## Related Guides

- [Agent base URL configuration examples](agent-base-url-configuration-examples.md)
- [Base URL path joining rules](base-url-path-joining-rules.md)
- [OpenAI SDK custom base URL examples](openai-sdk-custom-base-url-examples.md)
