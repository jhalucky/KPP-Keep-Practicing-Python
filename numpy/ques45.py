import numpy as np

checkboard = np.zeros((8,8), dtype=int)

checkboard[1::2, ::2] = 1 
checkboard[::2, 1::2] = 1

print(checkboard)