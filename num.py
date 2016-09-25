import numpy as np
arr = list(map(float, input().split()))
arr = np.array(arr)
print(arr.reshape(3,3))
