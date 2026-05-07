# Troubleshoot Model Not Found With API NODE

`model_not_found`, `invalid model`, or similar errors usually mean the request model name does not match a model available through the endpoint.

## Default model

These examples use:

```text
gpt-5.5
```

## Check your environment

```bash
echo "$APINODE_MODEL"
```

If it is empty, set it explicitly:

```bash
export APINODE_MODEL="gpt-5.5"
```

## Check your tool config

Many tools have separate fields for display name and actual model ID.

Use `gpt-5.5` as the model ID:

```text
Display name: API NODE GPT-5.5
Model ID:     gpt-5.5
Base URL:     https://apinode.pro
```

## Common causes

- The display label was used as the model ID.
- The local config still references an older model.
- The model field is nested in a provider-specific config block.
- A fallback chain is sending requests to another provider with a different model list.

## Quick test

```bash
curl "$APINODE_BASE_URL/responses" \
  -H "Authorization: Bearer $APINODE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-5.5","input":"Say hello"}'
```
