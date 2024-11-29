import struct
import sys

fields = [
    ("ChunkID", "4s"),
    ("ChunkSize", "I"),
    ("Format", "4s"),
    ("Subchunk1ID", "4s"),
    ("Subchunk1Size", "I"),
    ("AudioFormat", "H"),
    ("NumChannels", "H"),
    ("SampleRate", "I"),
    ("ByteRate", "I"),
    ("BlockAlign", "H"),
    ("BitsPerSample", "H"),
    ("Subchunk2ID", "4s"),
    ("Subchunk2Size", "I"),
]

s = '<' + ''.join(el[1] for el in fields)

data = sys.stdin.buffer.read(44)
if len(data) < 44:
    print("NO")
    sys.exit()

try:
    unp = struct.unpack(s, data)
except struct.error:
    print("NO")
    sys.exit()

header = {}
for (name, field_fmt), val in zip(fields, unp):
    if 's' in field_fmt:
        try:
            val = val.decode('ascii').strip()
        except UnicodeError:
            print("NO")
            sys.exit()
    header[name] = val

if header["ChunkID"] != "RIFF" or header["Format"] != "WAVE" or header["Subchunk2ID"] != "data":
    print("NO")
    sys.exit()

print(f"Size={header['ChunkSize']}, Type={header['AudioFormat']}, Channels={header['NumChannels']}, Rate={header['SampleRate']}, Bits={header['BitsPerSample']}, Data size={header['Subchunk2Size']}")

