# Learn Pyhton The Hard Way ex19 - Functions and Variables
# Manuel Lameira


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
