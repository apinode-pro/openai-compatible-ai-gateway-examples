# Choose the Right OpenAI-Compatible Base URL

Most custom endpoint bugs come from mixing up the provider origin, `/v1`, and
the request path.

Use this guide before opening a provider issue or changing SDK code.

## Quick Decision Table

| Client sends | Use this base URL | Final path |
| --- | --- | --- |
| OpenAI Responses API | `https://apinode.pro` | `/responses` |
| OpenAI Chat Completions | `https://apinode.pro/v1` | `/chat/completions` |
| OpenAI Embeddings | `https://apinode.pro/v1` | `/embeddings` |
| Client appends `/v1` itself | provider origin only | client-managed |

## Responses API Example

```bash
export OPENAI_API_KEY="your_api_key"
export OPENAI_BASE_URL="https://apinode.pro"
export OPENAI_MODEL="gpt-5.5"
```

The final request path is:

```text
https://apinode.pro/responses
```

## Chat Completions Example

```bash
export OPENAI_API_KEY="your_api_key"
export OPENAI_BASE_URL="https://apinode.pro/v1"
export OPENAI_MODEL="gpt-5.5"
```

The final request path is:

```text
https://apinode.pro/v1/chat/completions
```

## Regression Test To Add

```text
configured_base_url + request_path = expected_final_url
```

Test at least:

- custom host is used instead of `api.openai.com`
- `/v1` appears exactly once
- API keys are redacted in logs and snapshots

## Related Guides

- [Base URL path joining rules](base-url-path-joining-rules.md)
- [Base URL regression test fixtures](base-url-regression-test-fixtures.md)
- [OpenAI SDK custom base URL examples](openai-sdk-custom-base-url-examples.md)
