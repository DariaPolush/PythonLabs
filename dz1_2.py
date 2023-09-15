import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-9, 9, 0.001)
y = (x ** 3 - 4) / ((x - 1) ** 3)

plt.plot(x, y)
plt.axis([-9, 9, -5,5])
plt.grid()
plt.show()

#эксремум в точке x = 2
