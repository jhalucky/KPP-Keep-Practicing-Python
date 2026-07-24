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

# a = np.arange(12).reshape(4,3)
# b = np.arange(3).reshape(3)
# print(a)

# print(a > 50)

# print(a[a>50])

# print(a[(a%2==0) & (a > 50)])
# print(a[a%7!=0])
# print(a[a%2==0]) 

# print(b)

# print(a+b)


# def sigmoid(array):
#     return 1/(1 + np.exp(-(array)))


# a = np.arange(100)
# print(sigmoid(a))

# mean squared error

# def mse(actual, predicted):

#     return np.mean((actual - predicted)**2)



# actual = np.random.randint(1,50,25)
# predicted = np.random.randint(1,50,25)

# print(mse(actual, predicted))


# working with missing values null and nan

# a = np.array([2,4,6,8,10,np.nan,34,56])
# # print(a)

# print(a[~np.isnan(a)])


# plotting a graph
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

x = np.linspace(10,-10,100)
y = 1/(1+np.exp(-x))

plt.plot(x,y)
plt.show()