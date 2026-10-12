import os
os.environ["OMP_NUM_THREADS"] = "1"
import faiss
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import litellm
import time
from AnswerResult import AnswerResult

def read_samples_as_lines():
    with open("../2026-07-23-block-2/samples.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Clean up newlines from all lines
    lines = [line.strip() for line in lines]
    return lines

def answer_the_question(question_text, lines, indexes):
    qa_pipeline = pipeline("question-answering")

    result = ""
    for indexOfFundedSentence in indexes:
        text = qa_pipeline(
            question=question_text,
            context=lines[indexOfFundedSentence],
        )

        if result == "":
            result = text["answer"]
        else:
            result = result + ", " + text["answer"]

    return result


def generate_answer(question, context, retry_count =3, base_delay=1):
    # Loop from 0 to retry_count (inclusive)
    for i in range(retry_count + 1):
        try:
            # Construct prompt using f-string formatting
            prompt_content = (
                f"Answer this question: '{question}', use the following sentences as context: '{context}'. "
                f"The answer will be in the sentences, do not say it is not there. "
                f"Select the right sentence. I don't need any extra explanation just the right sentence."
            )

            response = litellm.completion(
                model="ollama/llama3.2",
                messages=[
                    {"role": "user", "content": prompt_content}
                ]
            )

            # Return answer immediately on success
            answer = response["choices"][0]["message"]["content"]

            return AnswerResult(answer=answer, success=True, attempts=i + 1)

        except Exception as e:
            # Handle failure on final attempt
            if i == retry_count:
                print(f"Error invoking model after {retry_count + 1} attempts:", e)
                return AnswerResult(answer="", success=False, attempts=i + 1)

            # Exponential backoff delay (e.g., 1s, 2s, 4s, 8s...)
            delay = base_delay * (2 ** i)
            print(f"Attempt {i + 1} failed ({e}). Retrying in {delay} seconds...")
            time.sleep(delay)

def map_lines_to_sentences(lines, indexes):
    sentences = ""
    for index in indexes:
        if sentences == "":
            sentences = lines[index]
        else:
            sentences = sentences + ". " + lines[index]

    return sentences

def answer_it(question_text):
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    lines = read_samples_as_lines()
    sample_vectors = model.encode(lines)

    db = faiss.IndexFlatL2(sample_vectors.shape[1])
    db.add(sample_vectors)

    question_vector = model.encode([question_text])

    search_results = db.search(question_vector, 3)

    return generate_answer(question_text, map_lines_to_sentences(lines, search_results[1][0]))


def main():
    question_text = "According to the text, what specific reason is given for why people prefer digital tablets over physical books?"

    for i in range(5):
        answer = answer_it(question_text)
        print("RESULT(", i+1, "):", answer)


if __name__ == "__main__":
    main()