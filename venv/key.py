from constants import *
from functions import *

def shift(str, bit, dir):
    return (str * 3)[len(str) + bit: 2 * len(str) + bit] if dir==0 else (str * 3)[len(str) - bit: 2 * len(str) - bit]

def generateKey(key):
    key = hexToBin(key)
    key56= permute(key, PC1)
    l_key,r_key = divide(key56)
    keysLR = [l_key, r_key]
    for i in range(len(L_SH)):
        keysLR.append(shift(keysLR[i*2], L_SH[i], 0))
        keysLR.append(shift(keysLR[(i*2)+1], L_SH[i], 0))

    keysJoin =[]
    for i in range(2, len(keysLR), 2):
        keysJoin.append(keysLR[i]+keysLR[i+1])

    keys48 = []
    for i in range(len(keysJoin)):
        temp = permute(keysJoin[i], PC2)
        keys48.append(temp)

    return keys48