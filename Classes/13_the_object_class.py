class Animal(object):  # object is the base class in python
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

# Animal: Parent, Base
# Mammal: Child, Sub


class Mammal(Animal):
    def walk(self):
        print("walk")


m = Mammal()
print(isinstance(m, object))
print(issubclass(Mammal, Animal))
print(issubclass(Mammal, object))
