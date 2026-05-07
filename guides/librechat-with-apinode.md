# Use LibreChat With API NODE

LibreChat supports multi-provider chat setups and OpenAI-compatible endpoints.

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

## Configuration Shape

Use LibreChat's OpenAI-compatible custom endpoint configuration and map these fields:

```yaml
name: API NODE
apiKey: "${APINODE_API_KEY}"
baseURL: "https://apinode.pro"
models:
  default:
    - gpt-5.5
```

If your LibreChat version uses a different endpoint schema, keep the same API key, base URL, and model values.

## Smoke Test

Send:

```text
Reply with "API NODE is connected" and nothing else.
```

## Notes

- Store `APINODE_API_KEY` as a deployment secret.
- Use a model enabled for your API NODE account.
- Start with one model before adding more routing options.

