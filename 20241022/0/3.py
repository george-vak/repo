def walk2d():
    x, y = 0, 0

    while True:
        dx, dy = yield (x, y)
        x += dx
        y += dy

gen = walk2d()
print(next(gen))
print(gen.send((1, 2)))
print(gen.send((-3, -4)))


