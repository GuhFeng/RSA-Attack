# File: exploit.sage

import time
import sys

# You will not known this
msg = b'Your PIN code is 4394'

def long_to_bytes(data):
    data = str(hex(long(data)))[2:-1]
    return "".join([chr(int(data[i:i + 2], 16)) for i in range(0, len(data), 2)])
    
def bytes_to_long(data):
    return int(data.encode('hex'), 16)

def main():
    e,N = (3L, 101100845141156293469516586973179461987930689009763964117872470309684853512775295312081121501322683984914454311655512983781714534411655378725344931438891842226528067586198216797211681076517718505980665732445770547794541814618131322049740520275847849231052080791884055178607671253203354019327951368529475389269L)

    c = bytes_to_long(msg)**e % N
    m = bytes_to_long("Your PIN code is \x00\x00\x00\x00")
    P.<x> = PolynomialRing(Zmod(N), implementation='NTL')
    pol = (m + x)^e - c
    roots = pol.small_roots(epsilon=1/30)
    print("Potential solutions:")
    for root in roots:
       print(root, long_to_bytes(m+root))
	
main()