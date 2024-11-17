from collections import UserString


class DivStr(UserString):
    def __init__(self, seq=""):
        if not isinstance(seq, (str, UserString)):
            raise ValueError("not format")
        super().__init__(seq)

    def __floordiv__(self, n):
        if not isinstance(n, int) or n <= 0:
            raise ValueError("not positive integer")

        part_length = len(self.data) // n
        for i in range(n):
            yield DivStr(self.data[i * part_length:(i + 1) * part_length])

    def __mod__(self, n):
        if not isinstance(n, int) or n <= 0:
            raise ValueError("not positive integer")

        part_length = len(self.data) // n
        remainder_start = n * part_length
        return DivStr(self.data[remainder_start:])


import sys
exec(sys.stdin.read())


