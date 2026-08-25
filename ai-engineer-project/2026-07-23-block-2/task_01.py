import os
os.environ["OMP_NUM_THREADS"] = "1"

import faiss
from sentence_transformers import SentenceTransformer
from transformers import pipeline

# Read lines into a list
with open("samples.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Clean up newlines from all lines
lines = [line.strip() for line in lines]
print(lines)

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
vectors = model.encode(lines)

index = faiss.IndexFlatL2(vectors.shape[1])
index.add(vectors)

question_text = "How does reading manage to take us on imaginary journeys without us ever leaving our rooms?"
question = model.encode([question_text])

result = index.search(question, 3)

qaPipeline = pipeline("question-answering")


for indexOfFundedSentence in result[1][0]:
    text = qaPipeline(
        question=question_text,
        context=lines[indexOfFundedSentence],
    )
    print(text["answer"], " - ", text["score"])

eredmeny = ""

for indexOfFundedSentence in result[1][0]:
    eredmeny = eredmeny + lines[indexOfFundedSentence]

print(eredmeny)

text = qaPipeline(question=question_text, context=eredmeny)
print("ASSEMBLED: ", text["answer"], " - ", text["score"])