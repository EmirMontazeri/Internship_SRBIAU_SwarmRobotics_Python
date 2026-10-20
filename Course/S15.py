from numpy import random as rnd
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])

rnd.shuffle(a)
print(a)

import matplotlib.pyplot as plt

xp = np.array([2, 6])
yp = np.array([0, 10])

plt.plot(xp, yp)
plt.show()