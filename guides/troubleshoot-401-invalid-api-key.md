# Troubleshoot 401 Invalid API Key With API NODE

A `401` response usually means the request reached the API gateway, but authentication failed.

## Check the key

```bash
test -n "$APINODE_API_KEY" && echo "APINODE_API_KEY is set"
```

Do not print the key itself in public logs.

## Check the header

Requests must include a bearer token:

```bash
curl "$APINODE_BASE_URL/responses" \
  -H "Authorization: Bearer $APINODE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-5.5","input":"Say hello"}'
```

## Common causes

- The environment variable is empty in the current shell.
- The CI secret name does not match the workflow environment variable.
- The key was pasted with extra spaces or line breaks.
- The key was revoked or expired.
- Browser-side code is calling the API directly and exposing the key.

## Safe CI check

```bash
if [ -z "$APINODE_API_KEY" ]; then
  echo "APINODE_API_KEY is missing"
  exit 1
fi
```

## Next step

If the key is set and the request still returns `401`, rotate the key and update the secret manager or GitHub Actions secret.
