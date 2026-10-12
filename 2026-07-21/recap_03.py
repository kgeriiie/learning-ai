from collections import Counter

from datasets import load_dataset
import spacy

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

dataset = load_dataset("cornell-movie-review-data/rotten_tomatoes")

train = dataset["train"].shuffle()
test = dataset["test"].shuffle()

nlp = spacy.load("en_core_web_md")

train_text = train["text"][:5000]
train_label = train["label"][:5000]
test_text = test["text"][:200]
test_label = test["label"][:200]

# NER:
#for text in train_text:
#    doc = nlp(text)
#    for ent in doc.ents:
#        print(ent.text, "->", ent.label_)

# Klasszifikáció:
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(train_text)
X_test = vectorizer.transform(test_text)

model = LogisticRegression()
model.fit(X_train, train_label)

prediction = model.predict(X_test)

print("prediction: ", accuracy_score(test_label, prediction))
C_train_label = Counter(train_label)
C_test_label = Counter(test_label)

print(C_train_label.most_common(5))
print(C_test_label.most_common(5))