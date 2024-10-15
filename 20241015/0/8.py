from collections import Counter

main = input().split()
small = input().split()

m = Counter(main)
s = Counter(small)



print("True") if s <= m else print("False")















