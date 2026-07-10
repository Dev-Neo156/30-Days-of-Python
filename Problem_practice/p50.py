# Write a python function to print multiplication table of a given number.


def mul(n, i=1):
    if i > 10:
        return
    print(f"{n} x {i} = {n * i}")
    mul(n, i + 1)

n = int(input("Enter your number: "))

mul(n)

