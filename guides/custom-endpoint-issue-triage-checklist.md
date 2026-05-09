# Custom OpenAI Endpoint Issue Triage Checklist

Use this checklist when an issue says a custom OpenAI-compatible endpoint is ignored, routed to the wrong provider, or returns `model not found`, `invalid API key`, or `404`.

## Confirm The Request Shape

Ask for redacted values only:

```text
base_url: https://example.com/v1
model: model-name
api style: responses | chat-completions | embeddings
client/library:
error status:
first error line:
```

Never ask for a real API key, bearer token, organization id, account id, billing data, or full request logs.

## Common Root Causes

- The app reads `OPENAI_API_KEY` but ignores `OPENAI_BASE_URL`.
- The app has separate code paths for chat, templates, images, embeddings, or title generation.
- The UI option says "OpenAI-compatible" but the runtime still calls an Anthropic or native provider path.
- The base URL includes a path, and the app appends `/v1` or `/chat/completions` incorrectly.
- The model value is a provider display name, not the exact model id required by the endpoint.
- A browser-side request hits CORS because the endpoint is not meant to be called directly from the frontend.

## Safe Diagnostic Reply

```text
This looks like a config propagation issue rather than an API key issue. A quick way to narrow it down is to log the resolved client settings right before the request is sent:

- provider/protocol selected
- redacted base URL host/path
- request path, for example /responses or /chat/completions
- model id
- whether the key came from the expected env var

If curl against the same redacted base URL works but the app fails, check for secondary code paths such as template generation, embeddings, title generation, or streaming. Those often create a separate OpenAI client and accidentally fall back to api.openai.com.
```

## When To Open A PR

Open a small docs or code PR only when one of these is true:

- The repo has a clear docs/examples area and asks for custom endpoint examples.
- The issue owner or maintainer asks for a PR.
- The code path is small and you can add a provider-neutral test.
- The fix improves all OpenAI-compatible endpoints, not only one commercial provider.

If the thread is just a feature request with no maintainer signal, prefer a short helpful comment or a private draft.

