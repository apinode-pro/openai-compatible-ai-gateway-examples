# Use Flowise With API NODE

Flowise can connect to OpenAI-compatible chat model nodes when they expose a base URL or custom endpoint field.

## Values

```text
API key:  your_api_key
Base URL: https://apinode.pro
Model:    gpt-5.5
```

## Suggested Flowise setup

1. Add an OpenAI-compatible chat model node.
2. Set the model to `gpt-5.5`.
3. Set the base URL or custom endpoint to `https://apinode.pro`.
4. Save the API key in Flowise credentials or environment variables.

## Test prompt

```text
Reply with one sentence confirming this Flowise flow can reach API NODE.
```

## Notes

- Keep credentials in Flowise secrets, not inside exported flow JSON.
- If a node only supports the default OpenAI endpoint, use a node that supports custom base URLs.
- For production flows, add retries and timeout handling around model calls.
