import numpy as np

a1 = np.arange(10)
print(f"Original Array: {a1}")

np.random.shuffle(a1)
print(f"Shuffled Array: {a1}")