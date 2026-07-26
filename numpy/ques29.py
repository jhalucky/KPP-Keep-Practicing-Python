import numpy as np

a1 = np.random.randint(1,100,9).reshape(3,3)
print(a1)
print(np.sort(a1, axis=1))