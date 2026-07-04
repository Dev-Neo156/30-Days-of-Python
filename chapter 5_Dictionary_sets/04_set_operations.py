s1 = {1, 3, 5, 6, 8}
s2 = {3, 11, 4, 9, 7}

print(s1.union(s2)) # combine all the elements in both the sets
print(s1.intersection(s2)) # only prints common elements in both
print(s1.difference(s2)) # elements that are present in only s1
print(s2.difference(s1)) # elements that are only present in s2
print(s1.symmetric_difference(s2)) # elements that are neither in the both sets
    
