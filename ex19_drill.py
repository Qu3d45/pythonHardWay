# Learn Pyhton The Hard Way ex19 - Functions and Variables
# Manuel Lameira

# DRILL
# 1. Go back through the script and type a comment above each line explaining in English what it
# does.
# 2. Start at the bottom and read each line backward, saying all the important characters.
# 3. Write at least one more function of your own design, and run it 10 different ways.


# defining the function and passing argv


def cheese_and_crackers(chesse_cont, boxes_of_crackers):
    print(f"You have {chesse_cont} cheese!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man thats's enouth for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
# Calling the faction and passing the argv to substitut that existing in the function
cheese_and_crackers(20, 30)


print("Or, we can use variables from our script:")
# Creating to variables
amount_of_cheese = 10
amount_of_crackers = 50
# Passing the variabels to the function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("And we can combine the two, variables and math:")
# Passing the variabels to the function and adding numbers
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 100)

print("Now we ask the user:")
# my solution, ask the user for inicial data and adds unitis if necessary
ask_amount_of_cheese = int(input("How much cheese do you have? "))
ask_amount_of_crackers = int(input("How much crackers do you have? "))
adding_cheese = int(input("How much cheese must I add? "))
adding_crackers = int(input("How much crackers must I add? "))
# Calls the function and pass the sum of the two arguments
cheese_and_crackers(ask_amount_of_cheese + adding_cheese,
                    ask_amount_of_crackers+adding_crackers)
