number = 23
guess = int(input('enter a number:'))

if guess == number:
    print("guess == number : " + str(guess))

elif guess < number:
    print("guess < number, guess:" + str(guess))

else:
    print("guess > number, guess:" + str(guess))

print("done")
