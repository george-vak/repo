from itertools import product

s = product("abcdefgh", range(1, 9))
print([f"{let}{num}" for let, num in list(s)])
