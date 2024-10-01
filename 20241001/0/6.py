def f():
    # x = 2
    def fun():
        return x
    print('>>', fun.__closure__[0])
    x = 3
    print('>>', fun.__closure__[0])
    return fun

res = f()
print(res())
