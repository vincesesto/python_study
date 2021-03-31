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

# Welcome the user and provide a menu
while True:
  print("Welcome to Python Savings.")
  print("Choose from one of the tasks below.")
  print("1. Add Savings.")
  print("2. View Savings.")
  print("3. Quit Program.")

  choice = input("From the items above make a select from 1 - 3: ")

  if (int(choice) == 3):
    break
  elif (int(choice) < 3):
    if (int(choice) == 1):
      savings = input("\nHow much money did you save today? ")
      add_savings(savings)
    else:
      check_savings()
  else:
    print("\nYou have made an invalid choice, please try again\n")
