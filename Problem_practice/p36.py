# Write a program to find the sum of first n natural numbers using while loop.

n = int(input("Enter the number:\n"))

i = 1
num = 0
while(i <= n):
    num = num + i
    i = i + 1
print("Sum of first ", n, " natural number is ", num)