# Learn Pyhton The Hard Way ex40 - Modules, Classes, and Objects
# Manuel Lameira

### A dictionary ###
# myStuff = {
#     'apple': 'I AM APPLES!'
# }

# print(myStuff['apple'])


### Modules ###

# this goes in mystuff.py
# def apple():
#     print("I AM APPLES!")

# this is just a variable
# tangerine = "Living reflection of a dream"

# Once I have this code, I can use the module MyStuff
# with import and then access the apple function

# import mystuff

# mystuff.apple()
# print(mystuff.tangerine)

# 1. A Python file with some functions or variables in it ..
# 2. You import that file.
# 3. And you can access the functions or variables in
#    that module with the . (dot) operator.

# mystuff['apple']  # get apple from dict
# mystuff.apple()   # get apple from the module
# mystuff.tangerine # same thing, it's just a variable

# In the case of the dictionary, the key is a string
# and the syntax is [key] . In the case of the module, the
# key is an identifier, and the syntax is .key .
# Other than that they are nearly the same thing.


### Classes ###
# A class is a way to take a grouping of functions and
# data and place them inside a container so you can
# access them with the . (dot) operator.

# class MyStuff(object):

#     def __init__(self):
#         self.tangerine = "And now a thousand years between"

#     def apple(self):
#         print("I AM CLASSY APPLES!")


### I now have three ways to get things from things: ###
# dict style
# mystuff['apples']

# module style
# mystuff.apples()
# print(mystuff.tangerine)

# class style
# thing = MyStuff()
# thing.apples()
# print(thing.tangerine)
