import numpy as np

# f = np.array([[[10,20],[1,2]],[[3,4],[40,0]]],dtype=complex)
# print(f)
# print(type(f))

# f = np.arange(16).reshape(2,2,2,2)
# print(f)
# print(type(f))

# we use them np.ones() and np.zeros( when we need to create or initilaze an array without passing any values

# f = np.ones((9,10))
# print(f)

# g = np.zeros((2,3))
# print(g)


# f = np.random.random((3,4))
# print(f)

# f = np.linspace(10,-10,10)
# print(f)

# f = np.identity(5)

# f = np.arange(20).reshape(2,2,5)
# print(f)
# print(f.ndim)
# print(f.shape)
# print(f.size)

a1 = np.arange(16).reshape(8,2)
a2 = np.arange(16,32).reshape(8,2)
# print(np.dot(a1,a2))

# print(a1)
# print(a2)

# print(a1[1:2,::3])
# print(a1[2:,1::2])

# print(np.hstack((a1,a2)))
# print(np.vstack((a2,a1)))

# print(np.hstack((np.vstack((a1,a2)), np.arange(32).reshape(16,2))))

# print(np.vsplit(a1,2))
print(np.vsplit(np.stack((a1,a2)), 2))