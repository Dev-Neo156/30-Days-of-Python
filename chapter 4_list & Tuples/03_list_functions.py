name = ["Aditya", "Rohit", "Harry", "Anya"]

print(name)

name.append("William")
print(name)

name.sort() # if your list is of integers then use sort to sort the list in ascending order. If your list is of strings then it will sort the list in alphabetical order.
print(name)

name.reverse()
print(name)

name.insert(2,"Allice")
print(name)

print(name.pop(1)) # removes the element at index 1 and returns it's value

name.remove("Aditya") # removes the first occurence of the value from the list
print(name)