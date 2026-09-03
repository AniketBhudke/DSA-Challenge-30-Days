# What is File Handling?
# File handling is the process of creating, opening, reading, writing, and closing files
# using a Python program.
# Opening a file in Python can be done in two ways:
# 1. Using open() directly
file = open("E:\DSA Challenge 30 Days\otes.txt", "r")
print(file.read())
file.close()


# 2. Using with open()
# with open("notes.txt", "r") as file:
#     print(file.read())