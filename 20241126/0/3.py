import struct
import random

with open("dt.bin", "wb") as f:
    for _ in range(10):
        f.write(struct.pack("<f3si", random.random(), b"abc", random.randint(0, 100)))

with open("dt.bin", "rb") as f:
    data = f.read()

with open("dta.bin", "wb") as f:
    for i in range(10):
        offset = i * struct.calcsize("<f3si")
        float_val, bytes_val, int_val = struct.unpack("<f3si", data[offset:offset + struct.calcsize("<f3si")])
        f.write(struct.pack("!f3si", float_val, bytes_val, int_val))

