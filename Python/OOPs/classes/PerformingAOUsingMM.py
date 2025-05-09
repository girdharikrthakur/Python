class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point {self.x} {self.y}")

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)


point = Point(11, 2)
other = Point(2, 3)
combined = point+other
print(combined.x)
