# Maintainer Regression Test for Custom OpenAI Endpoints

Use this when a bug report says a custom OpenAI-compatible endpoint works in
curl but fails in an app.

## Minimal Test Cases

Create a request-builder test that checks these inputs:

| Input | Expected POST target |
| --- | --- |
| `https://provider.example.com/v1` | `https://provider.example.com/v1/chat/completions` |
| `https://provider.example.com/v1/` | `https://provider.example.com/v1/chat/completions` |
| `https://provider.example.com/v1/chat/completions` | `https://provider.example.com/v1/chat/completions` |

## Assertions

- The configured model name is passed unchanged.
- The API key is sent as an authorization header or documented custom header.
- The test does not call the real provider.
- Validation errors include the endpoint shape problem, not a generic unknown
  error.
- Redacted logs show the resolved request URL.

## PR Scope

A useful first PR should include:

- One URL normalization helper.
- One validation path using the helper.
- One runtime request path using the helper.
- Regression tests for base URL and full endpoint input.

Avoid adding provider-specific promotion to the fix. The bug is the request
builder contract.

