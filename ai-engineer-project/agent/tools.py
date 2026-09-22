
def calculate(expression: str) -> float:
    result = eval(expression, {"__builtins__": {}}, {})
    return float(result)

tools = [
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Calculate mathematical expression",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Expression to calculate",
                    }
                },
                "required": ["expression"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "answer_it",
            "description": "Answer the question from the Clean Code book.",
            "parameters": {
                "type": "object",
                "properties": {
                    "question": {
                        "type": "string",
                        "description": "Clean Code related question",
                    }
                },
                "required": ["question"]
            }
        }
    }
]