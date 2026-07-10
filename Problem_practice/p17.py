#Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []

for i in range(3):
    mark = input("Enter marks of student {} :".format(i+1))
    marks.append(mark)

marks2 = sorted(marks)
print("Marks of the students are as follows", marks2)

