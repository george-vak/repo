s = input().lower()
mas =[]

for i in range(len(s)-1):
    if s[i].isalpha() and s[i+1].isalpha():
        mas.extend([s[i], s[i+1]])
print(len(set(mas)))
