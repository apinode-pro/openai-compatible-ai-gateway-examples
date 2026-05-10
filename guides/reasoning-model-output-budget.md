# Reasoning Model Output Budget Notes

Some reasoning-capable models count internal reasoning tokens against the same completion budget that visible output uses. If the budget is too small or reasoning effort is too high, the request may succeed but return little or no visible text.

## Symptoms

- HTTP status is 200.
- Token usage is non-zero.
- The visible message is empty, truncated, or missing expected JSON.
- Retrying with the same small budget repeats the failure.

## What To Check

- Which API shape is used: Responses API or Chat Completions.
- Which output budget field is used: `max_output_tokens`, `max_completion_tokens`, or `max_tokens`.
- Whether the model supports a reasoning-effort control.
- Whether the task needs reasoning, or only extraction/classification/formatting.

## Safer Defaults For Extraction

For deterministic extraction, JSON classification, routing, or small rewrites:

- Use a sufficient output token budget.
- Prefer minimal or low reasoning effort when the API supports it.
- Keep the prompt explicit about returning only the final JSON or final answer.
- Add a test that fails when output text is missing even if HTTP status is 200.

## App Maintainer Checklist

- Treat "200 with empty output" as a compatibility failure.
- Log redacted usage fields when available.
- Separate output budget from context/input budget in the UI.
- Document provider/model-specific parameter constraints.

