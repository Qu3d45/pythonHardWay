# Learn Pyhton The Hard Way ex8 - Printing, Printing
# Manuel Lameira

formatter = "{} {} {} {}"

# call for format function do modyfi the formatter variable
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "tow", "three", "four"))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
