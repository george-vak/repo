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


obj = Rectangle(1, 2, 3, 4)
ob = Rectangle(2, 3, 4, 5)
okm = Rectangle(2, 4, 5, 6)
print(dir(ob))
