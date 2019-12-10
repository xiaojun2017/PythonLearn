for i in range(1, 5):
    print(i)

even_numbers = list(range(1, 4))
print(even_numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
    print(squares)
