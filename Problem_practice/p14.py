#Replace the double space with single space from p13

string_ = input("Enter a string: ")
if "  " in string_:
    string_ = string_.replace("  ", " ")
    print("After replacing double space with single space- ",string_)
else:
    print("No double space detected.")