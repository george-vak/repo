from itertools import filterfalse

n = 7
s = filterfalse(lambda x: x%n, range(11, 66))

print(*s)
