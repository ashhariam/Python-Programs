person_dict = {'Name': 'Asher', 'Phone': 8109503302, "Address": 'Bangalore'}


def addperson():
    name = input("Enter full name of the person: ")
    phone = input("Phone number of the person: ")
    adress = str(input("address of the person: "))
    add = False
    for i in person_dict:
        if i.lower() == name.lower():
            print("Name already Exist!!!")
        elif person_dict[i][name].lower() == name.lower():
            print("Name already Exist!!!")
        else:
            add = True
        if add:
            person_dict.update({'Name': name, 'phone': phone, 'address': adress})


def indexpers():
    name = input("Enter Person\'s full name: ")
    for i in person_dict:
        if i.lower() == name.lower() or person_dict[i]['name'].lower() == name.lower():
            print('\nName: %s\nPhone Number: %s\nAddress: %s\n' % (
                person_dict[i]['name'], person_dict[i]['phone'], person_dict[i]['adress']))
        else:
            print("Name not found!!!")


def yesno():
    ques = input("Do you want to add person the address book? y/n: ")
    if ques == 'n':
        indexpers()
    elif ques == 'y':
        addperson()
    else:
        print("Invalid response")


if __name__ == '__main__':

    while True:
        out = input("Would you like to quit? y/n:")
        if out == 'n':
            pass
        elif out == 'y':
            break
        else:
            print("Invalid response!!!")



