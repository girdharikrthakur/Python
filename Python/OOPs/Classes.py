# Classes in python

# Classes are blue print for creating an object
# Obkect : is an instance of a class
# Class : Human
# Object : Jhon , Mary , Jack



# 1: Creating a Class
# Syntax : Class ClassName

class Point:
    def draw(self):
        print("Draw")


point = Point()
print(type(point))
print(isinstance(point, Point))  # Check is point is an instance of Point
