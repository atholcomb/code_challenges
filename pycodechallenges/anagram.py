#!/usr/bin/python3
# written by: atholcomb
# anagram.py
# Program identifies if the two strings passed in are anagrams

def is_anagram(str_one, str_two):
  if sorted(str_one) == sorted(str_two):
    return True
  return False

print(is_anagram("typhoon", "opython"))
print(is_anagram("Alice", "Bob"))
