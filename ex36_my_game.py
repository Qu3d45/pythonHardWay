# Learn Pyhton The Hard Way ex36 - My Game
# Manuel Lameira

from sys import exit


def gold_room(p1):
    print("This room is full of gold. How much kg do you take?")
    try:
        how_much = int(input("> "))
    except:
        dead(f"{p1} learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room(p1):
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print(f" {p1}, how are you going to move the bear?")
    print("1. Steal the honey.")
    print("2. Taunt the bear")
    print("3. Shout at the bear.")
    print("4. Force door to open.")
    bear_moved = False

    while True:
        try:
            choice = int(input("> "))
        except:
            dead("Come on, learn to type a number.")

        if choice == 1:
            dead("The bear looks at you then slaps your face off.")
        elif choice == 2 and not bear_moved:
            print("The bear has moved from the door.")
            print("After you open the door, you can go through it.")
            bear_moved = True

        elif choice == 3 and not bear_moved:
            dead("The bear gets pissed off and chews your leg off.")

        elif choice == 4 and bear_moved:

            gold_room(p1)

        else:
            print("I got no idea what that means.")


def cthulhu_room(p1):
    print("You are facing the great evil Cthulu.")
    print("He, it, whatever... stares at you and you go insane.")
    print(f"{p1} Do you flee for your life or eat your head?")
    print("(Please type your answer)")

    choice = input("> ")

    if "flee" in choice:
        start(p1)
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room(p1)


def dead(why):
    print(why, "GAME OVER!")
    exit(0)


def player():
    print("Before you start your adventure, tell me your name.")
    p1 = input("> ")
    print(f"So {p1}, do you want me to tell you how the game works?")
    print("1. Yes")
    print("2. No")

    try:
        choice = int(input("> "))
    except:
        dead("Man, learn to type a number.")

    if choice == 1:
        rules(p1)
    elif choice == 2:
        start(p1)
    else:
        dead("TILT...TILT...TILT... Maybe next time you follow the rules.")


def start(p1):
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print(f"{p1}, which one do you take?")
    print("1. Right")
    print("2. Left")

    try:
        choice = int(input(" > "))
    except:
        dead("Man, learn to type a number.")

    if choice == 1:
        bear_room(p1)
    elif choice == 2:
        cthulhu_room(p1)
    else:
        dead("You stumble around the room until you starve.")


def rules(p1):
    print(f"""
    Ok {p1}, it's very easy. Just select the number
    for the desired answer or type it whenever it says to do so. """)
    print("So let's begin your adventure!")
    print("")
    start(p1)
    exit(0)


player()
