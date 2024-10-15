from math import *

def define(s, fdict, count):
    s = s.split()
    name = s[0]
    args = s[1:-1]
    body = s[-1]
    lambda_func_str = f"lambda {', '.join(args)}: {body}"
    func = eval(lambda_func_str)
    fdict[name] = func
    return count + 1



def call(s):
    s = s.split()
    name = s[0]
    args = [eval(el) for el in s[1:]]
    print(funcDict[name](*args))



def q(s, dco, stco, m):
    for el in m:
        call(el)

    s = s.replace("quit", "").strip()
    s = s.replace("{}", str(dco + 1), 1).replace("{}", str(stco), 1).replace('"', '')
    print(s)
    exit()


funcDict = {}
d_count, st_count = 0, 0
m = []
while True:
    s = input()
    st_count +=1
    if s[0] == 'q':
        q(s, d_count, st_count, m)
    elif s[0][0] == ":":
        d_count = define(s[1:], funcDict, d_count)
    else:
        m.append(s)

