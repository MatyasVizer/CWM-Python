class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")


class Chicken(Bird):  # chicken inherits fly but it cannot fly
    pass


# Employee - Person - LivingCreature - Thing
# it is not great to model the entire universe
# classes are there to solve business problems
