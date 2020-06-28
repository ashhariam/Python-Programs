# A Simple Calculator
flag = "y"
while flag == "y":
    print("Select the operations:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4. Division")

    your_choice = input("Please Enter your choice(1/2/3/4): ")

    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter Second number: "))

    if your_choice == "1":
        result = number1 + number2
        print("Addition for the two number is: ", result)
    elif your_choice == "2":
        result = number1 - number2
        print("Subtraction of the two number is: ", result)
    elif your_choice == "3":
        result = number1 * number2
        print("Multiplication of the two number is: ", result)
    elif your_choice == "4":
        result = number1 / number2
        print("Division of the two number is: ", result)
    else:
        print("Please make right choice!!!!")
    flag = input("Do you want to continue(y/n)")
print("Calculation is completed!!!!")
