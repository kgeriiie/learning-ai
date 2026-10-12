import litellm

response = litellm.completion(
    model="anthropic/claude-haiku-4-5-20251001",
    messages=[
        {"role":"user", "content": "1 usd how many hungarian forint?"}
    ]
)
print(response["choices"][0]["message"]["content"])