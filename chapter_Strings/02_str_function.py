a = "Harry"

print(len(a))

print(a.endswith("rry"))

print(a.startswith("Har"))

print(a.capitalize())

text = "   Hello World!   "
print(text.strip())  # Output: "Hello World!"

text = "I like apples."
print(text.replace("apples", "bananas"))  # Output: "I like bananas."

text = "Python is fun"
print(text.split())  # Output: ['Python', 'is', 'fun']

csv = "apple,banana,cherry"
print(csv.split(",")) # Output: ['apple', 'banana', 'cherry']

words = ['Python', 'is', 'fun']
print(" ".join(words))  # Output: "Python is fun"
print("-".join(words))  # Output: "Python-is-fun"

text = "hello WoRld"
print(text.lower())  # Output: "hello world"
print(text.upper())  # Output: "HELLO WORLD"
print(text.title())  # Output: "Hello World"

text = "Hello, welcome to Python."
print(text.find("welcome"))  # Output: 7
print(text.find("Java"))     # Output: -1

text = "apple, banana, apple"
print(text.count("apple"))  # Output: 2

filename = "document.pdf"
print(filename.endswith(".pdf"))  # Output: True

print("12345".isdigit())  # Output: True
print("Python3".isalpha()) # Output: False (because of the '3')
print("Python3".isalnum()) # Output: True