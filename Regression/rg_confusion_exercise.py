import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay 
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('mall_customers.csv')
df.columns = ['id', 'gender', 'age', 'income', 'spending']

df['high spending'] = 0
df.loc[df['spending'] > 90, 'high spending'] = 1

X = df[['age', 'income']]
y = df['high spending']

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, shuffle=True)

X_train = StandardScaler().fit_transform(X_train)
X_test = StandardScaler().fit_transform(X_test)

model = LogisticRegression(solver="liblinear", random_state=0)
model.fit(X_train, y_train)

print(f'{model.score(X_test, y_test):.2f}')

cm = confusion_matrix(y_test, model.predict(X_test))
cm_display = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['low', 'high'])
cm_display.plot()

plt.show()