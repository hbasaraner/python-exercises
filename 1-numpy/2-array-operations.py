import numpy as np

# -- Arithmetic Operations --
data = np.array([[5, 6, 7],
                 [8, 9, 10]])

# adds 5 to all items
print(data+5)
print('\n'+'-'*6+'\n')

# removes 3 from all items
print(data-3)
print('\n'+'-'*6+'\n')

# multiplies items with themselves
print(data*data)
print('\n'+'-'*6+'\n')

# -- Transposing And Swapping Axis --

data = np.arange(16).reshape((4, 4))
print(data)
print('\n'+'-'*6+'\n')

# transpose of array
print(data.T)
