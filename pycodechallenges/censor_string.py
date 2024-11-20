#!/usr/bin/python3
# written by: atholcomb
# censor_string.py
# For a given text string, censor the word inside the list with the given char

def censor_string(text_str, censor_list, censor_character):
  for word in censor_list:
    text_str = text_str.replace(word, censor_character*len(word))
  
  return text_str

print(censor_string("Today is a Wednesday!", ["Today", "a"], "-"))
print(censor_string("The cow jumped over the moon.", ["cow", "moon"], "*"))
print(censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*"))
