from math import *

w, h, a, b, func = input().split()
w, h = int(w), int(h)
a, b = float(a), float(b)
F = lambda x: eval(func)

x_vals = [a + (b - a) * i / (w - 1) for i in range(w)]
y_vals = [F(x) for x in x_vals]
y_min, y_max = min(y_vals), max(y_vals)


def scale(y, h, y_min, y_max):
    return int((y - y_min) / (y_max - y_min) * (h - 1)) if y_max != y_min else h // 2


grap = [[' ' for i in range(w)] for i in range(h)]

for i in range(w):
    y = scale(y_vals[i], h, y_min, y_max)
    grap[h - 1 - y][i] = '*'

for i in range(w - 1):
    y1 = scale(y_vals[i], h, y_min, y_max)
    y2 = scale(y_vals[i + 1], h, y_min, y_max)

    if y1 != y2:
        for j in range(min(y1, y2), max(y1, y2)):
            if grap[h - 1 - j][i] == ' ':
                grap[h - 1 - j][i] = '*'

for row in grap:
    print(''.join(row))

