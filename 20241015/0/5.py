import timeit
from collections import Counter


def word_count1(s):
    words = s.split()
    return Counter(words)

def word_count2(s):
    words = s.split()
    word_dict = {}

    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

ex_t1 = timeit.timeit('word_count1', globals=globals(), number=1000)
ex_t2 = timeit.timeit('word_count2', globals=globals(), number=1000)

print(ex_t1, "sec")
print(ex_t2, "sec")
