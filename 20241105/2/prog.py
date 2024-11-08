from math import isclose

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = tuple(p1)
        self.p2 = tuple(p2)
        self.p3 = tuple(p3)

    def area(self):
        x1, y1 = self.p1
        x2, y2 = self.p2
        x3, y3 = self.p3
        r = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)
        return r if r!= 0.0 else 0

    def __abs__(self):
        return self.area()

    def __bool__(self):
        return not isclose(self.area(), 0)

    def __lt__(self, other):
        return self.area() < abs(other)

    def __contains__(self, other):
        if not other:
            return True
        if not self:
            return False
        return (self.is_p_in_triag(other.p1) and
                self.is_p_in_triag(other.p2) and
                self.is_p_in_triag(other.p3))

    def __and__(self, other):
        if not self or not other:
            return False
        return (self.is_p_in_triag(other.p1) or
                self.is_p_in_triag(other.p2) or
                self.is_p_in_triag(other.p3) or
                other.is_p_in_triag(self.p1) or
                other.is_p_in_triag(self.p2) or
                other.is_p_in_triag(self.p3))

    def is_p_in_triag(self, point):
        x, y = point
        x1, y1 = self.p1
        x2, y2 = self.p2
        x3, y3 = self.p3

        etalon = self.area()
        area1 = Triangle((x, y), self.p2, self.p3).area()
        area2 = Triangle(self.p1, (x, y), self.p3).area()
        area3 = Triangle(self.p1, self.p2, (x, y)).area()

        return isclose(etalon, area1 + area2 + area3)

import sys
exec(sys.stdin.read())

