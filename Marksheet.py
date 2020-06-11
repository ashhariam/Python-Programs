Name = str(input("Enter Your Name: "))
Mob =  int(input("Enter 10 digit mobile number: "))

Eng = int(input("Enter English Marks: "))
Math = int(input("Enter Mathematics marks: "))
Sci = int(input("ENnter science Marks: "))
Hindi = int(input("Enter Hindi Marks: "))
Urdu = int(input("Enter Urdu Marks: "))

avg = (Eng+Math+Sci+Hindi+Urdu)/5
if(avg>=90):
    print(Name, "You got Grade: A")
elif(avg>=80 and avg<90):
    print(Name, "You got Grade: B")
elif(avg>=70 and avg<80):
    print(Name, "You got Grade: C")
elif(avg>=60 and avg<70):
    print(Name, "You got Grade: D")
else:
    print(Name,"You are fail")