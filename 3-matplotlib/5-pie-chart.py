import matplotlib.pyplot as plt

languages = ['C#', 'C++', 'Java', 'Python', 'Ruby', 'PHP']
usage = [10, 20, 40, 60, 20, 30]

plt.axis('equal')

plt.pie(usage, labels=languages, shadow=True)
plt.title('Pie Chart Example')

plt.show()
