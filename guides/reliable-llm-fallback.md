# Building Reliable LLM Fallback With An OpenAI-Compatible Gateway

LLM applications fail in ordinary ways: rate limits, provider incidents, model availability changes, latency spikes, and account-level quota issues.

The simplest way to prepare for that is to keep your application on a stable OpenAI-compatible interface and put provider selection behind a gateway.

## Basic Pattern

Application code talks to one endpoint:

```text
https://apinode.pro
```

The gateway can then handle provider choice, model choice, or fallback policy behind that endpoint.

## What To Measure

Before adding fallback, measure:

- Success rate.
- Average latency.
- P95 latency.
- Error types.
- Retry behavior.
- Cost per successful request.

## Minimal Smoke Test

```bash
export APINODE_API_KEY="your_api_key"
export APINODE_BASE_URL="https://apinode.pro"
export APINODE_MODEL="gpt-5.5"

curl -fsS "$APINODE_BASE_URL/responses" \
  -H "Authorization: Bearer $APINODE_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"model\":\"$APINODE_MODEL\",\"input\":\"ping\"}"
```

Run that from CI on a schedule. A boring smoke test catches many integration failures before users do.

## Try API NODE

```text
https://apinode.pro
```

