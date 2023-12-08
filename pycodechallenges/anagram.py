#!/usr/bin/python3
# written by: atholcomb
# anagram.py

def is_anagram(str1, str2):

  if sorted(str1) == sorted(str2):
    return True
  return False


print(is_anagram("typhoon", "opython"))
print(is_anagram("Alice", "Bob"))
