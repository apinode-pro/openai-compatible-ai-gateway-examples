# Use Open WebUI With API NODE

Open WebUI can connect to OpenAI-compatible API endpoints.

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

## Environment-Style Setup

If your Open WebUI deployment is configured through environment variables, use the OpenAI-compatible endpoint fields:

```bash
OPENAI_API_KEY="your_api_key"
OPENAI_API_BASE_URL="https://apinode.pro"
```

Then select `gpt-5.5` or another enabled model in the UI.

## Smoke Test

Send:

```text
Reply with "API NODE is connected" and nothing else.
```

## Notes

- Keep API keys in deployment secrets.
- Verify the base URL expected by your Open WebUI version.
- Use a small prompt first before testing long chats or tools.

