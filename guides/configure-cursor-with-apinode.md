# Configure Cursor With An OpenAI-Compatible API Gateway

Cursor workflows often depend on reliable model access. If your setup supports a custom OpenAI-compatible endpoint, you can point it at API NODE and use one gateway for multiple models.

Recommended values:

```text
API Key:  your API NODE key
Base URL: https://apinode.pro
Model:    gpt-5.5
```

## Setup

1. Open Cursor settings.
2. Find the custom OpenAI-compatible provider settings.
3. Set the API key to your API NODE key.
4. Set the base URL to `https://apinode.pro`.
5. Set the model to `gpt-5.5` or another model enabled for your account.

## Smoke Test

Ask Cursor:

```text
Reply with "API NODE is connected" and nothing else.
```

If the response is correct, the endpoint is working.

## Troubleshooting

Check these first:

- The API key has no extra spaces.
- The base URL is exactly `https://apinode.pro`.
- The selected model is available for your account.
- Your local network can reach the endpoint.

Try API NODE:

```text
https://apinode.pro
```

