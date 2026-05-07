# Test API NODE in a GitHub Actions Matrix

A matrix smoke test helps verify that multiple runtimes can reach the same OpenAI-compatible API gateway.

## Secret

Add this repository secret:

```text
APINODE_API_KEY
```

## Workflow

```yaml
name: API NODE matrix smoke test

on:
  workflow_dispatch:

jobs:
  smoke:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [20, 22]
    steps:
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}

      - name: Call Responses API
        env:
          APINODE_API_KEY: ${{ secrets.APINODE_API_KEY }}
          APINODE_BASE_URL: https://apinode.pro
          APINODE_MODEL: gpt-5.5
        run: |
          node -e '
          const response = await fetch(`${process.env.APINODE_BASE_URL}/responses`, {
            method: "POST",
            headers: {
              Authorization: `Bearer ${process.env.APINODE_API_KEY}`,
              "Content-Type": "application/json"
            },
            body: JSON.stringify({
              model: process.env.APINODE_MODEL,
              input: "Say hello from GitHub Actions and API NODE."
            })
          });
          if (!response.ok) throw new Error(await response.text());
          const body = await response.json();
          console.log(body.output_text || JSON.stringify(body).slice(0, 500));
          '
```

## Notes

- Keep the sample count low in CI.
- Use scheduled checks only after confirming cost and rate limits.
- Never print full secrets or request headers in logs.
