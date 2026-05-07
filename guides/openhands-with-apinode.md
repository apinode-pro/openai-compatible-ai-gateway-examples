# Use OpenHands With API NODE

OpenHands users can test API NODE wherever an OpenAI-compatible provider, custom base URL, or custom API endpoint is accepted.

## Values

```text
Provider: OpenAI-compatible
Base URL: https://apinode.pro
Model:    gpt-5.5
API key:  your_api_key
```

## Environment-style setup

```bash
export APINODE_API_KEY="your_api_key"
export APINODE_BASE_URL="https://apinode.pro"
export APINODE_MODEL="gpt-5.5"
```

Map those values into the OpenHands LLM provider settings for an OpenAI-compatible endpoint.

## Smoke test prompt

```text
Create a small README change and explain the diff before editing.
```

## Notes

- Use a test repository before connecting the agent to production code.
- Do not paste API keys into public issue comments, screenshots, or logs.
- If your OpenHands config supports separate model and base URL fields, keep the model as `gpt-5.5` and the base URL as `https://apinode.pro`.
