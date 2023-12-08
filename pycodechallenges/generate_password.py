#!/usr/bin/python3
# written by: atholcomb
# generate_password.py

import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special = '!@#$%^&*'

def generate_password(length):
    result = ''
    for l in range(length):
        password = random.choice(lower+upper+numbers+special)
        result += password
    return result

# print 5 different passwords of the specified length
length = int(input("Enter password length: "))
for i in range(5):
    print(generate_password(length))
