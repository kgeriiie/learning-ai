import re

from datasets import load_dataset

from reasoning_agent import run_agent

from task01 import extract_final_answer

def extract_agent_answer(text: str):
    numbers = re.findall(r"[\d,]+\.?\d*", text)
    if not numbers:
        return None
    last_number = numbers[-1].replace(",", "")
    try:
        return float(last_number)
    except ValueError:
        return None

dataset = load_dataset("openai/gsm8k", "main")

test = dataset["test"]

questions = test["question"][:10]
answers = test["answer"][:10]

correct = 0
wrong_cases = []

for index, question in enumerate(questions):
    agent_answer = extract_agent_answer(run_agent(question=question))
    official_answer = extract_final_answer(answer=answers[index])

    print(index, "--------->")
    print(question, "\nagent: ", agent_answer,"\nofficial: ", official_answer)

    if agent_answer is not None and abs(agent_answer - official_answer) < 0.01:
        correct += 1
    else:
        wrong_cases.append((question, agent_answer, official_answer))

final_score = correct / len(questions) * 100

print("---------------------")
print("\nscore: ", final_score)
print("\nwrong cases: ", wrong_cases)