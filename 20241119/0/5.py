from string import ascii_letters
import sys
from pympler.asizeof import asizeof

class Slotter:
    __slots__ = tuple(ascii_letters)
    def __init__(self):
        for attr in ascii_letters:
            setattr(self, attr, attr)


class Trad:
    def __init__(self):
        for attr in ascii_letters:
            setattr(self, attr, attr)

print("sl:", sys.getsizeof(Slotter), ";   tr:", sys.getsizeof(Trad))
print(asizeof(Slotter()), asizeof(Trad()))
t = [Trad() for _ in range(1000)]
s = [Slotter() for _ in range(1000)]

print(asizeof(s))
print(asizeof(t))
