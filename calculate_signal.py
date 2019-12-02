a = 2 + 3;
print(a)

b = 2 * 3
print(b)

# 打印ab
c = "a" + "b";
print(c)

d = -2
print(d)

# 打印mamama
e = 'ma' * 3
print(e)

# 乘方 等于 3*3*3*3 = 81
e = 3 ** 4
print(e)

# 等于4.333333333333333
f = 13 / 3
print(f)

# 四舍五入保留3位小数
# 5.536
print("{0:.3f}".format(5.5358))

# 4.333
print("{0:.3f}".format(5.5358))

# 整除 // : x 除以 y 并对结果向下取整至最接近的整数
# 打印4
g = 13 // 3
print(g)

# (-4.3333),取-5
g = -13 // 3
print(g)

# 取模 % 返回除法运算后的余数
# 打印1
m = 13 % 3
print(m)

# 打印 2
m = -13 % 3
print(m)

# << 左移, 二进制10 -> 1000 转成10进制为8
# 实际上是左移2位等于 2 * 2^2 = 8
m = 9 << 2
print(m)

# >>右移
m = 4 >> 2
print(m)

# 打印True
x = "str"
y = "str"
print(x == y)

# 打印False
x = "sTr"
y = "str"
print(x == y)

# not
# 打印False
x = True
print(not x)

# 逻辑与 and
# 打印False
x = True
y = False
print(x and y)

# 逻辑或 or
# 打印True
x = True
y = False
print(x or y)
