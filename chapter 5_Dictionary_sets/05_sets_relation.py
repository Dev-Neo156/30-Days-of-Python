s1 = {1, 3, 5, 6, 7}
s2 = {3, 5,}

print(s2.issubset(s1)) # check if all the elements of s2 is present in s1

print(s1.issuperset(s2)) # check if s1  contain the subset s2 in it

print(s1.isdisjoint({4})) # check if it has no common elements