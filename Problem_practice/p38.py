# Write a program to print the following star pattern.

n = int(input("Enter number of rows: "))

for i in range(1, n+1):
   print(" " * (n-i), end = "" ) # end parameter is used to avoid new line after printing space
   print("*" * (2*i - 1), end = "\n")


