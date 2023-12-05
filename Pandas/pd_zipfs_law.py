import numpy as np

values = np.arange(10, 1001, 10)
rank = np.arange(1, len(values) + 1)

values = 1.0/ values
print(values)
print(rank)
values = 1.0/ values

# if we devide rank by value then we get 0.1
# it means if we plot a graph for rank_V.s_value we'll get a straight line
for r, v in zip(rank, values):
    print(r, v)