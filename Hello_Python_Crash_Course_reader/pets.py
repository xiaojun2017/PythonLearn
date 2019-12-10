pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

removePet = 'cat'
while removePet in pets:
    pets.remove(removePet)
print(pets)
