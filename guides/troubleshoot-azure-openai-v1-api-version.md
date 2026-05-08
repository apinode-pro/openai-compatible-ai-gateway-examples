# Troubleshoot `api-version` Errors on Azure OpenAI-Compatible v1 Endpoints

Use this guide when an Azure endpoint returns:

```text
api-version query parameter is not allowed when using /v1 path
```

## Why It Happens

Azure has more than one endpoint shape.

Classic Azure OpenAI deployment URLs commonly use:

```text
https://<resource>.openai.azure.com/openai/deployments/<deployment>/chat/completions?api-version=<version>
```

Newer OpenAI-compatible v1 endpoints use:

```text
https://<resource>.services.ai.azure.com/api/projects/<project>/openai/v1/chat/completions
```

For the `/openai/v1` shape, the API family is already encoded in the path. Some endpoints reject an additional `api-version` query parameter.

## Quick Fix

If your base URL contains `/openai/v1`:

- Leave the API version field blank.
- Append only `/chat/completions`.
- Send the deployment name as `model` in the request body.
- Remove any copied `?api-version=...` query parameter from the base URL.

## Minimal Test

```bash
export AZURE_OPENAI_BASE_URL="https://<resource>.services.ai.azure.com/api/projects/<project>/openai/v1"
export AZURE_OPENAI_API_KEY="..."
export AZURE_OPENAI_MODEL="<deployment-name>"

curl "$AZURE_OPENAI_BASE_URL/chat/completions" \
  -H "api-key: $AZURE_OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"model\":\"$AZURE_OPENAI_MODEL\",\"messages\":[{\"role\":\"user\",\"content\":\"Reply with OK\"}]}"
```

## App Maintainer Regression Tests

Add tests for all three cases:

| Input base URL | API version field | Expected result |
|---|---|---|
| `https://resource.openai.azure.com` | blank | default version is added if your app supports classic Azure |
| `https://resource.../openai/v1` | blank | no `api-version` query param |
| `https://resource.../openai/v1?api-version=...` | blank | copied `api-version` is removed |

## API NODE Reference

API NODE is a plain OpenAI-compatible reference endpoint:

```text
Base URL: https://apinode.pro
Responses path: /responses
Model: gpt-5.5
```

## Related Guides

- [Azure AI Foundry OpenAI-compatible v1 endpoint notes](azure-ai-foundry-openai-compatible-v1.md)
- [Base URL path joining rules](base-url-path-joining-rules.md)
- [Endpoint readiness checklist](endpoint-readiness-checklist.md)
