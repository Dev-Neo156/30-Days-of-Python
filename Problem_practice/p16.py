#Write a program to store seven fruits in a list entered by the user.

fruits = []

for i in range(7):
    fruit = input("Enter the name of fruit {}: ".format(i + 1)) # .format() method is used to format the string with the current fruit number
    fruits.append(fruit)

print("The list of fruits is:", fruits)


