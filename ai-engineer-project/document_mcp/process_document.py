import os.path

from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from document_mcp.document_results import DocumentResult
import faiss
import time
import litellm
import os

def read_pdf() -> str:
    pdf_path = os.path.join(os.path.dirname(__file__), "clean_code.pdf")

    reader = PdfReader(pdf_path)
    full_text = ""

    for page in reader.pages:
        full_text += page.extract_text()

    return full_text

def split_text(full_text: str) -> list[str]:
    return full_text.split()

def chunk_words(words: list[str], chunk_size: int, overlap: int) -> list[str]:
    result = []
    step = chunk_size - overlap

    if step <= 0:
        return result

    for i in range(0, len(words), step):
        result.append(" ".join(words[i:i + chunk_size]))

    return result

def build_index(chunks: list[str])-> tuple[faiss.IndexFlatL2, SentenceTransformer, list[str]]:
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    vectors = model.encode(chunks)
    db = faiss.IndexFlatL2(vectors.shape[1])
    db.add(vectors)

    return db, model, chunks


def search_chunks(question: str, db: faiss.IndexFlatL2, model: SentenceTransformer, chunks: list[str], k: int = 3) -> str:
    vector = model.encode([question])
    search_result = db.search(vector, k)

    return ". ".join(chunks[index] for index in search_result[1][0])

def answer_question(question: str, context: str, retry_count: int = 3, base_delay: int = 1)-> DocumentResult:
    ollama_base = os.environ.get("OLLAMA_API_BASE", "http://localhost:11434")
    for i in range(retry_count + 1):
        try:
            # Construct prompt using f-string formatting
            prompt_content = (
                f"Answer this question: '{question}', use the following sentences as context: '{context}'. "
                f"The answer will be in the sentences, do not say it is not there. "
                f"Explain it in nutshell. "
                f"Do not duplicate sentences."
            )

            response = litellm.completion(
                api_base=ollama_base,
                model="ollama/llama3.2",
                messages=[
                    {"role": "user", "content": prompt_content}
                ]
            )

            # Return answer immediately on success
            answer = response["choices"][0]["message"]["content"]

            return DocumentResult(answer=answer, success=True, attempts=i + 1)

        except Exception as e:
            # Handle failure on final attempt
            if i == retry_count:
                print(f"Error invoking model after {retry_count + 1} attempts:", e)
                return DocumentResult(answer="", success=False, attempts=i + 1)

            # Exponential backoff delay (e.g., 1s, 2s, 4s, 8s...)
            delay = base_delay * (2 ** i)
            print(f"Attempt {i + 1} failed ({e}). Retrying in {delay} seconds...")
            time.sleep(delay)

def answer_it(question: str) -> DocumentResult:
    print("start answering")
    context = search_chunks(question, db, model, chunks)

    return answer_question(question, context)

full_text = read_pdf()
words = split_text(full_text)
chunks = chunk_words(words, 200, 50)
(db, model, chunks) = build_index(chunks)

def main():
    result = answer_it("What is single responsibility?")
    print(result.answer)

if __name__ == "__main__":
    main()