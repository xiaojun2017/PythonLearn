import os
import shutil
import re
import random
from collections import deque
from datetime import date
from urllib.request import urlopen
import collections

import zlib

os.getcwd()

os.chdir('./class')

print(os.getcwd())

# os.system('mkdir today')

dir(os)
# help(os)

shutil.copy('../class/class.py', '../class/class1.py')

str = "Resesd ad ".replace('ad', 'ac')
print(str)

s = random.choice(['apple', 'pear', 'banana'])
print(s)

s = random.sample(range(10), 5)
print(s)

s = random.randrange(6)
print(s)

str = ''
for line in urlopen("https://docs.pythontab.com/python/python3.5/stdlib.html"):
    _line = line.decode("utf-8")
    str += _line

# print(str)

now = date.today()
print(now)
birthday = date(1987, 7, 31)
age = now - birthday
print(age.days)

s = b'witch which has which witches wrist watch'
len = len(s)
print(len)
t = zlib.compress(s)

d = deque([1, 2, 3, 4, 5])
type = type(d)
print(type)

print(d)

d.append('8')

print(d)

d.popleft()
print(d)

d.pop()
print(d)

d = deque([1, 2, 3, 4, 5])
d.pop()
print(d)


def _all(list):
    for element in list:
        if not element:
            return False
    return True


list = ''"None"''

if list:
    print("list")


# result = _all(list)
# print("result:", result)

a = bin("10")
print(a)
