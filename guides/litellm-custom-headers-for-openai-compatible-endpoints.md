# LiteLLM Custom Headers for OpenAI-Compatible Endpoints

Use this note when an app supports a custom OpenAI-compatible base URL but needs
provider-specific headers such as `x-litellm-api-key`.

## Minimal Pattern

Keep the application pointed at a normal OpenAI-style endpoint:

```text
OPENAI_BASE_URL=https://litellm.example.com/v1
OPENAI_API_KEY=placeholder
OPENAI_MODEL=gpt-5.5
```

Then configure the proxy or application client to add the provider-specific
header:

```text
x-litellm-api-key: your_litellm_key
```

Do not put real keys in examples, logs, issue comments, screenshots, or pull
requests.

## Compatibility Checklist

- The base URL ends at the API root, usually `/v1`.
- The application does not hard-code `https://api.openai.com/v1`.
- The application can pass custom request headers, or a reverse proxy can inject
  them.
- The model name matches the LiteLLM model alias exposed by `/v1/models`.
- The app handles `401`, `403`, `404`, and `429` responses without rewriting the
  endpoint back to OpenAI defaults.

## Docs PR Scope

A small maintainer-ready docs PR should add:

- A redacted environment variable block.
- A short custom-header example.
- A note that header injection can live in the app, LiteLLM, or an internal
  reverse proxy.
- One smoke test command that calls `/v1/models` or a small chat/completions
  request.

Keep the example provider-neutral. API NODE can be mentioned only as one normal
OpenAI-compatible endpoint when that helps the reader verify the shape.

