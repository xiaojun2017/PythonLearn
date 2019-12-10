# 4-3 数到 20 :使用一个 for 循环打印数字 1~20 (含)。
for value in range(1, 21):
    print(value)

# 4-4 一百万 :创建一个列表,其中包含数字 1~1 000 000 ,
# 再使用一个 for 循环将这些数字打印出来
# (如果输出的时间太长,按 Ctrl + C 停止输出,或关闭输出窗口)。
listValue = list(range(1, 1000001))
for value in listValue:
    print(value)

# 4-5 计算 1~1 000 000 的总和 :创建一个列表,其中包含数字 1~1 000 000 ,
# 再使用 min() 和 max() 核实该列表确实是从 1 开始,到 1 000 000 结束的。另外,对这个列表
# 调用函数 sum() ,看看 Python 将一百万个数字相加需要多长时间。
valueList = list(range(1, 1000001))
minValue = min(valueList)
maxValue = max(valueList)
total = sum(valueList)

print(minValue, maxValue, total)

# 4-6 奇数 :通过给函数 range() 指定第三个参数来创建一个列表,其中包含 1~20 的奇数;
# 再使用一个 for 循环将这些数字都打印出来。
valueList = list(range(1, 21, 2))
for value in valueList:
    print(value)

# 4-7 3 的倍数 :创建一个列表,其中包含 3~30 内能被 3 整除的数字;
# 再使用一个 for 循环将这个列表中的数字都打印出来。
valueList = []
for v in range(3, 31):
    if v % 3.0 == 0:
        valueList.append(v)
print(valueList)

# 4-8 立方 :将同一个数字乘三次称为立方。例如,在 Python 中,
# 2 的立方用 2**3 表示。请创建一个列表,其中包含前 10 个整数(即 1~10 )的立方,再使用一个 for 循
# 环将这些立方数都打印出来。
valueList = list(i ** 3 for i in range(1, 11))
print("valueList: ", valueList)
for value in valueList:
    print(value, end=" ")
