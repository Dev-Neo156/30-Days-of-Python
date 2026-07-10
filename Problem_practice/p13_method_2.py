name = input("Enter your name:")

if name.find("  ") != -1:
    print("Double space detected.")
else:
    print("No double space detected.")