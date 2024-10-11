from math import *

def Calc(s, t, u):
    s_func = lambda x: eval(s)
    t_func = lambda x: eval(t)
    u_func = lambda x, y: eval(u)

    def fun(x):
        s_value = s_func(x)
        t_value = t_func(x)

        return u_func(s_value, t_value)

    return fun


s, t, u = eval(input())
f = Calc(s, t, u)

result = f(eval(input()))
print(result)
