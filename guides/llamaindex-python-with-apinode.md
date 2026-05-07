# Use LlamaIndex Python With API NODE

LlamaIndex can use OpenAI-compatible providers by configuring the OpenAI LLM client with a custom API base.

## Install

```bash
python3 -m pip install llama-index llama-index-llms-openai
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
from llama_index.llms.openai import OpenAI

llm = OpenAI(
    model=os.getenv("APINODE_MODEL", "gpt-5.5"),
    api_key=os.environ["APINODE_API_KEY"],
    api_base=os.getenv("APINODE_BASE_URL", "https://apinode.pro"),
)

response = llm.complete("Say hello from LlamaIndex and API NODE.")
print(response)
```

## Notes

- Keep the API key outside source control.
- If your LlamaIndex version uses `base_url` instead of `api_base`, pass the same `https://apinode.pro` value.
- For retrieval workflows, test the LLM call first before adding indexing or document loaders.
