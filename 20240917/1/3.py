def count(n):
    c = 1
    while n != 0:
        c += n % 10
        n //= 10
    return c

def vyv(a):
    i = 0
    while i < 3:
        r = a * (a + i)
        if count(r) != 6:
            print(a, ' * ', a + i, ' = ', r, end='       ')
        else:
            print(a, ' * ', a + i, ' = :=)', end='       ')
        i += 1
    print()

n = int(input())

for i in range(3):
    vyv(n)
    n += 1
