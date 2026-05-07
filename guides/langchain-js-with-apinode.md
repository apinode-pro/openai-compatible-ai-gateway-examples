# Use LangChain JS With API NODE

LangChain JS can call OpenAI-compatible chat endpoints through a custom configuration.

API NODE endpoint:

```text
https://apinode.pro
```

## Environment

```bash
export APINODE_API_KEY="your_api_key"
export APINODE_BASE_URL="https://apinode.pro"
export APINODE_MODEL="gpt-5.5"
```

## Example

```ts
import { ChatOpenAI } from "@langchain/openai";

const model = new ChatOpenAI({
  apiKey: process.env.APINODE_API_KEY,
  model: process.env.APINODE_MODEL || "gpt-5.5",
  configuration: {
    baseURL: process.env.APINODE_BASE_URL || "https://apinode.pro",
  },
});

const response = await model.invoke("Say hello from API NODE");

console.log(response.content);
```

## Notes

- Keep secrets out of committed config files.
- Confirm your installed `@langchain/openai` version supports `configuration.baseURL`.
- Use `APINODE_MODEL` to switch models without editing code.

