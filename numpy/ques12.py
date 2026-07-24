import numpy as np

arr = np.arange(1,17).reshape(4,4)
print(f"Array:\n{arr}")
print(f"First array: {arr[0]}")
print(f"Second array: {arr[:,-1]}")