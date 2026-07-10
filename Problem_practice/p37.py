# Write a program to calculate the factorial of a given number using for loop.

n = int(input("Enter your number: "))
x = n
factorial = 1

for i in range(1,n+1):
    factorial = factorial*i
    n = n-1

print("Factorial of ", x, "is ", factorial)
