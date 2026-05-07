# Use Aider With API NODE

Aider can be used with OpenAI-compatible providers by pointing its OpenAI base URL at API NODE and selecting the model you want to use.

## Environment

```bash
export OPENAI_API_KEY="your_api_key"
export OPENAI_API_BASE="https://apinode.pro"
```

## Example

```bash
aider --model openai/gpt-5.5
```

If your local Aider version uses a different OpenAI base URL flag, keep the same values:

```text
API key:  your_api_key
Base URL: https://apinode.pro
Model:    gpt-5.5
```

## Notes

- Store the API key in your shell or secret manager, not in the repository.
- Start with a small edit before running broad refactors.
- If a request fails, confirm the configured model and base URL first.
