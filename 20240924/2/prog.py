def key(n):
    return n ** 2 % 100

l = list(map(int, input().split(',')))

for i, e in enumerate(l):
    l[i] = [e, key(e)]

N = len(l)
for i in range(N-1):
    for j in range(N-1-i):
        if l[j][1] > l[j+1][1]:
            l[j], l[j+1] = l[j+1], l[j]

res = []
for e in l:
    res.append(e[0])
print(res)
