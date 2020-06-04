def countBits(n):
    return str(bin(n)).count('1')



decimal = 24
print(countBits(decimal))


#binary = bin(decimal)[2:].zfill(8)
#print(binary)
