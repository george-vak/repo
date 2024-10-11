def pareto(a):
    def x_dom_y(x, y):
        return True if (y[0] < x[0] and y[1] <= x[1]) or (y[0] <= x[0] and y[1] < x[1]) else False
    res = []
    for el in a:
        for el2 in a:
            if  x_dom_y(el2, el):
                break
        else:
            res.append(el)
    return res

print(tuple(pareto(eval(input()))))
