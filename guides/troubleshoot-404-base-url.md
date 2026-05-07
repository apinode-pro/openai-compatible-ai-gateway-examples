# Troubleshoot 404 Base URL Issues With API NODE

A `404` response often means the request path does not match the API endpoint.

## Correct base URL

Use:

```text
https://apinode.pro
```

For the Responses API, the final request URL should be:

```text
https://apinode.pro/responses
```

## Avoid double paths

If a tool already appends `/responses`, configure only the base URL:

```text
https://apinode.pro
```

Do not configure:

```text
https://apinode.pro/responses
```

as the base URL unless the tool explicitly asks for a full endpoint URL.

## Quick test

```bash
export APINODE_BASE_URL="https://apinode.pro"

curl "$APINODE_BASE_URL/responses" \
  -H "Authorization: Bearer $APINODE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-5.5","input":"Say hello"}'
```

## Common causes

- The tool appends `/responses`, but the configured base URL already includes `/responses`.
- The tool expects a base URL, but you pasted a full endpoint URL.
- An older config still points at a different API path.
- A proxy or gateway strips the path before forwarding the request.
