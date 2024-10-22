def dop():
    yield "по кочкам"

def maing(n):
    while n > 0:
        yield from dop()
        n -= 1
    return "в яму"

gen = maing(4)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


