from datasets import load_dataset

dataset = load_dataset("openai/gsm8k", "main")

train = dataset["train"]
test = dataset["test"]

train_question = train["question"][:3]
train_answer = train["answer"][:3]

def answer_the_question_at_index(question:str):
    index = next((i for i, item in enumerate(train_question) if item == question), None)

    if index is None:
        return None

    answer = train_answer[index]

    result = answer.split("#### ")[1]

    return result

def extract_final_answer(answer: str) -> float:
    result = answer.split("#### ")[1]
    return float(result)

for index, item in enumerate(train_answer):
    answered_value = extract_final_answer(item)
    print(answered_value)

