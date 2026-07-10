# A spam comment is defined as a text containing following keywords: “Make a lot of
# money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

msg = input("Enter the message: ")

spam = "Make a lot of money"
spam2 = "buy now"
spam3 = "subscribe this"
spam4 = "click this"

if spam in msg or spam2 in msg or spam3 in msg or spam4 in msg:
    print("This is a spam message!")
else:
    print("Not a spam!")
