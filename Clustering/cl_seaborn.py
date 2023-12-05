# import sklearn.datasets as ds
# import seaborn as sn
# import matplotlib.pyplot as plt

# data = ds.load_iris(as_frame=True)

# target = data['target']
# target_names = data['target_names']

# df = data['data']
# df['species_index'] = target
# df['species'] = target.map(lambda n: target_names[n])

# print(df)

# sn.pairplot(df)

# plt.show()

import sklearn.datasets as ds
import seaborn as sns
import matplotlib.pyplot as plt

data = ds.load_iris(as_frame=True)

target = data['target']
target_names = data['target_names']

df = data['data']
df['species_index'] = target
df['species'] = target_names[target]

sns.pairplot(df, hue='species')
plt.show()

print(df)