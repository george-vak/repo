m = []
while line := input():
    m.append(list(map(int, line.split())))

n = len(m)
if all(len(row) == n for row in m):
    for i in range(len(m)):
        for j in range(i+1, len(m)):
            m[i][j], m[j][i] = m[j][i], m[i][j]

    for row in m:
        print(*row)
else:
    print('не квадратная!')

