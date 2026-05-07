# Call the Responses API From Rust With API NODE

Rust services can call API NODE with `reqwest` and a small JSON payload.

## Environment

```bash
export APINODE_API_KEY="your_api_key"
export APINODE_BASE_URL="https://apinode.pro"
export APINODE_MODEL="gpt-5.5"
```

## Example

```rust
use reqwest::Client;
use serde_json::json;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("APINODE_API_KEY")?;
    let base_url = std::env::var("APINODE_BASE_URL")
        .unwrap_or_else(|_| "https://apinode.pro".to_string());
    let model = std::env::var("APINODE_MODEL")
        .unwrap_or_else(|_| "gpt-5.5".to_string());

    let response = Client::new()
        .post(format!("{}/responses", base_url))
        .bearer_auth(api_key)
        .json(&json!({
            "model": model,
            "input": "Say hello from Rust and API NODE."
        }))
        .send()
        .await?;

    let status = response.status();
    let text = response.text().await?;
    if !status.is_success() {
        return Err(format!("request failed: {}\n{}", status, text).into());
    }

    println!("{}", text);
    Ok(())
}
```

## Notes

- Keep API keys in environment variables or your deployment secret manager.
- Add retries and timeouts for background jobs.
