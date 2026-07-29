import numpy as np

A = np.array([[4, 2],
              [1, 3]])

eigenvals, eigenvecs = np.linalg.eig(A)
print(f"Eigen Vales:\n{eigenvals}")
print(f"Eigen Vectors:\n{eigenvecs}")