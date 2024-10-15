s = input()
a, b = map(int, input().split(','))

res1 = eval(s, {"x": a, "y": b})
res2 = eval(s, {"x": b, "y": a})

print(res1)
print(res2)

