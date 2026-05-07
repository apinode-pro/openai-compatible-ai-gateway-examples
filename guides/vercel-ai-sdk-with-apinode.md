# Use Vercel AI SDK With API NODE

The Vercel AI SDK can use OpenAI-compatible providers through a custom OpenAI client configuration.

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
import { generateText } from "ai";
import { createOpenAI } from "@ai-sdk/openai";

const apinode = createOpenAI({
  apiKey: process.env.APINODE_API_KEY,
  baseURL: process.env.APINODE_BASE_URL || "https://apinode.pro",
});

const { text } = await generateText({
  model: apinode(process.env.APINODE_MODEL || "gpt-5.5"),
  prompt: "Say hello from API NODE",
});

console.log(text);
```

## Notes

- Store `APINODE_API_KEY` as a deployment secret.
- Use a model enabled for your API NODE account.
- Test locally before deploying to Vercel or another serverless runtime.

