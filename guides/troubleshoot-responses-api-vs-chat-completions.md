# Troubleshoot Responses API vs Chat Completions

Some tools use the OpenAI Responses API. Others still use Chat Completions.

These examples default to:

```text
API: Responses API
Endpoint: /responses
Base URL: https://apinode.pro
Model: gpt-5.5
```

## Responses API smoke test

```bash
curl "https://apinode.pro/responses" \
  -H "Authorization: Bearer $APINODE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-5.5","input":"Say hello"}'
```

## When a tool expects Chat Completions

Look for a setting such as:

```text
useResponsesApi
responses_api
wire_api
api_type
```

If the tool supports the Responses API, enable it. If it only supports Chat Completions, use the tool's OpenAI-compatible configuration and confirm the expected endpoint with its docs.

## Common symptoms

- `404`: wrong endpoint path.
- `400`: request payload shape does not match the endpoint.
- Empty output: client is parsing a Chat Completions response from a Responses-style request, or the reverse.
- Streaming fails but non-streaming works: the client and endpoint may use different stream event formats.

## Debugging order

1. Test a direct `/responses` request with `curl`.
2. Confirm whether the tool uses Responses API or Chat Completions.
3. Configure only the base URL unless the tool asks for a full endpoint.
4. Re-test with a one-sentence prompt before using agent workflows.
