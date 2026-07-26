import numpy as np

arr = np.array([[34, 43, 73], [82,22,12], [53,94,66]])
new_column_to_insert = np.array([10,10,10])

deletedarr = np.delete(arr, 1, axis=1)
print(f"Array after Deletion: {deletedarr}")

insertedarr = np.insert(deletedarr, 1, new_column_to_insert, axis=1)
print(insertedarr)