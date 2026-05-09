# Azure AI Foundry OpenAI-Compatible Maintainer Case Study

This note summarizes a real maintainer-friendly fix pattern for Azure AI Foundry endpoints that expose an OpenAI-compatible `/openai/v1` path.

## Problem Shape

An app may support classic Azure OpenAI deployment URLs and still fail with Azure AI Foundry OpenAI-compatible URLs.

Classic Azure deployment-style URLs often expect an `api-version` query parameter. Azure AI Foundry OpenAI-compatible `/openai/v1` URLs can fail when an app appends that same parameter.

The safe behavior is path-aware:

- Keep the Azure `api-version` default for deployment-style Azure URLs.
- Omit or strip `api-version` for `/openai/v1` URLs when no version is explicitly configured.
- Route `/openai/v1` chat requests to `/chat/completions`.
- Put the deployment or model name in the request body `model` field.

## Redacted Config Shape

```text
base_url: https://<resource>.services.ai.azure.com/api/projects/<project>/openai/v1
model: <deployment-or-model-name>
api_version: empty
```

## Regression Tests To Add

Add tests for both URL shapes:

- Classic Azure deployment URL with blank `api_version` still gets the default version.
- `/openai/v1` URL with blank `api_version` does not send `api-version`.
- `/openai/v1` URL copied with `?api-version=...` strips the query parameter when the field is blank.
- Connection-test code and runtime proxy code behave the same way.

## Maintainer Reply Template

```text
Thanks for the report. This looks like the app needs to distinguish classic Azure deployment URLs from Azure AI Foundry OpenAI-compatible /openai/v1 URLs.

The behavior I would test is:
- deployment-style Azure URLs keep the default api-version
- /openai/v1 URLs omit or strip api-version when the field is blank
- /openai/v1 calls route to /chat/completions with the selected deployment/model in the request body

That should preserve existing Azure users while fixing OpenAI-compatible Foundry endpoints.
```

