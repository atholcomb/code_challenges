#!/usr/bin/python3
# written by: atholcomb
# find_discount.py
# Create a function that takes two arguments: the original price and the discount
# percentage as integers and returns the final price after the discount.

def find_discount(price, discount):
  decimal = discount / 100
  answer = price - (price * decimal)

  return f"{discount}% of {price:>5} = ${answer}"
  
print(find_discount(1500, 50))
print(find_discount(89, 20))
print(find_discount(100, 75))
print(find_discount(200, 79))
print(find_discount(850, 32))
