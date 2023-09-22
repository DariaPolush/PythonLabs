import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10)
plt.plot(x, x**2, ls = "--", lw = 2, color = "pink", marker = "<", mew = 2, ms = 10, mec = "blue", mfc = "purple")
plt.show()
