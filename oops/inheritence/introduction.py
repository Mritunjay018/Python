class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


class Cuboid(Rectangle):
    def __init__(self, l, b, h):
        super().__init__(l, b)
        self.height = h

    def volume(self):
        return self.length * self.breadth * self.height
c = Cuboid(5, 3, 4)
print(c.area())      # 15
print(c.volume())    # 60
print(c.perimeter()) # 16
