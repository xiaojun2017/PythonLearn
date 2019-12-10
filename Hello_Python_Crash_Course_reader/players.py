# 处理列表部分元素---列表切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# 打印結果:['charles', 'martina', 'michael'], 打印0-3位置
print(players[0:3])

# 打印1-4位置的值
# ['martina', 'michael', 'florence', 'eli']
print(players[1:4])

strValue = "abccba"
if strValue == strValue[::-1]:
    print("回文串")
else:
    print("not 回文串")