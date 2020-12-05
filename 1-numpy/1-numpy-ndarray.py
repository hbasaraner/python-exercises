#import numpy
import numpy as np

data = [[2, 6, 1, 3, 7],
        [5, 10, 4, 9, 8]]

data = np.array(data)

# prints matrix
print(data)
print('\n'+'-'*6+'\n')

# prints matrix dimension
print(data.shape)
print('\n'+'-'*6+'\n')

# prints 2x3 matrix with full of zeros
print(np.zeros((2, 3)))
print('\n'+'-'*6+'\n')

# prints 3x3 matrix with full of ones
print(np.ones((3, 3)))
print('\n'+'-'*6+'\n')

# prints array with numbers from 0 to 10
array = np.arange(10)
print(array)
print('\n'+'-'*6+'\n')

# prints array items between index 2 and 5
print(array[2:5])
print('\n'+'-'*6+'\n')

# prints array's changed values
array[5:8] = 0
print(array)
