import numpy as np

arr = np.array([10, 20, 30, 100, 200, 300])

mean = np.mean(arr)
median = np.median(arr)
standard_dev = np.std(arr)

print(f"Mean: {mean}, Median: {median}, Standard Deviation: {standard_dev}")