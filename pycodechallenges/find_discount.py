#!/usr/bin/python3
# written by: atholcomb
# find_discount.py
# Create a function that takes two arguments: the original price and the discount
# percentage as integers and returns the final price after the discount.

def main():
  # Ask user for two input values
  price = int(input("What is the price of the product: "))
  discount = int(input("What is the percent of the discount: "))

  print(find_discount(price, discount))
   
# find_discount function call
def find_discount(price, discount):
  decimal = discount / 100
  answer = price - (price * decimal)

  return f"{discount}% of {price:>1} = ${answer}"
  
main()
