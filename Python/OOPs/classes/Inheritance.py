# Inheritance
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

