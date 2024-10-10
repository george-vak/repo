import math

def calc(cont):
    g_count = 0
    l_count = 0

    for row in cont[1:-1]:
        g_count += row.count('.')
        l_count += row.count('~')

    h = len(cont) - 2
    w = len(cont[0]) - 2

    return g_count, l_count, w, h

cont = [input()]
while True:
    s = input()

    if all(char == s[0] for char in s):
        cont.append(s)
        break
    else:
        cont.append(s)

gas, liquid, new_h, new_w = calc(cont)

v = new_w * new_h
l_rows = math.ceil(liquid / new_w)
gas_rows = new_h - l_rows

gas_out = gas_rows * new_w
liquid_out = l_rows * new_w


print("#" * (new_w + 2))
while gas_rows > 0:
    print("#", "." * new_w, "#", sep='')
    gas_rows -= 1

while l_rows > 0:
    print("#", "~" * new_w, "#", sep='')
    l_rows -= 1
print("#" * (new_w + 2))

g = "." * gas_out
l = "~" * liquid_out

print(f"{g:<{max(gas_out, liquid_out)}} {gas_out:>{len(str(v))}}/{v}")
print(f"{l:<{max(gas_out, liquid_out)}} {liquid_out:>{len(str(v))}}/{v}")


