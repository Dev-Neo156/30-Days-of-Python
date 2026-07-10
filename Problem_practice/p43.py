# Write a program using functions to find greatest of three numbers.

def greatestnumber(a, b, c):
    if (a > b and a > c):
        return a
    elif(b > a and b > c):
        return b
    else:
        return c

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

print(greatestnumber(x, y, z))