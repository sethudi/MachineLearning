from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

wine = load_wine(as_frame=True)
X = wine["data"]
y = np.choose(wine['target'], wine['target_names'])

X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True, train_size=0.7)

X_train = StandardScaler().fit_transform(X_train)
X_test = StandardScaler().fit_transform(X_test)

pca = PCA(0.95)
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)

print("Number of components: ", pca.n_components_)

tree = DecisionTreeClassifier()
tree.fit(X_train, y_train)

y_predicted = tree.predict(X_test)

df = pd.DataFrame(pca.components_)
df.columns = X.columns
df = df.abs()
print(df)

for idx in range(pca.n_components_):
    print("Biggest contributor PC1:", df.columns[np.argmax(df.iloc[idx])])

print('Accuracy:', accuracy_score(y_test, y_predicted))

