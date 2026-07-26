import numpy as np

arr = np.arange(9).reshape(3,3)


print(f"Before:\n{arr}")
arr[:, [1,2]] = arr[:,[2,1]]
print(f"After:\n{arr}")