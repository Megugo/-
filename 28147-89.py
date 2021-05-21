#!/usr/bin/env python3

from os import urandom


# Узлы замены определенные документом RFC 4357. Согласно ГОСТу можно брать произвольные SBOXES



SBOXES = {
  "id-Gost28147-89-CryptoPro-A-ParamSet": (
    (9, 6, 3, 2, 8, 11, 1, 7, 10, 4, 14, 15, 12, 0, 13, 5),
    (3, 7, 14, 9, 8, 10, 15, 0, 5, 2, 6, 12, 11, 4, 13, 1),
    (14, 4, 6, 2, 11, 3, 13, 8, 12, 15, 5, 10, 0, 7, 1, 9),
    (14, 7, 10, 12, 13, 1, 3, 9, 0, 2, 11, 4, 15, 8, 5, 6),
    (11, 5, 1, 9, 8, 13, 15, 0, 14, 4, 2, 3, 12, 7, 10, 6),
    (3, 10, 13, 12, 1, 2, 0, 11, 7, 5, 9, 4, 8, 15, 14, 6),
    (1, 13, 2, 9, 7, 10, 6, 0, 8, 12, 4, 5, 15, 3, 11, 14),
    (11, 10, 15, 5, 0, 12, 14, 8, 6, 2, 3, 9, 1, 7, 13, 4)
  ),
  "id-Gost28147-89-CryptoPro-B-ParamSet": (
    (8, 4, 11, 1, 3, 5, 0, 9, 2, 14, 10, 12, 13, 6, 7, 15),
    (0, 1, 2, 10, 4, 13, 5, 12, 9, 7, 3, 15, 11, 8, 6, 14),
    (14, 12, 0, 10, 9, 2, 13, 11, 7, 5, 8, 15, 3, 6, 1, 4),
    (7, 5, 0, 13, 11, 6, 1, 2, 3, 10, 12, 15, 4, 14, 9, 8),
    (2, 7, 12, 15, 9, 5, 10, 11, 1, 4, 0, 13, 6, 8, 14, 3),
    (8, 3, 2, 6, 4, 13, 14, 11, 12, 1, 7, 15, 10, 0, 9, 5),
    (5, 2, 10, 11, 9, 1, 12, 3, 7, 4, 13, 0, 6, 15, 8, 14),
    (0, 4, 11, 14, 8, 3, 7, 1, 10, 2, 9, 6, 15, 13, 5, 12)
  ),
  "id-Gost28147-89-CryptoPro-C-ParamSet": (
    (1, 11, 12, 2, 9, 13, 0, 15, 4, 5, 8, 14, 10, 7, 6, 3),
    (0, 1, 7, 13, 11, 4, 5, 2, 8, 14, 15, 12, 9, 10, 6, 3),
    (8, 2, 5, 0, 4, 9, 15, 10, 3, 7, 12, 13, 6, 14, 1, 11),
    (3, 6, 0, 1, 5, 13, 10, 8, 11, 2, 9, 7, 14, 15, 12, 4),
    (8, 13, 11, 0, 4, 5, 1, 2, 9, 3, 12, 14, 6, 15, 10, 7),
    (12, 9, 11, 1, 8, 14, 2, 4, 7, 3, 6, 5, 10, 0, 15, 13),
    (10, 9, 6, 8, 13, 14, 2, 0, 15, 3, 5, 11, 4, 1, 12, 7),
    (7, 4, 0, 5, 10, 2, 15, 14, 12, 6, 1, 11, 13, 9, 3, 8)
  ),
  "id-Gost28147-89-CryptoPro-D-ParamSet": (
    (15, 12, 2, 10, 6, 4, 5, 0, 7, 9, 14, 13, 1, 11, 8, 3),
    (11, 6, 3, 4, 12, 15, 14, 2, 7, 13, 8, 0, 5, 10, 9, 1),
    (1, 12, 11, 0, 15, 14, 6, 5, 10, 13, 4, 8, 9, 3, 7, 2),
    (1, 5, 14, 12, 10, 7, 0, 13, 6, 2, 11, 4, 9, 3, 15, 8),
    (0, 12, 8, 9, 13, 2, 10, 11, 7, 3, 6, 5, 4, 14, 15, 1),
    (8, 0, 15, 3, 2, 5, 14, 11, 1, 10, 4, 7, 12, 9, 13, 6),
    (3, 0, 6, 15, 1, 14, 9, 2, 13, 8, 12, 4, 11, 10, 5, 7),
    (1, 10, 6, 8, 15, 11, 0, 4, 12, 3, 5, 9, 7, 13, 2, 14)
  )
}

def xor(a,b):
    res = int(a,16)^int(b,16)
    #print ('%x'%res)
    return res


def str_to_hex(s):

    return "".join("{:02x}".format(ord(c)) for c in s)

def str_to_array(str):
    astr = []
    for i in range(0,len(str),2):
        astr.append(str[i]+str[i+1])
    return astr

def array_to_str(arr):
    return "".join(c for c in arr)

def msg_to_strs(msg):
    strs =[]
    for i in range(0,len(msg),8):
        strs.append(msg[i:i+8])
    return strs

def sf(part,key):
    sbox = (
      (9, 6, 3, 2, 8, 11, 1, 7, 10, 4, 14, 15, 12, 0, 13, 5),
      (3, 7, 14, 9, 8, 10, 15, 0, 5, 2, 6, 12, 11, 4, 13, 1),
      (14, 4, 6, 2, 11, 3, 13, 8, 12, 15, 5, 10, 0, 7, 1, 9),
      (14, 7, 10, 12, 13, 1, 3, 9, 0, 2, 11, 4, 15, 8, 5, 6),
      (11, 5, 1, 9, 8, 13, 15, 0, 14, 4, 2, 3, 12, 7, 10, 6),
      (3, 10, 13, 12, 1, 2, 0, 11, 7, 5, 9, 4, 8, 15, 14, 6),
      (1, 13, 2, 9, 7, 10, 6, 0, 8, 12, 4, 5, 15, 3, 11, 14),
      (11, 10, 15, 5, 0, 12, 14, 8, 6, 2, 3, 9, 1, 7, 13, 4)
    )
    buff = part^key
    out=0
    for i in range(8):
        out |=((sbox[i][(buff >> (4*i)) & 0b1111]) << (4 * 1))

    return ((out >> 11) | (out << (32-11))) & 0xFFFFFFFF

def encrypt(plain,key):
    left = int(str_to_hex(plain[:4]),16)
    right = int(str_to_hex(plain[4:]),16)
    subkeys = [(key >> (32 * i)) & 0xFFFFFFFF for i in range(8)]
    for i in range(24):
        left, right = enc_round(left,right,subkeys[i%8])
    for i in range(8):
        left, right = enc_round(left,right,subkeys[7-i])
    return (str(left)+str(right))
def enc_round(left,right,key):

    return right, left^sf(right,key)

message = input()
if len(message)<8:
    for i in range(8 - len(message)):
        message +=' '
else:
    while (len(message) % 8!=0):
        message+= " "

print(msg_to_strs(message))
message = str_to_hex(message)
#key = b'0475f6e05038fbfad2c7c390edb3ca3d1547124291ae1e8a2f79cd9ed2bcefbd'
key = 18318279387912387912789378912379821879387978238793278872378329832982398023031
print(encrypt(message,key))
#for i in subkeys:
#    print(len(hex(i)[2:]))

#print((str_to_array(message)[4:],str_to_array(message)[:4]))
#print(xor(str_to_array(message)[4:][0],str_to_array(message)[:4][0]))
#print(xor(message[32:],message[:32]))
