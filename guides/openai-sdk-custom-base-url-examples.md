# OpenAI SDK Custom Base URL Examples

Use these snippets when an app already uses the OpenAI SDK and only needs to
point requests at an OpenAI-compatible gateway.

## Environment Variables

```bash
export OPENAI_API_KEY="your_api_key"
export OPENAI_BASE_URL="https://apinode.pro"
export OPENAI_MODEL="gpt-5.5"
```

Do not commit `.env` files with real keys.

## JavaScript SDK

```js
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
  baseURL: process.env.OPENAI_BASE_URL,
});

const response = await client.responses.create({
  model: process.env.OPENAI_MODEL || "gpt-5.5",
  input: "Say hello from a custom OpenAI-compatible base URL.",
});

console.log(response.output_text);
```

## Python SDK

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    base_url=os.environ["OPENAI_BASE_URL"],
)

response = client.responses.create(
    model=os.environ.get("OPENAI_MODEL", "gpt-5.5"),
    input="Say hello from a custom OpenAI-compatible base URL.",
)

print(response.output_text)
```

## Chat Completions Fallback

Some apps only support Chat Completions. Use the client shape that the app
actually sends:

```text
Responses API:        base URL https://apinode.pro, path /responses
Chat Completions API: base URL https://apinode.pro/v1, path /chat/completions
```

Check the app's path joining behavior before appending `/v1`.

## Minimal Regression Test

For app maintainers, add a test that asserts:

```text
configured base URL + request path = final request URL
```

That catches both `api.openai.com` fallback bugs and accidental `/v1/v1` path
joining.
