# Gateway latency and error baseline template

Use this lightweight template when comparing direct provider calls with an OpenAI-compatible gateway path. The goal is not to claim a universal benchmark; it is to make routing, timeout, and 429 debugging reproducible for your own Cursor, Claude Code, Codex CLI, or app setup.

## What to record

For each test run, keep the prompt, model, endpoint, and client constant where possible.

| Field | Example |
|---|---|
| Client/tool | Cursor / Claude Code / Codex CLI / Python SDK |
| Endpoint shape | direct provider / gateway `base_url` |
| Model | `gpt-5.5` or target model name |
| Request type | chat completions / responses / streaming |
| Timestamp | ISO-8601 UTC |
| HTTP status | `200`, `429`, `5xx`, timeout |
| Total latency | ms |
| First-token latency | ms, if streaming |
| Retry count | `0`, `1`, `2` |
| Upstream provider | record internally if available |
| Notes | model-name mismatch, auth issue, quota limit, etc. |

## Minimal smoke-test loop

```bash
export APINODE_BASE_URL="https://apinode.pro/v1"
export APINODE_API_KEY="your_api_key"
export APINODE_MODEL="gpt-5.5"

for i in 1 2 3 4 5; do
  start=$(python3 - <<'PY'
import time
print(int(time.time() * 1000))
PY
)
  code=$(curl -sS -o /tmp/apinode-benchmark-response.json -w "%{http_code}" \
    "$APINODE_BASE_URL/chat/completions" \
    -H "Authorization: Bearer $APINODE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"model":"'"$APINODE_MODEL"'","messages":[{"role":"user","content":"Reply with one short sentence."}]}' || true)
  end=$(python3 - <<'PY'
import time
print(int(time.time() * 1000))
PY
)
  echo "run=$i status=$code latency_ms=$((end-start))"
done
```

## Interpreting results

- A single slow request is not a benchmark; repeat enough times to separate cold starts, provider queueing, and local network noise.
- For 429s, record whether the limit came from the gateway account, the upstream provider, or the client retry loop.
- For timeouts, record both client timeout settings and upstream timeout/error details when available.
- For model errors, verify the exact model name and whether the client is using Chat Completions or Responses API.

## Sharing a useful issue

If you open a compatibility or performance issue, include:

1. tool/client name and version;
2. redacted config showing `base_url` shape;
3. request type and model name;
4. 3-5 lines of status/latency output;
5. whether the same request succeeds against a direct provider endpoint.

Never include API keys, billing details, or private prompts in benchmark logs.
