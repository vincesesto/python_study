#!/usr/bin/env python

# Set up the functions our program will use
import savings_functions

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
      savings_functions.add_savings(savings)
    else:
      savings_functions.check_savings()
  else:
    print("\nYou have made an invalid choice, please try again\n")
  
