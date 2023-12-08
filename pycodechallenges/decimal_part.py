#!/usr/bin/python3
# written by: atholcomb
# decimal_part.py
# Create a function which takes a number n and return its decimal part.

def decimal_part(n):
    # create str object out of float(n) to enumerate over
    n_string = str(n)
    
    # find the position where the decimal is at
    # return str with decimal part only
    # else return n
    for pos, nstr in enumerate(n_string):
        if '.' in n_string[pos]:
            return f'0{n_string[pos:]}'
    return 0
        

print(decimal_part(1.2))    # 0.2
print(decimal_part(-3.73))  # 0.73
print(decimal_part(10))     # 0
