import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(200)
y = np.random.randn(200)

plt.scatter(x, y, c='r')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot Example')

plt.show()
