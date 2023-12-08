#!/usr/bin/python3
# written by: atholcomb
# ascii_to_dict.py
# Given a list of characters, return the ascii code equivalent 
# of the character in a dictionary

def ascii_to_dict(some_list):
    result = dict()

    for item in some_list:
        result[item] = ord(item)

    return result

print(ascii_to_dict(["a", "b", "c"]))
print(ascii_to_dict(["^"]))
print(ascii_to_dict([]))
