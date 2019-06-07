# Learn Pyhton The Hard Way ex33 - While loops
# Manuel Lameira

numbers = []

for i in range(0, 6):
    print(f"Adding {i} to the list.")
    numbers.append(i)
    #i += 1

for i in numbers:
    print(f"Element was: {i}")
