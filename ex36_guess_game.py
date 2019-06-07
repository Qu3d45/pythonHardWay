# Learn Pyhton The Hard Way ex36 - Number guessing Game
# Manuel Lameira

import random

correct = False

r = random.randint(1, 20)

i = 0

while correct == False:
    n = input("Guess my number between 1 and 20: ")

    i += 1
    if int(n) == r:
        correct = True
    else:
        if int(n) > r:
            print("Sorry, my number is lower. Try again.")
        else:
            print("Sorry, my number is higher. Try again.")

print(f"Well done. The correct answer was {r}. You got it in {i} tries.")
