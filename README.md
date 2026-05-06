# OpenAI-Compatible AI Gateway Examples

Copy-paste examples for using an OpenAI-compatible AI API gateway with Claude, GPT, Gemini, Cursor, Codex CLI, Claude Code, GitHub Actions, Node.js, Python, and curl.

These examples use API NODE by default:

```text
Base URL: https://apinode.pro
Model:    gpt-5.5
API:      OpenAI Responses API
```

[Try API NODE](https://apinode.pro)

## Quickstart

```bash
export APINODE_API_KEY="your_api_key"
export APINODE_BASE_URL="https://apinode.pro"
export APINODE_MODEL="gpt-5.5"
```

Then choose an example:

```text
examples/curl
examples/node
examples/python
examples/cursor
examples/codex-cli
examples/claude-code
examples/github-actions
```

## Why This Repo Exists

Developers often want to test a new LLM provider or gateway without rewriting an app. Most modern AI tools and SDKs can use a custom OpenAI-compatible endpoint.

This repo keeps those setup paths small, explicit, and easy to verify.

## Examples

### curl

```bash
cd examples/curl
export APINODE_API_KEY="your_api_key"
export APINODE_BASE_URL="https://apinode.pro"
export APINODE_MODEL="gpt-5.5"
curl "$APINODE_BASE_URL/responses" \
  -H "Authorization: Bearer $APINODE_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"model\":\"$APINODE_MODEL\",\"input\":\"Say hello from API NODE\"}"
```

### Node.js

```bash
cd examples/node
npm install
export APINODE_API_KEY="your_api_key"
export APINODE_BASE_URL="https://apinode.pro"
export APINODE_MODEL="gpt-5.5"
npm start
```

### Python

```bash
cd examples/python
python3 -m pip install -r requirements.txt
export APINODE_API_KEY="your_api_key"
export APINODE_BASE_URL="https://apinode.pro"
export APINODE_MODEL="gpt-5.5"
python3 main.py
```

### Codex CLI

See:

```text
examples/codex-cli/config.toml
```

The Codex CLI example uses:

```toml
[model_providers.OpenAI]
base_url = "https://apinode.pro"
wire_api = "responses"
requires_openai_auth = true
```

## GitHub Actions Smoke Test

Copy this workflow into `.github/workflows/api-smoke-test.yml`:

```text
examples/github-actions/api-smoke-test.yml
```

Add `APINODE_API_KEY` as a repository secret, then run the workflow manually or on schedule.

## Repository Topics

Suggested GitHub topics:

```text
ai-gateway
openai-compatible
llm-api
api-gateway
claude-code
codex-cli
cursor
openai
model-router
developer-tools
```

## Contributing

Useful additions:

- LangChain example.
- Vercel AI SDK example.
- LiteLLM example.
- Continue, Cline, and Roo Code config recipes.
- Open WebUI and LibreChat setup recipes.

Please do not commit API keys or account secrets.

