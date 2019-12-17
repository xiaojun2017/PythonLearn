pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

removePet = 'cat'
while removePet in pets:
    pets.remove(removePet)
print(pets)

list1 = [1, 2]
list2 = [3, 4]
list1.extend(list2)
print(list1 + list2)
