# Learn Pyhton The Hard Way ex45 - Rock, Paper, Scissors Game
# Manuel Lameira

# ROCK, PAPER, SCISSORS
# Passed down from the ancient Chinese Han dynasty, yhe game
# shoushiling is now better known as Rock, Paper, Scissors.
# This code implements a version of the game that is you against
# the computer.

# Here we're doing some setup by importing the random module
# and setting up the winner veriable.

from random import randint


class Rock_Paper_Scissors(object):

    def __init__(self):

        self.winner = ''

        self.random_choice = randint(0, 2)

        if self.random_choice == 0:
            self.computer_choice = 'rock'
        elif self.random_choice == 1:
            self.computer_choice = 'paper'
        else:
            self.random_choice = 'scissors'

        self.user_choice = ''

        while (self.user_choice != 'rock' and
               self.user_choice != 'paper' and
               self.user_choice != 'scissors'):
            self.user_choice = input("rock, paper, scissors? ")

        uc = self.user_choice
        print(">>>> uc", uc)
        cc = self.computer_choice
        win = self.winner

        if cc == uc:
            win = 'Tie'
        elif cc == 'paper' and uc == 'rock':
            win = 'Computer'
        elif cc == 'rock' and uc == 'scissors':
            win = 'Computer'
        elif cc == 'scissors' and uc == 'paper':
            win = 'Lhytros'
        else:
            win = 'You'

        if win == 'Tie':
            print("Both choose", cc + ", both died...")

            # return 'death'

        else:
            print(win, "won. Gothon Lhytros choose",
                  cc + ".")

            # return 'laser_weapon_armory'


a_game = Rock_Paper_Scissors()

# todo: dividir o program em funcções (escolha do utilizador / escolha do gotho) e depois testar
# Esta a dar um erro: imposivel entregar retono em __init__
