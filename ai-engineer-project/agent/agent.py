import json

import litellm
import os
from tools import tools
from tools import calculate

from document_mcp.process_document import answer_it

ollama_base = os.environ.get("OLLAMA_API_BASE", "http://localhost:11434")

messages = [
    {
        "role": "user",
        "content": "What is single responsibility?"
    }
]

for i in range(5):
    response = litellm.completion(
        api_base=ollama_base,
        model="ollama/qwen2.5:14b",
        messages=messages,
        tools=tools if i == 0 else None,
        tool_choice="auto" if i == 0 else None,
    )

    if response.choices[0].message.tool_calls is None:
        print("result: ", response.choices[0].message)
        break

    tool_call = response.choices[0].message.tool_calls[0]
    arguments = json.loads(tool_call.function.arguments)

    if tool_call.function.name == "calculate":
        result = calculate(arguments["expression"])
    elif tool_call.function.name == "answer_it":
        result = answer_it(arguments["question"]).answer

    messages.append(response.choices[0].message)
    messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": str(result)
    })
else:
    print("nem sikerült break-kel kilépni")






