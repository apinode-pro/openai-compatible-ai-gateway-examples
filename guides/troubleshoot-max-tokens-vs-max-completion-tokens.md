# Troubleshoot `max_tokens` vs `max_completion_tokens`

Some newer OpenAI-compatible endpoints reject `max_tokens` and require `max_completion_tokens` instead.

## Symptom

An endpoint returns an error like:

```text
Unsupported parameter: 'max_tokens' is not supported with this model. Use 'max_completion_tokens' instead.
```

This often appears with newer reasoning-capable models, Azure AI Foundry deployments, or gateways that closely follow the newer OpenAI chat-completions parameter shape.

## What To Check

- Is the app using Chat Completions, Responses API, or a provider-native API?
- Is the model a newer GPT-style deployment that rejects `max_tokens`?
- Does the app hardcode `max_tokens` in both connection tests and runtime calls?
- Does the app use the same request body for Anthropic and OpenAI-compatible providers?

## Provider-Neutral Fix

Do not blindly replace every `max_tokens` field in the codebase. Keep the field protocol-aware:

```text
Anthropic-style messages API: max_tokens
OpenAI-compatible newer chat models: max_completion_tokens
Responses API: max_output_tokens
```

## Test Cases

Add regression tests for:

- Connection test request body.
- Runtime chat request body.
- Streaming request body.
- The provider branch that must keep `max_tokens`.
- The OpenAI-compatible branch that must send `max_completion_tokens`.

## Safe User Workaround

If the app exposes custom request parameters, remove `max_tokens` and set the provider-supported equivalent. If the app hardcodes the field, it needs a code fix.

