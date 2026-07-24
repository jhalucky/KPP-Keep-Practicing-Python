import numpy as np

a1 = np.arange(10, dtype=np.uint32).reshape(5,2)
# print(a1)

print(f"The shape of the array is: {a1.shape}")
print(f"The dimension of the array is: {a1.ndim}")
print(f"The size of each element is: {a1.itemsize}")
      