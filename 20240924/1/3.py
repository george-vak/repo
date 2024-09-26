def sqr_test(a, n):
    if all(len(row) == n for row in a):
        return True
    return False


def matrix_multiply(A, B, n):
    r = [[0] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                r[i][j] += A[i][k] * B[k][j]

    return r

m = []
while line := input():
    m.append(list(map(int, line.split(','))))

n = len(m)//2
A = (m[:len(m)//2])
B = (m[len(m)//2:])

if sqr_test(A, n) and sqr_test(B, n):
    for e in matrix_multiply(A, B, n):
        print(*e, sep=',')

