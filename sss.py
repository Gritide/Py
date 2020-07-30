import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-2, 2, 4)
fx=(x**4)+x
gx=(x**3)-(x**2)+4 
fig, ax = plt.subplots()
ax.plot(x, fx)
ax.plot(x, gx)
plt.show()
