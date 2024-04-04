#!/usr/bin/python3
# written by: atholcomb
# chkpasswords.py
# Program checks the complexity of the password
# Complexity must meet 8 characters length, alpha-numeric, and a special symbol

from passwords import generate_passwords

def chkpasswords():
  # Set the length of the password to be tested here
  password = generate_passwords(8)

  pswd_char_set = [
  'a','b','c','d','e','f','g','h','i','j','k','l','m',
  'n','o','p','q','r','s','t','u','v','w','x','y','z',
  'A','B','C','D','E','F','G','H','I','J','K','L','M',
  'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
  '%','&','$','#','@','!','*','?','/',
  '1','2','3','4','5','6','7','8','9','0' 
  ]

  for pswd in pswd_char_set:
    for p in password:
      if p in pswd and len(password) >= 8:
        return password, True
      return password, False


def main():
  for i in range(10):
    print(chkpasswords())

main()
