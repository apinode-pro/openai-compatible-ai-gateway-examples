# Base URL Regression Test Fixtures

Use these fixtures when adding tests for custom OpenAI-compatible endpoints.

## Fixture 1: Responses API

```json
{
  "api_family": "openai-responses",
  "base_url": "https://apinode.pro",
  "path": "/responses",
  "expected_final_url": "https://apinode.pro/responses"
}
```

## Fixture 2: Chat Completions With `/v1`

```json
{
  "api_family": "openai-chat-completions",
  "base_url": "https://apinode.pro/v1",
  "path": "/chat/completions",
  "expected_final_url": "https://apinode.pro/v1/chat/completions"
}
```

## Fixture 3: Prevent Double `/v1`

```json
{
  "api_family": "openai-chat-completions",
  "base_url": "https://example.test/v1",
  "path": "/v1/chat/completions",
  "expected_error": "base URL and path both include /v1"
}
```

## Fixture 4: Do Not Fall Back To OpenAI

```json
{
  "configured_base_url": "https://example.test/v1",
  "forbidden_host": "api.openai.com"
}
```

## What To Assert

- The final URL uses the saved custom base URL.
- The request path is appended exactly once.
- API keys are redacted in logs and test failures.
- The selected adapter matches the configured API family.

## Related Guides

- [Base URL path joining rules](base-url-path-joining-rules.md)
- [OpenAI-compatible request regression tests](openai-compatible-request-regression-tests.md)
