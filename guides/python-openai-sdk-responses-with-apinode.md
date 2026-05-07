# Use the Python OpenAI SDK Responses API With API NODE

The OpenAI Python SDK can call an OpenAI-compatible Responses API endpoint when configured with API NODE credentials and base URL.

## Install

```bash
python3 -m pip install openai
```

## Environment

```bash
export APINODE_API_KEY="your_api_key"
export APINODE_BASE_URL="https://apinode.pro"
export APINODE_MODEL="gpt-5.5"
```

## Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["APINODE_API_KEY"],
    base_url=os.getenv("APINODE_BASE_URL", "https://apinode.pro"),
)

response = client.responses.create(
    model=os.getenv("APINODE_MODEL", "gpt-5.5"),
    input="Say hello from the Python OpenAI SDK and API NODE.",
)

print(response.output_text)
```

## Notes

- Do not hard-code API keys in Python files.
- Use this as a quick SDK compatibility smoke test.
- If your SDK version does not include `responses`, upgrade the `openai` package.
