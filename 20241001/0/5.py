def F(*f):
    def fun(x):
        return min(g(x) for g in f)
    return fun

function = F(lambda x: x**2, lambda x: x+2)
print(function(3))
