#!/usr/bin/env python

# Set up the functions our program will use
def check_savings():
  total = 0
  f = open("savings.txt", "r")
  savings_from_file = f.readlines()
  f.close()

  for i in savings_from_file:
    total += int(i)
  print("\nI have saved ${} so far this year\n".format(total))

def add_savings(amount):
  f = open("savings.txt","a")
  f.write("\n{}".format(amount))
  f.close()
  check_savings()
