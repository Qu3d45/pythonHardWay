# Learn Pyhton The Hard Way ex13 - Parameters, Unpacking, Variables
# Manuel Lameira

from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("You first variable is:", first)
print("You second variable is:", second)
print("You third variable is:", third)

age = input("How old are you? ")
print(f"So, you're {age}")
