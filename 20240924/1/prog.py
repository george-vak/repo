m, n = eval(input())
print([x for x in range(m, n) if all(x % i for i in range(2, x)) and x > 1])
