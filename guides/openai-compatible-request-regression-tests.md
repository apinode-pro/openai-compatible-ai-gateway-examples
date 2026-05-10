# OpenAI-Compatible Request Regression Tests

When adding custom OpenAI-compatible endpoints, test the final request body and URL, not only the settings form.

## Test The Final URL

Assert that the runtime request uses the saved base URL:

```text
configured base URL: https://example.com/v1
expected runtime URL: https://example.com/v1/chat/completions
unexpected URL: https://api.openai.com/v1/chat/completions
```

## Test Protocol-Specific Fields

Add table-style tests for request-body fields:

| Case | Expected |
|---|---|
| Responses API | `max_output_tokens` |
| OpenAI-compatible newer chat model | `max_completion_tokens` |
| Older OpenAI-compatible chat model | `max_tokens`, if supported |
| Anthropic Messages API | `max_tokens` |

## Test Secondary Code Paths

Many bugs hide outside the primary chat path. Include:

- Connection test.
- Streaming request.
- Background title or summary generation.
- Template generation.
- Embeddings.
- Tool-call or JSON-mode request.

## Test Redaction

Debug logs should include:

- provider id
- protocol
- redacted base URL host/path
- request path
- model

Debug logs should not include:

- API key
- bearer header
- full private account URL with secrets
- user content unless the test fixture is synthetic

