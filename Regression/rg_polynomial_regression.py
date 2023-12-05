from xml.etree.ElementInclude import include
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

df = pd.read_csv('cooling.csv')

print(df)

X = df['minute'].values.reshape(-1, 1)
y = df['temperature']

poly = PolynomialFeatures(degree=3, include_bias=False)
poly_features = poly.fit_transform(X)

model = LinearRegression()
model.fit(poly_features, y)

y_pred = model.predict(poly_features)

fig = plt.figure(figsize=(16, 9))
ax = fig.add_subplot()

ax.scatter(X, y)
ax.plot(X, y_pred)

plt.show()
