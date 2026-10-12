from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# tanító adat: mondat + címke (1 = pozitív, 0 = negatív)
texts = [
	"I love this product, it's amazing",
	"Terrible experience, would not recommend",
	"Best purchase I've made this year",
	"Waste of money, very disappointed",
	"Highly recommend, exceeded expectations",
	"Poor quality, broke after one day",
	"I would have bought something else if I knew how it worked",
	"I regret my choice",
	"That is a fantastic idea"
]

labels = [1, 0, 1, 0, 1, 0, 0, 0, 1]

vectorizer = TfidfVectorizer() # szöveget számvektorrá alakít (szógyakoriság alapján)
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels) # megtanulja a mintát: mely szavak jeleznek pozitív/negatív véleményt

#teszteld új mondatokkal:
test = ["This is fantastic", "I regret buying this"]
X_text = vectorizer.transform(test)
print(model.predict(X_text))