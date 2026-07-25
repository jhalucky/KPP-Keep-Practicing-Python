import numpy as np

a1 = np.array([1,2,3,4,5])
a2 = np.array([4,5,6,7,8])

mask = np.isin(a1, a2)

result1 = a1[~mask]
result2 = a2[~mask]


print(result1)
print(result2)