def f(a, b):
    return lambda x: a * x + b

res = f(2, 5)
print(res(2))
