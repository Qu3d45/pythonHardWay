# Learn Pyhton The Hard Way ex36 - word guessing Game
# Manuel Lameira

import random

WORDLIST = ["orange", "table", "monkey", "balloon",
            "mouse", "speaker", "lorry", "apple"]
theWord = random.choice(WORDLIST)


def startGuessing():
    triesLeft = 10
    answer = "-" * len(theWord)

    while triesLeft > -1 and not answer == theWord:
        print(f"\n {answer}")
        print(f"{triesLeft} tries left.")
        guess = input("Guess a letter:")
        if len(guess) != 1:
            print("Just guess one letter at a time.")
        elif guess in theWord:
            print("Yes that letter is in the Word.")
            answer = updateAnswer(theWord, answer, guess)
        else:
            print("Sorry, that letter is not in the word.")
            triesLeft -= 1
    if triesLeft < 0:
        print(f"Sorry, you have run out od tries. The word was: {theWord}")
    else:
        print(f"Well done, you guessed right. The wors was: {theWord}")


def updateAnswer(word, ans, guess):
    result = ""
    for i in range(len(word)):
        if word[i] == guess:
            result = result + guess
        else:
            result = result + ans[i]
    return result


print("I'm thinking of a word...")
startGuessing()
