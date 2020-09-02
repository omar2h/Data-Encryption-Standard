def hexToBin(str):
    return  ( bin(int(str, 16))[2:] ).zfill(len(str)*4)
def permute(str, pc):
    newStr = ""
    for i in range(len(pc)): newStr+= str[pc[i]-1]
    return newStr

def divide(str):
    return str[:(len(str)//2)],str[len(str)//2 :]

def xor(str1, str2):
    res=""
    for i in range(len(str1)): res+= str(int(str1[i])^int(str2[i]))
    return res

def binToDec(str):
    value = 0
    for i in range(len(str) - 1, -1, -1):
        if str[i]=='1': value = value + pow(2, abs(i - (len(str) - 1)))
    return value

def decToBin(n):
    str=""
    while(n>0):
        str+= '1' if n%2 else '0'
        n//=2
    return str[::-1]