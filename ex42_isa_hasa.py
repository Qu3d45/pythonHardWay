# Learn Pyhton The Hard Way ex42 - Is-a, Has-a, Objects and Classes
# Manuel Lameira

# Animaal is-a object (yes, sort of confusing) look at the extra credit


class Animal(object):
    pass

# ? --> Dog is-a Animal


class Dog(Animal):
    # init takes self and name
    def __init__(self, name):
        # ? --> Dog has-a attribute named name
        self.name = name

# ? --> Cat is-a Animal


class Cat(Animal):
    def __init__(self, name):
        # ? --> Cat has-a attribute named name
        self.name = name

# ? --> PErson is-a Object


class Person(object):
    def __init__(self, name):
        # ? --> Person has-a attribuite named name
        self.name = name

        # Person has-a pet of some kind
        self.pet = None

# ? --> Employee is-a person


class Employee(Person):
    def __init__(self, name, salary):
        # ? hmm is this strange magic?
        # -->
        super(Employee, self).__init__(name)
        # ? --> employee has-a salary
        self.salary = salary

# ? --> Fish is-a object


class Fish(object):
    pass

# ? --> Salmon is-a Fish


class Salmon(Fish):
    pass

# ? --> Halibut is-a Fish


class Halibut(Fish):
    pass


# rover is-a Dog
rover = Dog("Rover")

# ? --> Satan is-a Cat
satan = Cat("Satan")

# ? --> Mary is-a Person
mary = Person("Mary")

# ? --> MAry has-a Pet call satan
mary.pet = satan

# ? --> fran is-a employee with a salary os 120000
frank = Employee("Frank", 120000)

# ? --> frank has-a pet call rover
frank.pet = rover

# ? --> Flipper is-a Fish
flipper = Fish()

# ? --> crouse is-a Salmon
crouse = Salmon()

# ? --> Harry is-a Halibut
harry = Halibut()
