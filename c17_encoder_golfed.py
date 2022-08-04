from struct import *
R=range
N=[x&255 for x in R(2,9999)if all(x%i for i in R(2,x))]
a=B(R(97,123))
def encode(b):
    return B(q^w for q,w in zip((b"BEGN\0\0\0\x1a"+a+b"DATA"+pack(">I",len(b))+b+b"END.\0\0\0\x1a"+a.upper()),N))

# nc -v playing-golf.2021.ctfcompetition.com 1337
# CTF{EncodingSuccessfulIntelReceivedCorrectly}
