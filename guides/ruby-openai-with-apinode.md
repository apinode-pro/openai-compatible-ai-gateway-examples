# Use ruby-openai With API NODE

The `ruby-openai` gem supports custom API endpoints through `uri_base`.

API NODE endpoint:

```text
https://apinode.pro
```

## Environment

```bash
export APINODE_API_KEY="your_api_key"
export APINODE_MODEL="gpt-5.5"
```

## Example

```ruby
require "openai"

client = OpenAI::Client.new(
  access_token: ENV.fetch("APINODE_API_KEY"),
  uri_base: "https://apinode.pro"
)

response = client.responses.create(
  parameters: {
    model: ENV.fetch("APINODE_MODEL", "gpt-5.5"),
    input: "Say hello from API NODE"
  }
)

puts response.dig("output", 0, "content", 0, "text")
```

## Notes

- Keep `APINODE_API_KEY` outside source code.
- Use a model enabled for your API NODE account.
- This setup uses the same `uri_base` pattern as other OpenAI-compatible endpoints.

