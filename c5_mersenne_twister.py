from MTRecover import MT19937Recover
from robo import arr

mtr = MT19937Recover()
r2 = mtr.go(arr)

def encodeSecret(s):
    key = [r2.getrandbits(8) for i in range(len(s))]
    return bytes([a^b for a,b in zip(key,(s))]

with open("secret.enc", "rb") as f:
    s = f.read()

print(encodeSecret(s))

# CTF{n3v3r_3ver_ev3r_use_r4nd0m}
