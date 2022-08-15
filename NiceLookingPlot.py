import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
plt.plot(x, x, label="y=x")
plt.plot(x, x ** 2, label="y=x**2")
plt.plot(x, x ** 3, label="y=x**3")
plt.legend()
plt.xlim(x[0], x[-1])
plt.show()
