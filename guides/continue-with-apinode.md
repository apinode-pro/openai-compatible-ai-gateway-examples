# Use Continue With API NODE

Continue users can configure OpenAI-compatible model providers for coding workflows.

API NODE endpoint:

```text
https://apinode.pro
```

## Recommended Values

```text
API key:  your API NODE key
Base URL: https://apinode.pro
Model:    gpt-5.5
```

## Example Provider Shape

Use the OpenAI-compatible provider path in Continue and set:

```yaml
models:
  - name: API NODE
    provider: openai
    model: gpt-5.5
    apiKey: ${APINODE_API_KEY}
    apiBase: https://apinode.pro
```

If your Continue version uses a different config schema, keep the same values and map them to the current OpenAI-compatible provider fields.

## Smoke Test

Ask Continue:

```text
Summarize this repository in three bullets.
```

## Notes

- Store `APINODE_API_KEY` in your local environment or secret manager.
- Use a model enabled for your API NODE account.
- Start with a small repository before using long-context tasks.

