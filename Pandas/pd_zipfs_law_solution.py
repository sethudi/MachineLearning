import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('wordcounts.txt')

print(type(df))
print()
plt.plot(1.0/df.iloc[:2000, 1])
plt.show()