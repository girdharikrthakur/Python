class Animal:

    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammel(Animal):

    def __init__(self):
        print("Mammel  Contructor")
        self.weight = 2
        super().__init__()

    def walk(self):
        print("walk")


class Fish(Animal):

    def swim(self):
        print("swim")


m = Mammel()

print(m.age)
print(m.weight)
