# Learn Pyhton The Hard Way ex28 - The Truth Tables
# Manuel Lameira

# True and True         --> True
# False and True        --> False
# 1 == 1 and 2 == 1     --> False
# "test" == "test"      --> True
# 1 == 1 or 2 != 1      --> True
# True and 1 == 1       --> True
# False and 0 != 0      --> False
# True or 1 == 1        --> True
# "test" == "testing"   --> False
# 1 != 0 and 2 == 1     --> False
# "test" != "testing"   --> True
# "test" == 1           --> False
# not (True and False)  --> True
# not (1 == 1 and 0 != 1)       --> False
# not (10 == 1 or 1000 == 1000) --> False
# not (1 != 10 or 3 == 4)       --> False
# not ("testing" == "testing" and "Zed" == "Cool Guy")  --> True
# 1 == 1 and (not ("testing" == 1 or 1 == 0))           --> True
# "chunky" == "bacon" and (not (3 == 4 or 3 == 3))                  --> False
# 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))    --> False

print("1", True and True)
print("2", False and True)
print("3", 1 == 1 and 2 == 1)
print("4", "test" == "test")
print("5", 1 == 1 or 2 != 1)
print("6", True and 1 == 1)
print("7", False and 0 != 0)
print("8", True or 1 == 1)
print("9", "test" == "testing")
print("10", 1 != 0 and 2 == 1)
print("11", "test" != "testing")
print("12", "test" == 1)
print("13", not (True and False))
print("14", not (1 == 1 and 0 != 1))
print("15", not (10 == 1 or 1000 == 1000))
print("16", not (1 != 10 or 3 == 4))
print("17", not ("testing" == "testing" and "Zed" == "Cool Guy"))
print("18", 1 == 1 and (not ("testing" == 1 or 1 == 0)))
print("19", "chunky" == "bacon" and (not (3 == 4 or 3 == 3)))
print("20", 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")))
