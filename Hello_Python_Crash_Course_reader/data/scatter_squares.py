import matplotlib.pyplot as plt

# plt.scatter(2, 4, s=200)

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 26]
plt.scatter(x_values, y_values, s=100)

# 设置图表标题
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Square of Value", fontsize=24)
plt.ylabel("Value", fontsize=24)

plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()
