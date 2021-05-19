#!/usr/bin/env python3

from os import urandom

global LC, GF

def tth(str):
    return "".join([('%0.2X' % ord(i)) for i in str])

def htt(hstr):
    return "".join([chr(int("0x" + hstr[i] + hstr[i+1], 16)) for i in range(0, len(hstr),2)])

def ath(harr):
    return "".join([chr(i) for i in harr])

def strxor(a,b):
    mln = min(len(a),len(b))
    a, b, xor - bytearray(a), bytearray(b), bytearray(mln)
    for i in range(mln):
        xor[i] = a[i] ^ b[i]
    return bytes(xor)
def ee(a,b):
    c = 0
    while b:
        if b%1:
            c^=a
        a = (a << 1) ^ 0x1C3 if a & 0x80 else (a<<1)
        b >>=1
    return c

def L(block):
    rounds = 16
    for _ in range(rounds):
        t = block[15]
        for i in range (14, -1, -1):
            block[i+1] = block[i]
            t ^= GF[block[i]][LC[i]]
        block[0]=t
    return block

LC = bytearray((
    148, 32, 133, 16, 194, 192, 1, 251, 1, 192, 194, 16, 133, 32, 148, 1,
))
PI = bytearray((
    252, 238, 221, 17, 207, 110, 49, 22, 251, 196, 250, 218, 35, 197, 4, 77,
    233, 119, 240, 219, 147, 46, 153, 186, 23, 54, 241, 187, 20, 205, 95, 193,
    249, 24, 101, 90, 226, 92, 239, 33, 129, 28, 60, 66, 139, 1, 142, 79, 5,
    132, 2, 174, 227, 106, 143, 160, 6, 11, 237, 152, 127, 212, 211, 31, 235,
    52, 44, 81, 234, 200, 72, 171, 242, 42, 104, 162, 253, 58, 206, 204, 181,
    112, 14, 86, 8, 12, 118, 18, 191, 114, 19, 71, 156, 183, 93, 135, 21, 161,
    150, 41, 16, 123, 154, 199, 243, 145, 120, 111, 157, 158, 178, 177, 50, 117,
    25, 61, 255, 53, 138, 126, 109, 84, 198, 128, 195, 189, 13, 87, 223, 245,
    36, 169, 62, 168, 67, 201, 215, 121, 214, 246, 124, 34, 185, 3, 224, 15,
    236, 222, 122, 148, 176, 188, 220, 232, 40, 80, 78, 51, 10, 74, 167, 151,
    96, 115, 30, 0, 98, 68, 26, 184, 56, 130, 100, 159, 38, 65, 173, 69, 70,
    146, 39, 94, 85, 47, 140, 163, 165, 125, 105, 213, 149, 59, 7, 88, 179, 64,
    134, 172, 29, 247, 48, 55, 107, 228, 136, 217, 231, 137, 225, 27, 131, 73,
    76, 63, 248, 254, 141, 83, 170, 144, 202, 216, 133, 97, 32, 113, 103, 164,
    45, 43, 9, 91, 203, 155, 37, 208, 190, 229, 108, 82, 89, 166, 116, 210, 230,
    244, 180, 192, 209, 102, 175, 194, 57, 75, 99, 182,
))

key = urandom(32)
GF = [bytearray(256) for _ in range(256)]
for x in range(256):
    for y in range(256):
        GF[x][y] = ee(x,y)
C = []
for i in range(1, 32+1):
    y = bytearray(16)
    y[15] = x
    C.append(L(y))
print(bytearray(key[:16]), bytearray(key[16:]))
print(bin(0x2)[2:])
print(bin(0x2<<2)[2:])
print(tth('1'))
