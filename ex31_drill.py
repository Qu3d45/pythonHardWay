# Learn Pyhton The Hard Way ex31 - Making Decisions... a basic game
# Manuel Lameira

print("Hi, player! What's your name?")

name = input("> ")

print(f"So your name is {name}.")

print(f"""{name} you enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = int(input("> "))

if door == 1:
    print("There's a giant bear here eating a chesse cake.")
    print(f"What do you do {name}?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = int(input("> "))

    if bear == 1:
        print(f"The bear eats your face off. Good job {name}!")
    elif bear == 2:
        print(f"The bear eats your legs off. Good job {name}!")
    else:
        print(f"Well, doing {bear} is probably better.")  # on linux
        # print("Well, doing ", bear, " is probably better.") # on windows machines
        print("Bear runs away after eating his cheese cake.")

elif door == 2:
    print(f"{name} you stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = int(input("> "))

    if insanity == 1 or insanity == 2:
        print("Your body survives powerd by a mind of jello.")
        print(f"Good job {name}!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print(f"Good job {name}!")

else:
    print(f"You stumble around and fall on a knife and die. Good job {name}!")
