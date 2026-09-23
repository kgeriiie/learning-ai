import json

import litellm
import os
import sys

current_dir = os.path.dirname(__file__)
agent_dir = os.path.join(current_dir, "..", "agent")
sys.path.append(agent_dir)

from agent_tools import tools
from agent_tools import calculate

from document_mcp.process_document import answer_it

ollama_base = os.environ.get("OLLAMA_API_BASE", "http://localhost:11434")

def run_agent(
    question: str,
    model: str = "ollama/qwen2.5:14b",
    max_iterations: int = 5,
) -> str:
    messages = [
        {
            "role": "user",
            "content": question
        }
    ]

    for i in range(max_iterations):
        response = litellm.completion(
            api_base=ollama_base,
            model=model,
            messages=messages,
            tools=tools if i == 0 else None,
            tool_choice="auto" if i == 0 else None,
        )

        if response.choices[0].message.tool_calls is None:
            return response.choices[0].message.content

        try:
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
        except Exception as e:
            print(f"Hiba történt: {e}")
            return ""
    else:
        print("nem sikerült break-kel kilépni")
        return ""