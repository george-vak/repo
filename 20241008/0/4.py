w = 20
h = 10
screen = [[' '] * w for i in range(h)]

def show(screen):
    print('\n'.join(''.join(s) for s in screen))

for i in range(10):
    screen[i][i*2] = '#'

show(screen)
