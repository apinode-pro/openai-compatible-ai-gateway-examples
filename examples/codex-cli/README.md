# API NODE Codex CLI Setup

Use API NODE as an OpenAI-compatible endpoint in Codex CLI.

Recommended config:

```toml
model_provider = "OpenAI"
model = "gpt-5.5"
review_model = "gpt-5.5"
model_reasoning_effort = "xhigh"
disable_response_storage = true
network_access = "enabled"
windows_wsl_setup_acknowledged = true
model_context_window = 1000000
model_auto_compact_token_limit = 900000

[model_providers.OpenAI]
name = "OpenAI"
base_url = "https://apinode.pro"
wire_api = "responses"
requires_openai_auth = true
```

Suggested smoke test prompt:

```text
Create a one-line JavaScript function that adds two numbers.
```

If your Codex CLI configuration file uses environment variables, keep secrets outside the committed config:

```bash
export APINODE_API_KEY="your_api_key"
```
