import itertools
print(*filter(lambda s: s.count("TOR") == 2, map("".join, sorted(list(itertools.product("TOR", repeat=int(input())))))))

import sys
exec(sys.stdin.read())
