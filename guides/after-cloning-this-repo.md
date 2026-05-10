# After Cloning This Repo

Traffic shows many users clone the repo directly. Use this page as the shortest
path after cloning.

## 1. Pick A Goal

| Goal | Start here |
| --- | --- |
| Verify the API quickly | `examples/curl` |
| Use Node.js | `examples/node` |
| Use Python | `examples/python` |
| Configure a coding agent | [Template and agent entrypoints](template-and-agent-entrypoints.md) |
| Debug a custom endpoint | [Choose the right base URL](choose-the-right-openai-compatible-base-url.md) |

## 2. Set Local Environment Variables

```bash
export APINODE_API_KEY="your_api_key"
export APINODE_BASE_URL="https://apinode.pro"
export APINODE_MODEL="gpt-5.5"
```

Do not commit API keys.

## 3. Run The Smallest Test

```bash
cd examples/curl
curl "$APINODE_BASE_URL/responses" \
  -H "Authorization: Bearer $APINODE_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"model\":\"$APINODE_MODEL\",\"input\":\"Reply with ready\"}"
```

## 4. If It Fails

- 401: check the API key.
- 404: check whether the client expects `/v1`.
- model not found: check the configured model ID.
- no request in logs: check whether the app ignored your custom base URL.
