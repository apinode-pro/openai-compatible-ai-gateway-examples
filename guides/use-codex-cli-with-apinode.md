# Use Codex CLI With API NODE

API NODE can be configured as an OpenAI-compatible model provider for Codex CLI.

Use this configuration:

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

Keep your key outside the config file:

```bash
export APINODE_API_KEY="your_api_key"
```

## Smoke Test

Use a small prompt first:

```text
Create a one-line JavaScript function that adds two numbers.
```

Then try a repository-aware task:

```text
Inspect this repository and summarize the project in three bullets.
```

Try API NODE:

```text
https://apinode.pro
```

