# Learn Pyhton The Hard Way ex32 - Loops and List
# Manuel Lameira

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'orange', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    # variable named number is assigned the value of each element
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    # variable name fuit is assigned the value of each fruits
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also buid lists, first start with an empty one
elements = []
# copy the entire list
# elements2 = elements[:]

# Then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")

# The range() function returns a sequence of numbers, starting from 0 by default,
# and increments by 1 (by default), and ends at a specified number.
# Example
# Create a sequence of numbers from 0 to 5, and print each item in the sequence:
# x = range(6)
# for n in x:
#   print(n)

# There are four collection data types in the Python programming language:
    # List is a collection which is ordered and changeable. Allows duplicate members.
    # Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    # Set is a collection which is unordered and unindexed. No duplicate members.
    # Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# When choosing a collection type, it is useful to understand the properties of that type.
# Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
