word = "вопрос"
encoded_decoded = word.encode('koi8-r').decode('cp1251')
print(f'"{word}" "{encoded_decoded}"')

encoded_1 = "бМХЛЮМХЕ".encode('cp1251').decode('koi8-r')
encoded_2 = "ОХРЮМХЕ".encode('cp1251').decode('koi8-r')

print(f'"бМХЛЮМХЕ" "{encoded_1}"')
print(f'"ОХРЮМХЕ" "{encoded_2}"')

