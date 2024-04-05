#!/usr/bin/python3
# written by: atholcomb
# create_passwords.py
# Program creates passwords from Passwords Module
# Which need to be tested against check_passwords.py
# To confirm that the password is valid

from passwords import generate_passwords

def main():
  # Set the length of the password to be tested here
  password = generate_passwords(8)

  return password
  
if __name__ == "__main__":
    print(main())
