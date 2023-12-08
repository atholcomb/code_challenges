#!/usr/bin/python3
# written by: atholcomb
# Decimal2Binary.py

def Decimal2Binary(n):
    value = []
    orignal_n = n
    
    while n != 0:
        if n % 2 == 0:
            n = n // 2
            value.append(0) 
        elif n % 2 == 1:
            n = n // 2
            value.append(1)
        else:
            break

    return f"{orignal_n} = {value[::-1]} in binary"
    

print(Decimal2Binary(10))
print(Decimal2Binary(12))
print(Decimal2Binary(25))
print(Decimal2Binary(45))
