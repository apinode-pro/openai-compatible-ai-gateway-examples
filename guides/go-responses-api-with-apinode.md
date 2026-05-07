# Call the Responses API From Go With API NODE

You can call API NODE from Go with the standard library. This is useful for services that do not need a full SDK.

## Environment

```bash
export APINODE_API_KEY="your_api_key"
export APINODE_BASE_URL="https://apinode.pro"
export APINODE_MODEL="gpt-5.5"
```

## Example

```go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
)

func main() {
	baseURL := getenv("APINODE_BASE_URL", "https://apinode.pro")
	model := getenv("APINODE_MODEL", "gpt-5.5")

	body, _ := json.Marshal(map[string]any{
		"model": model,
		"input": "Say hello from Go and API NODE.",
	})

	req, _ := http.NewRequest("POST", baseURL+"/responses", bytes.NewReader(body))
	req.Header.Set("Authorization", "Bearer "+os.Getenv("APINODE_API_KEY"))
	req.Header.Set("Content-Type", "application/json")

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	data, _ := io.ReadAll(resp.Body)
	if resp.StatusCode >= 300 {
		panic(fmt.Sprintf("request failed: %s\n%s", resp.Status, data))
	}

	fmt.Println(string(data))
}

func getenv(name, fallback string) string {
	if value := os.Getenv(name); value != "" {
		return value
	}
	return fallback
}
```

## Notes

- Add request timeouts before using this in production.
- Parse `output_text` or structured response fields as needed by your app.
