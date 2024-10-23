from itertools import islice

def fib_generator():
    x, y = 1, 1
    while True:
        yield x
        x, y = y, x + y

def fib(m, n):
    return islice(fib_generator(), m, m + n)

import sys
exec(sys.stdin.read())
