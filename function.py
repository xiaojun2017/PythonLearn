import sys


def sayHello():
    print("hello")


sayHello()
sayHello()


def calculator(a, b):
    print("a+b:", a + b)


calculator(3, 6)


def method():
    a = 5
    print(a)


m = method()
print("m:", m)

# global关键字
x = 50


def testGlobal():
    global x
    print("x", x)

    x = 33
    print("changed x: ", x)


testGlobal()
print("lastest x: ", x)


def m2():
    print("x:", x)


m2()


# 参数times默认值为1
def hello(message, times=1):
    print(message * times)


# ha ha ha ha ha
hello("ha ", 5)
hello("ha ")


def keyWordFun(a, b=5, c=10):
    print("a is", a, "b is", b, "c is", c)


# a is 3 b is 7 c is 10
# a is 25 b is 5 c is 35
# a is 100 b is 5 c is 59
keyWordFun(3, 7)
keyWordFun(25, c=35)
keyWordFun(c=59, a=100)


# 可变参数
def total(a=5, *numbers, **phoneBook):
    print("a", a)
    print("numbers:", numbers)
    print("phonbook:", phoneBook)

    for number in numbers:
        print("number:", number)

    for key, value in phoneBook.items():
        print(key, value)


# a 10
# numbers: (1, 2, 3)
# phonbook: {'jack': 1123, 'john': 2231, 'Inge': 3300}
# number: 1
# number: 2
# number: 3
# jack 1123
# john 2231
# Inge 3300
print(total(10, 1, 2, 3, jack=1123, john=2231, Inge=3300))


# function return
def add(x, y):
    return x + y


# 对于没有返回值的，打印为None
# 默认在函数末尾隐藏了一个return None
print("add: ", add(3, 8))


def some_fuction():
    pass


print("some_fuction :", some_fuction())


# DocStrings
def print_max(x, y):
    '''
    打印最大数
    :param x:
    :param y:
    :return:
    '''
    print(max(x, y))


print_max(4, 6)
print(print_max.__doc__)
help(print_max)
print('================================')
dir(str)
