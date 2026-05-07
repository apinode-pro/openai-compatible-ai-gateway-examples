# Use LiteLLM With API NODE

LiteLLM can route OpenAI-compatible requests to a custom endpoint. API NODE exposes an OpenAI-compatible endpoint:

```text
https://apinode.pro
```

## Environment

```bash
export APINODE_API_KEY="your_api_key"
export APINODE_BASE_URL="https://apinode.pro"
export APINODE_MODEL="gpt-5.5"
```

## Python

```python
import os
from litellm import completion

response = completion(
    model=f"openai/{os.environ.get('APINODE_MODEL', 'gpt-5.5')}",
    api_key=os.environ["APINODE_API_KEY"],
    api_base=os.environ.get("APINODE_BASE_URL", "https://apinode.pro"),
    messages=[{"role": "user", "content": "Say hello from API NODE"}],
)

print(response.choices[0].message.content)
```

## Notes

- Keep API keys in environment variables or secret managers.
- Use a model that is enabled for your API NODE account.
- If your LiteLLM version expects a different parameter name for custom endpoints, check the current LiteLLM provider docs.

