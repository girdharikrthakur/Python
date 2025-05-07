class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point {self.x} {self.y}")


point = Point(1, 2)
point.z = 10
print(point.z)
point.draw()


another = Point(20, 30)
another.draw()
