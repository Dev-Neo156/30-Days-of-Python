# While loops, This loop runs until the condition is satisfied
i = 0
while i < 5:
    print("Harry") # prints harry for five times
    i = i +1
    
# Write a program to print the content of a list using while loops.

name = ["Aditya", "Harry", "Rohan"]

i = 0
while( i < len(name)):
    print(name[i])
    i = i + 1

# A for loop is used to iterate through a sequence like list, tuple, or string [iterables]

l = ["Aditya", "Harry", "Rohan"]
for item in l:
    print(item)

for it in range(len(l)):
    print(name[it])

u = [1,7,8]
for item in u:
    print(item)
else:
    print("done") # this is printed when the loop exhausts!
