#!/usr/bin/python3
# written by: atholcomb
# capital_indexes.py
# return only the indices which contain capital letters

def capital_indexes(string):
  capitals = {}

  for i, s in enumerate(string):
    if s.isupper():
      capitals[i] = s

  print(string)
  return capitals

print(capital_indexes('HeLlO'))
print(capital_indexes('HHHHH'))
print(capital_indexes('0192H'))
