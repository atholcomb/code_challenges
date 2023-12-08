#!/usr/bin/python3
# written by: atholcomb
# check_square_and_cube.py
# Create a function that takes a list of two numbers and checks if the square root 
# of the first number is equal to the cube root of the second number.

import math

def check_square_and_cube(s_c_list):
    for number in s_c_list:
        square = int(math.sqrt(number))
        cube = math.ceil(number ** (1/3))
        if square == cube:
            return f'square: {square}, cube: {cube} -> True'
        return f'square: {square}, cube: {cube} -> False'


print(check_square_and_cube([4, 8])) # True
print(check_square_and_cube([16, 48])) # False
print(check_square_and_cube([9, 27])) # True
