import numpy as np

a = np.array([1,2,np.nan,3,4])
has_nan = np.isnan(a).any()

print(has_nan)