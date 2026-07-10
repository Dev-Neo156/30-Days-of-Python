#Write a python program to print the contents of a directory using the os module. Search online for the function which does that.

import os

directory = '.'

contents = os.listdir(directory)

print(f"Contents of '{directory}':\n")

for item in contents:
    path = os.path.join(directory, item)
    if os.path.isdir(path):
        print(f"[DIR]  {item}")
    else:
        print(f"[FILE] {item}")

    