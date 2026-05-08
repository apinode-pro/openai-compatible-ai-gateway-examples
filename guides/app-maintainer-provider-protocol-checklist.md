# App Maintainer Checklist for Custom OpenAI-Compatible Providers

If your app supports custom model providers, treat provider protocol as a first-class setting. A base URL alone is not enough.

## Minimum Config Fields

```text
protocol
base_url
api_key
model
api_family
```

Recommended protocol values:

```text
openai-responses
openai-chat-completions
anthropic-messages
azure-openai-deployments
azure-foundry-openai-v1
```

## Why This Matters

The same model name can be reachable through different request shapes:

- OpenAI Responses API: `/responses`.
- OpenAI Chat Completions: `/chat/completions`.
- Anthropic Messages: `/v1/messages`.
- Classic Azure OpenAI: `/openai/deployments/<deployment>/chat/completions`.
- Azure AI Foundry OpenAI-compatible v1: `/openai/v1/chat/completions`.

Routing a valid base URL through the wrong adapter produces confusing errors.

## Smoke Test Matrix

Add one test for each supported protocol:

| Protocol | Expected path | Model location |
|---|---|---|
| OpenAI Responses | `/responses` | body `model` |
| OpenAI Chat Completions | `/chat/completions` | body `model` |
| Anthropic Messages | `/v1/messages` | body `model` |
| Classic Azure OpenAI | `/openai/deployments/<deployment>/chat/completions` | path |
| Azure Foundry OpenAI v1 | `/openai/v1/chat/completions` | body `model` |

## UI Checklist

- Do not reuse Anthropic fields for OpenAI-compatible providers.
- Do not silently switch protocols when a user changes a model name.
- Show which adapter will be used before saving.
- Keep API keys redacted in logs and screenshots.
- Provide a one-click "test connection" request that uses the exact saved config.

## API NODE Reference Config

```text
protocol: openai-responses
base_url: https://apinode.pro
model: gpt-5.5
api_key: <redacted>
```

## Related Guides

- [Troubleshoot an endpoint routed to the wrong provider](troubleshoot-endpoint-routed-to-wrong-provider.md)
- [Base URL path joining rules](base-url-path-joining-rules.md)
- [Endpoint readiness checklist](endpoint-readiness-checklist.md)
