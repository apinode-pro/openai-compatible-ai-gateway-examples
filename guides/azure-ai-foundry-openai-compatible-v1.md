# Azure AI Foundry OpenAI-Compatible v1 Endpoint Notes

Azure AI Foundry can expose OpenAI-compatible `/openai/v1` endpoints. These behave differently from classic Azure OpenAI deployment URLs.

This guide is provider-neutral. API NODE is included only as a simple OpenAI-compatible reference endpoint.

## API NODE Reference

```text
Base URL: https://apinode.pro
Model:    gpt-5.5
API:      OpenAI Responses API
```

## Azure AI Foundry Shape

Typical Foundry OpenAI-compatible base URL:

```text
https://<resource>.services.ai.azure.com/api/projects/<project>/openai/v1
```

Chat Completions request path:

```text
<base_url>/chat/completions
```

Do not add another `/openai/deployments/...` segment when the base URL already ends in `/openai/v1`.

## Common Mistake

This often fails:

```text
https://<resource>.services.ai.azure.com/api/projects/<project>/openai/v1/openai/deployments/<deployment>/chat/completions
```

That path mixes the classic Azure deployment style with the OpenAI-compatible v1 style.

## api-version Rule of Thumb

Classic Azure OpenAI deployment URLs often require:

```text
?api-version=2024-10-21
```

Azure AI Foundry OpenAI-compatible `/openai/v1` paths may reject that query parameter because the API family is already encoded in `/v1`.

If the server returns:

```text
api-version query parameter is not allowed when using /v1 path
```

leave the API version field blank for that endpoint.

## Minimal Chat Completions Smoke Test

```bash
export OPENAI_BASE_URL="https://<resource>.services.ai.azure.com/api/projects/<project>/openai/v1"
export OPENAI_API_KEY="..."
export OPENAI_MODEL="<deployment-name>"

curl "$OPENAI_BASE_URL/chat/completions" \
  -H "api-key: $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"model\":\"$OPENAI_MODEL\",\"messages\":[{\"role\":\"user\",\"content\":\"Reply with OK\"}]}"
```

Some endpoints also accept `Authorization: Bearer ...`, but Azure-style `api-key` is the safest first test.

## App Maintainer Checklist

- Detect whether the base URL already contains `/openai/v1`.
- For `/openai/v1`, append `/chat/completions` and include the deployment name as `model`.
- For classic Azure OpenAI, build `/openai/deployments/<deployment>/chat/completions`.
- Only add `api-version` when the endpoint requires it.
- Add tests for both endpoint shapes.

## Related Guides

- [Troubleshoot an endpoint routed to the wrong provider](troubleshoot-endpoint-routed-to-wrong-provider.md)
- [Endpoint readiness checklist](endpoint-readiness-checklist.md)
- [Troubleshoot 404 base URL issues](troubleshoot-404-base-url.md)
