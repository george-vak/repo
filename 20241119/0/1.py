def is_type(typ):
    def decorator(func):
        def wrapper(*args):
            if not all(isinstance(arg, typ) for arg in args):
                raise TypeError("type error")
            return func(*args)
        return wrapper
    return decorator

@is_type(int)
def add(a, b, c, e = 10):
    return a + b + c + e

try:
    print(add(1, 2, 3))
    print(add(1, 1, 1, 1))
    print(add(3, "4"))
except TypeError as e:
    print(e)

