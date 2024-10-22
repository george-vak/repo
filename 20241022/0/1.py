def ryad():
    summ = 0
    n = 1
    while True:
        summ += 1 / (n * n)
        yield summ
        n += 1


gen = ryad()
for i in range(10):
    print(next(gen))

