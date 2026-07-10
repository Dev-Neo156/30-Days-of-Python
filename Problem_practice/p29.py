# Write a program to find whether a given username contains less than 10 characters or not.

name = input("Enter your username:\n")

if(len(name)>10):
    print("Username contains more than 10 characters")
elif(len(name) == 10):
    print("Username contains 10 characters")
else:
    print("Username has less than 10 characters")