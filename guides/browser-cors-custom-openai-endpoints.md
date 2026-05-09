# Browser CORS And Custom OpenAI-Compatible Endpoints

Some custom OpenAI-compatible endpoints work from a server script but fail from a browser app with a CORS error. That usually means the endpoint is not designed to be called directly by frontend code.

## Why It Happens

Browser requests are governed by CORS. A server-to-server request can call:

```text
https://apinode.pro/responses
https://apinode.pro/v1/chat/completions
```

but a browser page can only call an endpoint when that endpoint explicitly allows the page origin.

This is separate from OpenAI compatibility. An endpoint can be OpenAI-compatible and still reject browser-origin requests.

## Recommended Pattern

Use a backend route as a proxy:

```text
browser -> your backend -> OpenAI-compatible endpoint
```

Benefits:

- API keys stay server-side.
- CORS is controlled by your app.
- You can normalize `/responses`, `/chat/completions`, and `/embeddings`.
- You can log redacted request metadata for debugging.

## Minimal Backend Checklist

- Read the key from a server-side secret.
- Read the base URL from server-side config.
- Validate the requested model against an allowlist when possible.
- Never forward arbitrary headers from the browser.
- Return a clear error if the upstream response has no usable output.

## When Direct Browser Calls Are Acceptable

Direct calls can be acceptable for local-only demos, throwaway prototypes, or endpoints that intentionally support browser origins. Do not use direct browser calls for production apps with user data or real API keys.

