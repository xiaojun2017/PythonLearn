number = 23
running = True

while running:
    guess = int(input("number:"))

    if guess == number:
        running = False
    else:
        print("not 23")

print("done")

index = 0

while True:
    print("execute...")
    index += 1
    if index == 5:
        print("index == 5")
        break
print("while true is over")
