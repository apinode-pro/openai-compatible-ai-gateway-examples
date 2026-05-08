# OpenAI-Compatible Environment Variable Patterns

Many tools support custom OpenAI-compatible endpoints, but they do not all use the same environment variable names.

This guide gives a provider-neutral pattern and an API NODE example.

## API NODE Defaults

```bash
export APINODE_API_KEY="your_api_key"
export APINODE_BASE_URL="https://apinode.pro"
export APINODE_MODEL="gpt-5.5"
```

## Generic Pattern

When a project already uses OpenAI naming:

```bash
export OPENAI_API_KEY="$APINODE_API_KEY"
export OPENAI_BASE_URL="$APINODE_BASE_URL"
export OPENAI_MODEL="$APINODE_MODEL"
```

When a project supports provider-neutral naming:

```bash
export LLM_API_KEY="$APINODE_API_KEY"
export LLM_BASE_URL="$APINODE_BASE_URL"
export LLM_MODEL="$APINODE_MODEL"
```

## Pick One Source of Truth

Avoid setting multiple conflicting values in the same shell.

Risky:

```bash
export OPENAI_BASE_URL="https://api.openai.com/v1"
export APINODE_BASE_URL="https://apinode.pro"
```

Better:

```bash
export OPENAI_BASE_URL="https://apinode.pro"
export OPENAI_API_KEY="$APINODE_API_KEY"
```

## CI Pattern

For GitHub Actions:

```yaml
env:
  APINODE_BASE_URL: https://apinode.pro
  APINODE_MODEL: gpt-5.5
  APINODE_API_KEY: ${{ secrets.APINODE_API_KEY }}
```

Do not hard-code API keys in workflows.

## App Maintainer Pattern

If you maintain an app, support these fields together:

```text
base_url
api_key
model
api_family
```

`api_family` should distinguish:

- Responses API.
- Chat Completions.
- Embeddings.
- Audio.

This avoids routing a valid custom endpoint through the wrong request adapter.

## Related Guides

- [Endpoint readiness checklist](endpoint-readiness-checklist.md)
- [Troubleshoot 401 invalid API key](troubleshoot-401-invalid-api-key.md)
- [Troubleshoot model not found](troubleshoot-model-not-found.md)
