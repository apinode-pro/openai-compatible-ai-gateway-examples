# Custom OpenAI Base URL vs Chat Completions Endpoint

Many OpenAI-compatible providers document a base URL such as:

```text
https://provider.example.com/v1
```

Applications that call Chat Completions must send requests to:

```text
https://provider.example.com/v1/chat/completions
```

Do not post directly to `/v1` unless the provider explicitly documents that path
as a runnable endpoint.

## Maintainer Rule

If a UI field is named `base_url`, normalize it before making the request:

```text
input:  https://provider.example.com/v1
call:   https://provider.example.com/v1/chat/completions
```

If the UI field is named `endpoint`, either require the full endpoint or accept
both shapes and normalize safely.

## Safe Normalization

- Trim trailing `/`.
- If the URL ends with `/v1`, append `/chat/completions`.
- If the URL already ends with `/v1/chat/completions`, keep it unchanged.
- Do not append twice.
- Do not rewrite provider-specific endpoints such as Azure deployment URLs.

## Regression Test

Add a test with both accepted inputs:

```text
https://provider.example.com/v1
https://provider.example.com/v1/chat/completions
```

Both should produce the same POST target:

```text
https://provider.example.com/v1/chat/completions
```

The test should assert the exact outbound URL, not just that validation returns
success.

