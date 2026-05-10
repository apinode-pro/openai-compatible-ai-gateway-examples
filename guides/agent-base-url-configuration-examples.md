# Agent Base URL Configuration Examples

Use these examples when a coding agent or IDE supports an OpenAI-compatible
base URL.

## Common Environment Pattern

```bash
export OPENAI_API_KEY="your_api_key"
export OPENAI_BASE_URL="https://apinode.pro"
export OPENAI_MODEL="gpt-5.5"
```

Keep real keys in local settings, environment variables, or a secret manager.
Do not commit them.

## Responses API Agents

Use this when the agent sends OpenAI Responses API requests:

```text
Base URL: https://apinode.pro
Request path: /responses
Model: gpt-5.5
```

## Chat Completions Agents

Use this when the agent sends Chat Completions requests:

```text
Base URL: https://apinode.pro/v1
Request path: /chat/completions
Model: gpt-5.5
```

## Verification Prompt

Use a small non-sensitive prompt first:

```text
Reply with the word ready.
```

Then confirm:

- The agent used the configured provider entry.
- The final request host was the custom base URL.
- The request path did not contain duplicate `/v1/v1`.
- Any local logs redact the API key.

## Maintainer PR Scope

A useful docs PR should add:

- one redacted config block
- the exact base URL shape
- the expected API family
- one verification step
- one limitation note when the client cannot use custom local endpoints
