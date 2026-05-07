# Use LangGraph Python With API NODE

LangGraph applications commonly use LangChain chat models. Configure `ChatOpenAI` with the API NODE base URL and model.

## Install

```bash
python3 -m pip install langgraph langchain-openai
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
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model=os.getenv("APINODE_MODEL", "gpt-5.5"),
    api_key=os.environ["APINODE_API_KEY"],
    base_url=os.getenv("APINODE_BASE_URL", "https://apinode.pro"),
)

message = llm.invoke("Say hello from LangGraph and API NODE.")
print(message.content)
```

## Notes

- Build and test the model call before wiring it into a graph.
- Use environment variables for keys in local and CI workflows.
- If you use streaming, test both streaming and non-streaming paths.
