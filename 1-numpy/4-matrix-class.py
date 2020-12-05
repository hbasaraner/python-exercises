import numpy as np

x = np.random.randn(3, 3)
x = np.matrix(x)

y = np.random.randn(3, 4)
y = np.matrix(y)

# multiply two matrix
print(x*y)
