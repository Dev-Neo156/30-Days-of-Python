age = int(input("Enter your age:\n"))
while age > 0:

    if age >= 18:
        print("You are eligible to give vote")
        break;
    else:
        print("You are not eligible to give vote")
        break;

else:
    print("Enter a valid age")