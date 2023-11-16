import numpy as np

x = np.fromfunction(lambda i, j: i + j, (3, 4), dtype=int)
print(x)
