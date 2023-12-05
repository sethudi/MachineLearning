
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(10000)

plt.figure(figsize=(10, 5))

n, bins, patches = plt.hist(x, bins=[-5, -1, 1, 5], edgecolor='white')
plt.grid()
plt.show()