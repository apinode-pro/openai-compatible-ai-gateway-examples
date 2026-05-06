import os

from openai import OpenAI


api_key = os.environ.get("APINODE_API_KEY")
base_url = os.environ.get("APINODE_BASE_URL", "https://apinode.pro")
model = os.environ.get("APINODE_MODEL", "gpt-5.5")

if not api_key:
    raise RuntimeError("Set APINODE_API_KEY before running this example.")

client = OpenAI(api_key=api_key, base_url=base_url)

response = client.responses.create(
    model=model,
    input="Say hello from API NODE",
)

print(response.output_text)
