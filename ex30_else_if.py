# Learn Pyhton The Hard Way ex30 - Else if
# Manuel Lameira

people = 50
cars = 40
trucks = 40

# checks the first condition, if false go's to the next
if cars > people:
    print("We should take the cars.")
# checks the second condition, prints if true, if false go's to the next condition
elif cars < people:
    print("We should not take the cars.")
# if the first and second condition are false, prints this one
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
