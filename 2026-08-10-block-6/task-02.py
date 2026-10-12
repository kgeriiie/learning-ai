import litellm

try:
    response = litellm.completion(
        model="ollama/llama3.2",
        messages=[
            {"role":"user", "content": "1 usd how many hungarian forint?"}
        ]
    )
    print(response["choices"][0]["message"]["content"])
except Exception as e:
    print("Hiba a model betöltésekor", e)
