from math import sin

def scale(a, b, A, B, x):
    return (B - A) * (x - a) / (b - a) + A

def gra():
    w, h = 60, 20
    s = [[' ' for _ in range(w)] for _ in range(h)]

    for x in range(w):
        rx = scale(0, w, 0, 10, x)
        y = sin(rx)
        ny = int(scale(-1, 1, 0, h - 1, y))
        s[ny][x] = '*'

    for row in s[::-1]:
        print(''.join(row))

gra()

