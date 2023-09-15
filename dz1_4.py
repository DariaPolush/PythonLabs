import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-6, 6, 0.001)

plt.plot(x, (np.arcsin(2 * np.abs(x) / (1 + x ** 2))))
plt.grid()
plt.show()
