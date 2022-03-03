class Animal:
    def __init__(self):
        print("Animal contructor")
        self.age = 1

    def eat(self):
        print("eat")

# method overriding with __init__'s


class Mammal(Animal):
    def __init__(self):
        super().__init__()  # this resolves the conflict
        print("Mammal Constuctor")
        self.weight = 2

    def walk(self):
        print("walk")


m = Mammal()
print(m.age)
print(m.weight)
