class Employee:

    def greet(self):
        print("Employee greet")


class Person:

    def greet(self):
        print("Persion Greet")


class Manager(Employee, Person):
    pass


manager = Manager()
manager.greet()


