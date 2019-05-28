# Learn Pyhton The Hard Way ex16 - Reading and Writing Files
# Manuel Lameira

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you dont't want, hit CTRL-C (^C).")
print("If you want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbay!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

# creating spc permits to reduce the write code
spc = '\n'
target.write(line1 + spc + line2 + spc + line3 + spc)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print("And finally, we close it.")
target.close()

# Printing the created file
target = open(filename)

# printing the files content
print(f"\nHere's your file {filename}:\n")
print(target.read())
