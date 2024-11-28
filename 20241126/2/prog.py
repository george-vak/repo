import sys

text = sys.stdin.read()
lat = text.encode('latin1', errors='replace')
cp = lat.decode('cp1251', errors='replace')
sys.stdout.write(cp)

