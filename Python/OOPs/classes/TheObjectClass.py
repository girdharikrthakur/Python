
class Animal:

    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammel(Animal):

    def walk(self):
        print("walk")


class Fish(Animal):

    def swim(self):
        print("swim")


m = Mammel()

print(isinstance(m, Animal))  # True


# object class is the base class of alll the classes
# Evan if we do not inheritae it from


print(issubclass(Mammel, Animal))  # True
