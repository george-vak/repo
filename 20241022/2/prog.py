import itertools

def slide(seq, n):
    seq = iter(seq)
    wind = tuple(itertools.islice(seq, n))

    while wind:
        yield from wind
        wind = wind[1:] + tuple(itertools.islice(seq, 1))

import sys
exec(sys.stdin.read())
