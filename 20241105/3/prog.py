from collections import deque

class Maze:
    def __init__(self, n):
        self.n = n
        self.grid = [['█' for _ in range(2 * n + 1)] for _ in range(2 * n + 1)]
        for i in range(n):
            for j in range(n):
                self.grid[2 * i + 1][2 * j + 1] = '·'

    def __str__(self):
        return "\n".join("".join(row) for row in self.grid)

    def __setitem__(self, args, val):
            p1 = (args[1].start, args[0])
            p2 = (args[2], args[1].stop)

            if p1[0] == p2[0]:
                row = 2 * p1[0] + 1
                for col in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
                    if col < max(p1[1], p2[1]):
                        self.grid[row][2 * col + 2] = val
            elif p1[1] == p2[1]:
                col = 2 * p1[1] + 1
                for row in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
                    if row < max(p1[0], p2[0]):
                        self.grid[2 * row + 2][col] = val


    def __getitem__(self, args):
        p1 = (args[1].start, args[0])
        p2 = (args[2], args[1].stop)
        st = (2 * p1[0] + 1, 2 * p1[1] + 1)
        fin = (2 * p2[0] + 1, 2 * p2[1] + 1)

        queu = deque([st])
        visited = set([st])

        sides = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queu:
            x, y = queu.popleft()
            if (x, y) == fin:
                return True

            for dx, dy in sides:
                nx, ny = x + dx, y + dy

                if (0 <= nx < len(self.grid) and 0 <= ny < len(self.grid[0])
                        and self.grid[nx][ny] == '·'
                        and (nx, ny) not in visited):


                    visited.add((nx, ny))
                    queu.append((nx, ny))

        return False

import sys
exec(sys.stdin.read())
