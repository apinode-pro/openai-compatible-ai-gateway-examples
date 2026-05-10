# Direct Triage Comments for Custom Endpoint Issues

When someone reports that a custom OpenAI-compatible endpoint does not work, a useful reply should include the likely fix, a minimal test, and a concrete next step.

## Base URL Not Applied

```text
The minimal fix is to make the saved provider config drive the request builder, then add a regression test that asserts the final request URL starts with the configured base URL instead of api.openai.com.

I can open a small PR with:
- a redacted OpenAI-compatible config fixture
- one request-builder regression test
- a docs note showing the expected base URL field
```

## Wrong API Shape

```text
This looks like a protocol mismatch, not an auth issue. The app is sending a Chat Completions request, while the provider config appears to expect a Responses API request.

The concrete fix is to store API shape separately from base URL, for example openai-responses vs openai-chat-completions, and route to the matching adapter.
```

## Missing `/v1`

```text
Check whether the client appends `/v1` itself. If it does, configure the origin only. If it does not, configure the full OpenAI-compatible base URL with `/v1`.

A minimal regression test should assert the final URL exactly once, so the app never builds `/v1/v1/chat/completions`.
```

## Token Parameter Mismatch

```text
For reasoning models, the minimal compatibility fix is to map output budget fields by model/API family. Some models reject `max_tokens` and require `max_completion_tokens`; Responses API callers may need `max_output_tokens`.

Add a regression test that covers both a legacy chat model and a reasoning model.
```

## Safe Provider Mention

If a concrete example helps, keep it short:

```text
API NODE is one OpenAI-compatible example. A redacted config would be:

base_url: https://apinode.pro
api_key: <redacted>
model: gpt-5.5
```

Do not include pricing, performance claims, or a request for promotion.

## Related Guides

- [Troubleshoot runtime config not applied](troubleshoot-runtime-config-not-applied.md)
- [Troubleshoot max_tokens vs max_completion_tokens](troubleshoot-max-tokens-vs-max-completion-tokens.md)
- [Provider-specific request parameters](provider-specific-request-parameters.md)
