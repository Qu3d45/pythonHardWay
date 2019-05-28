# Learn Pyhton The Hard Way ex19 - Functions and Variables
# Manuel Lameira

# DRILL
# 1. Go back through the script and type a comment above each line explaining in English what it
# does.
# 2. Start at the bottom and read each line backward, saying all the important characters.
# 3. Write at least one more function of your own design, and run it 10 different ways.


def cheese_and_crackers(chesse_cont, boxes_of_crackers):
    print(f"You have {chesse_cont} cheese!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man thats's enouth for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("Or, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 100)
