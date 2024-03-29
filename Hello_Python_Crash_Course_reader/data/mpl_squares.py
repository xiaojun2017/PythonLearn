import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

# 设置图表标题
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Square of Value", fontsize=24)
plt.ylabel("Value", fontsize=24)

# 设置刻度大小
plt.tick_params(axis='both', labelsize=14)
plt.show()
