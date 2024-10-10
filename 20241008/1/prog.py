from fractions import Fraction

def splt(mas):
    pols = []
    i = 2

    while i < len(mas):
        step = int(mas[i])
        i += 1
        kfs = []
        for j in range(step + 1):
            if i < len(mas):
                kfs.append(Fraction(mas[i]))
                i += 1
        pols.append(kfs)

    return pols

def znach(mas, x):
    return sum(kf * (x ** st) for st, kf in enumerate(mas))


mas = input().split(', ')
s = Fraction(mas[0])
w = Fraction(mas[1])

a = (znach(splt(mas)[0], s))
b = (znach(splt(mas)[1], s))

if a / b == w:
    print('True')
else:
    print('False')

