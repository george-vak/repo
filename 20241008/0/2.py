from decimal import Decimal

def esum(n, one):
    e = 0
    fr = 1
    t = type(one)
    e = t(e)
    for i in range(1, n+1):
        fr = fr*i
        e += t(1/fr*i)
    return e

print(esum(100, 1.1))
print(esum(100, Decimal('0.1')))


