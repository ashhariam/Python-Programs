#program to swap first and last element of the list

def swapList(newList):
    size = len(newList)

    #swapping
    temp = newList[0]
    newList[0] = newList[size-1]
    newList[size - 1] = temp

    return newList
newList = [11, 45, 58, 16, 26]

print(swapList(newList))
