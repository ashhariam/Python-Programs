#Write a Python program to accept a filename from the user and print the extension of that.
filename = input("Enter the file name: ")
extsn = filename.split(".")
print("The Extension of the file is: " +repr(extsn[-1]))