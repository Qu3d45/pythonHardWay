﻿# Learn Pyhton The Hard Way ex45 - My Final Super Game
# Manuel Lameira

# in this file we creat the rooms or levels for our game

from sys import exit
from random import randint
# strips the leading white space from the beginning of lines in a string
from textwrap import dedent

import ex45_my_game_rps


class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your Mom would be proud... if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse tahn your Dad's jokes.",
        "No way! How can you fail on humanity?!"
    ]

    def enter(self):
        # "-1" prevents to go out of range
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship and
            destroyed your entire crew. You are the last surviving
            member and your last mission is to get the neutron destruct
            bomb from the Weapons Armory, put it in the bridge, and
            blow the ship up after getting into an escape pod.

            You're running down the central corridor to the Weapons
            Armory when a Gothon jumps out, red scaly skin, dark grimy
            teeth, and evil clown costume flowing around his hate
            filled body. He's blocking the door to the Armory and
            about to pull a weapon to blast you.
            [shoot, dodge, tell a joke]
            """))
        action = input("> ")

        if action == 'shoot':
            print(dedent("""
                Quick on the draw you yank out your blaster and fire
                it at the Gothon. His clown costume is flowing and
                moving around his body, which throws off your aim.
                Your laser hits his costume but misses him entirely.
                This completely ruins his brand new costume his mother
                bought him, which makes him fly into an insane rage
                and blast you repeatedly in the face until you are
                dead. Then he eats you.
                """))

            return 'death'

        elif action == 'dodge':
            print(dedent("""
                Like a world class boxer you dodge, weave, slip and
                slide right as the Gothon's blaster cranks a laser
                past your head. In the middle of your artful dodge
                your foot slips and you bang your head on the metal
                wall and pass out. You wake up shortly after only to
                die as the Gothon stomps on your head and eats you.
                """))

            return 'death'

        elif action == 'tell a joke' or action == '#':
            print(dedent("""
                Lucky for you they made you learn Gothon insults in
                the academy. You tell the one Gothon joke you know:
                Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
                fur fvgf nebhaq gur ubhfr. The Gothon stops, tries
                not to laugh, then busts out laughing and can't move. 
                You agree to settle the matter with a traditional game.
                """))

            x = ex45_my_game_rps.rock_paper_scissors_game()

            if x == 0:
                print(dedent("""
                Both shoot at the same time and both die...
                """))
                return 'death'
            else:
                print(dedent("""
                While he's looking at your hand, you shoot him square in
                the head putting him down, then jump through the
                Weapon Armory door.
                """))
                return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
            You do a dive roll into the Weapon Armory, crouch and scan
            the room for more Gothons that might be hiding. It's dead
            quiet, too quiet. You stand up and run to the far side of
            the room and find the neutron bomb in its container.
            There's a keypad lock on the box and you need the code to
            get the bomb out. If you get the code wrong 10 times then
            the lock closes forever and you can't get the bomb. The
            code is 3 digits.
            """))

        code = f"{randint(1,9),randint(1,9),randint(1,9)}"
        guess = input("[keypad]> ")

        guesses = 0

        # use ### to override the sistem :)
        if guess != '###':
            while guess != code and guesses < 10:
                print("BZZZEEEDDD!")
                guesses += 1
                guess = input("[keypad]> ")

            if guess == code:
                print(dedent("""
                    The container clicks open and the seal breaks, letting
                    gas out. You grab the neutron bomb and run as fast as 
                    you can to the bridge where you must place it in the
                    right spot.
                    """))
                return 'the_bridge'
            else:
                print(dedent(""" 
                    The lock buzzes one last time and then you hear a 
                    sickening melting sound as the mechanism is fused
                    together. You decide to sit there, and finally the 
                    Gothons blow up your ship from their ship and you die.
                    """))
                return 'death'
        else:
            return 'the_bridge'


class TheBrige(Scene):

    def enter(self):
        print(dedent(""" 
            You burst onto the Brige with the netron destruct bomb
            under your arm and surprise 5 Gothons who are trying to
            take control of the ship. Each of them has an even uglier
            clown costume than the last. They haven't pulled their
            weapons out yet, as they see the active bomb under your
            arm and don't want set it off.
            [throw the bomb, slowly place the bomb]
            """))

        action = input("> ")

        if action == 'throw the bomb':
            print(dedent("""
                In a panic you throw the bomb at the group of Gothons
                and make a leap for the door. Right as you drop it a
                Gothon shoots you right in the back killing you. As 
                you die, you see another Gothon frantically try to
                disarm the bomb. You die knowing they will probably
                blow up when it goes off.
                 """))
            return 'death'
        elif action == 'slowly place the bomb' or action == "#":
            print(dedent(""" 
                You point your blaster at the bomb under your arm and
                the Gothons put their hands up and start to sweat.
                You inch backward to the door, open it, and then
                carefully place the bomb on the floor, pointing your
                blaster at it. You then jump back through the door,
                punch the close button and blast the lock so the
                Gothons can't get out. Now that the bomb is placed
                you run to the escape pod to get off this tin can.
                """))
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return 'the_bridge'


class TheEscapePod(Scene):

    def enter(self):
        print(dedent(""" 
            You rush through the ship desperately trying to make it to
            the escape pod before the whole ship explodes. It seems
            like hardly any Gothons are on the ship, so your run is
            clear of interference. You get to the chamber with the
            escape pods, and now need to pick one to take.
            them could be damaged but you don't have time to look.
            There's 3 pods, which one do you take?
            """))
        good_pod = randint(1, 3)
        guess = input("[pod #]> ")

        if guess != '#':
            if guess != good_pod:
                print(dedent(f"""
                    You jump into pod {guess} and hit the eject button.
                    The pod escapes out into the void of space, then
                    implodes as the hull ruptures, crushing your body into
                    jam jelly.
                    """))
                return 'death'
            else:
                print(dedent(f""" 
                    You jump into pod {guess} and hit the eject button.
                    The pod easily slides out into space heading to the
                    planet below. As it flies to the planet, you look
                    back and see your ship implode then explode like a
                    bright star, taking out the Gothon ship at the same
                    time. You won!
                    """))
                return 'finished'
        else:
            return 'finished'


class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'
