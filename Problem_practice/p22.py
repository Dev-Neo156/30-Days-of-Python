# Write a program to input eight numbers from the user and display all the unique numbers
#(once).
s = set()
for i in range(8):
    s1 = input("Enter number {} :\n".format(i +1))
    num = int(s1)
    s.add(num)

print("List of unique numbers are:", s)