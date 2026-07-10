# Write a program to find out whether a student has passed or failed if it requires a total of
# 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an
# input from the user.

eng = int(input("Enter the marks of English\n"))
maths = int(input("Enter the marks of Maths\n"))
science = int(input("Enter the marks of Science\n"))

percentage_total = ((eng + maths + science)/300)*100

if percentage_total >= 40:
    if eng >= 33 and maths >= 33 and science >= 33:
        print("Congratulation You have Passed")
else:
    print("Better luck next time! you have failed")