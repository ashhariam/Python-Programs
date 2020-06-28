import random
n = random.randint(1,99)
guess = int(input("Enter any integer number between 1 to 99: "))
while n!= guess:
    if guess < n:
        print("You guess lower!")
        guess = int(input("Enter any integer number between 1 to 99: "))
    elif guess > n:
        print("guess is higher")

