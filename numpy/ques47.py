import numpy as np

arr = np.array([1, 2, 3, 4, 5])

obj_arr = np.empty(arr.size, dtype=object)

obj_arr[:] = arr

obj_arr[1] = 'a'

print(obj_arr)
print(obj_arr.dtype)