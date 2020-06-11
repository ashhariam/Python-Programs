num = int(input("Enter num of rows:"))

for i in range(0,num):
    for j in range(0,num-i-1):
        print("")
    for j in range(0,i+1):
        print("*",end = " ")
    for i in range(0, num):
        for j in range(0, num + i + 1):
            print("")
        for j in range(0, i - 1):
            print("#", end = " ")
    print()