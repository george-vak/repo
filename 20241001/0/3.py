def rec(N):
    return None if N <= 0 else rec(N-1)

print(rec(5))
