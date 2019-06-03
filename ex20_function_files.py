# Learn Pyhton The Hard Way ex20 - Functions and Files
# Manuel Lameira

from sys import argv

script, input_file = argv

# Function to print the entire file


def print_all(f):
    # read() -> read all contend of a file, returned as a string.
    print(f.read())


# Function reposition the starting point


def rewind(f):
    # start reading in position(0) -> 0 = at file start
    f.seek(0)

# Function to add a line counter and printig the line value


def print_a_line(line_count, f):
    # readline() -> next line from the file, as a string.
    # The end = '' serves to not print de double \n passt from the function
    print(line_count, f.readline(), end='')


# Opens the pre-existing file with pre-existing content
current_file = open(input_file)

print("First let's print the whole file:\n")

# Function call to print the selected file
print_all(current_file)

print("Now let's rewind, kind of like a tape.\n")

# Function repositioning of the reading file start point
rewind(current_file)

print("Let's print three lines\n")

# Calling and writing counter and line value

current_line = 1
print_a_line(current_line, current_file)

# current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

# current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)
