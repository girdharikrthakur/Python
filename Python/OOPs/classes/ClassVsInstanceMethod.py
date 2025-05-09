class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point {self.x} {self.y}")

    @classmethod
    def zero(cls):
        return cls(0, 0)


# point = Point(1, 2)


point = Point.zero()  # zero is called Factory Method
point.Draw()  # Instance Method



