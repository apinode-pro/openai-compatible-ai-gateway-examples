# LiteLLM OpenAI-Compatible Base URL Quickstart

Use this when you want LiteLLM to route requests through an
OpenAI-compatible gateway.

## Minimal Config

```yaml
model_list:
  - model_name: apinode-gpt-5-5
    litellm_params:
      model: openai/gpt-5.5
      api_base: https://apinode.pro
      api_key: os.environ/APINODE_API_KEY
```

Use `api_base: https://apinode.pro` for Responses API style routing when the
caller expects the gateway root. Use `https://apinode.pro/v1` only for clients
that build Chat Completions paths under `/v1`.

## Smoke Test

```bash
export APINODE_API_KEY="your_api_key"
litellm --config config.yaml
```

Then send a small request through the local LiteLLM proxy.

## Checks

- The final upstream host is `apinode.pro`, not `api.openai.com`.
- The request path includes `/v1` exactly once for Chat Completions callers.
- API keys are read from environment variables.
- Logs do not include raw authorization headers.

## Related Guides

- [Use LiteLLM with API NODE](litellm-with-apinode.md)
- [Choose the right OpenAI-compatible base URL](choose-the-right-openai-compatible-base-url.md)
- [Base URL regression test fixtures](base-url-regression-test-fixtures.md)
