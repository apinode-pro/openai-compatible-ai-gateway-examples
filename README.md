# OpenAI-Compatible AI Gateway Examples for Cursor, Claude Code, Codex, SDKs, and CI

Copy-paste examples for using one OpenAI-compatible `base_url` across Cursor, Claude Code, Codex CLI, Aider, OpenHands, Flowise, LangChain, LlamaIndex, GitHub Actions, Node.js, Python, Go, Rust, Deno, and curl.

These examples use API NODE by default:

```text
Base URL: https://apinode.pro/v1
Model:    gpt-5.5
API:      OpenAI-compatible Chat Completions / Responses API
```

Use this repo when you want to:

- keep your app independent from one upstream provider;
- configure coding tools with a custom OpenAI-compatible endpoint;
- centralize API keys, quota, usage logs, and model/provider switching;
- reproduce API smoke tests in CI before changing your production app.

Need trial credits? Open a [Request trial credits issue](https://github.com/apinode-pro/openai-compatible-ai-gateway-examples/issues/new?template=request-trial-credits.yml) and include your use case.

[Try API NODE](https://apinode.pro)

## Quickstart

```bash
export APINODE_API_KEY="your_api_key"
export APINODE_BASE_URL="https://apinode.pro/v1"
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

If you are choosing between SDKs, coding agents, and troubleshooting docs, start
with [template and agent entrypoints](guides/template-and-agent-entrypoints.md).

If you cloned this repository and want the shortest path, start with
[after cloning this repo](guides/after-cloning-this-repo.md).

## Why This Repo Exists

Developers often want to test a new LLM provider or gateway without rewriting an app. Most modern AI tools and SDKs can use a custom OpenAI-compatible endpoint.

This repo keeps those setup paths small, explicit, and easy to verify.

## Examples

### curl

```bash
cd examples/curl
export APINODE_API_KEY="your_api_key"
export APINODE_BASE_URL="https://apinode.pro/v1"
export APINODE_MODEL="gpt-5.5"
curl "$APINODE_BASE_URL/chat/completions" \
  -H "Authorization: Bearer $APINODE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5.5",
    "messages": [{"role": "user", "content": "Say hello from API NODE"}]
  }'
```

### Node.js

```bash
cd examples/node
npm install
export APINODE_API_KEY="your_api_key"
export APINODE_BASE_URL="https://apinode.pro/v1"
export APINODE_MODEL="gpt-5.5"
npm start
```

### Python

```bash
cd examples/python
python3 -m pip install -r requirements.txt
export APINODE_API_KEY="your_api_key"
export APINODE_BASE_URL="https://apinode.pro/v1"
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
base_url = "https://apinode.pro/v1"
wire_api = "responses"
requires_openai_auth = true
```

## Guides

- [How to use one OpenAI-compatible base URL for GPT, Claude, Gemini, and coding agents](guides/one-openai-compatible-base-url.md)
- [Configure Cursor with an OpenAI-compatible API gateway](guides/configure-cursor-with-apinode.md)
- [Use Codex CLI with API NODE](guides/use-codex-cli-with-apinode.md)
- [Use Aider with API NODE](guides/aider-with-apinode.md)
- [Use OpenHands with API NODE](guides/openhands-with-apinode.md)
- [Building reliable LLM fallback with an OpenAI-compatible gateway](guides/reliable-llm-fallback.md)
- [Use LiteLLM with API NODE](guides/litellm-with-apinode.md)
- [LiteLLM OpenAI-compatible base URL quickstart](guides/litellm-openai-compatible-base-url-quickstart.md)
- [LiteLLM custom headers for OpenAI-compatible endpoints](guides/litellm-custom-headers-for-openai-compatible-endpoints.md)
- [Use Vercel AI SDK with API NODE](guides/vercel-ai-sdk-with-apinode.md)
- [Use LangChain JS with API NODE](guides/langchain-js-with-apinode.md)
- [Use LangGraph Python with API NODE](guides/langgraph-python-with-apinode.md)
- [Use LlamaIndex Python with API NODE](guides/llamaindex-python-with-apinode.md)
- [Call API NODE with fetch](guides/fetch-responses-api-with-apinode.md)
- [Use the Python OpenAI SDK Responses API with API NODE](guides/python-openai-sdk-responses-with-apinode.md)
- [Call the Responses API from Go with API NODE](guides/go-responses-api-with-apinode.md)
- [Call the Responses API from Rust with API NODE](guides/rust-responses-api-with-apinode.md)
- [Call the Responses API from Deno with API NODE](guides/deno-fetch-responses-api-with-apinode.md)
- [Test API NODE in a GitHub Actions matrix](guides/github-actions-matrix-with-apinode.md)
- [Use ruby-openai with API NODE](guides/ruby-openai-with-apinode.md)
- [Use Continue with API NODE](guides/continue-with-apinode.md)
- [Use Cline with API NODE](guides/cline-with-apinode.md)
- [Use Roo Code with API NODE](guides/roo-code-with-apinode.md)
- [Use Open WebUI with API NODE](guides/open-webui-with-apinode.md)
- [Use LibreChat with API NODE](guides/librechat-with-apinode.md)
- [Use Flowise with API NODE](guides/flowise-with-apinode.md)
- [OpenAI-compatible environment variable patterns](guides/openai-compatible-env-vars.md)
- [Endpoint readiness checklist](guides/endpoint-readiness-checklist.md)
- [Base URL path joining rules](guides/base-url-path-joining-rules.md)
- [Custom OpenAI base URL vs Chat Completions endpoint](guides/custom-openai-base-url-vs-chat-completions-endpoint.md)
- [Azure AI Foundry OpenAI-compatible v1 endpoint notes](guides/azure-ai-foundry-openai-compatible-v1.md)
- [Azure AI Foundry OpenAI-compatible maintainer case study](guides/azure-openai-compatible-maintainer-case-study.md)
- [App maintainer checklist for custom OpenAI-compatible providers](guides/app-maintainer-provider-protocol-checklist.md)
- [Provider abstraction for custom OpenAI-compatible endpoints](guides/provider-abstraction-for-custom-openai-compatible-endpoints.md)
- [OpenAI-compatible embeddings endpoint checklist](guides/openai-compatible-embeddings-endpoint.md)
- [OpenAI-compatible embeddings troubleshooting index](guides/embeddings-troubleshooting-index.md)
- [Separate chat and embeddings endpoints](guides/separate-chat-and-embeddings-endpoints.md)
- [Custom OpenAI endpoint issue triage checklist](guides/custom-endpoint-issue-triage-checklist.md)
- [Browser CORS and custom OpenAI-compatible endpoints](guides/browser-cors-custom-openai-endpoints.md)
- [Provider-specific request parameters](guides/provider-specific-request-parameters.md)
- [Token limit parameter compatibility](guides/token-limit-parameter-compatibility.md)
- [Reasoning model output budget notes](guides/reasoning-model-output-budget.md)
- [OpenAI-compatible request regression tests](guides/openai-compatible-request-regression-tests.md)
- [Maintainer regression test for custom OpenAI endpoints](guides/maintainer-regression-test-for-custom-openai-endpoints.md)
- [Maintainer-ready docs PR for an OpenAI-compatible provider](guides/maintainer-ready-openai-compatible-docs-pr.md)
- [Direct triage comments for custom endpoint issues](guides/direct-triage-comments-for-custom-endpoints.md)
- [OpenAI SDK custom base URL examples](guides/openai-sdk-custom-base-url-examples.md)
- [Base URL regression test fixtures](guides/base-url-regression-test-fixtures.md)
- [Agent base URL configuration examples](guides/agent-base-url-configuration-examples.md)
- [Codex provider block reference](guides/codex-provider-block-reference.md)
- [Choose the right OpenAI-compatible base URL](guides/choose-the-right-openai-compatible-base-url.md)
- [Template and agent entrypoints](guides/template-and-agent-entrypoints.md)
- [After cloning this repo](guides/after-cloning-this-repo.md)

## Troubleshooting

- [Troubleshoot 401 invalid API key](guides/troubleshoot-401-invalid-api-key.md)
- [Troubleshoot 404 base URL issues](guides/troubleshoot-404-base-url.md)
- [Troubleshoot model not found](guides/troubleshoot-model-not-found.md)
- [Troubleshoot custom OpenAI endpoint configuration](guides/troubleshoot-custom-openai-endpoint.md)
- [Troubleshoot runtime config not applied](guides/troubleshoot-runtime-config-not-applied.md)
- [Troubleshoot an endpoint routed to the wrong provider](guides/troubleshoot-endpoint-routed-to-wrong-provider.md)
- [Troubleshoot Azure OpenAI-compatible v1 api-version errors](guides/troubleshoot-azure-openai-v1-api-version.md)
- [Troubleshoot max_tokens vs max_completion_tokens](guides/troubleshoot-max-tokens-vs-max-completion-tokens.md)
- [Troubleshoot embeddings encoding_format null errors](guides/troubleshoot-embeddings-encoding-format-null.md)
- [Troubleshoot Responses API vs Chat Completions](guides/troubleshoot-responses-api-vs-chat-completions.md)
- [Troubleshoot streaming output](guides/troubleshoot-streaming-output.md)

## Requests, trial credits, and working configs

- Need trial credits? Open a [Request trial credits issue](https://github.com/apinode-pro/openai-compatible-ai-gateway-examples/issues/new?template=request-trial-credits.yml) with your tool, current problem, expected usage, and first test.
- Open an issue to request a new integration guide, report a compatibility issue, or share a working redacted config.
- Use Discussions for questions, guide ideas, and community config notes. See [DISCUSSIONS.md](DISCUSSIONS.md).

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
openai-api
responses-api
llm-api
llm-gateway
api-gateway
ai-api
claude-code
codex-cli
cursor
aider
openai
model-router
developer-tools
github-actions
langchain
llamaindex
```

## Contributing

Useful additions:

- More SDK recipes for popular OpenAI-compatible clients.
- More coding-agent and chat-app configuration examples.
- CI smoke tests for additional languages and package managers.
- Short troubleshooting notes for common base URL, model, and streaming issues.

Please do not commit API keys or account secrets.
