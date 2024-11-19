#!/usr/bin/python3
# written by: atholcomb
# find_discount.py
# Create a function that takes two arguments: the original price and the discount
# percentage as integers and returns the final price after the discount.

#from decimal import Decimal
from random import randint

def main():
  print("Discount   = Per%   $Amt  $Difference")

  for price, discount in generate_values_1000s().items():
    if discount % 10 == discount:
      print(find_discount_1s_place(price, discount))
    elif discount % 100 == discount:
      print(find_discount_2s_place(price, discount))
   
  print("\nDiscount   = Per%   $Amt  $Difference")

  for price, discount in generate_values_100s().items():
    if discount % 10 == discount:
      print(find_discount_1s_place(price, discount))
    elif discount % 100 == discount:
      print(find_discount_2s_place(price, discount))

  print("\nDiscount   = Per%   $Amt  $Difference")

  for price, discount in generate_values_10s().items():
    if discount % 10 == discount:
      print(find_discount_10s_place(price, discount))
    elif discount % 100 == discount:
      print(find_discount_10s_place(price, discount))

# generate_values_1000s instantiates a dict of values to be tested
def generate_values_1000s():
  values = {}
  for i in range(5):
    price = randint(1000, 10000)
    discount = randint(1, 99)
    values[price] = discount

  return values

# generate_values_100s instantiates a dict of values to be tested
def generate_values_100s():
  values = {}
  for i in range(5):
    price = randint(100, 1000)
    discount = randint(1, 99)
    values[price] = discount

  return values

# generate_values_10s instantiates a dict of values to be tested
def generate_values_10s():
  values = {}
  for i in range(5):
    price = randint(1, 10)
    discount = randint(1, 99)
    values[price] = discount

  return values

# find_discount function calls either the 1s place function
# or the 2s place function depending on the discount applied
def find_discount_1000s_place(price, discount):
  answer = round(price - ((price * discount) / 100), 2)
  #return f"${answer:<8} = {discount}% of ${price}"
  return f"${answer:<9} = .{discount}% of ${price} (${price:>4} - ${((price * discount) / 100)})"

def find_discount_100s_place(price, discount):
  answer = round(price - ((price * discount) / 100), 2)
  #return f"${answer:<8} = {discount}% of ${price}"
  return f"${answer:<9} = {discount}% of ${price} (${price:>4} - ${((price * discount) / 100)})"

def find_discount_10s_place(price, discount):
  answer = round(price - ((price * discount) / 10), 2)
  #return f"${answer:<8} = {discount}% of ${price}"
  return f"${answer:<9} = .{discount}% of ${price} (${price:>4} - ${((price * discount) / 10)})"
 
main()
