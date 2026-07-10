# Write a program to print multiplication table of a given number using for loop.

num = int(input("Enter Your number:\n"))

print("-----Multiplication Table of ", num)

for i in range(1, 10):
    print(num*i)