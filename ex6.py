# Learn Pyhton The Hard Way ex6 - Strings and text
# Manuel Lameira

# Variable declaration
types_of_people = 10
# string with format (f) to use {}
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

# A variable (string) insde a string
print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False

# The format is not defined
joke_evaluation = "Isn't that joke funny?! {}"

# define the string hilarious as format
print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = " a sting with a right side."

# adding strings
print(w + e)
