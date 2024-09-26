m, n = 1, 15
print([x for x in range(m, n+1) if all(x % i for i in range(2, x)) and x > 1])

