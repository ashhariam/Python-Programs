import random

min_val = int(input("Enter the minimum value of the die: "))
max_val = int(input("Enter the maximum value of the die: "))

print("Input valid program will revert to defaults:")
min_val = 1
max_val = 6
again = True

while again:
    print(random.randint(min_val,max_val))
    roll_again = input("Want to roll it again?: ")

    if roll_again.lower() == "Y" or roll_again.lower() == "y":
        continue
    else:
        print("unexpected answer!!!")
        break
