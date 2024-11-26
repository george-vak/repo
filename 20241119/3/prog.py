class Vowel:
    __slots__ = ["a", "e", "i", "o", "u", "y"]

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.__slots__:
                setattr(self, key, value)
            else:
                raise AttributeError(f"no such attr'{key}'")

    answer = 42

    @property
    def full(self):
        return all(hasattr(self, slot) and getattr(self, slot) is not None for slot in self.__slots__)



    def __str__(self):
        return ', '.join(f"{key}: {getattr(self, key)}" for key in sorted(self.__slots__)
                         if hasattr(self, key) and getattr(self, key) is not None)

import sys
exec(sys.stdin.read())




