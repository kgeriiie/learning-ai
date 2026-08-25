from transformers import pipeline

ip = pipeline("visual-question-answering")

text = ip(
    question="What do you see on the image?",
    image="test.JPG"
)

print(text)