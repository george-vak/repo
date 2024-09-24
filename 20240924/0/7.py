a, b = 12, 30
l = [i for i in range(a, b) if '3' not in str(i) and i % 2 == 1]

print(l)
