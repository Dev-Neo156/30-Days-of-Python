marks = {
    "Keys" : "value",
    "Harry" : 100,
    "Subham" : 80,
    "Rohan" : 45
}

print(marks, type(marks))
print(marks["Harry"])
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Harry": 99})
print(marks)
print(marks.get("Harry")) #Return none if the key doesn't exist
print(marks["Harry"]) #Throws error if the key doesn't exist
value = marks.pop("Harry")
print(value)
print(marks)
item = marks.popitem()
print(item)
item = marks.popitem()
print(item)
print(marks)

#Properties -
#It is unorderd
#It is mutable
#It is indexed
#Cannot contain duplicate keys