my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("my_foods ", my_foods)
print("friend_foods, ", friend_foods)

my_foods.append("banana")
friend_foods.append("egg")

print("my_foods ", my_foods)
print("friend_foods, ", friend_foods)

for food in my_foods:
    if food.__eq__("pizza"):
        print("a")

a = "a"
b = "aa"

print(a is b)
print(b == "Aa")
print(a.__eq__(b))

contains = "pizza" in my_foods
print("contains: ", contains)

not_contains = "amb" not in my_foods
print("not_contains: ", not_contains)

