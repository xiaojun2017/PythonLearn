import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

plt.scatter(x_values, y_values, s=40, edgecolors='none', c=y_values, cmap=plt.cm.Blues)
plt.axes([1, 100, 200, 3000])
# plt.show()

plt.savefig('squares_plot.png', bbox_inches='tight')
