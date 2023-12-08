#!/usr/bin/python3
# written by: atholcomb
# check_password.py

import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special = '!@#$%^&*?'

password = input("Enter a password: " )

def check_password(password):
    low = 0
    up = 0
    nums = 0
    spec = 0
    for passwd in password:
        if passwd in lower:
            low += 1
        elif passwd in upper:
            up += 1
        elif passwd in numbers:
            nums += 1
        elif passwd in special:
            spec += 1
        else:
            return "Password does not meet requirements or normal convention"
    
    return f"Your password has the following characteristics:\n{low} lowercase, {up} uppercase, {nums} number(s), {spec} special character(s)"
    

print(check_password(password))

