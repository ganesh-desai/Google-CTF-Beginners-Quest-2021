import struct
import base64
d = open("hideandseek.png", "rb").read()[8:]

k = b""

i = 0
while True:
    l = struct.unpack(">I", d[i:i+4])[0]
    t = d[i+4:i+8]
    c = d[i+8:i+8+1]
    i += 12 + 1

    if t == b"IEND":
        break

    if t == b'eDIH':
        print(t, l, c)
        k += c

print(base64.b64decode(k))

# edIH is saying HIDe lol
# CTF{DidYouKnowPNGisPronouncedPING?}
