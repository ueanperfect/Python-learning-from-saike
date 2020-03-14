import numpy as np
import matplotlib.pyplot as plt
a = 1
t = np.linspace(0, 2 * np.pi)
x = a * (t - np.sin(t))
y = a * (1 - np.cos(t))
plt.plot(x, y)
plt.grid()
plt.show()
