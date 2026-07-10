# Write a program to print multiplication table of n using for loops in reversed order.

n = int(input("Enter your number: "))
x = 0

print("Multiplication table of ", n)

for i in reversed(range(1,10)):
    x = n*i
    print(x)
    