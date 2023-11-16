import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 3, 0.01)
y = np.sin(2 * np.pi * x)
z = np.cos(2 * np.pi * x)

plt.xlabel = ('x')
plt.ylabel = ('y')
plt.plot(x, y, label='sin2Πx')
plt.plot(x, z, label='cos2Πx')
plt.xlim(0, 3)
plt.ylim(-1, 1)
plt.xticks(np.arange(0, 3.1, 0.5))
plt.yticks(np.arange(-1, 1.1, 0.25))
plt.legend(loc='upper center', shadow=True)
plt.show()
