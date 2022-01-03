## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass


## class Dog is-a Animal,and initialize name variable
class Dog(Animal):
    def __init__(self, name):
        self.name = name


## class Cat is-a Animal,and initialize name variable
class Cat(Animal):
    def __init__(self, name):
        ## Initialize the name variable
        self.name = name


## class Person is-a object,and initialize name & pet variable
class Person(object):
    def __init__(self, name):
        ## Initialize the name variable
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None


## class Employee is-a Person, and initialize name and salary
class Employee(Person):
    def __init__(self, name, salary):
        ## ??
        super(Employee, self).__init__(name)
        ## Initialize salary variable of the instance
        self.salary = salary


## Class Fish is-a object
class Fish(object):
    pass


## Class Salmon is-a Fish
class Salmon(Fish):
    pass


## class Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary's pet is satan
mary.pet = satan

## frank is-a Employee with 120000 salary
frank = Employee("Frank", 120000)

## frank's pet is rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
coruse = Salmon()

##harry is-a Halibut
harry = Halibut()
