import matplotlib.pyplot as plt

# Line 1
X1 = ([2, 4, 6, 10])
Y1 = ([4, 6, 6, 8])

# Line 2
X2 = ([2, 4, 6, 10])
Y2 = ([2, 4, 8, 10])

# Plotting, linestyle, color and legends
plt.plot(X1, Y1, linestyle='--', c='g', label='Line 1')
plt.plot(X2, Y2, linestyle='-', c='r', label='Line 2')

plt.legend()

# Set title
plt.title('Matplotlib Demo')

# Set labels
plt.xlabel('X value')
plt.ylabel('Y value')

# Set axis ticks
plt.xticks([0, 2, 4, 6, 8, 10, 12])
plt.yticks([0, 2, 4, 6, 8, 10, 12])

plt.show()

# Saving plots to file
plt.savefig('plot.png')
