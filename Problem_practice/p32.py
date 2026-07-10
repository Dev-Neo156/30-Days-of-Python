# Write a program to find out whether a given post is talking about “Harry” or not

post = input("Enter your post\n")

if "Harry" in post or "harry" in post:
    print("Yes, This post talks about Harry")
else:
    print("No, This post doesn't talks about Harry")

