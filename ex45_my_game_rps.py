# Learn Pyhton The Hard Way ex45 - Rock, Paper, Scissors Game
# Manuel Lameira

import random


def comp_choice():

    possible_moves = ['rock', 'paper', 'scissors']

    computer_choice = random.choice(possible_moves)

    # random_choice = random.randint(0, 2)

    # if random_choice == 0:
    #     computer_choice = possible_moves[0]
    # elif random_choice == 1:
    #     computer_choice = possible_moves[1]
    # else:
    #     computer_choice = possible_moves[2]

    print(">>>> ", computer_choice)
    return computer_choice


def usr_choice():

    user_choice = ''

    while (user_choice != 'rock' and
           user_choice != 'paper' and
           user_choice != 'scissors'):
        user_choice = input("rock, paper, scissors? ")

    # print(">>>> " user_choice)
    return user_choice


def rock_paper_scissors_game():

    winner = ''

    cc = comp_choice()
    uc = usr_choice()

    if cc == uc:
        winner = 'Tie'
    elif cc == 'paper' and uc == 'rock':
        winner = 'Gothon Lhytros'
    elif cc == 'rock' and uc == 'scissors':
        winner = 'Gothon Lhytros'
    elif cc == 'scissors' and uc == 'paper':
        winner = 'Gothon Lhytros'
    else:
        winner = 'You'

    if winner == 'Tie' or winner == 'Gothon Lhytros':
        print(f"\nGothon Lhytros choose {cc}.")
        return 0
    else:
        print(f"\nYou won. Gothon Lhytros choose {cc}.")
        return 1


# rock_paper_scissors_game()
