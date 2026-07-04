s = {1, 3, 4, 5, 6, "Harry"}

print(s, type(s))

s.add("89")
print(s)

s.update([11, 42, 53])
print(s)

s.remove(5)
print(s)

value = s.pop()
print(value)
print(s)

s.clear()
print(s)
