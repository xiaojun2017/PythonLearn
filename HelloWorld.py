print("Hello")
print("world")


def HelloWorld():
    print("Hello Wold method")


a = 200;
print(a);

b = "It's a cat";
print(b)

c = "Hello \n hello"
print(c)

d = '''a
b, "ok", 'yes'
c
d
'''
print(d)

e = 'b'
print("bb: " + e)
print("%s", e)

age = 20
name = "swap"
msg = "{0} was {1} years old".format(name, age)
msg1 = "{0} is good".format(name)
msg2 = name + ' is ' + str(age) + ' years old'
msg3 = '{} is {} years old'.format(name, age)

print(msg3)
print(msg2)
print(msg1)
print(msg)

# 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(1.0 / 3))

# 使用下划线填充文本,并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:_^11}'.format("hello"))

# 基于关键词输出
print("name is {name}, {age} years old".format(name='Jun', age='20'))

# 打印a == b == c，end="", end指定结束符,类似java中StringBuffer.append()
print('a', end=" == ")
print('b', end=" == ")
print('c')

print("What\'s your name?")

# 转义 \ What's your \ name
print("What's your \\ name")

# What's your name?
#  age is ?
print("What's your name? \n age is ?")

# What's your name? 	 age is ?
print("What's your name? \t age is ?")

# \放在最后不会下一行
# arg is test.
msg = "arg is \
test."
print(msg)

# r 或 R 来指定一个 原始(Raw) 字符串
# 打印Newlines arg indicated by \n
m = r"Newlines arg indicated by \n"
print(m)

m = R"Newlines arg indicated by \n"
print(m)

myname = "xiao"
myName = "jun"
print(myname)
print(myName)

# 等价于i = 8
i = \
    8;
print(i)

__version__ = '1.0'
