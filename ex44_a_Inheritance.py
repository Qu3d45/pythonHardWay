﻿# Learn Pyhton The Hard Way ex44 - Inheritance Versus Composition
# Manuel Lameira

# ----------------------------
# Implicit Inheritance
# ----------------------------
# class Parent(object):

#     def implicit(self):
#         print("PARENT implicit()")


# class Child(Parent):
#     pass


# dad = Parent()
# son = Child()

# dad.implicit()
# son.implicit()


# ----------------------------
# Override Explicitly
# ----------------------------
# class Parent(object):

#     def override(self):
#         print("PARENT override")


# class Child(Parent):

#     def override(self):
#         print("CHILD override")


# dad = Parent()
# son = Child()

# dad.override()
# son.override()


# ----------------------------
# Alter Before or After
# ----------------------------
# class Parent(object):

#     def altered(self):
#         print("PARENT alterd()")


# class Child(Parent):

#     def altered(self):
#         print("CHILD, BEFORE PARENT altered()")
#         super(Child, self).altered()
#         print("CHILD, AFTER PARENT altered()")


# dad = Parent()
# son = Child()

# dad.altered()
# son.altered()

# ----------------------------
# All Three Combined
# ----------------------------

class Parent(object):

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")


class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
