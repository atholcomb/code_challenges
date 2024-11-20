#!/usr/bin/python3
# written by: atholcomb
# car_listing.py
# Program outputs a cars cost in dollar amounts

def car_listing(car_prices):
  result = {}
  for model, price in car_prices.items():
    result[model] = price
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))
