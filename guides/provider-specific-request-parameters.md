# Provider-Specific Request Parameters

OpenAI-compatible does not mean every provider accepts every request parameter. The endpoint path and response shape may be compatible while some fields still differ by model or provider.

## Common Parameter Differences

| API shape | Common output limit field |
|---|---|
| Responses API | `max_output_tokens` |
| Chat Completions, newer OpenAI-compatible models | `max_completion_tokens` |
| Chat Completions, older models and many local servers | `max_tokens` |
| Anthropic messages API | `max_tokens` |

Other fields that may vary:

- `temperature`
- `top_p`
- `parallel_tool_calls`
- `reasoning_effort`
- `response_format`
- `tool_choice`
- `encoding_format` for embeddings

## App Maintainer Pattern

Keep a small provider capability layer instead of scattering conditionals through the app.

```text
provider protocol -> supported request fields
model id -> parameter constraints
runtime path -> request builder
```

This makes it easier to fix one provider without breaking others.

## Useful Errors To Surface

Show the user the first safe upstream error line:

```text
Unsupported parameter: max_tokens
Model not found
api-version query parameter is not allowed when using /v1 path
```

Do not replace these with a generic "provider failed" message. The exact upstream error often identifies the fix.

## Minimal Compatibility Probe

Start with the smallest possible request:

```json
{
  "model": "model-id",
  "messages": [
    {
      "role": "user",
      "content": "Reply OK"
    }
  ]
}
```

Then add optional parameters one at a time. The first added field that breaks identifies the compatibility gap.

