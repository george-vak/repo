class IsType:
    def __init__(self, typ):
        self.typ = typ

    def __call__(self, func):
        def wrapper(*args):
            if not all(isinstance(arg, self.typ) for arg in args):
                raise TypeError("type error")
            return func(*args)
        return wrapper

@IsType(int)
def add(a, b, c, e=10):
    return a + b + c + e

try:
    print(add(1, 2, 3))
    print(add(1, 2, "3"))
except TypeError as e:
    print(e)

