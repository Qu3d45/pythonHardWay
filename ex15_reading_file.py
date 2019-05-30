# Learn Pyhton The Hard Way ex15 - Reading Files
# Manuel Lameira

# imports a module to use arguments
from sys import argv

# This are the arguments we need
script, filename = argv

# opens a faile and stors it under txt
# filename = input('> ') # use this if you don't wont to use sys
txt = open(filename)

# printing the files content
print(f"Here's your file {filename}:")
print(txt.read())

# asks for the filename again, but you can type anithing you wont
# because it will call the filename stored when we gave the argv

print("Type the filename again:")
file_again = input('> ')

txt_again = open(filename)

print(txt_again.read())
