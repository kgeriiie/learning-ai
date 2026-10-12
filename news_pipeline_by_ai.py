from datasets import load_dataset
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. Nyílt dataset betöltése
dataset = load_dataset("ag_news")
label_names = dataset["train"].features["label"].names
print("Kategóriák:", label_names)

train_texts = dataset["train"]["text"][:1000]
train_labels = dataset["train"]["label"][:1000]
test_texts = dataset["test"]["text"][:200]
test_labels = dataset["test"]["label"][:200]

# 2. NER néhány valódi hírcímen
nlp = spacy.load("en_core_web_sm")
for text in train_texts[:5]:
    doc = nlp(text)
    print(text)
    print("Entitások:", [(ent.text, ent.label_) for ent in doc.ents])
    print()

# 3. Klasszifikáció: hír szövege -> kategória
vectorizer = TfidfVectorizer(max_features=5000)
X_train = vectorizer.fit_transform(train_texts)
X_test = vectorizer.transform(test_texts)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, train_labels)

predictions = model.predict(X_test)
print("Pontosság a teszthalmazon:", accuracy_score(test_labels, predictions))