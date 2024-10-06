def vych(a, b):
    if isinstance(a, (int, float)):
        return a - b

    elif isinstance(a, (list, tuple)):
        res = [el for el in a if el not in set(b)]
        return type(a)(res)

    else:
        return False

x, y = eval(input())
print(vych(x, y))
