# Base URL Path Joining Rules for OpenAI-Compatible Endpoints

Most custom endpoint bugs come from joining paths twice or mixing incompatible endpoint styles.

## API NODE Reference

```text
Base URL: https://apinode.pro
Responses path: /responses
Model: gpt-5.5
```

## Keep Operation Paths Out of Base URLs

Prefer:

```text
base_url = https://apinode.pro
operation = /responses
```

Avoid:

```text
base_url = https://apinode.pro/responses
operation = /responses
```

The second shape can produce:

```text
https://apinode.pro/responses/responses
```

## Chat Completions Examples

Generic OpenAI-compatible endpoint:

```text
base_url = https://example.com/v1
path = /chat/completions
```

Classic Azure OpenAI:

```text
base_url = https://resource.openai.azure.com
path = /openai/deployments/<deployment>/chat/completions?api-version=<version>
```

Azure AI Foundry OpenAI-compatible v1:

```text
base_url = https://resource.services.ai.azure.com/api/projects/project/openai/v1
path = /chat/completions
```

## Responses API Examples

API NODE:

```text
base_url = https://apinode.pro
path = /responses
```

OpenAI-style `/v1` endpoint:

```text
base_url = https://example.com/v1
path = /responses
```

## Implementation Pattern

Normalize once:

```text
base_url_without_trailing_slash + operation_path_with_leading_slash
```

Then test:

- Empty path base URL.
- Base URL ending in `/v1`.
- Base URL ending in `/openai/v1`.
- Base URL that already contains query parameters.

## Related Guides

- [Endpoint readiness checklist](endpoint-readiness-checklist.md)
- [Troubleshoot 404 base URL issues](troubleshoot-404-base-url.md)
- [Azure AI Foundry OpenAI-compatible v1 endpoint notes](azure-ai-foundry-openai-compatible-v1.md)
