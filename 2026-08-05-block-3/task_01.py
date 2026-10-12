from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

X, y = make_blobs()

model = KMeans(n_clusters=3)
model.fit(X)

p = model.predict(X)

plt.scatter(X[:, 0], X[:, 1], c=p)
plt.show()

print(p)

print("--")

print(y)