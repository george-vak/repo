import math
def S(f, g):
    def fun(x):
        return f(x) + g(x)
    return fun

res = S(math.sin, math.cos)
print(res(math.pi))
