import sentence_transformers
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

sentences = [
    "Am I a dog?",
    "Sometimes I like to barking",
    "I love sports",
]

sVectors = model.encode(sentences)

similarities = model.similarity(sVectors, sVectors)

print(similarities)
