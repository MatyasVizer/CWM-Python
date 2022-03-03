class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


# whichever comes first, it's conflicting function will gets called first


class Manager(Person, Employee):
    pass


manager = Manager()
manager.greet()


# good example of multiple inheritance --->>>

class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass
