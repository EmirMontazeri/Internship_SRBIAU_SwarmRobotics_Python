import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
b = np.array([1, 2, 3, 4, 5], dtype='S')

newa = a.reshape(2 ,3)

print(a[1:5:2])
print(b.dtype)
print(newa)