def word_count(s):
    words = s.split()
    word_dict = {}

    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

print(word_count(input()))


