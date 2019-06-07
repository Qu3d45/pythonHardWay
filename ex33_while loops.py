# Learn Pyhton The Hard Way ex33 - While loops
# Manuel Lameira


def while_func(num_top, increments):
    i = 0
    numbers = []

    while i < num_top:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += increments

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)


numi = input("How much numbers? ")
incre = input("How much it increments? ")

while_func(int(numi), int(incre))
