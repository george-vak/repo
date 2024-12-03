w1, w2, w3 = input().split()


while s := input():
    items = s.split()
    match items:
        case [w, *_] if w == w1 and "yes" in items:
            print("1")
        case [w2]:
            print("2")
        case [w3, *_, last] if last == w2:
            print("3")
        case _:
            print("No match")
