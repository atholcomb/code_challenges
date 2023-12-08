#!/usr/bin/python3
# written by: atholcomb
# caught_speeding.py

def caught_speeding(speed, is_birthday):
  if is_birthday == True:
    return 0
  elif speed <= 60:
    return 0 
  elif speed > 60 and speed <= 80:
    return 1
  else:
    return 2


print(caught_speeding(60, False))
print(caught_speeding(65, False))
print(caught_speeding(65, True))
print(caught_speeding(85, True))
