import numpy as np

arr = np.arange(11)
print(arr)

arr[arr % 2 == 1] = -1
print(arr)