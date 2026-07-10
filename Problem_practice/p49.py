# Write a python function to remove a given word from a list and strip it at the same time.


def listfunc(l, word):
    l.remove(word)
    l2 = [item.replace(word, "") for item in l]
    return l2

l = ["Harry", "Aditya", "Mango"]
print(l)
word = input("Enter the word you wnat to remove: ")
print(listfunc(l, word))

