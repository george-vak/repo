from itertools import repeat, chain


def rep(seq, n):
    yield from chain.from_iterable(map(lambda x: repeat(x, n), seq))

print(*(rep("qwe", 2)))
