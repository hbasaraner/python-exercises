import matplotlib.pyplot as plt
import numpy as np

# Bar Plots

plt.bar([11, 14, 19, 13, 16], [0.2, 0.4, 0.6, 0.8, 1.0])
plt.xticks(np.arange(11, 20))
plt.title('Bar Graph Example')
plt.show()

# Histogram
iq = [85, 92, 115, 121, 72, 102, 104, 99, 110,
      120, 121, 122, 90, 115, 119, 92, 98, 110, 138]
age = [70, 80, 90, 100, 110, 120, 130, 140, 150]
plt.hist(iq, age, histtype='bar', rwidth=0.8)

plt.xlabel('IQ Range')
plt.ylabel('# of Students')

plt.title('Histogram Example')
plt.legend()
plt.show()
