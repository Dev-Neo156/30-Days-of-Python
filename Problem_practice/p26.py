# Write a program to find the greatest of four numbers entered by the user.

numm = []

for i in range(4):
    num = int(input("Enter number {}:\n".format(i + 1)))
    numm.append(num)

print("largest number is ", max(numm))


# By else if method

num1 = int(input("Enter number 1:"))

num2 = int(input("Enter number 2:"))

num3 = int(input("Enter number 3:"))

num4 = int(input("Enter number 4:"))

if(num1 > num2 and num1 > num3 and num1 > num4):
    print("Largest number is ", num1)
elif(num2 > num1 and num2 > num3 and num2 > num4):
    print("Largest number is ", num2)
elif(num3 > num2 and num3 > num1 and num3 > num4):
    print("Largest number is ", num3)
else:
    print("Largest number is ", num4)
