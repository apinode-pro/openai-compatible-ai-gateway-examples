# One `base_url` for Cursor, Claude Code, Codex, and agent scripts

A common failure mode in AI coding-tool setups is spreading provider-specific configuration across every tool:

- Cursor uses one endpoint and key
- Claude Code or Codex CLI uses another
- local scripts use direct OpenAI-compatible SDK settings
- GitHub Actions or internal agents have their own env vars

That works until a provider starts returning 429s, a model name changes, or a teammate needs to switch providers quickly.

A cleaner pattern is to keep client tools pointed at one OpenAI-compatible endpoint and move provider/model routing behind that layer.

```bash
export OPENAI_BASE_URL="https://api.apinode.pro/v1"
export OPENAI_API_KEY="your_api_key"
```

Why this helps:

1. Tool configs stay stable.
2. Keys and quota can be managed centrally.
3. Usage logs are easier to compare across tools.
4. Provider fallback can happen behind the same interface.
5. 429/timeout debugging becomes an upstream-routing problem instead of an app-config mystery.

This repo keeps examples for that workflow across coding agents, SDKs, and automation scripts.
