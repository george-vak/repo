while True:
    try:
        n = int(input())
    except Exception:
        print("wrong!")
    else:
        print("..at last")
        break
print(n)
