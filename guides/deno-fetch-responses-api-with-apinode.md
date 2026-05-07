# Call the Responses API From Deno With API NODE

Deno has built-in `fetch`, so a smoke test only needs environment variables and one POST request.

## Environment

```bash
export APINODE_API_KEY="your_api_key"
export APINODE_BASE_URL="https://apinode.pro"
export APINODE_MODEL="gpt-5.5"
```

## Example

```ts
const baseURL = Deno.env.get("APINODE_BASE_URL") ?? "https://apinode.pro";
const model = Deno.env.get("APINODE_MODEL") ?? "gpt-5.5";

const response = await fetch(`${baseURL}/responses`, {
  method: "POST",
  headers: {
    Authorization: `Bearer ${Deno.env.get("APINODE_API_KEY")}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    model,
    input: "Say hello from Deno and API NODE.",
  }),
});

if (!response.ok) {
  throw new Error(`API request failed: ${response.status} ${await response.text()}`);
}

console.log(await response.json());
```

Run:

```bash
deno run --allow-env --allow-net main.ts
```

## Notes

- Do not expose the API key in browser-side Deno code.
- Use `--allow-net=apinode.pro` for a tighter local permission scope.
