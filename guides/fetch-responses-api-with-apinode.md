# Call API NODE With fetch

You do not need an SDK to test an OpenAI-compatible Responses API endpoint.

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

## Node.js fetch

```js
const baseURL = process.env.APINODE_BASE_URL || "https://apinode.pro";
const model = process.env.APINODE_MODEL || "gpt-5.5";

const response = await fetch(`${baseURL}/responses`, {
  method: "POST",
  headers: {
    Authorization: `Bearer ${process.env.APINODE_API_KEY}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    model,
    input: "Say hello from API NODE",
  }),
});

if (!response.ok) {
  throw new Error(`API request failed: ${response.status} ${await response.text()}`);
}

const body = await response.json();
const text = body.output_text || body.output?.[0]?.content?.[0]?.text;

console.log(text);
```

## Notes

- This is useful for quick smoke tests, CI checks, and debugging.
- Do not expose API keys in browser-side code.

