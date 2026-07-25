import numpy as np

a1 = np.array([10,20,30,40,50])

a2 = (a1 - a1.min())/(a1.max() - a1.min())

print(a2)