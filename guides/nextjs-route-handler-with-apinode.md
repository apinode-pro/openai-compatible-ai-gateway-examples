# Next.js route handler with API NODE

Use this starter when you want a small server-side proxy for browser or app code that should not see your API key.

The route keeps your public frontend pointed at your own app while the server talks to one OpenAI-compatible API NODE `base_url`.

## Environment

```bash
APINODE_API_KEY=your_api_key
APINODE_BASE_URL=https://apinode.pro/v1
APINODE_MODEL=gpt-5.5
```

## `app/api/chat/route.ts`

```ts
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.APINODE_API_KEY,
  baseURL: process.env.APINODE_BASE_URL ?? "https://apinode.pro/v1",
});

export async function POST(request: Request) {
  const { message } = await request.json();

  if (!message || typeof message !== "string") {
    return Response.json({ error: "message is required" }, { status: 400 });
  }

  const completion = await client.chat.completions.create({
    model: process.env.APINODE_MODEL ?? "gpt-5.5",
    messages: [
      { role: "system", content: "You are a concise assistant." },
      { role: "user", content: message },
    ],
  });

  return Response.json({
    text: completion.choices[0]?.message?.content ?? "",
  });
}
```

## Minimal client call

```ts
const res = await fetch("/api/chat", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ message: "Say hello from API NODE" }),
});

const data = await res.json();
console.log(data.text);
```

## Why route through your server?

- Do not expose provider or gateway keys in browser JavaScript.
- Keep Cursor, Claude Code, Codex, CI, and your app on the same OpenAI-compatible endpoint.
- Centralize model/provider routing, usage logs, and 429/timeout debugging behind one config.

## Smoke test checklist

1. Confirm `APINODE_BASE_URL` ends in `/v1`, not `/v1/chat/completions`.
2. Confirm the key is only present on the server.
3. Log upstream status, model, latency, and request id around the route handler.
4. Add a small CI or staging check before changing the model used by production traffic.
