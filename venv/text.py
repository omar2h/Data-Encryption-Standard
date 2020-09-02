from constants import *
from functions import *
from key import generateKey


def s(str, s):
    newStr = ""
    for i in range(8):
        j=i*6
        row = binToDec(str[j] + str[j+5])*16
        col = binToDec(str[j+1] + str[j+2] + str[j+3] + str[j+4])
        pos = row + col
        newStr+= decToBin(s_boxes[i][pos]).zfill(4)
    return newStr

def f(str, keys, i):
    per = permute(str, EXPANSION)
    xortext = xor(per, keys[i - 1])
    stext = s(xortext, s_boxes)
    per2 = permute(stext, P32)
    return per2

def encrypt(text, key):
    keys = generateKey(key)
    text = hexToBin(text)
    text = permute(text, IP)
    l_text, r_ight = divide(text)
    textLR = [l_text, r_ight]
    for i in range(1,17,1):
        textR = textLR[i*2-1]
        textL= textLR[i*2-2]
        textLR.append(textLR[i*2-1])
        textLR.append(xor(textLR[i*2-2], f(textLR[i*2-1], keys, i)))
    rightLeft16=textLR[33] + textLR[32]
    return hex(int(permute(rightLeft16, IP_INV),2))[2:].upper().zfill(16)

def decrypt(text, key):
    keys = generateKey(key)[::-1]
    text = hexToBin(text)
    text = permute(text, IP)
    l_text, r_ight = divide(text)
    textLR = [l_text, r_ight]
    for i in range(1,17,1):
        textR = textLR[i*2-1]
        textL= textLR[i*2-2]
        textLR.append(textLR[i*2-1])
        textLR.append(xor(textLR[i*2-2], f(textLR[i*2-1], keys, i)))
    rightLeft16=textLR[33] + textLR[32]
    return hex(int(permute(rightLeft16, IP_INV),2))[2:].upper().zfill(16)
