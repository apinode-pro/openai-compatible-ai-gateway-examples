# Daily growth note — 2026-05-13

Small content asset added for developers who want to keep browser/app keys private while still using one OpenAI-compatible API NODE endpoint behind their own application server.

## Added

- Guide: [Next.js route handler with API NODE](../guides/nextjs-route-handler-with-apinode.md)
- README entry under Guides.

## Audience

- Next.js app builders testing custom OpenAI-compatible endpoints.
- Developers moving from direct browser calls to server-side key handling.
- Teams standardizing Cursor, Claude Code, Codex, CI, and app traffic around one `base_url`.

## Outreach-safe angle

No-link technical framing for forums:

> If your frontend needs AI calls, do not put provider/gateway keys in browser code. Keep the browser talking to your own `/api/chat` route, and have that route call one OpenAI-compatible `base_url`. That keeps keys server-side and makes model, latency, 429, and timeout logs easier to compare.
