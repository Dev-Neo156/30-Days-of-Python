#Write a program to create a dictionary of hindi words with values as their English translation. Provide user with an option to look it up!

translation = {
"घर" : "Home",
"पानी" : "Water",
"किताब"	:"Book",
"कलम":"Pen",
"मेज़":"Table",
"कुर्सी":"Chair",
"दरवाज़ा":"Door",
"खिड़की":"Window",
"स्कूल":"School",
}

word = input("Enter the word for which you want to know the translation :")

print(translation[word])