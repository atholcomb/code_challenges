#!/usr/bin/python3
# written by: atholcomb
# find_discount.py
# Create a function that takes two arguments: the original price and the discount
# percentage as integers and returns the final price after the discount.

#from decimal import Decimal
from random import randint

def main():
  print("Printing first 5 values to be tested")

  for price, discount in generate_values().items():
    if discount % 10 == discount:
      print(find_discount_1s_place(price, discount))
    elif discount % 100 == discount:
      print(find_discount_2s_place(price, discount))
   
# Generate values instantiates a list of values to be tested
def generate_values():
  values = {}
  for i in range(5):
    price = randint(1, 10000)
    discount = randint(1, 99)
    values[price] = discount

  return values

# find_discount function calls either the 1s place function
# or the 2s place function depending on the discount applied
def find_discount_1s_place(price, discount):
  answer = (price * discount) / 10

  return f"{discount}% of {price:>1} = ${answer}"

def find_discount_2s_place(price, discount):
  answer = (price * discount) / 100

  return f"{discount}% of {price:>1} = ${answer}"
 
main()
