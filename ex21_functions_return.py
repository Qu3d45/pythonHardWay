# Learn Pyhton The Hard Way ex21 - Funcions and Returns
# Manuel Lameira


def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b


def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b


def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b


def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# Study Drill 2 and 3: Puzzel formula
what2 = ((30+5) + ((78-4)-((90*2)*((100/2)/2))))

# Study Drill 4
inverse = divide(add(age, multiply(height, subtract(weight, 45))), iq)

print("That becomes: ", what, "Can you do it by hand?")

print(f"Puzzel result: {what2}")

print(f"Puzzel Inverse Study Drill 4: {inverse}")
