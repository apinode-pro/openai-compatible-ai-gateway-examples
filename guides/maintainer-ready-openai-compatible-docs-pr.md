# Maintainer-Ready Docs PR for an OpenAI-Compatible Provider

Use this checklist when a project maintainer asks for custom endpoint, base URL, or OpenAI-compatible provider documentation.

## Small PR Scope

Keep the first PR narrow:

```text
- one config snippet
- one exact base URL
- one model placeholder
- one verification command
- one limitation note
```

Avoid broad provider comparisons, pricing claims, or performance claims.

## Copy-Paste Snippet

```text
Provider: OpenAI-compatible
Base URL: https://apinode.pro
API key: <redacted>
Model: gpt-5.5
API shape: Responses API
```

If the app only supports Chat Completions, state that explicitly:

```text
Provider: OpenAI-compatible
Base URL: https://apinode.pro/v1
API key: <redacted>
Model: gpt-5.5
API shape: Chat Completions
```

## Verification Step

Add one concrete smoke test:

```bash
curl "$OPENAI_BASE_URL/responses" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-5.5","input":"Say hello"}'
```

For Chat Completions clients, verify the client app builds the final path correctly and does not double-append `/v1`.

## Direct PR Comment

Use direct contribution language:

```text
I can open a small docs PR with a redacted OpenAI-compatible config, the exact base URL shape, and one smoke-test command. The minimal useful change is a short provider-neutral snippet plus a note about whether the client expects /v1.
```

## Review Checklist

- The API key is redacted.
- The base URL matches the client's expected path joining behavior.
- The model name is a placeholder or current example, not a hard guarantee.
- The guide does not ask maintainers to promote a provider.
- The PR can be merged even if the maintainer swaps in a different OpenAI-compatible provider.

## Related Guides

- [Base URL path joining rules](base-url-path-joining-rules.md)
- [OpenAI-compatible request regression tests](openai-compatible-request-regression-tests.md)
- [App maintainer checklist for custom OpenAI-compatible providers](app-maintainer-provider-protocol-checklist.md)
