import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = np.concatenate((a, b))
d = np.dstack((a, b))
x = np.where(a == 2)

print(c)
print(d)
print(x)