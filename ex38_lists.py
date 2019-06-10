# Learn Pyhton The Hard Way ex38 - Doing things to Lists
# Manuel Lameira

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')  # splits in to individual words

# ten_things.split(' ') == split(ten_things, ' ')

more_stuff = ["Day", "Night", "Song",
              "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# while len(stuff) != 10:
#     next_one = more_stuff.pop()
#     # more_stuff.pop() == pop(more_stuff)
#     # Call pop on more_stuff == Call pop with argument more_stuff
#     print("Adding: ", next_one)
#     stuff.append(next_one)
#     # stuff.append(next_one) == append(stuff, next_one)
#     # Call append on stuff and add next_one == Call append with argument stuff and add variable next_one
#     print(f"There are {len(stuff)} item now.")

for i in more_stuff:
    if len(i) <= 10:
        i = more_stuff.pop()
        print("Adding: ", i)
        stuff.append(i)
        print(f"There are {len(stuff)} item now.")
    else:
        pass
else:
    pass


print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])  # whoa! fancy
print(stuff.pop())
# stuff.pop() == pop(stuff)
# Call pop on stuff == Call pop with argument stuff
print(' '.join(stuff))  # What? Cool!
print('#'.join(stuff[3:5]))  # super stellar!
