n = int(input())
text = []
words = {}
while row:=input():
    text.append(row)

text = "\n".join(text)
text = text.lower()
flt = ""

for ch in text:
    if ch.isalpha():
        flt += ch
    else:
        flt += " "
flt = flt.split()
for el in flt:
    if len(el) == n:
        words[el] = words.get(el, 0) + 1

p = [key for key, value in words.items() if value == max(words.values())]

print(*p)
