import OpenAI from "openai";

const apiKey = process.env.APINODE_API_KEY;
const baseURL = process.env.APINODE_BASE_URL || "https://apinode.pro";
const model = process.env.APINODE_MODEL || "gpt-5.5";

if (!apiKey) {
  throw new Error("Set APINODE_API_KEY before running this example.");
}

const client = new OpenAI({ apiKey, baseURL });

const response = await client.responses.create({
  model,
  input: "Say hello from API NODE",
});

console.log(response.output_text);
