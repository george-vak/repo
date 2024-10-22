from itertools import dropwhile, islice


def ryad():
    summ = 0
    n = 1
    while True:
        summ += 1 / (n * n)
        yield summ
        n += 1


gen = ryad()
s = list(islice(dropwhile(lambda x: x < 1.6, gen), 10))

print(s)
