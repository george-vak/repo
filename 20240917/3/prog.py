def count(n):
    c = 0
    while n != 0:
        c += n % 10
        n //= 10
    return c

n = int(input())

for i in range(n, n + 3):
    for j in range(n, n + 3):
        r = i * j
        if count(r) == 6:
            print(f"{i} * {j} = :=)", end=" ")
        else:
            print(f"{i} * {j} = {r}", end=" ")
    print()

