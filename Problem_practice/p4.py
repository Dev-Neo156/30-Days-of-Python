#Label the program written in problem 4 with comments.
import os

# Directory to list (use '.' for current directory)
directory = '.'

# Get list of all files and directories
contents = os.listdir(directory)

print(f"Contents of '{directory}':\n")

for item in contents:
    path = os.path.join(directory, item)
    if os.path.isdir(path):
        print(f"[DIR]  {item}")
    else:
        print(f"[FILE] {item}")
