# Learn Pyhton The Hard Way ex41 - My test
# Manuel Lameira

# A simple math calculator using OOP
# User has to introduce two numbers and the program return's varios math operations


class math_operation(object):
    def __init__(self, num1, num2):
        self.x = num1
        self.y = num2

    def add(self):
        r_sum = self.x + self.y
        print(f" The sum of {self.x} + {self.y} = {r_sum}\n")
        return r_sum

    def sub(self):
        r_sub = self.x - self.y
        print(f" The subtraction of {self.x} - {self.y} = {r_sub}\n")
        return r_sub

    def multi(self):
        r_multi = self.x * self.y
        print(f" The multiplication of {self.x} * {self.y} = {r_multi}\n")
        return r_multi

    def divi(self):
        r_div = self.x / self.y
        print(f" The division of {self.x} / {self.y} = {r_div}\n")
        return r_div

    def floor_div(self):
        r_fdiv = self.x // self.y
        print(f" The floor division of {self.x} // {self.y} = {r_fdiv}\n")
        return r_fdiv

    def remind(self):
        r_remind = self.x % self.y
        print(f" The reminder of {self.x} % {self.y} = {r_remind}\n")
        return r_remind

    # try to some all but in this way it multipleis the result...
    def crazy(self, r_sum, r_sub, r_multi, r_div, r_fdiv, r_remind):
        r_cray = r_sum + r_sub + r_multi + r_div + r_fdiv + r_remind
        print(
            f"If we sum all the results {r_sum} + {r_sub} + {r_multi} + {r_div} + {r_fdiv} + {r_remind}= {r_cray}\n")


try:
    print("what's the first number?")
    num1 = int(input("> "))
    print("what's the second number?")
    num2 = int(input("> "))
except:
    print("\nSomething is Wrong!")

test = math_operation(num1, num2)

test.add()
test.sub()
test.multi()
test.divi()
test.floor_div()
test.remind()

# test.crazy()

test.crazy(test.add(), test.sub(), test.multi(),
           test.divi(), test.floor_div(), test.remind())
