class Rectangle():
    rectcnt = 0

    def __init__(self, x1, y1, x2, y2):
        self.__class__.rectcnt += 1
        setattr(self, f"rect_{self.rectcnt}", self.rectcnt)
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def __str__(self):
        return f"({self.x1},{self.y1})({self.x1},{self.y2})({self.x2},{self.y2})({self.x2},{self.y1})"

    def area(self):
        return abs((self.x2 - self.x1) * (self.y2 - self.y1))

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __mul__(self, num):
        return Rectangle(self.x1 * num, self.y1 * num, self.x2 * num, self.y2 * num)

    def __rmul__(self, num):
        return self.__mul__(num)

obj = Rectangle(0, 0, 4, 5)
obj2 = Rectangle(1, 1, 3, 4)
obj3 = obj2.__class__(0, 0, 4, 5)

print(2 * obj3 * 2)
