import sys


text = sys.stdin.buffer.read()
n = text[0]
tail = text[1:]
dl = len(tail)
parts = []
for i in range(n):
    start = round(i * dl / n)
    end = round((i + 1) * dl / n)
    parts.append(tail[start:end])

res = bytes([n]) + b''.join(sorted(parts))
sys.stdout.buffer.write(res)

