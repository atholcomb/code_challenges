#!/usr/bin/python3
# written by: atholcomb
# counting_syllables.py
# return the number of syllables found in each word

def count(string):
  words = string.split('-') # split on hyphens (syllables)
  word_count = 0

  for index, syllable in enumerate(words):
    word_count += 1
  return word_count


print(count("ho-tel"))          # 2
print(count("cat"))             # 1
print(count("met-a-phor"))      # 3
print(count("ter-min-a-tor"))   # 4
