import numpy as np
arr = np.array([5, 12, 29, 30, 44, 7, 18])
filtered = arr[arr < 30]
print(filtered)