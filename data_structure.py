# 列表
shopList = ['apple', 'mango', 'carrot', 'banana']
print('shotList size:', len(shopList), 'items to purchase')

print('these items are:', end=' ')
for item in shopList:
    print(item, end=' ')

shopList.append('rice')
print('shopList:', shopList)

shopList.sort()

numList = [1, 2, 5, 0, 3, 9]
print(numList)

numList.sort()

numList.sort(reverse=True)
print(numList)

del numList[1]

print(numList)

# 元组
zoo = ('python', 'elephant', 'penguin')
print('zoon:', zoo)

newZooo = 'aa', zoo
print(newZooo)
print(len(zoo))

# 字典 类似于java中Map
# "ab" Addrress-Book
ab = {
    'a': 'aa',
    'b': 'bb',
    'c': 'cc'
}
# 打印{'a': 'aa', 'b': 'bb', 'c': 'cc'}
print(ab)

# 打印bb
print(ab['b'])

# 删除b:bb
del ab['b']
# 打印{'a': 'aa', 'c': 'cc'}a
print(ab)

# 打印
# key: a, value: aa
# key: c, value: cc
for key, value in ab.items():
    print('key: {}, value: {}'.format(key, value))

# 添加一个键值对m:mm
ab['m'] = "mm"
# 打印{'a': 'aa', 'c': 'cc', 'm': 'mm'}
print(ab)

# 打印m :  mm
if 'm' in ab:
    print('m : ', ab['m'])

# 切片
shopList = ['a', 'b', 'c', 'd']
print(shopList)

# item 0 is: a
# item -1 is :  d
# item -2 is :  c
# item -3 is :  b
print('item 0 is:', shopList[0])
print('item -1 is : ', shopList[-1])
print('item -2 is : ', shopList[-2])
print('item -3 is : ', shopList[-3])

# 报错，越界
# print('item -5 is : ', shopList[-5])

# 切片 类似于substring()
# 打印 1 to 3 is: ['b', 'c']
print('1 to 3 is:', shopList[1:3])
print(shopList)

# 1 to end : ['b', 'c', 'd']
print('1 to end :', shopList[1:])

print(' to 3', shopList[:3])

# -1 to 1 is: []
print('-1 to 1 is:', shopList[-1:1])

# 1 to -1 is: ['b', 'c']
print('1 to -1 is:', shopList[1:-1])

print(shopList)

# 设置步长
print("=============1===")
shopList[::3]
print(shopList)
print("222222222222")

# {'1', '3', '22'}
# {'11', '33', '22'}
set1 = set(['1', '2', '3'])
print(set1)
set2 = set(['11', '22', '33'])
print(set2)

a = '22' in set2
print(a)

# {'4', '1', '2', '3'}
# {'4', '1', '2', '3'}
set1.add('4')
print(set1)

set3 = set1.copy()
print(set3)

# 引用，跟java一样，会指向同一地址
list1 = [1, 2, 3]
list2 = list1
print(list1)
print(list2)

list3 = list1[:]
print('list3:', list3)

del list2[1]
print(list1)
print(list2)

# 字符串操作
name = "Swaroop"
print(name.startswith("Sw"))  # True
print(name.__contains__('oo'))  # True

print('p' in name)  # True

print(name.find('ar'))  # 找到ar的位置 2

delimter = '='
list = ['a', 'b', 'c']
# a=b=c
print(delimter.join(list))
