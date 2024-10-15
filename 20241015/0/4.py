from collections import Counter

def word_count(s):
    words = s.split()
    return Counter(words)

s = input()
print(word_count(s))

