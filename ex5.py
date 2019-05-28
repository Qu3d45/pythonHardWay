# Learn Pyhton The Hard Way ex5 - More Variables
# Manuel Lameira

name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
height_cm = height * 2.54
weight = 180  # lbs
weight_kg = weight / 2
eyes = 'Blue'
theeth = 'White'
hair = 'Brown'

print(f"Let's talk about {age}.")
print(f"He's {height} inches tall or {height_cm} cm.")
print(f"He's {weight} pounds heavy or {weight_kg} kg.")
print("Actaully that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"He's teeth are usually {theeth} depending on the coffee.")

# this line is tricky, try get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
