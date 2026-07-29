import numpy as np
arr = np.array([2, 3, 2, 5, 3, 3, 2, 5])

vals, count = np.unique(arr, return_counts=True)
for v, c in zip(vals, count):
    print(f"Value {v} occurs {c} time(s)")