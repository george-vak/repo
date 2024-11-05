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

    def __getitem__(self, ind):
        dots = [(self.x1, self.y1), (self.x1, self.y2), (self.x2, self.y2), (self.x2, self.y1)]
        return dots[ind]

    def __bool__(self):
        return self.area() != 0

    def __del__(self):
        self.__class__.rectcnt -= 1
        print("&", self.__class__.rectcnt)


obj = Rectangle(0, 0, 4, 5)
obj2 = Rectangle(1, 1, 3, 4)
obj3 = obj.__class__(0, 0, 0, 0)

print(list(obj))
print(obj[3])
for x, y in obj2:
    print(x, y)

print(obj3.__bool__())
print(obj.__bool__())


for i in Rectangle(2, 3, 4, 5):
    print("#", i)
