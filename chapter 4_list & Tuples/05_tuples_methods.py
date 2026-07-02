t = (1, 2, 3, 4, "banana")
print(t)

a = t.count(1) # count how many times 1 is present in the tuple
print(a)
print(t)

print(t.index(3)) # returns the index of the first occurrence of 3 in the tuple

print(t.index(3, 2, 3)) # returns the index of the first occurrence of 3 in the tuple, searching only within the slice [1:3]

print(t.index("banana"))

t2 = (7, 8, 9)

con = t + t2 # concatenation of two tuples
print(con)

repeat = t * 2 # repetition of the tuple
print(repeat)

print("banana" in t) # check if "banana" is present in the tuple or not. Returns True or False

print(len(t)) # returns the length of the tuple

a, b, c = t2 # unpacking of tuple. The number of variables on the left must match the number of elements in the tuple
print(a, b, c)