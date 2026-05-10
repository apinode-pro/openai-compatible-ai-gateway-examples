# Token Limit Parameter Compatibility

Different OpenAI-compatible endpoints can use different names for the output token budget. A request can be otherwise compatible and still fail because the wrong token-limit field is sent.

## Quick Matrix

| API or provider shape | Safer token field |
|---|---|
| Responses API | `max_output_tokens` |
| OpenAI Chat Completions, newer reasoning models | `max_completion_tokens` |
| Many older Chat Completions models | `max_tokens` |
| Anthropic Messages API | `max_tokens` |
| Some Azure AI Foundry model-inference deployments | model/provider dependent |

The important rule is to send only one token-limit field per request.

## Bad Pattern

```json
{
  "model": "gpt-5.5",
  "messages": [],
  "max_tokens": 1000,
  "max_completion_tokens": 1000
}
```

This is ambiguous and often rejected.

## Better Pattern

Choose the field in the provider adapter or request builder:

```python
def token_limit_param(api_shape: str, model: str) -> str:
    if api_shape == "responses":
        return "max_output_tokens"
    if api_shape == "anthropic-messages":
        return "max_tokens"
    if model.startswith(("gpt-5", "o1", "o3", "o4")):
        return "max_completion_tokens"
    return "max_tokens"
```

Then build the request body with one field:

```python
body[token_limit_param(api_shape, model)] = max_tokens
```

## Regression Tests

Add tests for each adapter path:

- Responses requests send `max_output_tokens`.
- Newer OpenAI reasoning-model chat requests send `max_completion_tokens`.
- Older chat-completions requests keep `max_tokens` if supported.
- Anthropic requests keep `max_tokens`.
- A request never includes both `max_tokens` and `max_completion_tokens`.

