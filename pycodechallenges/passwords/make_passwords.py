#!/usr/bin/python3
# written by: atholcomb
# create_passwords.py
# Program creates passwords from Passwords Module

from passwords import generate_passwords

def main():
  print(generate_passwords(9))


if __name__ == "__main__":
    main()
