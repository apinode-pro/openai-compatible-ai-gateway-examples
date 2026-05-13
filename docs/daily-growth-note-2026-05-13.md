# Daily note: one OpenAI-compatible endpoint for coding agents

When a team uses Cursor, Claude Code, Codex CLI, SDK scripts, and internal agents at the same time, provider-specific configuration tends to spread everywhere:

- different `base_url` values per tool
- different API keys per developer or script
- model names that work in one provider but fail in another
- unclear 429/timeout source when something breaks

A practical pattern is to keep every client pointed at one OpenAI-compatible endpoint, then move provider/model routing behind a gateway layer.

```bash
export OPENAI_BASE_URL="https://api.apinode.pro/v1"
export OPENAI_API_KEY="your_api_key"
```

Benefits:

- one stable `base_url` across Cursor, Claude Code, Codex CLI, and app code
- centralized usage logs and quota tracking
- easier provider switching and fallback
- clearer debugging for upstream 429s, timeouts, and model-name mismatches

This repo collects small examples for that workflow. If you want trial credits for a real Cursor / Claude Code / Codex / app setup, open a Request trial credits issue and include your use case.
