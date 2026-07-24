# list
# a = [i for i in range(10000000)]
# b = [i for i in range(10000000,20000000)]
# c = []

# import time

# start = time.time()
# for i in range(len(a)):
#     c.append(a[i]+b[i])
# print(time.time() - start)

# # numpy array

import numpy as np

# a1 = np.arange(10000000)
# a2 = np.arange(10000000,20000000)
# start = time.time()
# c = a1 + a2
# print(time.time() - start)

# # memory

# import sys
# print(sys.getsizeof(a))
# print(sys.getsizeof(a1))


# fancy Indexing

# a1 = np.arange(16).reshape(4,4)
# print(a1)

# print(a1[:,[0,1,3]])

# Boolean indexing

a = np.random.randint(1,100,36).reshape(4,9)
print(a)

print(a > 50)