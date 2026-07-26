import numpy as np

arr = np.array([[8,4,1],[5,2,7],[6,9,3]])
sorted_indices = arr[:, 1].argsort()

sorted_arr = arr[sorted_indices]
print(sorted_arr)