#!/usr/bin/python3
# written by: atholcomb
# convert_to_binary.py
# Given an integer, returns its corresponding binary number

def convert_to_binary(integers):
  print("Integer\t", "Binary")
  for integer in integers:
    print(integer, "\t", bin(integer)[2:])

def main():
  convert_to_binary([10, 12, 25, 45])

if __name__ == "__main__":
          main()
