import numpy as np

a = np.array([1,2,3,4])
has_nan = np.isnan(a).any()

print(has_nan)