def rbin(n, count):
    if count == 0:
        print(*n, sep='')
    else:
        rbin(n + [0], count - 1)
        rbin(n + [1], count - 1)


rbin([1], int(input()) - 1)
