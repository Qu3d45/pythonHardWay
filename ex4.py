# Learn Pyhton The Hard Way ex4 - Variables and Names
# Manuel Lameira

# Variable declaretion
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

# Study Drills
# Traceback ( most recent call last ) :
# File ”ex4.py”, line8, in <module>
#   average_passengers_per_car = car_pool_capacity / passenger
# NameError : name ’ car_pool_capacity’ is not defined
#
# Explain this error in your own words. Make sure you use line numbers and explain why.
#
# Answer: Fail to declare the car_pool_capacity
#
