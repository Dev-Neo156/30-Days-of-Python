# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and
# use key as their names. Assume that the names are unique.
s = {}

for i in range(4):
    name = input("Enter name: ")
    lang = input("Enter your favourite language: ")
    s.update({name: lang})

print(s)